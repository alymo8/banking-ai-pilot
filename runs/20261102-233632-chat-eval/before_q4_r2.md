# before / Q4 / run 2

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. The bank's records show Meridian Fabrication LLC out of covenant compliance.** Every month from November 2024 through May 2025, the most recent month on file, has the status "Covenant Breach." The figures are self-reported by the borrower.

**Latest month (May 2025) [PERF:MER:2025-05]**

| Covenant | Requirement | Actual | Status |
|---|---|---|---|
| DSCR (TTM) | at least 1.20x | 1.03x | Below minimum |
| Leverage | at most 4.0x | 4.5x | Above maximum |

Other figures that month: revolver use at 85%, 0 days past due, loan balance $7.6MM [PERF:MER:2025-05].

**How it got here**
- **Jan–Sep 2024:** Compliant. DSCR fell from 1.45x to 1.21x and leverage rose from 3.2x to 3.8x [PERF:MER:2024-01] [PERF:MER:2024-09].
- **Oct 2024:** DSCR was 1.18x. The performance record marks this "Covenant Watch" [PERF:MER:2024-10], but the RM's CRM entry calls it "the first formal breach" [CRM:2024-10-15:MER].
- **Nov 2024:** Status changed to "Covenant Breach." DSCR was 1.14x and leverage was at the 4.0x max. A waiver was granted on 11/22 [PERF:MER:2024-11]. Its conditions were the Q4 package by Jan 31 plus updated projections showing a path to recovery [CRM:2024-11-08:MER].
- **Dec 2024 – May 2025:** In breach every month. Leverage has been above 4.0x since December [PERF:MER:2024-12] through [PERF:MER:2025-05].

**Reporting covenant**
- **Q1 2025 package:** Not received. Records say it was overdue as of 5/1 [PERF:MER:2025-05]. Sarah's 4/28 notice says that under the November waiver, late submission triggers a reporting default [EMAIL:T1.6]. As of 5/12 there was no reply [NOTE:T1.1].
- **Q4 2024 package:** Arrived 1/18, 18 days late [PERF:MER:2025-01] [EMAIL:T1.1].
- **Q2 2024 package:** Arrived 12 days late [PERF:MER:2024-06].
- **Items promised but not logged as received:**
  - The firm aerospace PO that Marcus Chen asked for [CRM:2025-01-23:MER].
  - The updated projections, which were one of the waiver's conditions. The CFO offered to share them on a call [EMAIL:T1.1], but no record shows they arrived.

**Conflicting records to check**
- **Q4 package date:** Records show it received 1/18 [PERF:MER:2025-01] [EMAIL:T1.1]. Sarah's internal email of 1/22 says "received today" [EMAIL:T1.4].
- **Q1 package due date:** Sarah's 4/28 notice says the package "was due April 30" but treats it as already overdue [EMAIL:T1.6]. The actual due date should be confirmed against the loan agreement.
- **Q4 lateness:** "18 days late" [PERF:MER:2025-01] fits a 12/31 deadline. A 1/18 arrival would still fall within the waiver's Jan 31 deadline [CRM:2024-11-08:MER].

**Contact status:** The last logged conversation with the client was on 3/14/2025 [CRM:2025-03-14:MER]. The formal notice sent on 4/28 got no response [CRM:2025-04-28:MER].

Under bank policy 4.2, I can't assess risk or recommend credit actions. That decision belongs to Sarah Okonkwo, the relationship manager, and credit.

**Grade:**

```json
{
  "arm": "before",
  "question": "is Meridian in compliance with its covenants?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 12100,
    "output_tokens": 1919
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "No. The bank's records show Meridian Fabrication LLC out of covenant compliance.",
      "Below minimum",
      "Above maximum",
      "In breach every month.",
      "Leverage has been above 4.0x since December"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 4,
  "rep": 2,
  "seconds": 29.3
}
```
