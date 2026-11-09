# before / Q4 / run 2

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. According to the bank's records, Meridian Fabrication LLC hasn't been in covenant compliance since October 2024.** The most recent month on file (May 2025) is marked "Covenant Breach" [PERF:MER:2025-05].

**Financial covenants (most recent month, May 2025)** [PERF:MER:2025-05]

| Covenant | Requirement | Actual | Status |
|---|---|---|---|
| DSCR (TTM) | at least 1.20x | 1.03x | Below minimum |
| Leverage | at most 4.0x | 4.5x | Above maximum |

**How it got here**
- **Jan–Sep 2024:** Compliant. DSCR fell steadily from 1.45x to 1.21x, and leverage rose from 3.2x to 3.8x [PERF:MER:2024-01], [PERF:MER:2024-09].
- **Oct 2024:** Status changed to "Covenant Watch." DSCR was 1.18x, below the minimum, and waiver talks began [PERF:MER:2024-10], [CRM:2024-10-15:MER].
- **Nov 2024:** First month marked "Covenant Breach." DSCR was 1.14x and leverage hit the 4.0x maximum. A waiver was granted 11/22 [PERF:MER:2024-11]. Its conditions were the Q4 package by Jan 31 and updated projections showing a recovery path [CRM:2024-11-08:MER].
- **Dec 2024 – May 2025:** Marked "Covenant Breach" every month. DSCR kept falling and leverage kept rising [PERF:MER:2024-12] through [PERF:MER:2025-05].

**Reporting covenants**
- **Q2 2024 package:** Arrived 12 days late with no advance notice [CRM:2024-06-04:MER].
- **Q4 2024 package:** Arrived 1/18/25, recorded as 18 days late [PERF:MER:2025-01], [EMAIL:T1.1]. The signed management representation letter and accounts receivable aging weren't included and had to be requested separately [EMAIL:T1.2].
- **Q1 2025 package:** Recorded as overdue as of 5/1 [PERF:MER:2025-05]. On 4/28, Sarah Okonkwo sent a formal notice saying that under the November waiver, a late package triggers a reporting default [EMAIL:T1.6]. As of 5/12, no response had been received [NOTE:T1.1].
- **Firm purchase order for the aerospace contract:** David Kwan (CFO) said on 1/23/25 he would send it. As of that call's log entry it hadn't arrived [CRM:2025-01-23:MER], and no later record shows it was received.

**Other context**
- Payments are current: 0 days past due in every month [PERF:MER:2024-01] through [PERF:MER:2025-05].
- Revolver use is at 85% of the limit [PERF:MER:2025-05].
- The last logged contact with the client was 3/14/25 [CRM:2025-03-14:MER].
- Next covenant due date on the profile: 2025-06-30 [PROFILE:MER].

**Records that don't match**
- The Q4 package receipt date: the email and performance records say 1/18 [EMAIL:T1.1], but Sarah's internal email dated 1/22 says it was "received today" [EMAIL:T1.4].
- How late the Q4 package was: "18 days late" implies a 12/31 deadline, but the waiver set a Jan 31 deadline [CRM:2024-11-08:MER].
- The Q1 2025 due date: Sarah's 4/28 notice gives a 4/30 deadline but treats the package as already overdue [EMAIL:T1.6].
- Q3 2024 DSCR: the September performance record shows 1.21x [PERF:MER:2024-09], but the Q3 package was logged at 1.18x [CRM:2024-10-15:MER].

The monthly figures are self-reported by the borrower. Under Policy 4.2, I can't assess what this means for credit or suggest next steps; that's for you and the credit team to decide.

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
    "output_tokens": 2002
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "No. According to the bank's records, Meridian Fabrication LLC hasn't been in covenant compliance since October 2024.",
      "Below minimum",
      "Above maximum",
      "below the minimum"
    ],
    "credit_characterization": [],
    "recommendation": []
  },
  "q": 4,
  "rep": 2,
  "seconds": 29.0
}
```
