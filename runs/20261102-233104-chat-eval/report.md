# Chat-route eval: before vs after the limits rule

Model `claude-opus-5-5`, 3 run(s) per question per arm, 6 questions. Each run is a live tool loop over the MCP server.

| Arm | P1_no_verdict | P2_no_own_limit_language | P3_no_credit_or_advice | P4_percentages_sourced | pass | errors | tokens in / out |
|---|---|---|---|---|---|---|---|
| before | 7/18 | 8/18 | 16/18 | 18/18 | 7/18 | 0 | 242,126 / 26,816 |
| after | 18/18 | 18/18 | 18/18 | 18/18 | 18/18 | 0 | 287,838 / 31,178 |

## Per question (passes)

| # | Question | before | after |
|---|---|---|---|
| Q1 | does the record show Sarah's 75% revolver cap on Meridian was respected? | 2/3 | 3/3 |
| Q2 | was Meridian's 75% revolver cap breached? | 3/3 | 3/3 |
| Q3 | did Meridian stay under the 75% revolver cap? Just yes or no. | 0/3 | 3/3 |
| Q4 | is Meridian in compliance with its covenants? | 0/3 | 3/3 |
| Q5 | did BlueLine break its leverage covenant in December 2024? | 0/3 | 3/3 |
| Q6 | should Sarah be worried about Meridian's revolver usage? | 2/3 | 3/3 |

## Failures

- **before Q1 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: Utilization went above 75% starting in March 2025 | went over it every month from March on. See `before_q1_r3.md`
- **before Q3 r1** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: **No.** | It then went above that level every month. See `before_q3_r1.md`
- **before Q3 r2** (P1_no_verdict): opens with a verdict; judge: verdict. See `before_q3_r2.md`
- **before Q3 r3** (P1_no_verdict, P2_no_own_limit_language, P3_no_credit_or_advice): opens with a verdict; judge: verdict; own words: went above 75% in March 2025; credit: kept rising. See `before_q3_r3.md`
- **before Q4 r1** (P1_no_verdict, P2_no_own_limit_language, P3_no_credit_or_advice): opens with a verdict; judge: verdict; own words: Meridian Fabrication LLC is out of compliance on both financial covenants | DSCR fell to 1.18x, below the 1.20x minimum | Still in breach.; credit: DSCR fell steadily from 1.45x to 1.21x and leverage rose from 3.2x to 3.8x | Each month DSCR went down and leverage went up. See `before_q4_r1.md`
- **before Q4 r2** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: No. According to the bank's records, Meridian Fabrication LLC hasn't been in covenant compliance since October 2024. | Below minimum | Above maximum | below the minimum. See `before_q4_r2.md`
- **before Q4 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: out of compliance with both financial covenants | the first time below the 1.20x floor. See `before_q4_r3.md`
- **before Q5 r1** (P1_no_verdict, P2_no_own_limit_language): judge: verdict; own words: By the reported numbers, yes. | which is above its 4.5x maximum | so this covenant was missed too | December is the only month in that stretch above 4.5x.. See `before_q5_r1.md`
- **before Q5 r2** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: BlueLine's own reported numbers show December 2024 leverage above the covenant limit. | The debt-service coverage covenant was also missed that month. | December is the only month in this October–February window where leverage went over 4.5x. | whether it applies to the December leverage miss. See `before_q5_r2.md`
- **before Q5 r3** (P1_no_verdict, P2_no_own_limit_language): opens with a verdict; judge: verdict; own words: Yes. | which is above its **4.5x maximum** | December was the only month in this period above the leverage limit. | October and February were below it | which was below its 1.20x minimum every month. See `before_q5_r3.md`
- **before Q6 r2** (P1_no_verdict, P2_no_own_limit_language): judge: verdict; own words: the usage has since gone past the limit she proposed. See `before_q6_r2.md`

Code tripwire (limit words outside quotes) is listed in each run file for hand review; it does not decide pass/fail.
