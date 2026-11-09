# after / Q4 / run 2

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't give you a yes or no on compliance. Under the bank's Policy 4.2 that call is yours. Below are Meridian Fabrication LLC's readings next to its covenant limits, along with what the records say about the waiver and the open items. All figures are self-reported by the borrower.

**Covenant readings vs. limits** (minimum DSCR 1.20x; maximum leverage 4.0x)

| Month | DSCR (TTM) | Leverage | Bank's recorded `covenant_status` field | Source |
|---|---|---|---|---|
| 2024-09 | 1.21 | 3.8 | "Compliant" | [PERF:MER:2024-09] |
| 2024-10 | 1.18 | 3.9 | "Covenant Watch" | [PERF:MER:2024-10] |
| 2024-11 | 1.14 | 4.0 | "Covenant Breach" | [PERF:MER:2024-11] |
| 2024-12 | 1.10 | 4.1 | "Covenant Breach" | [PERF:MER:2024-12] |
| 2025-01 | 1.08 | 4.2 | "Covenant Breach" | [PERF:MER:2025-01] |
| 2025-02 | 1.06 | 4.3 | "Covenant Breach" | [PERF:MER:2025-02] |
| 2025-03 | 1.05 | 4.3 | "Covenant Breach" | [PERF:MER:2025-03] |
| 2025-04 | 1.04 | 4.4 | "Covenant Breach" | [PERF:MER:2025-04] |
| 2025-05 | 1.03 | 4.5 | "Covenant Breach" | [PERF:MER:2025-05] |

For context, in January 2024 DSCR was 1.45 and leverage was 3.2 [PERF:MER:2024-01]. The status column is the bank's own field, quoted word for word, not my assessment.

**The November 2024 waiver**
- **Date conflict:** the performance record says "waiver granted 11/22" [PERF:MER:2024-11], and so does the memo [MEMO:MER.7]. The CRM log records "Waiver Granted" on a call dated 2024-11-08 [CRM:2024-11-08:MER].
- **Conditions:** (1) the Q4 package by January 31 and (2) updated projections showing a path back to the limits by Q3 2025 [MEMO:MER.7; CRM:2024-11-08:MER].
  - **Condition 1:** The Q4 package arrived January 18, 18 days late. The memo says this triggered a reporting default that was cured because it came before the January 31 waiver deadline [MEMO:MER.4; EMAIL:T1.1].
  - **Condition 2:** As of January 31, "the projections have not" arrived [MEMO:MER.7]. Nothing later in the records shows they were received.
- **What happened next:** The RM memo proposed keeping the waiver in place, setting a February 14 deadline for documents, and not granting a second waiver [MEMO:MER.13]. These were proposals only. The records don't show whether the credit committee adopted them.

**Proposed 75% revolver cap**
The memo proposed restricting revolver draws above 75% [MEMO:MER.14]. The records don't show this cap was ever put in place. Readings since then: 72% (Jan), 75% (Feb), 78% (Mar), 81% (Apr), 85% (May) [PERF:MER:2025-01 to 2025-05].

**Reporting requirements**
- **Q2 2024 package:** 12 days late [PERF:MER:2024-06].
- **Q4 2024 package:** 18 days late [PERF:MER:2025-01].
- **Q1 2025 package:** The records give conflicting deadlines:
  - The overdue notice dated April 28 says the package "was due April 30" [EMAIL:T1.6].
  - The May 12 note calls May 12 "14 days after deadline," which points to April 28 [NOTE:T1.1].
  - The May data says the package was "overdue as of 5/1" [PERF:MER:2025-05].
  - Either way, no response was on file as of May 12 [NOTE:T1.1; CRM:2025-04-28:MER].
- **Still outstanding:** the aerospace purchase order, the updated projections, and the customer names behind the 60–90 day receivables [MEMO:MER.8–10, MEMO:MER.13].
- **Last contact:** The last logged call with the borrower was March 14, 2025 [CRM:2025-03-14:MER].
- **Next covenant due date:** 2025-06-30 [PROFILE:MER].
- **Payments:** Days past due is 0 in every month [PERF:MER:2024-01 to 2025-05].

Before you decide, it would help to confirm with credit administration what the credit committee actually decided after the January 31 memo, and the correct waiver date.

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
    "input_tokens": 15734,
    "output_tokens": 2499
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
  "rep": 2,
  "seconds": 30.8
}
```
