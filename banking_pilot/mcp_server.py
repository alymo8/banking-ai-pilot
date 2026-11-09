"""Northfield Bank MCP server: read-only, policy-filtered tools over the pilot data.

In Claude Desktop / Claude for Work the RM asks a question and Claude fetches only the
records it needs, instead of the RM pasting tables into the prompt (Tom's pattern).
The filters in banking_pilot.data run inside every tool, so no prompt can get around them:
credit grade never leaves the server, internal classification references are redacted,
and Special Assets borrowers are refused.

Run:  python -m banking_pilot.mcp_server   (stdio)
"""
from __future__ import annotations

import os

from mcp.server.mcpserver import MCPServer

from banking_pilot import data

# BANK_PILOT_MCP_LIMIT_RULES=0 turns off the limits rule added after the Desktop finding
# (notes/03-mcp-chat-finding.md). Only scripts/chat_route_eval.py uses it, as the "before" arm.
LIMIT_RULES = os.environ.get("BANK_PILOT_MCP_LIMIT_RULES", "1") != "0"

BASE_INSTRUCTIONS = (
    "Read-only access to Northfield Bank commercial relationship records for the Claude "
    "pilot. Every record has a source id in [brackets]; cite source ids for every fact. "
    "Policy 4.2: do not characterize creditworthiness, risk level, or likelihood of breach, "
    "and do not recommend credit actions. Those words come from the RM only."
)
LIMIT_INSTRUCTIONS = (
        "When asked whether a limit, cap or covenant was met, respected or exceeded, do not answer "
        "yes or no and do not use the words breach, violation, exceeded or non-compliant yourself: "
        "show each reading next to the limit, with source ids, and say whether the record shows the "
        "limit was put in place. A field the bank recorded (e.g. covenant_status) may be quoted "
        "verbatim with its source id, labeled as the bank's recorded field. The conclusion is the RM's. "
        "If you decline to give a yes/no, say it is this pilot's rule for AI answers, which applies "
        "policy 4.2. Policy 4.2 itself does not mention yes/no answers, so do not say it does. "
        "Do not explain what a field means or covers unless a record says so; if you infer it, "
        "say it is your inference."
)

server = MCPServer(
    name="northfield-bank",
    instructions=BASE_INSTRUCTIONS + (" " + LIMIT_INSTRUCTIONS if LIMIT_RULES else ""),
)


LIMITS_NOTE = "" if not LIMIT_RULES else (
    "\n\n[Reminder, this pilot's rule applying policy 4.2: state readings next to any limit; no yes/no "
    "verdict on whether it was met and no breach language of your own. The conclusion is the RM's. "
    "Say it is this pilot's rule, not the policy's wording.]")


def _guard(fn, *args) -> str:
    try:
        recs = fn(*args)
    except data.RestrictedBorrowerError as e:
        return f"REFUSED: {e}"
    except KeyError as e:
        return f"ERROR: {e}"
    if isinstance(recs, data.Record):
        recs = [recs]
    if not recs:
        return "No records."
    return "\n".join(r.render() for r in recs)


@server.tool()
def list_borrowers(rm_name: str = "") -> str:
    """List borrowers (optionally for one RM) with industry and RM. Credit grades are not exposed."""
    rows = data._read_csv("portfolio_reference.csv")
    out = []
    for r in rows:
        if rm_name and rm_name.lower() not in r["rm_name"].lower():
            continue
        flag = data.restricted_borrowers().get(r["borrower_name"])
        status = f" [RESTRICTED: {flag}]" if flag else ""
        out.append(f"{r['borrower_name']} | {r['industry']} | RM {r['rm_name']}{status}")
    return "\n".join(out) or "No borrowers."


@server.tool()
def get_borrower_profile(borrower: str) -> str:
    """Relationship metadata: facility, rate, maturity, contacts, covenant due date."""
    return _guard(data.profile, borrower)


@server.tool(description="Monthly financials and covenant status (YYYY-MM range, inclusive). Borrower self-reported."
                         + (" Report readings next to their limits. Do not give a yes/no verdict on whether a limit "
                            "was met." if LIMIT_RULES else ""))
def get_monthly_performance(borrower: str, from_month: str = "", to_month: str = "") -> str:
    def rows(b):
        return [r for r in data.performance(b)
                if (not from_month or r.date >= from_month) and (not to_month or r.date <= to_month)]
    out = _guard(rows, borrower)
    return out if out.startswith(("REFUSED", "ERROR", "No records")) else out + LIMITS_NOTE


@server.tool()
def get_activity_log(borrower: str) -> str:
    """CRM contact log entries. Reflects what was logged, not necessarily everything that happened."""
    return _guard(data.activity, borrower)


@server.tool()
def get_email_threads(borrower: str) -> str:
    """Email correspondence with the borrower and internal emails about it."""
    return _guard(data.emails, borrower)


@server.tool(description="Most recent RM-written relationship review memo, by paragraph."
                         + (" Proposals in the memo (caps, deadlines, waivers) are the RM's proposals, not "
                            "decisions in effect." if LIMIT_RULES else ""))
def get_prior_memo(borrower: str) -> str:
    out = _guard(data.memo, borrower)
    return out if out.startswith(("REFUSED", "ERROR", "No records")) else out + LIMITS_NOTE


if __name__ == "__main__":
    server.run()
