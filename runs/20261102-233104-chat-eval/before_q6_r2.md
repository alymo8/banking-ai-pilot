# before / Q6 / run 2

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank policy 4.2 bars me from judging risk or likelihood of breach, or recommending credit actions, so that call is hers. But the records show that she has already raised this herself in writing, and the usage has since gone past the limit she proposed.

**Sarah's own view (Jan 31, 2025 memo)**
- "The revolver situation worries me more than the DSCR." She saw the rise as "linear and persistent," not seasonal, and as the company "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6].
- She proposed blocking further draws above 75% usage while the review was open: "I don't want them drawing the revolver to 85% while we're waiting on documentation" [MEMO:MER.14].

**Revolver usage over time (company-reported)**
- Jan 2024: 38% [PERF:MER:2024-01]
- Jul 2024: 55%. The CFO called it a seasonal working-capital need, and Sarah logged that she wasn't sure she agreed [PERF:MER:2024-07], [CRM:2024-07-09:MER]
- Dec 2024: 69% [PERF:MER:2024-12]
- Feb 2025: 75% [PERF:MER:2025-02]
- Mar 2025: 78% [PERF:MER:2025-03]
- Apr 2025: 81% [PERF:MER:2025-04]
- May 2025: 85% [PERF:MER:2025-05]

It rose in 15 of 17 months, dipping only in Mar 2024 and Sep 2024. The records don't say whether the 75% limit was ever adopted.

**What happened alongside it**
- Debt coverage (DSCR) fell from 1.45x to 1.03x against a 1.20x minimum. Leverage rose from 3.2x to 4.5x against a 4.0x maximum. The status has been "Covenant Breach" every month since Nov 2024 [PERF:MER:2024-01], [PERF:MER:2025-05].
- Monthly revenue fell from $7.1M to $5.6M, and margin from 14.0% to 10.8% [PERF:MER:2024-01], [PERF:MER:2025-05].
- A waiver was granted on Nov 22, 2024 [PERF:MER:2024-11]. Its condition of updated projections had not been met as of Jan 31 [MEMO:MER.7].

**Documents still missing (as of the latest records)**
- The aerospace purchase order, which has been requested several times. The expected revenue date has moved from Q2 2024 to Q4 2024 to Q2 2025 [MEMO:MER.8], [EMAIL:T1.1].
- Customer names on the 60–90 day receivables [MEMO:MER.10], [EMAIL:T1.5].
- The Q1 2025 covenant package. A formal overdue notice went out Apr 28 and got no reply as of May 12 [EMAIL:T1.6], [NOTE:T1.1]. Under the waiver terms, a late package triggers a reporting default [EMAIL:T1.6].
- The last logged contact with the company was Mar 14, 2025 [CRM:2025-03-14:MER].

**Caveats**
- All the financial figures are reported by the company, and the latest is May 2025 [PERF:MER:2025-05].
- The records don't show whether the company met the Feb 14 deadline Sarah proposed [MEMO:MER.13].
- One date conflict: the Apr 28 notice refers to an Apr 30 due date [EMAIL:T1.6], while the performance data marks the package overdue as of 5/1 [PERF:MER:2025-05]. Worth confirming the actual due date before acting on the default clock.

If it would help, I can put this into a short fact summary for Sarah to take to Marcus Chen.

**Grade:**

```json
{
  "arm": "before",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15319,
    "output_tokens": 1968
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "the usage has since gone past the limit she proposed"
    ],
    "credit_characterization": [],
    "recommendation": []
  },
  "q": 6,
  "rep": 2,
  "seconds": 27.7
}
```
