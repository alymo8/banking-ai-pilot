# after / Q2 / run 3

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't give you a yes or no on this. Under bank Policy 4.2, that call is yours. Two things decide it: the records don't show that the 75% cap was ever put in place, and they do show monthly utilization readings above 75%.

**1. Where the 75% cap comes from**
The only source for the cap is your January 31, 2025 memo: *"I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now."* [MEMO:MER.14]. That is written as a proposal for the credit committee [MEMO:MER.13–14]. Nothing in the profile, emails, CRM log or monthly performance data shows that:
- the committee approved it,
- it was added to the loan agreement or a waiver condition, or
- it was ever sent to David Kwan.

The November waiver conditions were a Q4 covenant package by January 31 and updated projections. They don't mention the revolver [CRM:2024-11-08:MER] [MEMO:MER.7]. The facility's recorded covenant limits are only DSCR (1.20x minimum) and leverage (4.0x maximum) [PERF:MER:2024-01 through 2025-05].

**2. Revolver usage compared with the proposed 75% level**

| Month | Revolver use | Proposed cap | Source |
|---|---|---|---|
| 2024-12 | 69% | 75% (proposed) | [PERF:MER:2024-12] |
| 2025-01 | 72% | 75% (proposed) | [PERF:MER:2025-01] |
| 2025-02 | 75% | 75% (proposed) | [PERF:MER:2025-02] |
| 2025-03 | 78% | 75% (proposed) | [PERF:MER:2025-03] |
| 2025-04 | 81% | 75% (proposed) | [PERF:MER:2025-04] |
| 2025-05 | 85% | 75% (proposed) | [PERF:MER:2025-05] |

The May record also carries the bank's note: "Revolver at 85%; Q1 package overdue as of 5/1" [PERF:MER:2025-05]. These figures are self-reported by the borrower.

**3. The bank's recorded covenant status**
The `covenant_status` field reads "Covenant Breach" from November 2024 through May 2025 [PERF:MER:2024-11 through 2025-05]. That status relates to the DSCR and leverage covenants. The record doesn't link it to the revolver.

**Gaps that matter here**
- The last logged contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER].
- Your April 28 overdue notice on the Q1 package has had no reply as of May 12 [EMAIL:T1.6] [NOTE:T1.1].
- So the records don't show the borrower was ever told about a 75% restriction.

If the committee approved the cap outside these systems, that approval would be the deciding document. It isn't in the records I can see.

**Grade:**

```json
{
  "arm": "after",
  "question": "was Meridian's 75% revolver cap breached?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15820,
    "output_tokens": 1477
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
  "q": 2,
  "rep": 3,
  "seconds": 19.2
}
```
