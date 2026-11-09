# after / Q4 / run 1

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't give you a yes or no on compliance. Under Policy 4.2 that call is yours. Here are the readings next to their limits, with sources, so you can decide.

## What the bank recorded
Meridian's `covenant_status` field in the bank's records shows:
- **"Compliant"** from Jan to Sep 2024 [PERF:MER:2024-01 to 2024-09]
- **"Covenant Watch"** in Oct 2024 [PERF:MER:2024-10]
- **"Covenant Breach"** every month from Nov 2024 to May 2025 [PERF:MER:2024-11 to 2025-05]

These are the bank's own recorded labels, quoted word for word. They aren't my assessment.

## Covenant readings vs. limits (figures reported by the borrower)
| Month | DSCR (TTM) | DSCR min | Leverage | Leverage max | Source |
|---|---|---|---|---|---|
| 2024-09 | 1.21 | 1.20 | 3.8 | 4.0 | [PERF:MER:2024-09] |
| 2024-10 | 1.18 | 1.20 | 3.9 | 4.0 | [PERF:MER:2024-10] |
| 2024-11 | 1.14 | 1.20 | 4.0 | 4.0 | [PERF:MER:2024-11] |
| 2024-12 | 1.10 | 1.20 | 4.1 | 4.0 | [PERF:MER:2024-12] |
| 2025-01 | 1.08 | 1.20 | 4.2 | 4.0 | [PERF:MER:2025-01] |
| 2025-02 | 1.06 | 1.20 | 4.3 | 4.0 | [PERF:MER:2025-02] |
| 2025-03 | 1.05 | 1.20 | 4.3 | 4.0 | [PERF:MER:2025-03] |
| 2025-04 | 1.04 | 1.20 | 4.4 | 4.0 | [PERF:MER:2025-04] |
| 2025-05 | 1.03 | 1.20 | 4.5 | 4.0 | [PERF:MER:2025-05] |

For comparison, Jan 2024 was DSCR 1.45 and leverage 3.2 [PERF:MER:2024-01]. Payments show 0 days past due in every month [PERF:MER:2024-01 to 2025-05]. The next covenant date is 2025-06-30 [PROFILE:MER].

## Waiver and reporting requirements
- **Waiver:** The records show it was put in place, but disagree on the date. The performance record says "waiver granted 11/22" [PERF:MER:2024-11], while the CRM log shows "Waiver Granted" on a call dated 2024-11-08 [CRM:2024-11-08:MER]. The conditions were (1) the Q4 package by Jan 31 and (2) updated projections showing a path back to the covenant levels [CRM:2024-11-08:MER; MEMO:MER.7].
  - **Q4 package:** Arrived Jan 18, 18 days late. That was still before the Jan 31 waiver deadline, and your memo calls the reporting default "cured" [MEMO:MER.4; EMAIL:T1.1].
  - **Projections:** As of your Jan 31 memo, they had "not" arrived [MEMO:MER.7]. Nothing in the records shows they were received later.
- **Q1 2025 package:** Due 4/30 [PERF:MER:2025-03]. It was recorded as overdue as of 5/1 [PERF:MER:2025-05], and there was no response to your Apr 28 notice as of May 12 [EMAIL:T1.6; NOTE:T1.1]. The records disagree slightly on timing: the May 12 note says "14 days after deadline," which points to Apr 28 rather than Apr 30.
- **Other documents still outstanding:** The aerospace purchase order and the customer names behind the 60–90 day receivables [MEMO:MER.8–10; CRM:2025-01-23:MER].

## Revolver usage vs. the proposed 75% cap
Your memo proposed limiting draws above 75% utilization [MEMO:MER.14]. It also proposed a Feb 14 deadline for the outstanding documents [MEMO:MER.13]. **Nothing in the records shows that either one was put in place.** Utilization readings:
- 75% in Feb 2025 [PERF:MER:2025-02]
- 78% in Mar 2025 [PERF:MER:2025-03]
- 81% in Apr 2025 [PERF:MER:2025-04]
- 85% in May 2025 [PERF:MER:2025-05]

## Contact
The last logged contact with the client was Mar 14, 2025 [CRM:2025-03-14:MER].

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
    "input_tokens": 15738,
    "output_tokens": 2607
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
  "q": 4,
  "rep": 1,
  "seconds": 28.5
}
```
