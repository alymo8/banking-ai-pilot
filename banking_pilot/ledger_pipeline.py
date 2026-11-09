"""Open-items ledger: who owes what to whom, since when, and does the record show it happened.

Sarah keeps open items on a legal pad, Tom in his head, Marcus nowhere. The asks are
spread across email, CRM and memos, and none of those systems tracks whether an ask was
answered. This pipeline rebuilds that column of the legal pad from the records.

    1 retrieve   (code)    all of one RM's borrowers, as of a date (Special Assets refused)
    2 extract    (Claude)  every request/commitment, merged across sources, cited
    3 reconcile  (Claude)  per item: done / partly / no record / superseded, with evidence
    4 compute    (code)    days open, times asked, overdue vs as-of date: no model arithmetic
    5 render     (code)    the Monday sheet, sorted by due date, no borrower ranking
    6 drafts     (Claude, optional)  one follow-up email per borrower for items owed by them

Run on demand by the RM over their own book (policy 3.2/3.3). It is not scheduled and does not
alert anyone else. Scheduling it would make it automated monitoring under policy 4.1, which needs
CCO approval first.

Usage:
    python -m banking_pilot.ledger_pipeline "Sarah Okonkwo" --as-of 2025-06-02 --drafts
"""
from __future__ import annotations

import argparse
from datetime import date
from typing import Literal

from pydantic import BaseModel

from banking_pilot import data
from banking_pilot.llm import Run, prompt
from banking_pilot.memo_pipeline import _filter_as_of, lexicon_hits


class Item(BaseModel):
    item_id: str
    description: str
    owed_by: str
    owed_to: str
    party: Literal["borrower", "rm", "bank_internal"]
    kind: Literal["document_or_information", "meeting_or_call", "reply_or_deliverable", "condition_or_limit"]
    first_asked_date: str
    first_asked_source: str
    repeat_asks: list[str]
    due_date: str | None
    due_basis: str | None


class Extracted(BaseModel):
    items: list[Item]


class Status(BaseModel):
    item_id: str
    status: Literal["done", "partly_done", "no_record", "superseded"]
    evidence: str
    evidence_source_ids: list[str]
    observed: str | None


class Reconciled(BaseModel):
    statuses: list[Status]


class Chase(BaseModel):
    subject: str
    body: str


BANK_SIDE = ("northfield", "credit committee", "marcus chen", "priya voss", "pricing", "senior credit officer")


def checked_party(it: Item, rm: str) -> str:
    """Code backstop for the extract prompt's party rule. Returns the corrected party."""
    who = it.owed_by.lower()
    if it.party == "borrower":
        if rm.lower() in who:
            return "rm"
        if any(b in who for b in BANK_SIDE):
            return "bank_internal"
        # A proposed cap or restriction is the bank's to put in place, whoever it binds.
        if it.kind == "condition_or_limit" and any(w in it.description.lower()
                                                   for w in ("proposed", "restrict", "cap ", "reset", "fee")):
            return "bank_internal"
    return it.party


def _d(s: str | None) -> date | None:
    try:
        return date.fromisoformat(s) if s else None
    except ValueError:
        return None


