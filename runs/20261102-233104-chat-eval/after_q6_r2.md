# after / Q6 / run 2

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank policy 4.2 says judgments about risk come from the relationship manager (RM), not from me. What I can do is lay out what the records show about Meridian's revolver, and her own memo already gives her view.

**Revolver utilization by month (self-reported)**

| Month | Utilization | Source |
|---|---|---|
| Jan 2024 | 38% | [PERF:MER:2024-01] |
| Jun 2024 | 51% | [PERF:MER:2024-06] |
| Sep 2024 | 52% | [PERF:MER:2024-09] |
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

From January 2024 to May 2025, the only month-to-month drop was August to September 2024 (58% to 52%) [PERF:MER:2024-08, 2024-09]. The records split the facility only as "Term Loan + Revolver" at $8.5MM total, so I can't turn these percentages into dollars [PROFILE:MER].

**The proposed 75% cap**
- On January 31, 2025, Sarah wrote that she wanted to "restrict additional revolver draws above 75% utilization pending this review" [MEMO:MER.14].
- That was her proposal. Nothing I found shows the cap was approved or added to the loan terms.
- Readings since then against that proposed 75%: 75% in February, 78% in March, 81% in April and 85% in May [PERF:MER:2025-02 to 2025-05].

**What Sarah has already written**
- "The revolver situation worries me more than the DSCR" [MEMO:MER.6]. DSCR is the debt-service coverage ratio.
- David Kwan called the borrowing "seasonal working capital needs." She wrote that the trend is "linear and persistent" and that the company is "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6]. Her July 2024 call notes say the same [CRM:2024-07-09:MER].

**Other figures from the same period**

| Measure | Covenant limit | Jan 2024 | May 2025 | Source |
|---|---|---|---|---|
| DSCR (trailing 12 months) | 1.20 minimum | 1.45 | 1.03 | [PERF:MER:2024-01], [PERF:MER:2025-05] |
| Leverage | 4.0 maximum | 3.2 | 4.5 | same |

- The bank's recorded `covenant_status` field reads "Covenant Breach" every month from November 2024 to May 2025 [PERF:MER:2024-11 to 2025-05].
- Current ratio went from 1.8 to 1.2. Days past due are 0 in every month [same].
- The November waiver required updated projections showing a path to recovery. The memo says those hadn't arrived [MEMO:MER.7].
- Sarah asked for three items by February 14: the aerospace purchase order, cash flow projections and the customer names on the 60–90 day receivables. Her memo set that date as her proposed deadline [MEMO:MER.13]. I found nothing showing any of the three arrived.
- The last logged contact with the client was March 14, 2025 [CRM:2025-03-14:MER].
- Her April 28 overdue notice on the Q1 package got no reply as of May 12 [EMAIL:T1.6], [NOTE:T1.1].

**Places where the records disagree**
- **Waiver date:** the call log records the waiver as approved on November 8 [CRM:2024-11-08:MER]. The monthly data and memo say November 22 [PERF:MER:2024-11], [MEMO:MER.7].
- **Q1 package:** Sarah's April 28 email calls it overdue but says it was due April 30 [EMAIL:T1.6].
- **Q4 package date:** Sarah's internal email says the package was "received today" (January 22) [EMAIL:T1.4]. Other records say January 18 [EMAIL:T1.1], [PERF:MER:2025-01].
- **Aerospace timing:** the January 2024 call notes say aerospace revenue was expected from Q1 2024 [CRM:2024-01-08:MER]. The memo says David first promised Q2 2024 [MEMO:MER.8].

The first question for Sarah is whether her proposed 75% cap was ever formally put in place. The records don't show it was, and the answer changes what the February–May readings mean. Whether this is cause for concern, and what to do about it, is her call and the credit team's.

**Grade:**

```json
{
  "arm": "after",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 13815,
    "output_tokens": 2378
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
  "rep": 2,
  "seconds": 26.0
}
```
