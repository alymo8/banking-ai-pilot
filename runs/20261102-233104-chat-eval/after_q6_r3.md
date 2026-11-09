# after / Q6 / run 3

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank policy 4.2 leaves risk judgments to the RM. But the records show what's happening with the revolver, and Sarah has already written down her own view.

**Revolver use, January 2024 to May 2025 (latest data)**

| Month | Revolver used | Source |
|---|---|---|
| Jan 2024 | 38% | [PERF:MER:2024-01] |
| Jun 2024 | 51% | [PERF:MER:2024-06] |
| Sep 2024 | 52% | [PERF:MER:2024-09] |
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] (note: "Revolver at 85%") |

The only dip was September 2024 (52%, down from 58%). Since then usage has gone up 3–5 points every month. The facility is $8.5MM in total (term loan plus revolver) [PROFILE:MER].

**The 75% cap was only proposed**
- In her January 31, 2025 memo, Sarah wrote that she wanted "to restrict additional revolver draws above 75% utilization pending this review… I don't want them drawing the revolver to 85%" [MEMO:MER.14].
- The records only show this as her proposal. Nothing I found shows the cap was approved or took effect.
- Readings against the proposed 75%: February 75%, March 78%, April 81%, May 85% [PERF:MER:2025-02 to 2025-05].

**What Sarah has already said**
- "The revolver situation worries me more than the DSCR." She also wrote that the rise is "linear and persistent — there's nothing seasonal about it" and that they appear to be "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6].
- Back in July 2024, CFO David Kwan called the higher usage a "seasonal working capital need." Sarah doubted that and raised it internally with Marcus Chen [CRM:2024-07-09:MER].

**Related readings, May 2025, next to their limits** [PERF:MER:2025-05]
- DSCR (debt service coverage) of 1.03, against a 1.20 minimum.
- Leverage of 4.5x, against a 4.0x maximum.
- Current ratio is 1.2, down from 1.8 in January 2024 [PERF:MER:2024-01].
- The bank's recorded `covenant_status` field reads "Covenant Breach" every month from November 2024 to May 2025.
- Days past due is still 0.
- Monthly EBITDA fell from $994K to $605K, and margin from 14.0% to 10.8% [PERF:MER:2024-01, 2025-05].

**Information still missing**
- **Aerospace purchase order:** requested on the January 23 call and not received by January 31 [MEMO:MER.8, CRM:2025-01-23:MER].
- **Updated projections:** a condition of the November waiver, not received by January 31 [MEMO:MER.7].
- **Names of the customers behind the 60–90 day receivables:** still outstanding [MEMO:MER.10].
- **February 14 deadline:** Sarah proposed it for the items above, but I don't see a record that it was set or that anything arrived [MEMO:MER.13].
- **Q1 2025 covenant package:** Sarah sent an overdue notice on April 28 and got no reply. As of May 12 there was still no response [EMAIL:T1.6, NOTE:T1.1].
- **Last logged contact:** March 14, 2025 [CRM:2025-03-14:MER].

**Small inconsistencies in the records**
- The waiver date appears as November 8 in the call log [CRM:2024-11-08:MER] but as November 22 in the monthly data and the memo [PERF:MER:2024-11, MEMO:MER.7].
- The April 28 "overdue" email gives a due date of April 30, two days later [EMAIL:T1.6].

Whether this calls for action, such as formally putting the cap in place, is Sarah's and credit's call.

**Grade:**

```json
{
  "arm": "after",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 14000,
    "output_tokens": 2121
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
  "q": 6,
  "rep": 3,
  "seconds": 23.5
}
```
