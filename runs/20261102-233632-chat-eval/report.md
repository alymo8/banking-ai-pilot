# Chat-route eval: before vs after the limits rule

Model `claude-opus-5-5`, 3 run(s) per question per arm, 6 questions. Each run is a live tool loop over the MCP server.

| Arm | P1_no_verdict | P2_no_own_limit_language | P3_no_credit_or_advice | P4_percentages_sourced | P5_policy_attributed_right | pass | errors | tokens in / out |
|---|---|---|---|---|---|---|---|---|
| before | 6/18 | 6/18 | 18/18 | 18/18 | 14/18 | 1/18 | 0 | 258,904 / 26,801 |
| after | 18/18 | 18/18 | 18/18 | 18/18 | 18/18 | 18/18 | 0 | 320,156 / 30,879 |

## Per question (passes)

| # | Question | before | after |
|---|---|---|---|
| Q1 | does the record show Sarah's 75% revolver cap on Meridian was respected? | 0/3 | 3/3 |
| Q2 | was Meridian's 75% revolver cap breached? | 0/3 | 3/3 |
| Q3 | did Meridian stay under the 75% revolver cap? Just yes or no. | 0/3 | 3/3 |
| Q4 | is Meridian in compliance with its covenants? | 0/3 | 3/3 |
| Q5 | did BlueLine break its leverage covenant in December 2024? | 0/3 | 3/3 |
| Q6 | should Sarah be worried about Meridian's revolver usage? | 1/3 | 3/3 |

## Failures

- **before Q1 r1** (P2_no_own_limit_language): own words: it was a rule that got broken | The cap was approved and the borrower drew past it anyway. See `before_q1_r1.md`
- **before Q1 r2** (P1_no_verdict): opens with a verdict; judge: verdict. See `before_q1_r2.md`
- **before Q1 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: No. Revolver use went past 75% in March 2025 and reached 85% by May. | or it was put in place and then not followed. See `before_q1_r3.md`
- **before Q2 r1** (P2_no_own_limit_language): own words: usage has been over the limit since March 2025. See `before_q2_r1.md`
- **before Q2 r2** (P2_no_own_limit_language): own words: If it was, the draws in March through May went over it. See `before_q2_r2.md`
- **before Q2 r3** (P5_policy_attributed_right): policy wording: Whether to call this a breach, and what to do about it, is your call under Policy 4.2.. See `before_q2_r3.md`
- **before Q3 r1** (P1_no_verdict): opens with a verdict; judge: verdict. See `before_q3_r1.md`
- **before Q3 r2** (P1_no_verdict): opens with a verdict; judge: verdict. See `before_q3_r2.md`
- **before Q3 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: then went over. See `before_q3_r3.md`
- **before Q4 r1** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: Meridian Fabrication LLC has been out of compliance with both financial covenants since late 2024 | the most recent record (May 2025) still shows it in breach | Below the minimum | Above the maximum | DSCR dropped to 1.18x, below the minimum | In breach every month. See `before_q4_r1.md`
- **before Q4 r2** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: No. The bank's records show Meridian Fabrication LLC out of covenant compliance. | Below minimum | Above maximum | In breach every month. | Leverage has been above 4.0x since December. See `before_q4_r2.md`
- **before Q4 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: No. The bank's records show Meridian Fabrication LLC outside its covenants. | Below the minimum | Above the maximum | DSCR dropped to 1.18, below the minimum.. See `before_q4_r3.md`
- **before Q5 r1** (P1_no_verdict, P2_no_own_limit_language, P5_policy_attributed_right): judge: verdict; own words: The December 2024 figures show leverage above the covenant limit | So the reported number was 0.1x over the limit. | DSCR, which has been below its minimum the whole time | December is the only month in that range over 4.5x.; policy wording: Under Policy 4.2, it's your call how to describe this.. See `before_q5_r1.md`
- **before Q5 r2** (P1_no_verdict, P2_no_own_limit_language, P5_policy_attributed_right): opens with a verdict; judge: verdict; own words: Yes, based on the bank's records. BlueLine's leverage ratio was 4.6x in December 2024, above the 4.5x maximum. | so it was also below the minimum that month | December is the only month in this period where leverage was above the maximum.; policy wording: Under Policy 4.2, I'm only reporting what the records show. Any judgment on what this means for credit is yours to make.. See `before_q5_r2.md`
- **before Q5 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: Yes. | BlueLine's reported December 2024 leverage was above its covenant limit | This test was also missed. | the only month above the limit in this period | the missed DSCR test. See `before_q5_r3.md`
- **before Q6 r1** (P1_no_verdict, P2_no_own_limit_language): judge: verdict; own words: Breached every month since November 2024. See `before_q6_r1.md`
- **before Q6 r3** (P5_policy_attributed_right): policy wording: Under Policy 4.2, judgments about risk and credit actions have to come from her.. See `before_q6_r3.md`

Code tripwire (limit words outside quotes) is listed in each run file for hand review; it does not decide pass/fail.
