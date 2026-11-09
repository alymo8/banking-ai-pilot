"""Relationship review memo: Tom's single ChatGPT prompt rebuilt as a checked pipeline.

    1 retrieve   (code)    policy-filtered records as of a date, each with a source id
    2 facts      (Claude)  fact sheet + source conflicts + gaps, every fact cited
    3 verify     (code)    every cited id exists; every figure appears in a cited record
    4 draft      (Claude)  factual sections only, from verified facts
    5 rm polish  (Claude)  RM's own notes -> prose, claim-mapped back to the notes
    6 check      (code + Claude)  policy 4.2 scan of AI-authored text; one neutral rewrite pass
    7 assemble   (code)    memo with RM sections verbatim + an RM review sheet

Usage:
    python -m banking_pilot.memo_pipeline meridian --as-of 2025-01-31 --rm-notes rm_input/meridian_2025-01-31.md
"""
from __future__ import annotations

import argparse
import re
from typing import Literal

from pydantic import BaseModel

from banking_pilot import data
from banking_pilot.llm import Run, prompt

Section = Literal["business", "facility", "financial_performance", "covenant_history",
                  "communications", "open_requests"]


class Fact(BaseModel):
    section: Section
    statement: str
    source_ids: list[str]


class Version(BaseModel):
    claim: str
    source_id: str


class Conflict(BaseModel):
    topic: str
    versions: list[Version]
    affects: str


class Gap(BaseModel):
    item: str
    last_requested_source: str | None


class FactSheet(BaseModel):
    facts: list[Fact]
    conflicts: list[Conflict]
    gaps: list[Gap]


class ClaimLink(BaseModel):
    sentence: str
    rm_note_lines: list[str]


class Polished(BaseModel):
    assessment: str
    recommendation: str
    claim_map: list[ClaimLink]
    questions_for_rm: list[str]


class Flag(BaseModel):
    sentence: str
    rule: str
    rewrite: str


class Review(BaseModel):
    flags: list[Flag]


# Deterministic first line of defence for policy 4.2. Cheap, explainable, and it runs
# before the model reviewer so a reviewer miss can't let these through.
CREDIT_LEXICON = [
    r"\bhigh[- ]risk\b", r"\belevated risk\b", r"\brisk profile\b", r"\bcreditworth", r"\bcredit quality\b",
    r"\blikely to (breach|default)\b", r"\bdeteriorat", r"\bweak(ness|ening)?\b", r"\bstrong credit\b",
    r"\bconcern(ing|s)?\b", r"\btroubl", r"\bworr", r"\balarming\b", r"\bdistress", r"\bred flag",
    r"\bwarning sign", r"\bheadwind", r"\bstruggl", r"\brecommend", r"\bshould (be|consider)\b",
    r"\bwarrant", r"\bdowngrade", r"\bupgrade", r"\bwatch\s?list", r"\bspecial assets\b",
]

NUM = re.compile(r"(?<![\w.])\$?\d+(?:,\d{3})*(?:\.\d+)?(?:x|%|MM|M|K|k)?(?![\w])")


def _filter_as_of(records: list[data.Record], as_of: str) -> list[data.Record]:
    return [r for r in records if r.date == "current" or not r.date or r.date[: len(as_of)] <= as_of]


def _norm_numbers(text: str) -> set[str]:
    out = set()
    for tok in NUM.findall(text):
        t = tok.lstrip("$").rstrip("xX%MKk").replace(",", "")
        try:
            out.add(f"{float(t):g}")
        except ValueError:
            pass
    return out


def verify(sheet: FactSheet, index: dict[str, data.Record]) -> tuple[list[Fact], list[dict]]:
    """Keep facts whose ids exist and whose figures appear in a cited record."""
    ok, problems = [], []
    for f in sheet.facts:
        missing = [s for s in f.source_ids if s not in index]
        cited = " ".join(index[s].text + " " + index[s].date for s in f.source_ids if s in index)
        cited_nums = _norm_numbers(cited)
        # Years, quarters and month numbers in dates show up as bare integers; skip small ones.
        unmatched = [n for n in _norm_numbers(f.statement)
                     if n not in cited_nums and not re.fullmatch(r"20\d\d|[1-4]|1[0-2]|[5-9]", n)]
        if missing or unmatched or not f.source_ids:
            problems.append({"statement": f.statement, "source_ids": f.source_ids,
                             "unknown_ids": missing, "figures_not_in_sources": unmatched})
        else:
            ok.append(f)
    return ok, problems


