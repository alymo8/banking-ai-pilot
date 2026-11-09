# after / Q6 / run 1

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you whether Sarah should be worried. Under the bank's Policy 4.2, judgments about risk are hers to make, not mine. What I can do is set out what the records show about the revolver so she can decide.

**Revolver use, Jan 2024 – May 2025 (as reported by the borrower)**

| Month | Revolver use | Source |
|---|---|---|
| Jan 2024 | 38% | [PERF:MER:2024-01] |
| Jun 2024 | 51% | [PERF:MER:2024-06] |
| Sep 2024 | 52% | [PERF:MER:2024-09] |
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% (the monthly note also says "Revolver at 85%") | [PERF:MER:2025-05] |

Apart from one dip in September 2024 (58% to 52%), the reading went up every month.

**The 75% cap**
- Sarah's January 31 memo says she wants to "restrict additional revolver draws above 75% utilization pending this review" [MEMO:MER.14]. That was her proposal, not a decision.
- I found nothing in the profile, CRM log or emails showing a 75% cap was ever approved or put in place. Against that proposed level, the readings were 75% in February, then 78%, 81% and 85% [PERF:MER:2025-02 to 05].
- In the same memo she wrote: "I don't want them drawing the revolver to 85% while we're waiting on documentation" [MEMO:MER.14]. May's reading is 85%.

**What has been said about why use is rising**
- David Kwan has called it seasonal working capital [CRM:2024-07-09:MER].
- Sarah wrote that "the trend is linear and persistent — there's nothing seasonal about it," and that they're "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6].
- She also wrote that the revolver "worries me more than the DSCR" [MEMO:MER.6]. That's her own earlier view, not mine.

**Other figures over the same period**
- **DSCR:** 1.45x in Jan 2024, 1.03x in May 2025. The minimum is 1.20x [PERF:MER:2024-01; PERF:MER:2025-05].
- **Leverage:** 3.2x in Jan 2024, 4.5x in May 2025. The maximum is 4.0x [same sources].
- **Bank's recorded covenant status:** the field reads "Covenant Breach" every month from Nov 2024 to May 2025 [PERF:MER:2024-11 to 2025-05].
- **Monthly revenue:** $7.1MM to $5.6MM. **EBITDA margin:** 14.0% to 10.8% [same sources].
- **Days past due:** 0 in every month [all PERF records].

**Items still outstanding**
- Not received: the aerospace purchase order, the updated projections required by the waiver, and the names of the customers behind the 60–90 day receivables [MEMO:MER.7, .8, .10, .13]. Nothing in the records shows the February 14 deadline Sarah proposed was set.
- The Q1 2025 covenant package is overdue [PERF:MER:2025-05]. The April 28 overdue notice got no reply as of May 12 [EMAIL:T1.6; NOTE:T1.1].
- The last logged contact with the client was March 14, 2025 [CRM:2025-03-14:MER].

**Date conflicts in the records**
- **Q1 package due date:** the records say April 30 [EMAIL:T1.6; PERF:MER:2025-03]. But the "overdue" notice went out April 28, and the record note counts days late from April 28 [NOTE:T1.1].
- **Waiver date:** one record says the waiver was granted November 22 [PERF:MER:2024-11], but the CRM log shows it approved on November 8 [CRM:2024-11-08:MER].

All performance figures are self-reported by the borrower. Any conclusion about the revolver, and whether a cap should be formally put in place, is Sarah's to make.

**Grade:**

```json
{
  "arm": "after",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 16112,
    "output_tokens": 2272
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
  "rep": 1,
  "seconds": 25.0
}
```
