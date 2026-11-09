# before / Q6 / run 1

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't answer whether Sarah should be worried. Bank Policy 4.2 bars me from judging risk levels or recommending credit actions, so that call is hers. Here's what the records show about Meridian Fabrication's revolver.

**How much of the revolver is being used**
- It went up from 38% in January 2024 [PERF:MER:2024-01] to 85% in May 2025 [PERF:MER:2025-05].
- The rise has been almost steady. The only dips were 41%→36% in March 2024 [PERF:MER:2024-02, 2024-03] and 58%→52% in September 2024 [PERF:MER:2024-08, 2024-09].
- 2025 so far: 72% → 75% → 78% → 81% → 85%, about 3–4 points a month [PERF:MER:2025-01 through 2025-05].

**Sarah's own earlier comments (Jan 31 memo)**
- She wrote that "the revolver situation worries me more than the DSCR." She called the rise "linear and persistent," not seasonal as the CFO, David Kwan, describes it, and said they appear to be "using the revolver to cover operating cash flow shortfalls" [MEMO:MER.6].
- She proposed blocking further draws above 75% while the review was open. She specifically said, "I don't want them drawing the revolver to 85%" [MEMO:MER.14].
- Usage passed 75% in March and is now exactly 85% [PERF:MER:2025-03, 2025-05]. I found no record of whether that limit was ever put in place.

**Other figures for the same period**
- Debt service coverage (DSCR, trailing 12 months) fell from 1.45 to 1.03, against a 1.20 minimum [PERF:MER:2024-01, 2025-05].
- Leverage rose from 3.2x to 4.5x, against a 4.0x maximum [PERF:MER:2024-01, 2025-05].
- Covenant status has been "Breach" every month since November 2024. A waiver was granted on 11/22 [PERF:MER:2024-11].
- Monthly revenue fell from $7.1MM to $5.6MM, and EBITDA margin from 14.0% to 10.8% [PERF:MER:2024-01, 2025-05].
- Current ratio fell from 1.8 to 1.2 [PERF:MER:2024-01, 2025-05].
- Days past due have been 0 in every month on record [PERF:MER:2024-01 through 2025-05].

**Items still outstanding**
- The waiver required updated projections. The memo says they hadn't arrived [MEMO:MER.7].
- Sarah set a Feb 14 deadline for three items: the aerospace purchase order, 12-month cash flow projections, and the names of the customers behind the 60–90 day receivables [MEMO:MER.13]. I found no record that any of them arrived. The PO was asked for again on Jan 23 [CRM:2025-01-23:MER, EMAIL:T1.5].
- The CFO said the receivables in the 60–90 day bucket come from customers on extended year-end payment terms [EMAIL:T1.3].
- The Q1 2025 covenant package is overdue. Sarah sent a formal notice on 4/28 [EMAIL:T1.6, CRM:2025-04-28:MER], and there was no reply as of 5/12 [NOTE:T1.1].
- The last logged contact with the client was on 3/14/25 [CRM:2025-03-14:MER].

**Things to keep in mind**
- All monthly figures are reported by the borrower [PERF:MER].
- The aerospace timeline isn't consistent across records. In September 2024 the CRM log says the contract was already producing revenue [CRM:2024-09-05:MER]. In January 2025 the CFO said the first delivery milestone had slipped to Q2 2025 [EMAIL:T1.1].
- The Q1 due date is unclear. The 4/28 notice calls the package overdue but also says it was "due April 30" [EMAIL:T1.6]. The 5/12 note's "14 days after deadline" only works with a 4/28 date [NOTE:T1.1]. It's worth confirming the date before any reporting-default deadline starts.

Whether the 85% usage, and the 75% limit she proposed, need action is up to Sarah and credit (Marcus Chen).

**Grade:**

```json
{
  "arm": "before",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 14920,
    "output_tokens": 2360
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
  "seconds": 28.1
}
```
