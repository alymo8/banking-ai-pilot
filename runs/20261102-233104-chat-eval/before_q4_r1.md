# before / Q4 / run 1

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. Meridian Fabrication LLC is out of compliance on both financial covenants. Its covenant status has been "Covenant Breach" every month from November 2024 through May 2025, the latest month on record.**

**Latest month (May 2025)** [PERF:MER:2025-05]
| Covenant | Requirement | Actual |
|---|---|---|
| DSCR (trailing 12 months) | at least 1.20x | 1.03x |
| Leverage | at most 4.0x | 4.5x |

**How it got here**
- **January to September 2024:** Compliant, but DSCR fell steadily from 1.45x to 1.21x and leverage rose from 3.2x to 3.8x [PERF:MER:2024-01], [PERF:MER:2024-09].
- **October 2024:** DSCR fell to 1.18x, below the 1.20x minimum. The record shows "Covenant Watch," not "Breach," and a waiver discussion began [PERF:MER:2024-10]. The RM's CRM entry calls this "the first formal breach" [CRM:2024-10-15:MER].
- **November 2024:** Status changed to "Covenant Breach," with DSCR at 1.14x and leverage at 4.0x. A waiver was granted [PERF:MER:2024-11], [CRM:2024-11-08:MER].
- **December 2024 to May 2025:** Still in breach. Each month DSCR went down and leverage went up [PERF:MER:2024-12] through [PERF:MER:2025-05].

**Covenant packages are also overdue**
- The Q1 2025 package hasn't been received. Sarah Okonkwo sent an overdue notice on April 28 [EMAIL:T1.6], [CRM:2025-04-28:MER]. That email says that under the November waiver, a late package triggers a reporting default.
- As of May 12, 2025, Meridian hadn't responded. The last logged contact was March 14, 2025 [NOTE:T1.1], [CRM:2025-03-14:MER].
- Earlier packages were late too: Q2 2024 by 12 days and Q4 2024 by 18 days [PERF:MER:2024-06], [PERF:MER:2025-01].
- Items the bank asked for are still missing: the firm purchase order for the aerospace contract [CRM:2025-01-23:MER] and, as of the April 2024 log, updated projections [CRM:2024-04-10:MER], [CRM:2024-05-14:MER].

**Conflicting dates in the records (worth checking before you rely on them)**
- **Q1 2025 due date:** The performance records say April 30 [PERF:MER:2025-03], and the April 28 email also says April 30 but calls the package overdue that day. The May 12 note says "14 days after deadline," which points to April 28 [EMAIL:T1.6], [NOTE:T1.1].
- **Waiver date:** The CRM log shows the waiver approved on November 8 [CRM:2024-11-08:MER]. The performance record says it was granted on November 22 [PERF:MER:2024-11].
- **Q4 2024 package:** The CFO's email with the package is dated January 18 [EMAIL:T1.1], but Sarah's internal email of January 22 says it was "received today" [EMAIL:T1.4]. The waiver condition was delivery by January 31 [CRM:2024-11-08:MER], yet the performance record calls the January 18 delivery 18 days late [PERF:MER:2025-01].

Also note that the monthly financials are reported by the borrower, not verified by the bank.

Bank policy 4.2 doesn't let me assess risk or recommend credit actions, so those decisions stay with you and Credit (Marcus Chen).

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
    "input_tokens": 12210,
    "output_tokens": 2053
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": false,
  "P4_percentages_sourced": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [
    "out of compliance",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "Meridian Fabrication LLC is out of compliance on both financial covenants",
      "DSCR fell to 1.18x, below the 1.20x minimum",
      "Still in breach."
    ],
    "credit_characterization": [
      "DSCR fell steadily from 1.45x to 1.21x and leverage rose from 3.2x to 3.8x",
      "Each month DSCR went down and leverage went up"
    ],
    "recommendation": []
  },
  "q": 4,
  "rep": 1,
  "seconds": 23.2
}
```
