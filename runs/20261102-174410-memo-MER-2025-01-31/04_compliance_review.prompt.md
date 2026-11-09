# SYSTEM

You are a compliance reviewer at Northfield Bank. You check AI-drafted memo text against the bank's AI Use Policy, section 4.2 (Credit-adjacent outputs):

> AI tools may NOT be used to: generate credit recommendations (approve, decline, downgrade, upgrade); produce content that characterizes a borrower's creditworthiness; recommend covenant modifications, waivers, or credit structure changes; generate content that could be interpreted as a credit decision or material influence on one. This restriction applies to the format of the output, not just its content. An AI-generated memo that says "Based on the financial data, this borrower presents elevated risk" -- even if framed as information -- may constitute a credit recommendation. AI tools may be used to: organize and present financial data, draft narrative around RM-authored assessments, flag missing information, summarize communications -- as long as the credit judgment language originates with the RM.

You will receive only the AI-authored sections of the memo. The RM-authored sections are excluded on purpose.

Flag every sentence that does any of the following, even mildly or implicitly:
- characterizes credit quality, risk, outlook, trajectory, or management quality (including loaded verbs and adjectives: "deteriorating", "struggling", "headwinds", "concerning", "only", "merely", "sharply", "fortunately");
- selects or orders facts to imply a conclusion (for example, a closing sentence that stacks negatives);
- implies an action ("which will require", "warrants attention", "should be monitored");
- states a borrower's claim or projection as fact without attribution.

Do not flag neutral statements of figures, dates, directions ("declined from X to Y"), or attributed quotes.

For each flag return the exact sentence, the rule it breaks, and a neutral rewrite that keeps the facts and citations. If nothing breaks a rule, return an empty list. Do not invent problems to look thorough.


# USER

AI-AUTHORED SECTIONS:

## Relationship and Business Overview

Meridian Fabrication LLC is an industrial manufacturing company headquartered in Ohio, with 312 employees and annual revenue of $82mm per the portfolio profile [PROFILE:MER]. Records reference automotive OEM customers and an aerospace contract as segments of the business [CRM:2024-01-08:MER, CRM:2024-04-10:MER, EMAIL:T1.1]. The banking relationship dates from 2019, the relationship tier is Core, and the RM is Sarah Okonkwo [PROFILE:MER]. The primary borrower contact is David Kwan, CFO [PROFILE:MER, EMAIL:T1.1]. Michelle Kwan attended the 2024-09-05 annual review with David Kwan, and the records do not state her title or role [CRM:2024-09-05:MER]. Other bank personnel on the account are Marcus Chen, Senior Credit Officer, and Priya Voss, who was copied on a 2025-01-22 internal email [EMAIL:T1.4, EMAIL:T1.5].

## Facility Summary

The facility is an $8.5mm term loan and revolver, priced at a variable rate of SOFR+275 and maturing 2027-03-31, for equipment expansion and working capital [PROFILE:MER]. Collateral is machinery and equipment plus accounts receivable, and the profile records a personal guarantee [PROFILE:MER]. The loan balance was $8.3mm in January 2024 and $7.8mm in December 2024 and January 2025 [PERF:MER:2024-01, PERF:MER:2024-12, PERF:MER:2025-01]. The profile lists the last annual review as 2024-09-15 and the next covenant due date as 2025-06-30 [PROFILE:MER].

## Financial Performance

Monthly revenue was $7,100k in January 2024 and reached the series high of $7,400k in March 2024. It was $6,200k in December 2024 and $6,000k in January 2025 [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-12, PERF:MER:2025-01]. Monthly EBITDA was $994k in January 2024 and $1,010k in March 2024, then $760k in December 2024 and $720k in January 2025 [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-12, PERF:MER:2025-01]. EBITDA margin was 14.0% in January and February 2024 and was lower in each subsequent month, reaching 12.3% in December 2024 and 12.0% in January 2025 [PERF:MER:2024-01, PERF:MER:2024-02, PERF:MER:2024-12, PERF:MER:2025-01]. The April 2024 PERF note records automotive sector orders down 8% YoY, per a client call [PERF:MER:2024-04].

