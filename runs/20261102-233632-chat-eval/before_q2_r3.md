# before / Q2 / run 3

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"})

**Answer:**

**I can't confirm a breach, because nothing in the records shows the 75% cap was ever put in place.** What the records do show is that reported revolver use went past 75% starting in March 2025.

**Where the 75% figure comes from**
- It appears only in your January 31, 2025 memo, as something you wanted: "I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now." [MEMO:MER.14]
- The covenant fields in the monthly records list only two limits: a DSCR minimum of 1.20 and a leverage maximum of 4.0x. There's no revolver limit [PERF:MER:2024-01 through PERF:MER:2025-05].
- None of the emails, CRM entries or other records show the restriction being approved by credit committee, sent to the borrower, or added to the loan or waiver terms. The November waiver had two conditions: the Q4 package by January 31 and updated projections [CRM:2024-11-08:MER] [MEMO:MER.7].

**Revolver use against 75% since the memo (borrower self-reported)**

| Month | Utilization | Source |
|---|---|---|
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% (at the level, not over) | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

May's 85% matches the level your memo said you wanted to avoid ("I don't want them drawing the revolver to 85%") [MEMO:MER.14]. The May record also notes "Revolver at 85%" [PERF:MER:2025-05].

**Related context**
- No contact with Meridian has been logged since March 14, 2025 [CRM:2025-03-14:MER].
- The Q1 2025 covenant package is overdue. Your April 28 notice got no reply as of May 12 [EMAIL:T1.6] [NOTE:T1.1].

**So:** if the 75% restriction was formally put in place somewhere outside these records, reported usage has been above it since March 2025. If it was never put in place, it's a proposal from your memo, not a limit that could be breached. Credit committee minutes or a written notice to the borrower would settle which one it is. Whether to call this a breach, and what to do about it, is your call under Policy 4.2.

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
    "input_tokens": 18253,
    "output_tokens": 1445
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": false,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "breach",
    "breached",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": [
      "Whether to call this a breach, and what to do about it, is your call under Policy 4.2."
    ]
  },
  "q": 2,
  "rep": 3,
  "seconds": 23.4
}
```
