# before / Q1 / run 2

**Question:** Using the northfield-bank tools: does the record show Sarah's 75% revolver cap on Meridian was respected?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"})

**Answer:**

I couldn't confirm the cap was ever put in place. And either way, utilization went above 75% starting in March 2025.

**The 75% cap was proposed, not shown as enacted.** It comes from Sarah's January 31, 2025 memo: "I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now. I don't want them drawing the revolver to 85% while we're waiting on documentation…" [MEMO:MER.14]. The other records I checked never mention it again. That includes the CRM log [CRM:2025-03-14:MER], [CRM:2025-04-28:MER], the email threads [EMAIL:T1.1]–[EMAIL:T1.6], [NOTE:T1.1] and the borrower profile [PROFILE:MER]. I found no credit committee approval, no note to the borrower and no amended terms. So the records don't say whether the cap was approved or communicated to Meridian.

**Revolver use by month (self-reported):**

| Month | Utilization | Source |
|---|---|---|
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] (note: "Revolver at 85%") |

Utilization reached exactly 75% in February and went higher every month after. By May it hit 85%, the level Sarah's memo specifically said she wanted to avoid [MEMO:MER.14].

**Other things to keep in mind:**
- These figures are reported by Meridian, not checked by the bank.
- The CRM log notes that its last recorded contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER]. The April 28 overdue notice for the Q1 package got no reply [EMAIL:T1.6], [CRM:2025-04-28:MER], [NOTE:T1.1]. So the records don't show any talk with Meridian about the cap while usage was going up.
- The logs only show what was entered. If a cap was set up through loan operations or credit admin, it might be recorded somewhere I can't see.

**What would settle it:** Credit admin or loan operations could check whether a draw block or a formal restriction was put on the revolver after January 31. Sarah or Marcus Chen could confirm whether the committee acted on that part of her memo. Based on what I can see, the cap was proposed, there's no record it was put in place, and usage went over 75% from March 2025 on.

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
    "input_tokens": 22487,
    "output_tokens": 1444
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
  "rep": 2,
  "seconds": 22.9
}
```
