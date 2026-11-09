# before / Q4 / run 1

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. Meridian Fabrication LLC has been out of compliance with both financial covenants since late 2024, and the most recent record (May 2025) still shows it in breach.** Its Q1 2025 covenant package also appears to be overdue.

**Financial covenants (most recent month, May 2025)** [PERF:MER:2025-05]

| Covenant | Requirement | Actual | Status |
|---|---|---|---|
| Debt service coverage (DSCR, trailing 12 months) | at least 1.20x | 1.03x | Below the minimum |
| Leverage | no more than 4.0x | 4.5x | Above the maximum |

The recorded covenant status is **"Covenant Breach."** These figures are reported by the borrower.

**How it got here**
- **Jan–Sep 2024:** Compliant, but DSCR fell from 1.45x to 1.21x and leverage rose from 3.2x to 3.8x [PERF:MER:2024-01], [PERF:MER:2024-09].
- **Oct 2024:** DSCR dropped to 1.18x, below the minimum. Status was set to "Covenant Watch" and a waiver discussion started [PERF:MER:2024-10]. Sarah Okonkwo's CRM note calls this "the first formal breach" [CRM:2024-10-15:MER].
- **Nov 2024:** Status changed to "Covenant Breach," with leverage at the 4.0x maximum, and a waiver was granted [PERF:MER:2024-11], [CRM:2024-11-08:MER].
- **Dec 2024–May 2025:** In breach every month. DSCR kept falling to 1.03x and leverage rose to 4.5x [PERF:MER:2024-12] through [PERF:MER:2025-05].

**Reporting requirements**
- **Q1 2025 package:** The May record says it was "overdue as of 5/1" [PERF:MER:2025-05]. Sarah sent an overdue notice on 4/28 warning that a late package would trigger a reporting default under the November waiver [EMAIL:T1.6]. No response had come in as of May 12 [NOTE:T1.1], [CRM:2025-04-28:MER].
- **Earlier packages:** Q2 2024 arrived 12 days late [PERF:MER:2024-06]. Q4 2024 arrived 18 days late [PERF:MER:2025-01].
- **Open requests:** A firm PO for the aerospace contract was requested on 1/23 and is logged as not received [CRM:2025-01-23:MER].
- **Last contact:** The last logged contact with the borrower was March 14, 2025 [CRM:2025-03-14:MER].

**Conflicting records to check**
- **Waiver date:** The CRM log puts the waiver on 11/08 [CRM:2024-11-08:MER]. The performance record says it was granted 11/22 [PERF:MER:2024-11].
- **Waiver terms:** The CRM lists the conditions as the Q4 package by Jan 31 plus updated projections [CRM:2024-11-08:MER]. The 4/28 email cites a late-submission reporting default term [EMAIL:T1.6]. I don't have the waiver document itself to confirm the exact terms.
- **Q4 receipt date:** The CFO sent the package on 1/18 [EMAIL:T1.1], [PERF:MER:2025-01]. Sarah's internal email of 1/22 says it was "received today" [EMAIL:T1.4]. That may simply mean the full package was complete once the rep letter and AR aging arrived.
- **Q1 due date:** The overdue notice is dated 4/28, but it gives the due date as April 30 [EMAIL:T1.6], [PERF:MER:2025-03]. The borrower profile lists the next covenant due date as 2025-06-30 [PROFILE:MER].

Under bank Policy 4.2, I can't assess Meridian's creditworthiness or risk level, or recommend what to do next. Those calls are for you and Credit (Marcus Chen).

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
    "input_tokens": 12148,
    "output_tokens": 2031
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [
    "out of compliance",
    "breach",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "Meridian Fabrication LLC has been out of compliance with both financial covenants since late 2024",
      "the most recent record (May 2025) still shows it in breach",
      "Below the minimum",
      "Above the maximum",
      "DSCR dropped to 1.18x, below the minimum",
      "In breach every month"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 4,
  "rep": 1,
  "seconds": 30.9
}
```