def run(rm: str, as_of: str, drafts: bool) -> Run:
    run = Run(f"ledger-{rm.split()[0]}-{as_of}")
    today = date.fromisoformat(as_of)
    sheet = [f"# Open items: {rm}'s book, as of {as_of}\n",
             "> AI-assisted, built on demand from your email, CRM and memos. Every line cites its source.",
             "> \"No record\" means nothing in the systems shows it was done. It does not mean it didn't happen.",
             "> Only you see this. It isn't scheduled, scored or shared.\n"]
    refused, all_rows = [], []

    for borrower in data.borrowers_for_rm(rm):
        try:
            data.check_allowed(borrower)
        except data.RestrictedBorrowerError as e:
            refused.append(str(e))
            continue
        records = _filter_as_of(data.all_records(borrower, include_memo=True), as_of)
        index = data.source_index(records)
        evidence = "\n".join(r.render() for r in records)
        code = data.SHORT[borrower]
        run.save(f"{code}_evidence.md", evidence)

        ext: Extracted = run.call(f"extract_{code}", prompt("ledger_1_extract"),
                                  f"Borrower: {borrower}\nAs-of date: {as_of}\n\nRECORDS:\n{evidence}", Extracted)
        items_txt = "\n".join(i.model_dump_json() for i in ext.items)
        rec: Reconciled = run.call(f"reconcile_{code}", prompt("ledger_2_reconcile"),
                                   f"As-of date: {as_of}\n\nLEDGER ITEMS:\n{items_txt}\n\nRECORDS:\n{evidence}", Reconciled)
        status = {s.item_id: s for s in rec.statuses}

        rows = []
        for it in ext.items:
            s = status.get(it.item_id)
            first, due = _d(it.first_asked_date), _d(it.due_date)
            unknown = [x for x in [it.first_asked_source, *it.repeat_asks, *(s.evidence_source_ids if s else [])]
                       if x not in index]
            party = checked_party(it, rm)
            rows.append({
                "borrower": borrower, **it.model_dump(), "party": party,
                "party_corrected_from": it.party if party != it.party else None,
                "status": s.status if s else "not_reconciled",
                "evidence": s.evidence if s else "", "observed": s.observed if s else None,
                "evidence_ids": s.evidence_source_ids if s else [],
                "times_asked": 1 + len(it.repeat_asks),
                "days_open": (today - first).days if first else None,
                "days_past_due": (today - due).days if due and today > due else None,
                "unknown_source_ids": unknown,
            })
        open_rows = [r for r in rows if r["status"] in ("no_record", "partly_done", "not_reconciled")]
        open_rows.sort(key=lambda r: (r["days_past_due"] is None, -(r["days_past_due"] or 0), r["first_asked_date"]))
        closed = [r for r in rows if r not in open_rows]
        all_rows += rows

        sheet.append(f"## {borrower}\n")
        for party, title in (("borrower", "Waiting on the borrower"), ("rm", "You said you would"),
                             ("bank_internal", "Inside the bank")):
            group = [r for r in open_rows if r["party"] == party]
            if not group:
                continue
            sheet.append(f"### {title}\n")
            sheet.append("| Item | Owed by → to | First asked | Asked | Due | Status | What the record shows |")
            sheet.append("|---|---|---|---|---|---|---|")
            for r in group:
                due = r["due_date"] or "none stated"
                if r["days_past_due"]:
                    due += f" (**{r['days_past_due']}d past**)"
                shows = r["evidence"] + (f" Observed: {r['observed']}" if r["observed"] else "")
                sheet.append(
                    f"| {r['description']} | {r['owed_by']} → {r['owed_to']} | {r['first_asked_date']} [{r['first_asked_source']}] "
                    f"| {r['times_asked']}× | {due} | {r['status'].replace('_', ' ')} | {shows} |")
            sheet.append("")
        if closed:
            sheet.append(f"<details><summary>{len(closed)} closed or superseded</summary>\n")
            sheet += [f"- {r['description']} ({r['status']}): {r['evidence']}" for r in closed]
            sheet.append("\n</details>\n")

        if drafts:
            # Chase only what is late or was asked for with no date. Never chase something not yet due.
            owed = [r for r in open_rows if r["party"] == "borrower" and r["kind"] == "document_or_information"
                    and (r["days_past_due"] or (r["due_date"] is None and r["first_asked_date"] < as_of))]
            if owed:
                contact = index[f"PROFILE:{code}"].meta
                lines = "\n".join(f"- {r['description']} (first requested {r['first_asked_date']}; {r['times_asked']} recorded mention(s) in total, "
                                  f"including internal notes, so don't count requests to the borrower from this)"
                                  for r in owed)
                ch: Chase = run.call(
                    f"chase_{code}", prompt("ledger_3_chase"),
                    f"From: {rm}\nTo: {contact['primary_contact']}, {contact['primary_contact_title']}, {borrower}\n"
                    f"Relationship since: {contact['relationship_since']}\n\nOUTSTANDING ITEMS:\n{lines}\n\nrm_added_points: (none)",
                    Chase, effort="medium")
                flags = lexicon_hits(ch.body)
                sheet.append(f"### Draft follow-up to {contact['primary_contact']} (review before sending)\n")
                sheet.append(f"**Subject:** {ch.subject}\n\n" + "\n".join(f"> {l}" for l in ch.body.splitlines()))
                if flags:
                    sheet.append("\n**Policy 4.2 check flagged:** " + " | ".join(flags))
                sheet.append("")

    if refused:
        sheet.append("## Not processed\n")
        sheet += [f"- {r}" for r in refused]
    run.save("ledger_rows.json", all_rows)
    run.save("open_items.md", "\n".join(sheet) + "\n")
    print(f"Done: {run.dir}")
    return run


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("rm", help='RM name, e.g. "Sarah Okonkwo"')
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--drafts", action="store_true", help="also draft follow-up emails for borrower-owed items")
    a = ap.parse_args()
    run(a.rm, a.as_of, a.drafts)
