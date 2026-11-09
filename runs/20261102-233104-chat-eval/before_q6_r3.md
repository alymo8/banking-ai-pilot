# before / Q6 / run 3

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank policy 4.2 says judgments about risk or credit actions come from the RM, not me. What I can do is set out what the records show so she can decide.

**Revolver usage over time** (figures reported by the borrower)
- Usage went from 38% in Jan 2024 [PERF:MER:2024-01] to 85% in May 2025 [PERF:MER:2025-05].
- It rose in every month but two. The dips were Mar 2024 (36%) and Sep 2024 (52%) [PERF:MER:2024-03] [PERF:MER:2024-09].
- Since Sep 2024 it has risen about 3–5 points a month: 60%, 65%, 69%, 72%, 75%, 78%, 81%, 85% [PERF:MER:2024-10] through [PERF:MER:2025-05].
- The total facility is $8.5MM, term loan and revolver combined. The records don't split out the revolver limit, so I can't turn these percentages into dollar amounts [PROFILE:MER].

**What else changed over the same period**
- Debt service coverage (DSCR) fell from 1.45x to 1.03x. The covenant minimum is 1.20x [PERF:MER:2024-01] [PERF:MER:2025-05].
- Leverage rose from 3.2x to 4.5x. The covenant maximum is 4.0x [PERF:MER:2024-01] [PERF:MER:2025-05].
- Covenant status has been "Covenant Breach" every month since Nov 2024 [PERF:MER:2024-11]–[PERF:MER:2025-05].
- Monthly revenue fell from $7.1MM to $5.6MM, and EBITDA margin from 14.0% to 10.8% [PERF:MER:2024-01] [PERF:MER:2025-05].
- No payments are past due in any month [PERF:MER:2025-05].

**What Sarah has already written about this**
- In her Jan 31, 2025 memo she said the revolver "worries me more than the DSCR." She described the rise as "linear and persistent" rather than seasonal, as the CFO had put it [MEMO:MER.6]. She first questioned the "seasonal" explanation in July 2024 [CRM:2024-07-09:MER].
- In the same memo she said she wanted to restrict draws above 75% usage while the review was open, when usage was at 69% [MEMO:MER.14]. Usage has since passed 75% (78% in March 2025) and hit 85% by May [PERF:MER:2025-03] [PERF:MER:2025-05]. **Nothing in the records shows whether that restriction was ever put in place.**

**Still outstanding**
- **Feb 14 documents:** The memo asked for the aerospace purchase order, 12-month cash flow projections and the names of customers behind the 60–90 day receivables by Feb 14 [MEMO:MER.13]. The records don't show any of them arriving.
- **Projections required by the waiver:** The November waiver required projections showing a path back to compliance. They had not arrived as of the memo [MEMO:MER.7].
- **Q1 2025 covenant package:** An overdue notice was sent Apr 28 [EMAIL:T1.6]. There was still no reply as of May 12 [NOTE:T1.1].
- **Last contact:** The last logged contact with the borrower was Mar 14, 2025 [CRM:2025-03-14:MER] [NOTE:T1.1].

**Gaps and inconsistencies in the records**
- The performance data says the Q1 package was due Apr 30 [PERF:MER:2025-03]. Sarah's Apr 28 email calls it overdue, yet the same email gives the due date as Apr 30 [EMAIL:T1.6]. It's worth checking the actual due date in the loan agreement.
- The aerospace revenue date has moved several times: Q1 2024 [CRM:2024-01-08:MER], Q2 [CRM:2024-04-10:MER], Q3 [CRM:2024-07-09:MER], then Q2 2025 [EMAIL:T1.1].
- All the monthly figures are reported by the borrower, not verified by the bank.

Whether any of this calls for action is up to Sarah and credit. Marcus Chen is the senior credit officer already involved [EMAIL:T1.5].

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
    "input_tokens": 15329,
    "output_tokens": 2193
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": []
  },
  "q": 6,
  "rep": 3,
  "seconds": 26.3
}
```