def unsourced_figures(draft: str, index: dict[str, data.Record]) -> list[dict]:
    """Sentence-level check on the draft: every figure must appear in a record the sentence cites.
    Figures Claude computed (differences, percentages) fail this by design; the RM checks them."""
    out = []
    for sent in re.split(r"\n\s*\n|(?<=[.!?\]])\s+(?=[A-Z*-])", draft):
        ids = re.findall(r"[A-Z]+:[A-Z0-9:.\-]+", " ".join(re.findall(r"\[([^\]]+)\]", sent)))
        if not ids:
            continue
        body = re.sub(r"\[[^\]]+\]", "", sent)
        cited = " ".join(index[i].text + " " + index[i].date for i in ids if i in index)
        extra = [n for n in _norm_numbers(body) - _norm_numbers(cited)
                 if not re.fullmatch(r"20\d\d|[1-9]|1[0-2]", n)]
        if extra:
            out.append({"sentence": body.strip()[:300], "figures_not_in_cited_sources": extra})
    return out


def lexicon_hits(text: str) -> list[str]:
    hits = []
    for sent in re.split(r"(?<=[.!?])\s+", text):
        for pat in CREDIT_LEXICON:
            if re.search(pat, sent, re.IGNORECASE):
                hits.append(sent.strip())
                break
    return hits


def financial_table(borrower: str, as_of: str) -> str:
    """Quarter-end figures rendered by code, so no number in the table passes through the model."""
    rows = [r for r in data.performance(borrower) if r.date <= as_of[:7]]
    quarter_ends = [r for r in rows if r.date[5:] in ("03", "06", "09", "12")]
    if rows and rows[-1] not in quarter_ends:
        quarter_ends.append(rows[-1])
    m = rows[0].meta if rows else {}
    head = ("| Period | Revenue ($K, month) | EBITDA margin | DSCR (TTM) | Leverage | Revolver util. | Covenant status |\n"
            "|---|---|---|---|---|---|---|")
    body = "\n".join(
        f"| {r.date} | {r.meta['monthly_revenue_k']} | {r.meta['ebitda_margin_pct']}% | {r.meta['dscr_ttm']}x | "
        f"{r.meta['leverage_ratio']}x | {r.meta['revolver_utilization_pct']}% | {r.meta['covenant_status']} |"
        for r in quarter_ends)
    covenants = (f"Covenants: DSCR minimum {m.get('covenant_dscr_min')}x, leverage maximum "
                 f"{m.get('covenant_leverage_max')}x. Source: PERF records, borrower self-reported.")
    return f"{head}\n{body}\n\n{covenants}"


