# after / Q6 / run 1

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"})

**Answer:**

I can't tell you whether Sarah should be worried. This pilot doesn't let AI answers judge risk or creditworthiness (that applies the bank's policy 4.2), so that call is hers. What I can do is set out what the records show about the revolver.

**Sarah has already written about this herself.** In her Jan 31, 2025 memo she wrote: "The revolver situation worries me more than the DSCR." She said usage was "linear and persistent — there's nothing seasonal about it" and that the company is "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6]. The CFO, David Kwan, has called it seasonal working capital [MEMO:MER.6][CRM:2024-07-09:MER].

**Monthly revolver usage (self-reported by the borrower)**
- 2024: 38% in Jan, 41% Feb, 36% Mar, 44% Apr, 47% May, 51% Jun, 55% Jul, 58% Aug, 52% Sep, 60% Oct, 65% Nov, 69% Dec [PERF:MER:2024-01 through 2024-12]
- 2025: 72% in Jan, 75% Feb, 78% Mar, 81% Apr, 85% May [PERF:MER:2025-01 through 2025-05]

**The 75% cap**
- Sarah's memo proposed it: "I want to restrict additional revolver draws above 75% utilization pending this review… I don't want them drawing the revolver to 85%" [MEMO:MER.14].
- Usage since then, next to the proposed 75%: 75% (Feb), 78% (Mar), 81% (Apr), 85% (May) [PERF:MER:2025-02 to 2025-05].
- **None of the records I checked show the cap was actually put in place.** It appears only as a proposal in the memo. There's no committee decision, notice to the borrower or CRM entry about it. Since I can't give a yes/no on whether a limit was met, here are the numbers side by side. Whether there was a cap in effect at all is worth checking with credit.

**Related readings, next to their limits**
| Month | DSCR (TTM) vs. 1.20 min | Leverage vs. 4.0 max | Recorded covenant_status (bank field, quoted as recorded) |
|---|---|---|---|
| 2024-01 | 1.45 | 3.2 | "Compliant" |
| 2024-12 | 1.10 | 4.1 | "Covenant Breach" |
| 2025-05 | 1.03 | 4.5 | "Covenant Breach" |
[PERF:MER:2024-01][PERF:MER:2024-12][PERF:MER:2025-05]

**Context around the trend**
- Monthly revenue fell from $7.1MM (Jan 2024) to $5.6MM (May 2025). EBITDA margin fell from 14.0% to 10.8% [PERF:MER:2024-01][PERF:MER:2025-05]. Current ratio went from 1.8 to 1.2 over the same period.
- The expected start of aerospace revenue has moved several times. The records give Q1 2024 [CRM:2024-01-08:MER], Q2 2024 [CRM:2024-04-10:MER], Q3 2024 [CRM:2024-07-09:MER], Q4 2024 [MEMO:MER.8] and now Q2 2025 [EMAIL:T1.1]. The purchase order has been requested and not received [MEMO:MER.8][CRM:2025-01-23:MER].
- Sarah set a Feb 14 deadline for the PO, 12-month projections and the customer names behind the 60–90 day receivables [MEMO:MER.13]. Nothing I found shows any of these arrived.
- The Q1 2025 covenant package was due Apr 30. Sarah sent an overdue notice on Apr 28 [EMAIL:T1.6]. As of May 12 there had been no response, and the last logged contact was Mar 14 [NOTE:T1.1][CRM:2025-03-14:MER].
- Payments are current: 0 days past due in every month [PERF:MER:2024-01 through 2025-05].

**Inconsistencies in the records**
- **Waiver date:** the CRM says it was approved Nov 8 [CRM:2024-11-08:MER]. The memo and performance notes say Nov 22 [MEMO:MER.7][PERF:MER:2024-11].
- **Q4 package date:** the memo says it arrived Jan 18 [MEMO:MER.4]. Sarah's internal email of Jan 22 says "received today" [EMAIL:T1.4].
- **Overdue notice timing:** it's dated Apr 28, two days before the Apr 30 due date it cites [EMAIL:T1.6].
- **Days without contact:** the April record says 47 days [PERF:MER:2025-04]. The CRM entry from Apr 28 says 45 [CRM:2025-04-28:MER].
- **No separate revolver size:** the profile lists only the combined $8.5MM facility [PROFILE:MER], so I can't turn the percentages into dollar amounts.

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
    "get_email_threads({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 14227,
    "output_tokens": 2460
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 6,
  "rep": 1,
  "seconds": 30.3
}
```
