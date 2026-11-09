# before / Q1 / run 1

**Question:** Using the northfield-bank tools: does the record show Sarah's 75% revolver cap on Meridian was respected?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"})

**Answer:**

The record shows utilization went past 75%. But the records don't show the cap was ever put in place, so it's unclear whether it was a rule that got broken or a request that was never acted on.

**What Sarah asked for**
In her January 31, 2025 memo, Sarah wrote that she wanted to "restrict additional revolver draws above 75% utilization pending this review." Utilization was 69% at the time. She added that she didn't want them "drawing the revolver to 85% while we're waiting on documentation" [MEMO:MER.14].

**What happened to utilization afterward**
| Month | Revolver utilization | Source |
|---|---|---|
| 2024-12 | 69% | [PERF:MER:2024-12] |
| 2025-01 | 72% | [PERF:MER:2025-01] |
| 2025-02 | 75% | [PERF:MER:2025-02] |
| 2025-03 | 78% | [PERF:MER:2025-03] |
| 2025-04 | 81% | [PERF:MER:2025-04] |
| 2025-05 | 85% | [PERF:MER:2025-05] |

Utilization reached 75% in February and kept rising each month after that. May hit 85%, the exact figure Sarah's memo warned about. The May record notes "Revolver at 85%" [PERF:MER:2025-05].

**Was the cap ever made official?**
I couldn't find any record that it was approved or put into effect. Her memo states what she wanted and is addressed to the credit committee [MEMO:MER.13–14]. Nothing in the CRM log mentions a draw restriction being approved, told to the borrower, or applied to the facility [CRM entries 2024-01-08 through 2025-04-28]. The emails don't mention it either. Sarah's only email to David after the memo is the April 28 overdue-package notice, which doesn't bring up the revolver [EMAIL:T1.6]. The borrower profile doesn't list a limit on the revolver [PROFILE:MER].

So there are two possibilities:
- The cap was approved and the borrower drew past it anyway, or
- The cap was never approved or communicated, and nothing on the facility stopped draws above 75%.

These records can't tell those apart. You would need to check the credit committee minutes, any loan amendment or notice to the borrower, or the loan servicing system.

**Things to keep in mind**
- The utilization figures come from the borrower's own monthly reports, not the bank's servicing data. Draw records would confirm them.
- The last logged contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER]. The April 28 overdue notice got no response as of May 12 [NOTE:T1.1].

I've stuck to what the records show. Bank policy leaves any judgment about what this means for the loan, or what to do next, to you and credit.

**Grade:**

```json
{
  "arm": "before",
  "question": "does the record show Sarah's 75% revolver cap on Meridian was respected?",
  "tool_calls": [
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 19091,
    "output_tokens": 1384
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "broken"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [
      "it was a rule that got broken",
      "The cap was approved and the borrower drew past it anyway"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 1,
  "rep": 1,
  "seconds": 27.0
}
```
