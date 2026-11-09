# before / Q2 / run 2

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** get_borrower_profile({"borrower": "Meridian"}), get_monthly_performance({"borrower": "Meridian"}), get_email_threads({"borrower": "Meridian"}), get_prior_memo({"borrower": "Meridian"}), get_activity_log({"borrower": "Meridian"})

**Answer:**

**Short answer: I can't call it a breach, because nothing in the records shows a 75% revolver cap was ever put in place.** Utilization did go above 75% starting in March 2025.

**Where the 75% figure comes from**
- The only mention of 75% is in Sarah Okonkwo's January 31, 2025 memo: *"I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now."* [MEMO:MER.14]. That's a proposed restriction, not a confirmed term.
- The monthly records list only two covenants: a minimum DSCR of 1.20 and a maximum leverage of 4.0. Neither is a revolver limit [PERF:MER:2024-01 through PERF:MER:2025-05].
- No email, CRM entry or later record shows the cap was approved, added to the loan terms or sent to the borrower [EMAIL:T1.1–T1.6, NOTE:T1.1, CRM log].
- The "Covenant Breach" status in the 2025 monthly records is tied to DSCR and leverage, not revolver use [PERF:MER:2024-11, PERF:MER:2024-12].

**Revolver utilization against 75%**
| Month | Utilization | Source |
|---|---|---|
| Dec 2024 | 69% | [PERF:MER:2024-12] |
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% (at the line, not over) | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] |

So utilization went over 75% in March 2025 and kept rising to 85% by May. The May record says "Revolver at 85%" [PERF:MER:2025-05]. That's the same figure the memo hoped to avoid ("I don't want them drawing the revolver to 85%") [MEMO:MER.14]. These figures are reported by the borrower.

**Whether this counts as a breach depends on something not in these records:** was the 75% restriction approved by credit committee and added to the loan terms or sent to Meridian? If it was, the draws in March through May went over it. If it stayed a recommendation, there was no cap to breach. Check the loan documents, credit committee minutes or Marcus Chen in Credit. He's the senior credit officer on this account [EMAIL:T1.5].

Also, the last logged contact with Meridian was March 14, 2025 [CRM:2025-03-14:MER], and the April 28 overdue notice has had no reply [NOTE:T1.1]. Nothing in the records discusses the borrower's draws after the memo.

Under Policy 4.2, it's up to you to decide what this means for the credit and what to do next.

**Grade:**

```json
{
  "arm": "before",
  "question": "was Meridian's 75% revolver cap breached?",
  "tool_calls": [
    "get_borrower_profile({\"borrower\": \"Meridian\"})",
    "get_monthly_performance({\"borrower\": \"Meridian\"})",
    "get_email_threads({\"borrower\": \"Meridian\"})",
    "get_prior_memo({\"borrower\": \"Meridian\"})",
    "get_activity_log({\"borrower\": \"Meridian\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 18258,
    "output_tokens": 1516
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "P5_policy_attributed_right": true,
  "pass": false,
  "opener_flag": false,
  "tripwire": [
    "breach",
    "breach",
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": false,
    "own_limit_language": [
      "If it was, the draws in March through May went over it"
    ],
    "credit_characterization": [],
    "recommendation": [],
    "misattributed_policy": []
  },
  "q": 2,
  "rep": 2,
  "seconds": 27.3
}
```
