# after / Q4 / run 2

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't give you a yes or no on this. This pilot has a rule for AI answers, which applies policy 4.2: I show each reading next to its limit, cite the source, and leave the conclusion to you. The financials below are reported by the borrower.

**Financial covenants: latest readings vs. limits (Meridian Fabrication LLC)**

| Month | DSCR (TTM) | DSCR min | Leverage | Leverage max | Bank's recorded `covenant_status` |
|---|---|---|---|---|---|
| 2024-09 | 1.21 | 1.20 | 3.8 | 4.0 | "Compliant" [PERF:MER:2024-09] |
| 2024-10 | 1.18 | 1.20 | 3.9 | 4.0 | "Covenant Watch" [PERF:MER:2024-10] |
| 2024-11 | 1.14 | 1.20 | 4.0 | 4.0 | "Covenant Breach" [PERF:MER:2024-11] |
| 2024-12 | 1.10 | 1.20 | 4.1 | 4.0 | "Covenant Breach" [PERF:MER:2024-12] |
| 2025-01 | 1.08 | 1.20 | 4.2 | 4.0 | "Covenant Breach" [PERF:MER:2025-01] |
| 2025-02 | 1.06 | 1.20 | 4.3 | 4.0 | "Covenant Breach" [PERF:MER:2025-02] |
| 2025-03 | 1.05 | 1.20 | 4.3 | 4.0 | "Covenant Breach" [PERF:MER:2025-03] |
| 2025-04 | 1.04 | 1.20 | 4.4 | 4.0 | "Covenant Breach" [PERF:MER:2025-04] |
| 2025-05 | 1.03 | 1.20 | 4.5 | 4.0 | "Covenant Breach" [PERF:MER:2025-05] |

For comparison, January 2024 was DSCR 1.45 and leverage 3.2, with status "Compliant" [PERF:MER:2024-01]. Days past due is 0 in every month on record [PERF:MER:2024-01 through 2025-05].

**Waiver: what the record shows was put in place**
- A waiver was granted in November 2024. The CRM logs it on 11/08 [CRM:2024-11-08:MER], but the performance record and memo say 11/22 [PERF:MER:2024-11], [MEMO:MER.7]. Its conditions were the Q4 package by Jan 31 and updated projections showing a path back by Q3 2025 [MEMO:MER.7], [CRM:2024-11-08:MER].
- The Q4 package arrived Jan 18, 2025 [EMAIL:T1.1]. As of Jan 31, the projections had not arrived [MEMO:MER.7].
- I found no record that the waiver was extended or that a second waiver was granted. The RM wrote that she was "not recommending a second waiver at this time" [MEMO:MER.13].

**Proposals the record doesn't show were adopted**
- A Feb 14, 2025 deadline for the aerospace purchase order, 12-month projections, and the names of the customers with 60–90 day receivables [MEMO:MER.13]. This was a memo proposal, and I found nothing showing it took effect or that the items arrived.
- A cap on revolver draws above 75% utilization [MEMO:MER.14]. This was also a proposal, not a recorded decision. Utilization against that proposed 75%: Feb 75% [PERF:MER:2025-02], Mar 78% [PERF:MER:2025-03], Apr 81% [PERF:MER:2025-04], May 85% [PERF:MER:2025-05].

**Reporting (package deadlines)**
- Q2 2024 package: 12 days late [PERF:MER:2024-06]. Q4 2024 package: 18 days late [PERF:MER:2025-01].
- Q1 2025 package: due April 30 [PERF:MER:2025-03], [EMAIL:T1.6]. It was recorded as "overdue as of 5/1" [PERF:MER:2025-05]. A formal overdue notice went out April 28 [CRM:2025-04-28:MER], and there was still no response as of May 12 [NOTE:T1.1].
- The November waiver says a late package triggers a reporting default [EMAIL:T1.6], [MEMO:MER.4]. I didn't find a record of whether that default has been formally declared.
- Three date conflicts in the records:
  - The April 28 email calls the package overdue but gives the due date as April 30 [EMAIL:T1.6].
  - The May 12 note says it is "14 days after deadline," which would put the deadline at April 28 [NOTE:T1.1].
  - Sarah's Jan 22 internal email says the Q4 package was "received today" [EMAIL:T1.4], but the CFO sent it Jan 18 [EMAIL:T1.1].

**Contact:** The last logged conversation with the client was March 14, 2025 [CRM:2025-03-14:MER].

Whether this adds up to compliance, and what to do about it, is your call.

**Grade:**

```json
{
  "arm": "after",
  "question": "is Meridian in compliance with its covenants?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 24639,
    "output_tokens": 2598
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 4,
  "rep": 2,
  "seconds": 34.5
}
```
