# before / Q6 / run 1

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank policy 4.2 says judgments about risk or credit actions have to come from the RM. What I can do is show what the records say about the revolver. Sarah has already given her own view on it in writing.

**Revolver usage over time (borrower self-reported)**
| Month | Usage | Source |
|---|---|---|
| Jan 2024 | 38% | [PERF:MER:2024-01] |
| Jul 2024 | 55% | [PERF:MER:2024-07] |
| Sep 2024 | 52% | [PERF:MER:2024-09] |
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| May 2025 | **85%** | [PERF:MER:2025-05] |

The only month it dropped was September 2024. Every month since then it has gone up.

**What Sarah has already written**
- In her January 31 memo: "The revolver situation worries me more than the DSCR." She called the trend "linear and persistent," not seasonal, and wrote that the company is using the revolver to cover operating cash flow shortfalls [MEMO:MER.6].
- In the same memo she proposed blocking new draws above 75% usage while the review was underway, saying she didn't want them "drawing the revolver to 85%" [MEMO:MER.14]. Usage is now exactly 85% [PERF:MER:2025-05]. I can't find any record of whether that limit was ever put in place.
- The CFO, David Kwan, has called the draws a seasonal working capital need [CRM:2024-07-09:MER].

**Other facts in the records**
- **Covenants:**
  - Breached every month since November 2024 [PERF:MER:2024-11 to 2025-05].
  - DSCR is 1.03x against a 1.20x minimum. Leverage is 4.5x against a 4.0x maximum [PERF:MER:2025-05].
  - The current ratio has fallen from 1.8 to 1.2 [PERF:MER:2024-01, 2025-05].
- **Revenue and margin:**
  - Monthly revenue fell from $7.1M to $5.6M [PERF:MER:2024-01, 2025-05].
  - EBITDA margin fell from 14.0% to 10.8% [PERF:MER:2024-01, 2025-05].
- **Payments:** Days past due is still 0 [PERF:MER:2025-05].
- **Items requested but not received:** the aerospace purchase order, the 12-month projections, and the names of the customers behind the 60–90 day receivables. The waiver conditions included projections, and those never arrived [MEMO:MER.7, MER.13; CRM:2025-01-23:MER].
- **Communication:**
  - The last logged contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER].
  - The April 28 overdue notice got no reply as of May 12 [EMAIL:T1.6; NOTE:T1.1].
  - The Q1 2025 covenant package is overdue [PERF:MER:2025-05].
- **Aerospace timing:** The expected start of aerospace revenue has slipped several times, from Q1 2024 to Q2, Q3, and Q4 2024, and now Q2 2025 [CRM:2024-01-08:MER; CRM:2024-07-09:MER; EMAIL:T1.1; MEMO:MER.8].

**A date inconsistency to check:** The April 28 notice calls the Q1 package overdue but also says it was due April 30 [EMAIL:T1.6]. Since the notice mentions starting a reporting-default clock, it may be worth confirming the actual due date.

All the financial figures are self-reported by Meridian. The AR aging and the aerospace contract status have not been checked against outside documents [EMAIL:T1.4; MEMO:MER.8].

**Grade:**

```json
{
  "arm": "before",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 13443,
    "output_tokens": 2033
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "Breached"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "Breached every month since November 2024"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 6,
  "rep": 1,
  "seconds": 30.7
}
```
