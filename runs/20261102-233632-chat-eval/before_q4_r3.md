# before / Q4 / run 3

**Question:** Using the northfield-bank tools: is Meridian in compliance with its covenants?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. The bank's records show Meridian Fabrication LLC outside its covenants.** The latest month on file, May 2025, has status "Covenant Breach," and that status has held every month since November 2024 [PERF:MER:2025-05].

**Latest numbers (May 2025), as reported by the borrower [PERF:MER:2025-05]**

| Covenant | Requirement | Actual | Status |
|---|---|---|---|
| DSCR (trailing 12 months) | at least 1.20 | 1.03 | Below the minimum |
| Leverage | no more than 4.0x | 4.5x | Above the maximum |

**How it got here**
- **Jan–Sep 2024:** Compliant, but DSCR fell steadily from 1.45 to 1.21 and leverage rose from 3.2x to 3.8x [PERF:MER:2024-01], [PERF:MER:2024-09].
- **Oct 2024:** DSCR dropped to 1.18, below the minimum. The monthly record calls this "Covenant Watch" [PERF:MER:2024-10], but the CRM log calls it "the first formal breach" [CRM:2024-10-15:MER].
- **Nov 2024:** Leverage hit 4.0x and DSCR was 1.14. A waiver was granted. Its conditions were the Q4 package by Jan 31 plus updated projections showing a path to recovery [CRM:2024-11-08:MER], [PERF:MER:2024-11].
- **Dec 2024 to May 2025:** Breach status every month, with DSCR falling from 1.10 to 1.03 and leverage rising from 4.1x to 4.5x [PERF:MER:2024-12] through [PERF:MER:2025-05].

**Reporting obligations**
- **Q4 2024 package:** Received Jan 18, 2025, logged as 18 days late [PERF:MER:2025-01]. Sarah asked for a signed management representation letter and an updated accounts receivable aging, which weren't in the package [EMAIL:T1.2]. Separately, the borrower said on Jan 23 it would send a firm purchase order for the aerospace contract. As of that log entry, it hadn't arrived [CRM:2025-01-23:MER].
- **Q1 2025 package:** Due Apr 30 [PERF:MER:2025-03]. On Apr 28 Sarah sent an overdue notice saying that under the November waiver, a late submission triggers a reporting default [EMAIL:T1.6]. No response had come in as of May 12 [NOTE:T1.1]. The last logged contact with the borrower was Mar 14, 2025 [CRM:2025-03-14:MER].

**Records that don't match**
- **Waiver date:** The CRM logs the waiver as granted on the Nov 8 call [CRM:2024-11-08:MER]. The monthly record says "waiver granted 11/22" [PERF:MER:2024-11].
- **Q4 deadline:** The waiver set a Jan 31 deadline for the Q4 package [CRM:2024-11-08:MER], yet the package received on Jan 18 is logged as 18 days late [PERF:MER:2025-01].
- **Q1 deadline:** The Apr 28 notice calls the package overdue while also saying it was due Apr 30 [EMAIL:T1.6].
- **Next covenant due date:** The borrower profile lists 2025-06-30 [PROFILE:MER], which doesn't match the Apr 30 Q1 deadline.

**Caveats**
- The monthly figures are self-reported by the borrower, not independently verified.
- Under Policy 4.2, I can't assess what this means for creditworthiness or risk, or recommend credit actions. That call belongs to you and credit.

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
    "input_tokens": 12176,
    "output_tokens": 2024
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [
    "Breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "No. The bank's records show Meridian Fabrication LLC outside its covenants.",
      "Below the minimum",
      "Above the maximum",
      "DSCR dropped to 1.18, below the minimum."
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 4,
  "rep": 3,
  "seconds": 26.8
}
```
