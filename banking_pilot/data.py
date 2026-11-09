"""Data access layer for the Northfield pilot.

Every workflow (the MCP server and both pipelines) reads bank data through this
module, so the policy controls live in one place instead of in each prompt:

- Policy 2.1: internal credit ratings / watchlist / Special Assets designations are
  prohibited model inputs. `credit_grade` is dropped from profiles, and sentences that
  reference an internal classification are redacted from free text.
- Policy 5: borrowers in Special Assets or litigation are refused outright
  (config/restricted_borrowers.json; in production this comes from the core system flag).

Every record carries a stable source id so model output can be checked against it.
"""
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TEXT = DATA / "text"
CONFIG = ROOT / "config"

# Columns that are never sent to a model (policy 2.1: internal credit ratings).
PROHIBITED_COLUMNS = {"credit_grade"}

# Free-text references to internal classifications (policy 2.1).
_REDACT_PATTERN = re.compile(
    r"watch\s?list|special assets|credit grade|risk rating|criticized|classified asset",
    re.IGNORECASE,
)
REDACTION = "[REDACTED: internal classification reference, policy 2.1]"

SHORT = {
    "Meridian Fabrication LLC": "MER",
    "BlueLine Logistics LLC": "BLU",
    "Crestwood Capital Advisors": "CRE",
    "Summit Retail Partners": "SUM",
    "Arcadia Property Group": "ARC",
}


class RestrictedBorrowerError(Exception):
    """Raised when a workflow asks for a borrower AI may not touch (policy 5)."""


@dataclass
class Record:
    source_id: str
    date: str
    kind: str
    text: str
    meta: dict = field(default_factory=dict)

    def render(self) -> str:
        return f"[{self.source_id}] ({self.date}, {self.kind}) {self.text}"


