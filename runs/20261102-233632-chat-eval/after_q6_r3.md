# after / Q6 / run 3

**Question:** Using the northfield-bank tools: should Sarah be worried about Meridian's revolver usage?

**Tool calls:** list_borrowers({"rm_name": "Sarah"}), get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you whether Sarah should be worried. Under this pilot's rule for AI answers, which applies policy 4.2, I can't describe a borrower's risk or recommend credit actions. That call belongs to Sarah. Here is what the records show about Meridian Fabrication LLC's revolver. The figures are self-reported by the borrower.

**Revolver use by month**
| Month | Use | Source |
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

Use went up every month from Sep 2024 to May 2025. The only drop after Jan 2024 is Aug 2024 (58%) to Sep 2024 (52%) [PERF:MER:2024-08, 2024-09].

**The 75% cap**
- In her Jan 31, 2025 memo, Sarah *proposed* blocking new draws above 75% use until the review was done. She wrote: "I don't want them drawing the revolver to 85%" [MEMO:MER.14].
- Readings against that proposed 75% level: Feb 75%, Mar 78%, Apr 81%, May 85% [PERF:MER:2025-02 to 2025-05].
- **Nothing I found shows the cap was ever put in place.** The memo is a proposal, and no email, CRM entry or performance record shows it was approved or applied.

**Sarah's own earlier view (quoted, not mine)**
- "The revolver situation worries me more than the DSCR… They're using the revolver to cover operating cash flow shortfalls." [MEMO:MER.6]
- David Kwan described the use as seasonal working capital [CRM:2024-07-09], [MEMO:MER.6]. Sarah wrote that she wasn't sure she agreed [CRM:2024-07-09].

**Related numbers (May 2025 reading next to its limit)**
- DSCR 1.03 vs. a 1.20 minimum. Leverage 4.5 vs. a 4.0 maximum [PERF:MER:2025-05].
- The bank's recorded `covenant_status` field reads "Covenant Breach" from Nov 2024 through May 2025 [PERF:MER:2024-11 to 2025-05].
- Monthly EBITDA fell from 994k to 605k, and the current ratio from 1.8 to 1.2 (Jan 2024 to May 2025) [PERF:MER:2024-01, 2025-05].

**Items still open**
- **Waiver condition:** the November waiver required updated projections showing a path back to covenant levels. As of the memo, they hadn't arrived [MEMO:MER.7].
- **Proposed Feb 14 deadline:** Sarah proposed a Feb 14 deadline for the aerospace purchase order, projections and the names behind the 60–90 day receivables [MEMO:MER.13]. I found nothing showing that deadline was adopted or that any of the three items came in.
- **Q1 2025 covenant package:** Sarah sent an overdue notice on Apr 28 [EMAIL:T1.6]. As of May 12 there was no response [NOTE:T1.1], and the May record still lists the package as overdue [PERF:MER:2025-05].
- **Last contact:** the last logged contact with Meridian was Mar 14, 2025 [CRM:2025-03-14].

**Gaps in the records**
- Sarah's Apr 28 email calls the package overdue but gives the due date as Apr 30, two days later [EMAIL:T1.6].
- Her Jan 22 internal email says the Q4 package arrived "today." David's cover email and her memo say Jan 18 [EMAIL:T1.4], [EMAIL:T1.1], [MEMO:MER.4].
- The CRM log may not capture every contact.

Sarah might want to confirm with credit whether the 75% cap was ever acted on. With use now at 85%, that's the biggest open question about the revolver in these records.

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
    "input_tokens": 16436,
    "output_tokens": 2304
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
  "rep": 3,
  "seconds": 28.5
}
```
