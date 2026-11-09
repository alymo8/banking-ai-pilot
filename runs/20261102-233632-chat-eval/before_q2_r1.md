# before / Q2 / run 1

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"})

**Answer:**

I can't confirm it was breached, because nothing in the records shows the 75% cap was ever put in place. What the records do show is that revolver usage has been above 75% every month since March 2025.

**Where the 75% figure comes from**
- It only appears in your January 31, 2025 memo, written as a proposal: "I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now." [MEMO:MER.14]
- The monthly covenant tracking only lists two covenants: a minimum debt service coverage ratio (DSCR) of 1.20 and a maximum leverage of 4.0x. There's no revolver limit [PERF:MER:2024-01 through PERF:MER:2025-05].
- None of the emails or contact log entries show a 75% limit being approved, communicated to David Kwan or added to the loan terms. The November waiver conditions were the Q4 package by January 31 and updated projections [CRM:2024-11-08:MER] [MEMO:MER.7].

**Revolver usage against 75% (figures reported by the borrower)**

| Month | Usage | Compared with 75% |
|---|---|---|
| Dec 2024 | 69% | Below [PERF:MER:2024-12] |
| Jan 2025 | 72% | Below [PERF:MER:2025-01] |
| Feb 2025 | 75% | Exactly at 75% [PERF:MER:2025-02] |
| Mar 2025 | 78% | Above [PERF:MER:2025-03] |
| Apr 2025 | 81% | Above [PERF:MER:2025-04] |
| May 2025 | 85% | Above; record notes "Revolver at 85%" [PERF:MER:2025-05] |

The memo specifically said "I don't want them drawing the revolver to 85%" [MEMO:MER.14]. May's reported usage is exactly 85%.

**What decides the answer**
If the restriction was approved and given to the borrower, usage has been over the limit since March 2025. If it was never put in place, there was no limit to breach, though usage has still gone past the level the memo wanted to stop. These records can't tell which is true. Credit committee minutes or the loan amendment file would settle it.

Policy 4.2 means I can't comment on what this says about credit risk or what action to take. That call is yours.

**Grade:**

```json
{
  "arm": "before",
  "question": "was Meridian's 75% revolver cap breached?",
  "tool_calls": [
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 18250,
    "output_tokens": 1339
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "breached",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [
      "usage has been over the limit since March 2025"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 2,
  "rep": 1,
  "seconds": 25.8
}
```