TTM DSCR was lower in each month of the series. It went from 1.45x in January 2024 to 1.21x in September 2024 and 1.18x in October 2024, and was 1.08x in January 2025 [PERF:MER:2024-01, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2025-01]. The leverage ratio rose from 3.2x in January 2024 to 4.0x in November 2024 and 4.2x in January 2025 [PERF:MER:2024-01, PERF:MER:2024-11, PERF:MER:2025-01]. The current ratio moved from 1.8 in January 2024 to 1.3 in January 2025 [PERF:MER:2024-01, PERF:MER:2025-01]. Revolver utilization rose from 38% in January 2024 to 58% in August 2024 and was 52% in September 2024. It then rose each month to 72% in January 2025 [PERF:MER:2024-01, PERF:MER:2024-08, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]. Days past due was 0 in every monthly record from January 2024 through January 2025 [PERF:MER:2024-01, PERF:MER:2025-01].

## Covenant Compliance History

The covenants are a 1.20x minimum DSCR and a 4.0x maximum leverage ratio, and both are recorded at those levels in every monthly record from January 2024 through January 2025 [PERF:MER:2024-01, PERF:MER:2025-01]. Covenant status was Compliant from January 2024 through September 2024 [PERF:MER:2024-01, PERF:MER:2024-09]. Status was Covenant Watch in October 2024, and the PERF note reads "DSCR below minimum — RM notified; waiver discussion initiated" [PERF:MER:2024-10]. Status was Covenant Breach in November 2024, December 2024 and January 2025, and the November 2024 note reads "Leverage at covenant max; DSCR below min" [PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]. The leverage ratio exceeded the 4.0x maximum at 4.1x in December 2024 and 4.2x in January 2025 [PERF:MER:2024-12, PERF:MER:2025-01].

The Q1 2024 covenant package was recorded as submitted on time. The CRM logged its receipt on 2024-03-05 showing DSCR of 1.41x and leverage of 3.3x, both compliant [PERF:MER:2024-03, CRM:2024-03-05:MER]. The Q2 2024 package was recorded as received 12 days late with no advance notice, in a CRM entry dated 2024-06-04 showing DSCR of 1.33x and leverage of 3.6x [PERF:MER:2024-06, CRM:2024-06-04:MER]. The Q3 2024 package was logged on 2024-10-15 as received on time, showing DSCR of 1.18x against the 1.20x minimum and leverage of 3.9x [CRM:2024-10-15:MER]. A waiver was approved on a 2024-11-08 call with David Kwan and Marcus Chen. Its conditions were delivery of the Q4 package by January 31 and updated projections showing a recovery path, and David Kwan committed to both [CRM:2024-11-08:MER]. The November 2024 PERF record notes "waiver granted 11/22" [PERF:MER:2024-11]. The Q4 2024 package had not been received as of December 31. Per the PERF record, it was received January 18, 18 days late [PERF:MER:2024-12, PERF:MER:2025-01, EMAIL:T1.1]. The Q4 package showed DSCR of 1.10x and leverage of 4.1x, and the RM logged "breach confirmed" on 2025-01-23 [CRM:2025-01-23:MER, EMAIL:T1.4].

## Recent Communications and Outstanding Requests

**2024**

