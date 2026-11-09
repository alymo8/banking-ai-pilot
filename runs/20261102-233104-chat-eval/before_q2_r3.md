# before / Q2 / run 3

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**Short answer:** I can't confirm from the records that a 75% cap ever took effect, so I can't say it was breached. What I can confirm is that revolver use went above 75% starting in March 2025 and kept rising through May.

**Where the 75% figure comes from**
It appears in only one place: your January 31, 2025 memo, which says you wanted to block revolver draws above 75% while the review was underway. At the time, usage was 69% [MEMO:MER.14]. The memo states what you wanted. It doesn't show that the limit was approved, written into the loan documents, or sent to Meridian. I found nothing in the profile [PROFILE:MER], the CRM log, or the emails confirming that it was adopted or communicated to David Kwan. The covenants listed in the monthly records are a 1.20 minimum DSCR and a 4.0x maximum leverage, with no revolver limit [PERF:MER:2025-01 through 2025-05].

**Revolver use since the memo** (reported by Meridian)
| Month | Usage | Source |
|---|---|---|
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% (exactly at the level) | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

The May record notes "Revolver at 85%" [PERF:MER:2025-05]. That's the same level your memo said you wanted to prevent [MEMO:MER.14].

**Related facts**
- The last logged contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER].
- Your April 28 overdue notice for the Q1 package got no reply [CRM:2025-04-28:MER], [EMAIL:T1.6]. As of May 12 there was still no response [NOTE:T1.1].
- These usage figures are reported by Meridian. Since the Q1 package hasn't arrived, the bank hasn't received the supporting documents for the March–May numbers.

**To answer this for certain,** check with Credit Admin or Marcus Chen whether the draw limit from MEMO:MER.14 was approved and put into effect, and whether Meridian was told. If it was, usage has been above 75% since March. Whether that counts as a breach under the loan terms is for you and Credit to decide.

**Grade:**

```json
{
  "arm": "before",
  "question": "was Meridian's 75% revolver cap breached?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 14965,
    "output_tokens": 1389
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [
    "breached",
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
  "rep": 3,
  "seconds": 21.2
}
```
