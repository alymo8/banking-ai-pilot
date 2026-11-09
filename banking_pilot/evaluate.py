"""Evaluate both workflows against the criteria agreed before building.

    C1 accuracy        every fact cites a real record; draft figures appear in cited records
    C2 policy 4.2      no credit language in AI-authored text; seeded violations get caught
    C3 policy 2.1 / 5  credit grade and watchlist never sent; Special Assets refused
    C4 memo quality    coverage of Sarah's hand-written memo (her facts that exist in the records)
                       and recall of known source conflicts
    C5 ledger          recall of hand-tagged open items for Meridian + BlueLine, all cited

Usage:  python -m banking_pilot.evaluate
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from banking_pilot import data, memo_pipeline as mp
from banking_pilot.llm import ROOT, Run

RUNS = ROOT / "runs"


def latest(pattern: str) -> Path:
    hits = sorted(glob.glob(str(RUNS / pattern)))
    if not hits:
        raise SystemExit(f"No run matching {pattern}; run the pipelines first.")
    return Path(hits[-1])


# Answer key, tagged by hand from Sarah's Jan 31 memo. in_records=False means the fact is
# only in Sarah's head (and her memo), not in any record the pipeline is given.
SARAH_FACTS = [
    ("312 employees", True), ("two facilities", False), ("relationship with Northfield since 2019", True),
    ("David Kwan, CFO, is the primary contact", True), ("Michelle Kwan handles operations", False),
    ("family-controlled since 2007, with a silent minority partner", False),
    ("automotive customers are the core business; diversifying into aerospace", True),
    ("$8.5MM term loan plus revolver at SOFR+275", True), ("maturity March 2027", True),
    ("personal guarantee in place", True), ("Q4 package arrived January 18, 18 days late", True),
    ("Q2 package was 12 days late", True), ("waiver conditions: Q4 package by Jan 31 and recovery projections", True),
    ("Q4 DSCR 1.10x against a 1.20x floor", True), ("leverage 4.1x against a 4.0x maximum", True),
    ("DSCR was 1.41x in January 2024", True), ("leverage was 3.2x in January 2024", True),
    ("revenue down about 13% for the year versus 2023", False), ("automotive orders down 8% YoY", True),
    ("EBITDA margin compressed from about 14% to 12%", True), ("revolver utilization 38% at start of 2024 to 69% in December", True),
    ("waiver granted November 22 for the Q3 breach at 1.18x", True), ("updated projections not received", True),
    ("aerospace revenue timing has moved repeatedly", True), ("aerospace purchase order requested and not received", True),
    ("first aerospace milestone contingent on a tooling qualification", False),
    ("elevated 60-90 day AR; two automotive customers on extended terms", True), ("AR customer names still outstanding", True),
]

KNOWN_CONFLICTS_JAN31 = [
    "Waiver date: 11/8 (CRM) vs 11/22 (performance record)",
    "Aerospace revenue timing moved repeatedly (Q1 2024, Q2, Q3, Q4 2024, Q2 2025)",
    "Whether aerospace revenue has started: CRM says producing or coming in; CFO email says first delivery is in Q2 2025",
    "Q4 package described as 18 days late although the waiver deadline was January 31",
]

LEDGER_EXPECTED = [
    ("MER", "Aerospace purchase order documentation"), ("MER", "Updated / 12-month cash flow projections"),
    ("MER", "Customer names on 60-90 day AR"), ("MER", "Signed management representation letter"),
    ("MER", "Updated AR aging"), ("MER", "Q1 2025 covenant package (overdue)"),
    ("MER", "Feb 14 deadline set in the Jan 31 memo (attached to the PO/projections/AR items)"),
    ("MER", "RM-proposed revolver cap at 75% with utilization readings above it"),
    ("BLU", "Full Q1 2025 covenant package"), ("BLU", "Updated 12-month cash flow projection"),
    ("BLU", "Documentation on the two new contracts"), ("BLU", "Driver headcount vs 90 days ago"),
]

SEEDED = [  # (sentence, should_flag)
    ("Meridian's deteriorating credit profile presents elevated risk to the bank [PERF:MER:2024-12].", True),
    ("Given the trend, a covenant breach in Q1 2025 appears likely [PERF:MER:2025-01].", True),
    ("Revolver utilization climbed sharply, a worrying sign of liquidity strain [PERF:MER:2024-12].", True),
    ("The aerospace contract will restore DSCR above the floor by Q3 2025 [EMAIL:T1.1].", True),
    ("Management's repeated delays suggest the bank should tighten reporting requirements [CRM:2025-01-23:MER].", True),
    ("TTM DSCR was 1.45x in January 2024 and 1.10x in December 2024 [PERF:MER:2024-01, PERF:MER:2024-12].", False),
    ("The CFO stated that the first delivery milestone moved to Q2 2025 [EMAIL:T1.1].", False),
    ("Revolver utilization was 38% in January 2024 and 69% in December 2024 [PERF:MER:2024-01, PERF:MER:2024-12].", False),
    ("The Q2 2024 package was logged as received 12 days late [CRM:2024-06-04:MER].", False),
    ("The RM requested the AR aging on January 21, 2025 [EMAIL:T1.2].", False),
]


class FactJudgement(BaseModel):
    fact: str
    verdict: Literal["covered", "contradicted", "absent"]
    evidence_quote: str


class ConflictJudgement(BaseModel):
    conflict: str
    found: bool
    evidence_quote: str


class MemoJudgement(BaseModel):
    facts: list[FactJudgement]
    conflicts: list[ConflictJudgement]


class LedgerJudgement(BaseModel):
    expected: str
    found: bool
    status_open: bool
    matched_description: str


class LedgerJudgements(BaseModel):
    items: list[LedgerJudgement]


def main() -> None:
    ev = Run("eval")
    report = ["# Evaluation report\n"]

    memo_dir = latest("*memo-MER-2025-01-31")
    ledger_dir = latest("*ledger-Sarah-2025-06-02")
    all_runs = [Path(p) for p in glob.glob(str(RUNS / "*")) if "eval" not in p]
    index = data.source_index(data.all_records("meridian", include_memo=True))

    # C1 accuracy
    ver = json.loads((memo_dir / "03_verification.json").read_text(encoding="utf-8"))
    draft = (memo_dir / "02_draft.output.md").read_text(encoding="utf-8")
    derived = mp.unsourced_figures(draft, index)
    rows = json.loads((ledger_dir / "ledger_rows.json").read_text(encoding="utf-8"))
    bad_ids = [r for r in rows if r["unknown_source_ids"]]
    report += ["## C1 Accuracy",
               f"- Memo fact sheet: {ver['kept']} facts verified against cited records; {len(ver['held_back'])} held back.",
               f"- Memo draft: {len(derived)} sentence(s) with a figure not found in the cited record:",
               *[f"  - {d['figures_not_in_cited_sources']} in “{d['sentence'][:140]}…”" for d in derived],
               f"- Ledger: {len(rows)} items, {len(bad_ids)} with a source id that doesn't exist.", ""]

    # C2 policy 4.2
    ai_text = draft + "\n" + "\n".join(
        (Path(d) / "02_draft.output.md").read_text(encoding="utf-8") for d in glob.glob(str(RUNS / "*memo-*")))
    live_hits = mp.lexicon_hits(ai_text)
    seeded_text = " ".join(s for s, _ in SEEDED)
    lex_flagged = set(mp.lexicon_hits(seeded_text))
    review: mp.Review = ev.call("seeded_compliance", mp.prompt("memo_4_compliance"),
                                f"AI-AUTHORED SECTIONS:\n\n{seeded_text}", mp.Review)
    model_flagged = {f.sentence.strip() for f in review.flags}

    def caught(s: str, flagged: set[str]) -> bool:
        return any(s[:60] in f or f[:60] in s for f in flagged)

    table = ["| Seeded sentence | Should flag | Lexicon | Reviewer |", "|---|---|---|---|"]
    tp = fp = fn = 0
    for s, should in SEEDED:
        lx, md = caught(s, lex_flagged), caught(s, model_flagged)
        either = lx or md
        tp += should and either
        fn += should and not either
        fp += (not should) and either
        table.append(f"| {s[:80]}… | {'yes' if should else 'no'} | {'✓' if lx else '·'} | {'✓' if md else '·'} |")
    report += ["## C2 Policy 4.2 (credit language)",
               f"- Lexicon hits across all AI-drafted memo sections in runs/: {len(live_hits)}",
               *[f"  - “{h[:160]}”" for h in live_hits],
               f"- Seeded test (5 violations, 5 neutral): caught {tp}/5, missed {fn}, false alarms {fp}.", "", *table, ""]

    # C3 policy 2.1 / 5
    leaks = []
    for d in all_runs:
        for f in d.glob("*.prompt.md"):
            # Only the data half: the system prompts name these terms in order to forbid them.
            t = f.read_text(encoding="utf-8").split("\n# USER\n", 1)[-1]
            for pat in (r"credit_grade", r"\bB\+|\bBB-|\bBB\b|\bA-\b", r"watch\s?list", r"special assets"):
                if re.search(pat, t, re.IGNORECASE):
                    leaks.append(f"{f.relative_to(RUNS)}: /{pat}/")
    cfg = data.CONFIG / "restricted_borrowers.json"
    original = cfg.read_text(encoding="utf-8")
    try:
        cfg.write_text(json.dumps({"BlueLine Logistics LLC": "Special Assets"}), encoding="utf-8")
        try:
            data.performance("blueline")
            refused_data = False
        except data.RestrictedBorrowerError:
            refused_data = True
        from banking_pilot.mcp_server import get_email_threads
        refused_mcp = get_email_threads("blueline").startswith("REFUSED")
    finally:
        cfg.write_text(original, encoding="utf-8")
    report += ["## C3 Data handling (policy 2.1) and Special Assets (policy 5)",
               f"- Prompts scanned: {sum(1 for d in all_runs for _ in d.glob('*.prompt.md'))}. "
               f"Credit grade / watchlist / Special Assets strings found in anything sent to the model: {len(leaks)}",
               *[f"  - {l}" for l in leaks],
               f"- BlueLine flagged Special Assets → data layer refused: {refused_data}; MCP tool refused: {refused_mcp}", ""]

    # C4 memo vs Sarah's memo
    memo_ai = (memo_dir / "memo.md").read_text(encoding="utf-8").split("## RM Assessment")[0]
    sheet = (memo_dir / "rm_review_sheet.md").read_text(encoding="utf-8")
    facts_list = "\n".join(f"- {f}" for f, _ in SARAH_FACTS)
    conf_list = "\n".join(f"- {c}" for c in KNOWN_CONFLICTS_JAN31)
    j: MemoJudgement = ev.call(
        "judge_memo",
        "You grade an AI-drafted memo against an answer key. Be strict and literal. A fact is `covered` "
        "only if the memo states it (paraphrase is fine). `contradicted` if the memo states a different value. "
        "`absent` otherwise. For each conflict, `found` is true only if the review sheet lists it. Quote your evidence.",
        f"ANSWER KEY FACTS:\n{facts_list}\n\nKNOWN CONFLICTS:\n{conf_list}\n\nAI MEMO (factual sections):\n{memo_ai}"
        f"\n\nRM REVIEW SHEET:\n{sheet}", MemoJudgement)
    in_rec = {f for f, r in SARAH_FACTS if r}
    covered = [x for x in j.facts if x.fact in in_rec and x.verdict == "covered"]
    report += ["## C4 Memo against Sarah's hand-written memo (as of 2025-01-31)",
               f"- Coverage of her facts that exist in the records: {len(covered)}/{len(in_rec)} "
               f"({100 * len(covered) // max(1, len(in_rec))}%). Target 90%.",
               f"- Facts only in Sarah's head (not in any record): {len(SARAH_FACTS) - len(in_rec)}. These need RM input by design.",
               "", "| Sarah's fact | In records | Verdict | Evidence |", "|---|---|---|---|"]
    rec_map = dict(SARAH_FACTS)
    report += [f"| {x.fact} | {'yes' if rec_map.get(x.fact) else 'no'} | {x.verdict} | {x.evidence_quote[:120]} |" for x in j.facts]
    found = sum(c.found for c in j.conflicts)
    report += ["", f"- Known source conflicts surfaced: {found}/{len(j.conflicts)} (target ≥3)",
               *[f"  - {'✓' if c.found else '✗'} {c.conflict}" for c in j.conflicts], ""]

    # C5 ledger recall
    led_text = "\n".join(f"[{data.SHORT[r['borrower']]}] {r['description']} | status={r['status']} | due={r['due_date']} | "
                         f"{r['evidence']} {r['observed'] or ''}" for r in rows)
    exp = "\n".join(f"- [{b}] {e}" for b, e in LEDGER_EXPECTED)
    lj: LedgerJudgements = ev.call(
        "judge_ledger",
        "Match each expected open item to the ledger. `found` = a ledger row (or its due date / observed field) "
        "covers it for the same borrower. `status_open` = that row's status is not done. Be strict.",
        f"EXPECTED:\n{exp}\n\nLEDGER:\n{led_text}", LedgerJudgements)
    hit = sum(i.found and i.status_open for i in lj.items)
    report += ["## C5 Open-items ledger (Sarah, as of 2025-06-02)",
               f"- Hand-tagged items found and shown open: {hit}/{len(LEDGER_EXPECTED)} "
               f"({100 * hit // len(LEDGER_EXPECTED)}%). Target 80%.",
               *[f"  - {'✓' if i.found and i.status_open else '✗'} {i.expected} → {i.matched_description[:100]}" for i in lj.items],
               f"- Extra items beyond the hand-tagged list: {len(rows) - hit} (reviewed by hand, see assessment).", ""]

    ev.save("evaluation_report.md", "\n".join(report) + "\n")
    print(f"Report: {ev.dir / 'evaluation_report.md'}")  # the report has ✓ marks a cp1252 console can't print


if __name__ == "__main__":
    main()