def redact(text: str) -> tuple[str, int]:
    """Replace each sentence that mentions an internal classification. Returns (text, count)."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    out, n = [], 0
    for s in sentences:
        if _REDACT_PATTERN.search(s):
            out.append(REDACTION)
            n += 1
        else:
            out.append(s)
    return " ".join(out), n


def resolve_borrower(name: str) -> str:
    """Accept a full name, short code, or unambiguous prefix ("meridian")."""
    key = name.strip().lower()
    for full, code in SHORT.items():
        if key in (full.lower(), code.lower()) or full.lower().startswith(key):
            return full
    raise KeyError(f"Unknown borrower: {name!r}. Known: {', '.join(SHORT)}")


def restricted_borrowers() -> dict[str, str]:
    path = CONFIG / "restricted_borrowers.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def check_allowed(borrower: str) -> None:
    reason = restricted_borrowers().get(borrower)
    if reason:
        raise RestrictedBorrowerError(
            f"{borrower} is flagged '{reason}'. Policy section 5 prohibits AI analysis or "
            "drafting for borrowers in Special Assets or active litigation. Work this one manually."
        )


def _read_csv(name: str) -> list[dict]:
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def profile(borrower: str) -> Record:
    borrower = resolve_borrower(borrower)
    check_allowed(borrower)
    row = next(r for r in _read_csv("portfolio_reference.csv") if r["borrower_name"] == borrower)
    safe = {k: v for k, v in row.items() if k not in PROHIBITED_COLUMNS}
    text = "; ".join(f"{k}={v}" for k, v in safe.items())
    return Record(f"PROFILE:{SHORT[borrower]}", "current", "portfolio reference", text, safe)


def performance(borrower: str) -> list[Record]:
    borrower = resolve_borrower(borrower)
    check_allowed(borrower)
    recs = []
    for r in _read_csv("loan_performance_monthly.csv"):
        if r["borrower_name"] != borrower:
            continue
        fields = {k: v for k, v in r.items() if k not in ("borrower_name",)}
        notes, _ = redact(fields.pop("notes") or "")
        text = "; ".join(f"{k}={v}" for k, v in fields.items() if k != "date")
        if notes:
            text += f"; notes={notes}"
        recs.append(Record(f"PERF:{SHORT[borrower]}:{r['date']}", r["date"], "monthly performance", text, fields))
    return recs


def activity(borrower: str) -> list[Record]:
    borrower = resolve_borrower(borrower)
    check_allowed(borrower)
    recs = []
    for r in _read_csv("rm_activity_log.csv"):
        if r["borrower_name"] != borrower:
            continue
        notes, _ = redact(r["raw_notes"])
        text = (
            f"{r['contact_type']} | {r['contact_direction']} | {r['contact_method']} | "
            f"{r['duration_minutes']} min | outcome={r['outcome']} | by {r['logged_by']} | {notes}"
        )
        recs.append(Record(f"CRM:{r['log_date']}:{SHORT[borrower]}", r["log_date"], "CRM log", text,
                           {"notes_quality": r["notes_quality"], "rm": r["rm_name"]}))
    return recs


_MONTHS = {m: i for i, m in enumerate(
    "January February March April May June July August September October November December".split(), 1)}


def _iso(date_text: str) -> str:
    m = re.match(r"(\w+) (\d{1,2}), (\d{4})", date_text)
    if not m:
        return date_text
    return f"{m.group(3)}-{_MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"


def _parse_threads() -> dict[str, list[Record]]:
    # pdftotext marks page breaks with form feeds, which hide "From:" line starts.
    raw = (TEXT / "emails.txt").read_text(encoding="utf-8").replace(chr(12), chr(10))
    threads: dict[str, list[Record]] = {}
    parts = re.split(r"^Thread (\d) — (.+)$", raw, flags=re.M)
    for i in range(1, len(parts), 3):
        num, name, body = parts[i], parts[i + 1].strip(), parts[i + 2]
        recs: list[Record] = []
        # Bracketed editorial/CRM notes sit between messages; split them out first.
        chunks = re.split(r"(^\[.*?\]$)", body, flags=re.M | re.S)
        msg_n = note_n = 0
        for chunk in chunks:
            chunk = chunk.strip().strip("-").strip()
            if not chunk:
                continue
            if chunk.startswith("["):
                note_n += 1
                text, _ = redact(chunk.strip("[]"))
                d = re.search(r"(\w+ \d{1,2}, \d{4})", chunk)
                recs.append(Record(f"NOTE:T{num}.{note_n}", _iso(d.group(1)) if d else "", "record note", text))
                continue
            for msg in re.split(r"^(?=From: )", chunk, flags=re.M):
                msg = " ".join(msg.split())
                if not msg.startswith("From:"):
                    continue
                msg_n += 1
                d = re.search(r"Date: (\w+ \d{1,2}, \d{4})", msg)
                text, _ = redact(msg)
                recs.append(Record(f"EMAIL:T{num}.{msg_n}", _iso(d.group(1)) if d else "", "email", text))
        threads[name] = recs
    return threads


def emails(borrower: str) -> list[Record]:
    borrower = resolve_borrower(borrower)
    check_allowed(borrower)
    return _parse_threads().get(borrower, [])


def memo(borrower: str) -> list[Record]:
    """Prior RM-written relationship review, split into paragraphs (only Meridian has one)."""
    borrower = resolve_borrower(borrower)
    check_allowed(borrower)
    if borrower != "Meridian Fabrication LLC":
        return []
    raw = (TEXT / "meridian_fabrication_relationship_review.txt").read_text(encoding="utf-8")
    paras = [" ".join(p.split()) for p in raw.replace("\f", "\n").splitlines() if p.strip()]
    paras = [p for p in paras if not p.startswith(("Meridian Fabrication LLC — Relationship", "Prepared by:"))]
    merged: list[str] = []
    for p in paras:  # rejoin paragraphs that a page break split mid-sentence
        if merged and p[0].islower():
            merged[-1] += " " + p
        else:
            merged.append(p)
    recs = []
    for n, p in enumerate(merged, 1):
        text, _ = redact(p)
        recs.append(Record(f"MEMO:MER.{n}", "2025-01-31", "prior RM memo (S. Okonkwo)", text))
    return recs


def borrowers_for_rm(rm: str) -> list[str]:
    rows = _read_csv("portfolio_reference.csv")
    names = [r["borrower_name"] for r in rows if rm.lower() in r["rm_name"].lower()]
    if not names:
        raise KeyError(f"No borrowers for RM {rm!r}")
    return names


def all_records(borrower: str, include_memo: bool = True) -> list[Record]:
    recs = [profile(borrower), *performance(borrower), *activity(borrower), *emails(borrower)]
    if include_memo:
        recs += memo(borrower)
    return recs


def source_index(records: list[Record]) -> dict[str, Record]:
    return {r.source_id: r for r in records}