def run(borrower: str, as_of: str, rm_notes_path: str | None) -> Run:
    borrower = data.resolve_borrower(borrower)
    data.check_allowed(borrower)  # policy 5: refuse before anything is sent
    run = Run(f"memo-{data.SHORT[borrower]}-{as_of}")

    # 1 retrieve. The prior memo is left out on purpose: it's the answer key for evaluation,
    # and a new memo should be built from records, not from last year's prose.
    records = _filter_as_of(data.all_records(borrower, include_memo=False), as_of)
    index = data.source_index(records)
    evidence = "\n".join(r.render() for r in records)
    run.save("01_retrieved_evidence.md", f"# Evidence for {borrower}, as of {as_of}\n\n{evidence}\n")

    # 2 facts
    sheet: FactSheet = run.call(
        "facts", prompt("memo_1_facts"),
        f"Borrower: {borrower}\nAs-of date: {as_of}\n\nRECORDS:\n{evidence}", FactSheet)

    # 3 verify
    good, problems = verify(sheet, index)
    run.save("03_verification.json", {"kept": len(good), "held_back": problems})

    # 4 draft (factual sections only)
    fact_text = "\n".join(f"- ({f.section}) {f.statement} [{', '.join(f.source_ids)}]" for f in good)
    draft: str = run.call(
        "draft", prompt("memo_2_draft"),
        f"Borrower: {borrower}\nAs-of date: {as_of}\n\nVERIFIED FACT SHEET:\n{fact_text}")

    # 5 RM sections: polish the RM's own notes, or leave an explicit slot
    redaction_notes: list[str] = []
    if rm_notes_path:
        raw_notes = re.sub(r"<!--.*?-->", "", open(rm_notes_path, encoding="utf-8").read(), flags=re.S).strip()
        # Redact line by line: bullet notes often have no sentence punctuation.
        cleaned = [data.redact(line) for line in raw_notes.splitlines()]
        safe_notes, n = "\n".join(t for t, _ in cleaned), sum(c for _, c in cleaned)
        if n:
            redaction_notes.append(
                f"{n} line(s) of your notes referenced an internal classification and were not sent to "
                "Claude (policy 2.1). Add that wording to the final memo yourself.")
        polished: Polished = run.call("rm_polish", prompt("memo_3_rm_polish"), f"RM NOTES:\n{safe_notes}", Polished)
        assessment, recommendation = polished.assessment, polished.recommendation
    else:
        polished = None
        assessment = recommendation = "> **[RM TO WRITE]** Policy 4.2: credit judgment must come from the RM. Claude leaves this blank."

    # 6 policy 4.2 check on AI-authored text only
    hits = lexicon_hits(draft)
    review: Review = run.call("compliance_review", prompt("memo_4_compliance"),
                              f"AI-AUTHORED SECTIONS:\n\n{draft}", Review)
    revised = draft
    for f in review.flags:
        if f.sentence in revised:
            revised = revised.replace(f.sentence, f.rewrite)
    residual = lexicon_hits(revised)
    derived = unsourced_figures(revised, index)
    run.save("06_draft_figure_check.json", derived)
    run.save("06_compliance.json", {
        "lexicon_hits_before": hits, "model_flags": [f.model_dump() for f in review.flags],
        "lexicon_hits_after_rewrite": residual})

    # 7 assemble
    memo = f"""# {borrower}: Relationship Review (DRAFT)

**As of:** {as_of} · **RM:** {index[f'PROFILE:{data.SHORT[borrower]}'].meta['rm_name']}

> **AI-assisted draft.** Sections 1–6 were drafted by Claude for Work from cited bank records
> (source ids in brackets) and checked against AI Use Policy 4.2. Sections 7–8 are the RM's own
> assessment, edited for prose only. The RM must review the whole document before it is filed
> (policy 4.3), and its AI assistance is disclosed here (policy 5).

{revised}

## Financial Summary (quarter-end, rendered from records)

{financial_table(borrower, as_of)}

## RM Assessment

{assessment}

## RM Recommendation

{recommendation}
"""
    run.save("memo.md", memo)

    review_sheet = ["# RM review sheet (not part of the memo)\n"]
    if redaction_notes:
        review_sheet += ["## Redactions", *[f"- {n}" for n in redaction_notes], ""]
    review_sheet.append("## Records disagree. Pick the right version before filing")
    for c in sheet.conflicts:
        review_sheet.append(f"- **{c.topic}**: " + "; ".join(f"“{v.claim}” [{v.source_id}]" for v in c.versions)
                            + f". *Affects:* {c.affects}")
    review_sheet.append("\n## Missing or never received")
    review_sheet += [f"- {g.item}" + (f" (last asked: [{g.last_requested_source}])" if g.last_requested_source else "")
                     for g in sheet.gaps]
    if problems:
        review_sheet.append("\n## Facts held back (could not be matched to a source)")
        review_sheet += [f"- {p['statement']} (cited {p['source_ids']}; unmatched figures {p['figures_not_in_sources']}; unknown ids {p['unknown_ids']})"
                         for p in problems]
    if derived:
        review_sheet.append("\n## Figures in the draft not found in the cited record (usually Claude's arithmetic). Check these")
        review_sheet += [f"- {d['figures_not_in_cited_sources']}: “{d['sentence']}”" for d in derived]
    review_sheet.append("\n## Compliance check (policy 4.2) on AI-authored sections")
    review_sheet.append(f"- Lexicon hits before review: {len(hits)}. Reviewer flags: {len(review.flags)}, rewritten neutrally. "
                        f"Lexicon hits remaining: {len(residual)}.")
    review_sheet += [f"  - Flagged: “{f.sentence}” ({f.rule}) → “{f.rewrite}”" for f in review.flags]
    review_sheet += [f"  - STILL PRESENT, edit by hand: “{s}”" for s in residual]
    if polished and polished.questions_for_rm:
        review_sheet.append("\n## Questions on your notes")
        review_sheet += [f"- {q}" for q in polished.questions_for_rm]
    run.save("rm_review_sheet.md", "\n".join(review_sheet) + "\n")
    print(f"Done: {run.dir}")
    return run


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("borrower")
    ap.add_argument("--as-of", required=True, help="YYYY-MM-DD; records after this date are excluded")
    ap.add_argument("--rm-notes", help="path to the RM's own assessment notes")
    a = ap.parse_args()
    run(a.borrower, a.as_of, a.rm_notes)
