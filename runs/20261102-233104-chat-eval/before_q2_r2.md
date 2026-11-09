# before / Q2 / run 2

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"})

**Answer:**

I can't confirm a breach, because the records don't show that a 75% cap was ever put in place. Revolver use did go above 75%, though.

**Where the 75% figure comes from**
The only mention of it is your own memo from January 31, 2025. You wrote: "I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now. I don't want them drawing the revolver to 85%…" [MEMO:MER.14]. That's a restriction you asked for, not a confirmed term. Nothing I can access shows it was approved or sent to the borrower:
- The profile lists no revolver cap [PROFILE:MER].
- The monthly records only track two covenants: a 1.20 minimum for debt service coverage and a 4.0 maximum for leverage [PERF:MER:2025-05].
- The November waiver conditions were just the Q4 package by January 31 and updated projections [CRM:2024-11-08:MER], [MEMO:MER.7].
- No email or log entry after January 31 mentions a 75% limit [EMAIL:T1.6], [CRM:2025-03-14:MER], [CRM:2025-04-28:MER].

**Revolver use against 75%** (reported by Meridian)
| Month | Used | Source |
|---|---|---|
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% (exactly at the level, not over) | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

Use first went over 75% in March 2025 and has stayed over since. May reached the 85% you said you wanted to prevent [PERF:MER:2025-05], [MEMO:MER.14].

**Other things to know**
- The "Covenant Breach" label in the monthly records since November 2024 is about the coverage and leverage covenants, not the revolver [PERF:MER:2024-11], [PERF:MER:2025-05].
- These figures come from Meridian, and the Q1 2025 covenant package is overdue. Your April 28 notice had no reply as of May 12, and the last logged contact was March 14 [EMAIL:T1.6], [NOTE:T1.1], [CRM:2025-03-14:MER].

**Next step**
Whether this counts as a breach depends on whether the restriction was approved and given to Meridian. Credit committee minutes, an amendment or a borrower notice would settle it, but I can't access those. Marcus Chen or the credit file may have them. Under Policy 4.2, what the overage means for the loan and what to do about it are your calls.

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
    "input_tokens": 20328,
    "output_tokens": 1481
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [
    "breach",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": []
  },
  "q": 2,
  "rep": 2,
  "seconds": 21.0
}
```