- **2024-01-08.** The CRM log records that David Kwan said the Q4 pipeline looked solid per management and that the aerospace contract was expected to contribute starting Q1. Auto OEM orders were described as soft but within normal seasonal range, and no covenant concerns were flagged [CRM:2024-01-08:MER].
- **2024-02-14.** He said the aerospace contract was on track and auto OEM orders were picking up slightly in February [CRM:2024-02-14:MER].
- **2024-04-10.** He disclosed that automotive OEM orders were down 8% YoY through March, worse than expected, and said the aerospace contract would offset this in Q2. He said he would send updated projections by end of month, and the log notes they were not received [CRM:2024-04-10:MER].
- **2024-05-14.** The RM sent a follow-up email requesting the projections and received no response [CRM:2024-05-14:MER].
- **2024-06-04.** David Kwan's cover note to the Q2 package mentioned continuing automotive softness. The RM logged that aerospace revenues were not yet flowing, and the RM's call to him went to voicemail [CRM:2024-06-04:MER].
- **2024-07-09.** He said the aerospace contract was delayed further, with first revenue now expected in Q3 rather than Q2. He framed 55% revolver utilization as a seasonal working capital need. The RM flagged the account internally to Marcus Chen [CRM:2024-07-09:MER].
- **2024-09-05.** At the annual review, a 60-minute video call, David and Michelle Kwan walked through Q3 financials. They stated the aerospace contract was producing revenue with a slower ramp than projected, and Michelle Kwan expressed confidence in the aerospace pipeline [CRM:2024-09-05:MER].
- **2024-10-15.** The RM emailed David Kwan about the Q3 DSCR result. He called back the same day and cited aerospace timing, and waiver discussion was initiated [CRM:2024-10-15:MER].

**2025**

- **2025-01-18, borrower email.** David Kwan attributed the Q4 package delay to year-end close complications. He stated that the aerospace contract's first delivery milestone was pushed to Q2 2025, that the expected Q4 revenue benefit did not occur, and that the contract was tracking about 11 weeks behind [EMAIL:T1.1]. He also stated that the company's internal projection has it back above the DSCR floor by Q3 2025, and he offered to share updated projections on a call [EMAIL:T1.1].
- **2025-01-21, RM reply.** The RM replied that she had logged the package and asked for a call. She requested the signed management representation letter and updated accounts receivable aging, which were not in the package, by Wednesday [EMAIL:T1.2].
- **2025-01-22, borrower email.** David Kwan confirmed a Thursday 11am call and said he would send the rep letter and AR aging by end of day Wednesday [EMAIL:T1.3]. He stated the AR aging would show larger balances in the 60-90 day bucket because two automotive customers went on extended payment terms at year-end. He described this as a pattern seen every December but more pronounced this year, and wrote, "Nothing we'd call collection risk at this point" [EMAIL:T1.3].
- **2025-01-23, internal email.** Marcus Chen asked the RM to ask David Kwan directly whether the aerospace contract has a firm PO or is still conditional. He also asked her to get the customer names on the 60-90 day AR items [EMAIL:T1.5].
- **2025-01-23, call.** The RM logged that David Kwan said aerospace revenues are coming in but behind projections, and that he committed to a Q1 recovery path. Marcus Chen asked about a firm PO on the aerospace contract, and David Kwan said he would send it [CRM:2025-01-23:MER].

Outstanding requests as of 2025-01-31:

- **Updated projections.** Requested on 2024-04-10 and promised by end of April. Requested again by email on 2024-05-14, with no response. Noted as to-be-requested on 2024-09-05. Set as a waiver condition on 2024-11-08. Asked to be presented on the call on 2025-01-21. No record shows written projections received [CRM:2024-04-10:MER, CRM:2024-05-14:MER, CRM:2024-09-05:MER, CRM:2024-11-08:MER, EMAIL:T1.1, EMAIL:T1.2].
- **Signed management representation letter.** Requested on 2025-01-21 and promised by end of day 2025-01-22. No record shows receipt [EMAIL:T1.2, EMAIL:T1.3].
- **Updated accounts receivable aging.** Requested on 2025-01-21 and promised by end of day 2025-01-22. No record shows receipt [EMAIL:T1.2, EMAIL:T1.3].
- **Firm PO for the aerospace contract.** Requested on the 2025-01-23 call. The CRM log records it as not received as of that entry [CRM:2025-01-23:MER, EMAIL:T1.5].
- **Customer names on 60-90 day AR balances.** Requested internally by Marcus Chen on 2025-01-23. No record shows they were asked of or received from the borrower [EMAIL:T1.5].
