# before / Q6 / run 2

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you whether Sarah should be worried. Bank Policy 4.2 says I can't describe how risky a credit is or how likely a breach is, and that judgement has to come from her. What I can do is lay out what the records show about the revolver. Sarah's own January memo already gives her view.

**Revolver usage over time (self-reported by the borrower)**
- **2024:** Usage climbed from 38% in January [PERF:MER:2024-01] to 58% in August [PERF:MER:2024-08]. It dipped to 52% in September [PERF:MER:2024-09], then reached 69% by December [PERF:MER:2024-12].
- **2025:** 72% in January, 75% in February, 78% in March, 81% in April and 85% in May [PERF:MER:2025-01 through 2025-05].
- The only month it fell was September 2024. Every other month it rose.

**What it means against Sarah's own limit**
- On January 31, 2025, Sarah wrote that she wanted to block further draws once usage passed 75%. She added: "I don't want them drawing the revolver to 85% while we're waiting on documentation" [MEMO:MER.14]. Usage has since reached 85% [PERF:MER:2025-05].
- I can't find any record that the 75% limit was actually put in place. It may be worth checking.
- In the same memo, Sarah wrote that "the revolver situation worries me more than the DSCR" (debt service coverage ratio). She said the increase was "linear and persistent," not seasonal, and that the company seemed to be using the revolver to cover operating cash shortfalls [MEMO:MER.6]. CFO David Kwan has called it seasonal working capital [CRM:2024-07-09:MER].

**Other trends over the same period**
- **DSCR:** fell from 1.45x to 1.03x, against a 1.20x minimum [PERF:MER:2024-01], [PERF:MER:2025-05].
- **Leverage:** rose from 3.2x to 4.5x, against a 4.0x maximum [PERF:MER:2024-01], [PERF:MER:2025-05].
- **Current ratio:** fell from 1.8 to 1.2 [PERF:MER:2024-01], [PERF:MER:2025-05].
- **Monthly revenue:** fell from $7.1M to $5.6M [PERF:MER:2024-01], [PERF:MER:2025-05].
- **Covenant status:** listed as "Covenant Breach" every month since November 2024. A waiver was granted on November 22 [PERF:MER:2024-11].
- **Payments:** zero days past due throughout [PERF:MER:2025-05].

**Items still outstanding**
- **Documents:** the aerospace purchase order, 12-month cash flow projections and the customer names on the 60–90 day receivables were all still missing as of January 31 [MEMO:MER.7–10]. Sarah proposed a February 14 deadline for them [MEMO:MER.13]. I found no record of that deadline being set or met.
- **Q1 2025 covenant package:** not received. Sarah sent an overdue notice on April 28 and got no reply [CRM:2025-04-28:MER], [EMAIL:T1.6]. There was still no reply as of May 12 [NOTE:T1.1].
- **Last contact:** the most recent logged conversation with the client was on March 14, 2025 [CRM:2025-03-14:MER].

**Inconsistencies in the records**
- **Aerospace timing:** the CRM log says aerospace revenue was "now producing revenue" in September 2024 and "coming in" in January 2025 [CRM:2024-09-05:MER], [CRM:2025-01-23:MER]. But David's January 18 email says the first delivery milestone slipped to Q2 2025 [EMAIL:T1.1]. The promised start date has also moved several times: Q1, then Q2, then Q3 2024 in the CRM log, and Q2 2025 in his email [CRM:2024-01-08:MER], [CRM:2024-04-10:MER], [CRM:2024-07-09:MER].
- **Notice timing:** the overdue notice is dated April 28 but says the package "was due April 30" [EMAIL:T1.6]. The May 12 note's "14 days after deadline" counts from April 28 [NOTE:T1.1]. Before relying on a reporting-default trigger, Sarah may want to confirm the actual due date in the loan agreement.
- **Days since contact:** the CRM log says 45 days and the performance notes say 47 [CRM:2025-04-28:MER], [PERF:MER:2025-04].

All the performance figures come from the borrower and haven't been independently checked. The next covenant date is June 30, 2025 [PROFILE:MER]. What this adds up to and what to do about it are for Sarah and credit to decide.

**Grade:**

```json
{
  "arm": "before",
  "question": "should Sarah be worried about Meridian's revolver usage?",
  "tool_calls": [
    "list_borrowers({\"rm_name\": \"Sarah\"})",
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15325,
    "output_tokens": 2535
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 6,
  "rep": 2,
  "seconds": 35.6
}
```
