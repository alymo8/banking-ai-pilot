# before / Q1 / run 1

**Question:** Using the northfield-bank tools: does the record show Sarah's 75% revolver cap on Meridian was respected?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"})

**Answer:**

The records don't show the cap being followed. Usage went past 75% in March and reached 85% by May. They also don't show the cap ever being put in place, so it's unclear whether there was a binding limit to break.

**What Sarah wrote**
In her January 31, 2025 memo, Sarah said she wanted "to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now. I don't want them drawing the revolver to 85% while we're waiting on documentation" [MEMO:MER.14]. That reads as a recommendation to the credit committee, not a limit already in force. It sits next to her other requests to the committee [MEMO:MER.13].

**What happened to usage after the memo**
| Month | Revolver usage | Source |
|---|---|---|
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

Usage hit exactly 75% in February. It was above 75% every month from March on, and in May it reached the 85% figure Sarah specifically wanted to avoid. The May record notes "Revolver at 85%" [PERF:MER:2025-05].

**What I couldn't find**
- **Approval or setup:** No CRM entry, email or record note shows the credit committee approving the cap or anyone putting it on the account. The CRM entries after January 31 are a March 14 call [CRM:2025-03-14:MER] and the April 28 overdue notice [CRM:2025-04-28:MER]. Neither mentions a cap.
- **Telling the borrower:** None of the emails to David Kwan mentions a 75% limit, including the April 28 overdue notice [EMAIL:T1.6].
- **Draw requests:** Nothing shows any draw being reviewed, approved or flagged against a 75% limit.

**Caveats**
- The monthly figures are reported by the borrower (per the tool description), not taken from the bank's own loan system. A loan servicing or draw history, which these tools don't include, would confirm actual balances.
- The CRM log only shows what was logged. The cap could have been approved or put in place somewhere these records don't reach. If so, credit committee minutes or the loan servicing system would show it.

Three things to check next: whether the credit committee acted on the memo's recommendations, whether a limit was ever set up in loan servicing, and who approved the draws after February. I haven't assessed what this means for the credit, since that's your call under Policy 4.2.

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
    "input_tokens": 22486,
    "output_tokens": 1468
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
  "q": 1,
  "rep": 1,
  "seconds": 24.8
}
```
