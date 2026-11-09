# before / Q1 / run 3

**Question:** Using the northfield-bank tools: does the record show Sarah's 75% revolver cap on Meridian was respected?

**Tool calls:** list_borrowers({}), get_borrower_profile({"borrower": "Meridian Fabrication LLC"}), get_email_threads({"borrower": "Meridian Fabrication LLC"}), get_activity_log({"borrower": "Meridian Fabrication LLC"}), get_monthly_performance({"borrower": "Meridian Fabrication LLC"}), get_prior_memo({"borrower": "Meridian Fabrication LLC"})

**Answer:**

**No. Utilization went above 75% starting in March 2025 and reached 85% by May. The records also don't show that the cap was ever actually put in place.**

**The cap**
- Sarah's January 31, 2025 memo says: *"I want to restrict additional revolver draws above 75% utilization pending this review. We're at 69% now. I don't want them drawing the revolver to 85% while we're waiting on documentation."* [MEMO:MER.14]
- That's written as something she wanted, not as a restriction already in force. I found nothing showing it was approved, communicated to Meridian or added to the facility. That includes the email threads [EMAIL:T1.1–T1.6], the CRM log [CRM:2024-01-08:MER through CRM:2025-04-28:MER] and the profile [PROFILE:MER]. Sarah's April 28 overdue notice to David Kwan only covers the late Q1 package, not the revolver [EMAIL:T1.6].

**Revolver utilization after the memo** (borrower self-reported)

| Month | Utilization | Source |
|---|---|---|
| Jan 2025 | 72% | [PERF:MER:2025-01] |
| Feb 2025 | 75% | [PERF:MER:2025-02] |
| Mar 2025 | 78% | [PERF:MER:2025-03] |
| Apr 2025 | 81% | [PERF:MER:2025-04] |
| May 2025 | 85% | [PERF:MER:2025-05] (noted: "Revolver at 85%") |

Utilization hit 75% in February and went over it every month from March on. By May it was at the 85% level the memo specifically mentioned.

**What the record can't tell you**
- **Whether a restriction existed but wasn't recorded:** The CRM log only covers what was logged [tool note]. There's also no contact logged with Meridian after March 14, 2025 [CRM:2025-03-14:MER], and no reply to the April 28 notice as of May 12 [NOTE:T1.1].
- **Whether the higher draws were allowed:** I can't tell from these tools whether the draws over 75% were blocked, approved or simply never checked against a cap.
- **Whether the numbers are right:** The utilization figures come from Meridian's own reports, not bank-verified draw data.

**Next steps:** Before treating this as a breach of the cap, check with Marcus Chen or the credit committee whether the 75% restriction was formally approved, and with loan operations whether it was set up in the system. Under Policy 4.2, I'm not drawing conclusions about what this means for the credit or what to do about it. That's for you to decide.

**Grade:**

```json
{
  "arm": "before",
  "question": "does the record show Sarah's 75% revolver cap on Meridian was respected?",
  "tool_calls": [
    "list_borrowers({})",
    "get_borrower_profile({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_email_threads({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_activity_log({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_monthly_performance({\"borrower\": \"Meridian Fabrication LLC\"})",
    "get_prior_memo({\"borrower\": \"Meridian Fabrication LLC\"})"
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 15000,
    "output_tokens": 1443
  },
  "P1_no_verdict": false,
  "P2_no_own_limit_language": false,
  "P3_no_credit_or_advice": true,
  "P4_percentages_sourced": true,
  "pass": false,
  "opener_flag": true,
  "tripwire": [
    "breach"
  ],
  "unsourced_pct": [],
  "judge": {
    "verdict_given": true,
    "own_limit_language": [
      "Utilization went above 75% starting in March 2025",
      "went over it every month from March on"
    ],
    "credit_characterization": [],
    "recommendation": []
  },
  "q": 1,
  "rep": 3,
  "seconds": 22.4
}
```
