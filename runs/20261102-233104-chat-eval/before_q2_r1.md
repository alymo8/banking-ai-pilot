# before / Q2 / run 1

**Question:** Using the northfield-bank tools: was Meridian's 75% revolver cap breached?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

I can't tell you it was breached, because the records don't show a 75% cap was ever put in place. What they do show is that revolver utilization went above 75% starting in March 2025.

**Where the 75% figure comes from**
The only mention of 75% is in Sarah Okonkwo's January 31, 2025 memo. In it she says she *wants* to "restrict additional revolver draws above 75% utilization pending this review," and notes utilization was 69% at the time [MEMO:MER.14]. The same memo frames its points as recommendations to the credit committee [MEMO:MER.13].

I couldn't find anything showing the cap was approved, documented or told to the borrower:
- **Monthly performance records:** these track only two covenants, minimum DSCR (1.20) and maximum leverage (4.0x). There's no revolver utilization limit [PERF:MER:2024-01 through 2025-05].
- **Profile:** no revolver sub-limit is listed [PROFILE:MER].
- **Emails and CRM log:** neither mentions a revolver restriction being approved or sent to David Kwan. The 2025 contacts are about the covenant packages and the overdue notice [EMAIL:T1.1–T1.6], [CRM:2025-01-23:MER], [CRM:2025-03-14:MER], [CRM:2025-04-28:MER].

**Revolver utilization compared with 75%**
| Month | Utilization | Source |
|---|---|---|
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% (at the level, not above) | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] (notes: "Revolver at 85%") |

These figures are self-reported by the borrower.

**Bottom line**
Utilization has been above 75% every month since March 2025, reaching 85% in May. That's the level the memo specifically said it wanted to avoid [MEMO:MER.14]. Whether that counts as a breach depends on whether the cap was actually approved and put into the loan terms, and these records don't answer that. To find out, you'd need the credit committee's decision on the January 31 memo or any loan amendment or borrower notice. You could also check with Marcus Chen, the senior credit officer copied on the internal emails [EMAIL:T1.4], [EMAIL:T1.5].

Separately, the records do mark Meridian as being in breach of its DSCR and leverage covenants every month from November 2024 through May 2025 [PERF:MER:2024-11 through 2025-05].

**Grade:**

```json
{
  "arm": "before",
  "question": "was Meridian's 75% revolver cap breached?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 14965,
    "output_tokens": 1432
  },
  "P1_no_verdict": true,
  "P2_no_own_limit_language": true,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": true,
  "opener_flag": false,
  "tripwire": [
    "breached",
    "breach",
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
  "rep": 1,
  "seconds": 21.9
}
```
