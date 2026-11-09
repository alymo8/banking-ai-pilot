# SYSTEM

You draft the factual sections of a relationship review memo for a Northfield Bank relationship manager. The audience is the Senior Credit Officer. The RM writes the assessment and recommendation separately. You never write them, summarize them, or anticipate them.

You will receive a verified fact sheet: facts by section, each with source ids. Write these sections, in this order, as Markdown with `##` headings:

## Relationship and Business Overview
## Facility Summary
## Financial Performance
## Covenant Compliance History
## Recent Communications and Outstanding Requests

How to write:
- Use only facts in the fact sheet. Do not add anything from general knowledge about the industry or the company.
- End every sentence that carries a figure, date, or borrower claim with its source ids in brackets, e.g. "...1.10x against a 1.20x minimum [PERF:MER:2024-12]."
- Attribute borrower statements: "The CFO stated...", "Per the borrower's January 18 email...".
- In Financial Performance, describe direction and magnitude with numbers ("revolver utilization rose from 38% to 69% over 2024"), never with evaluative words ("worrying", "sharp", "alarming", "healthy", "strong").
- Banking register: plain, specific, no filler, no hedging adjectives. One paragraph per section unless the facts need two. Use a short bullet list only for outstanding requests.
- Where the fact sheet marks a fact UNVERIFIED, leave it out. The RM will see it in the review notes.

Hard rules (bank AI policy section 4.2). Breaking any one makes the draft unusable:
- Do not characterize the borrower's creditworthiness, risk, outlook, or management quality, in any words, even implicitly. "The borrower faces significant headwinds" counts. "Results declined for four consecutive quarters" is fine.
- Do not state or imply a credit recommendation, covenant change, waiver decision, classification, or next credit step.
- Do not write a conclusion, summary of concerns, or "key risks" paragraph. The RM's sections follow yours.
- Do not mention the RM's assessment.


# USER

Borrower: Meridian Fabrication LLC
As-of date: 2025-01-31

VERIFIED FACT SHEET:
- (business) Meridian Fabrication LLC is classified in the Industrial Manufacturing industry and is headquartered in Ohio. [PROFILE:MER]
- (business) The profile records an employee count of 312 and annual revenue of $82mm. [PROFILE:MER]
- (business) The banking relationship dates from 2019 and is designated relationship tier 'Core'. [PROFILE:MER]
- (business) The primary borrower contact is David Kwan, CFO. [PROFILE:MER, EMAIL:T1.1]
- (business) Michelle Kwan attended the 2024-09-05 annual review alongside David Kwan. Her title and role are not stated in the records. [CRM:2024-09-05:MER]
- (business) The relationship manager is Sarah Okonkwo. Marcus Chen, Senior Credit Officer, and Priya Voss are the Northfield Bank colleagues involved in internal correspondence. [PROFILE:MER, EMAIL:T1.4, EMAIL:T1.5]
- (business) The records describe two customer segments: automotive OEM orders and an aerospace contract. [CRM:2024-01-08:MER, CRM:2024-04-10:MER, EMAIL:T1.1]
- (facility) The facility is a Term Loan plus Revolver with a total facility size of $8.5mm. [PROFILE:MER]
- (facility) The interest rate is variable at SOFR+275. [PROFILE:MER]
- (facility) The facility matures on 2027-03-31. [PROFILE:MER]
- (facility) The stated loan purpose is equipment expansion and working capital. [PROFILE:MER]
- (facility) Collateral is Machinery & Equipment plus A/R. [PROFILE:MER]
- (facility) The profile records personal_guarantee=Yes. The guarantor is not named. [PROFILE:MER]
- (facility) The reported loan balance was $8.3mm in Jan 2024 and $7.8mm in both Dec 2024 and Jan 2025. [PERF:MER:2024-01, PERF:MER:2024-12, PERF:MER:2025-01]
- (facility) The covenants are a minimum DSCR of 1.20x and a maximum leverage ratio of 4.0x. Both thresholds are unchanged in every monthly record from Jan 2024 through Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (facility) The profile lists the next covenant due date as 2025-06-30. [PROFILE:MER]
- (financial_performance) TTM DSCR fell from 1.45x (Jan 2024) to 1.08x (Jan 2025), declining in every month in between: 1.43, 1.41, 1.38, 1.36, 1.33, 1.28, 1.24, 1.21, 1.18, 1.14, 1.10. [PERF:MER:2024-01, PERF:MER:2024-02, PERF:MER:2024-03, PERF:MER:2024-04, PERF:MER:2024-05, PERF:MER:2024-06, PERF:MER:2024-07, PERF:MER:2024-08, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) The leverage ratio rose from 3.2x (Jan 2024) to 4.2x (Jan 2025). It was 3.8x in Sep 2024, 4.0x in Nov 2024 and 4.1x in Dec 2024. [PERF:MER:2024-01, PERF:MER:2024-09, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) Monthly revenue was $7,100k in Jan 2024 and $6,000k in Jan 2025. The highest month in the period was Mar 2024 at $7,400k. [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2025-01]
- (financial_performance) Monthly EBITDA was $994k in Jan 2024 and $720k in Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (financial_performance) EBITDA margin was 14.0% in Jan 2024 and 12.0% in Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (financial_performance) Revolver utilization was 38% in Jan 2024 and rose to 58% in Aug 2024. It was 52% in Sep 2024 and then rose each month to 72% in Jan 2025. [PERF:MER:2024-01, PERF:MER:2024-08, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) The current ratio was 1.8 in Jan 2024 and 1.3 in Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (financial_performance) Days past due was 0 in every monthly record from Jan 2024 through Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (covenant_history) Covenant status was recorded as Compliant in each month from Jan 2024 through Sep 2024. [PERF:MER:2024-01, PERF:MER:2024-02, PERF:MER:2024-03, PERF:MER:2024-04, PERF:MER:2024-05, PERF:MER:2024-06, PERF:MER:2024-07, PERF:MER:2024-08, PERF:MER:2024-09]
- (covenant_history) In Oct 2024, TTM DSCR was 1.18x against the 1.20x minimum and status was recorded as 'Covenant Watch'. The note reads 'DSCR below minimum — RM notified; waiver discussion initiated'. [PERF:MER:2024-10]
- (covenant_history) In Nov 2024, DSCR was 1.14x and leverage was 4.0x, and status was recorded as 'Covenant Breach'. The note reads 'Leverage at covenant max; DSCR below min'. [PERF:MER:2024-11]
- (covenant_history) Status was recorded as 'Covenant Breach' in Dec 2024 (DSCR 1.10x, leverage 4.1x) and in Jan 2025 (DSCR 1.08x, leverage 4.2x). [PERF:MER:2024-12, PERF:MER:2025-01]
- (covenant_history) The CRM log records that a waiver was approved on a 2024-11-08 call with David Kwan and Marcus Chen. The conditions were: Q4 package by Jan 31, and updated projections showing a recovery path. David Kwan committed to both. [CRM:2024-11-08:MER]
- (covenant_history) The Q1 2024 covenant package was recorded as received on time (CRM entry dated 2024-03-05, DSCR 1.41x, leverage 3.3x). [PERF:MER:2024-03, CRM:2024-03-05:MER]
- (covenant_history) The Q2 2024 covenant package was recorded as received 12 days late with no advance notice (CRM entry dated 2024-06-04, DSCR 1.33x, leverage 3.6x). [PERF:MER:2024-06, CRM:2024-06-04:MER]
- (covenant_history) The CRM log dated 2024-10-15 records the Q3 2024 covenant package as received on time, with DSCR 1.18x and leverage 3.9x. In that entry the RM wrote: 'This is the first formal breach.' [CRM:2024-10-15:MER]
- (covenant_history) The Q4 2024 covenant package was recorded as not yet received as of 12/31. The Jan 2025 record notes 'Q4 package received 1/18 — 18 days late'. [PERF:MER:2024-12, PERF:MER:2025-01]
- (covenant_history) The records contain no waiver or other documented action addressing the Dec 2024 or Jan 2025 covenant results. [PERF:MER:2024-12, PERF:MER:2025-01, CRM:2025-01-23:MER]
- (communications) On a 2024-01-08 call, David Kwan stated that the Q4 pipeline looked solid and that the aerospace contract was expected to contribute starting Q1. He described auto OEM orders as soft but within normal seasonal range. The RM logged 'No covenant concerns flagged' and a follow-up to request the Q1 package by end of April. [CRM:2024-01-08:MER]
- (communications) On a 2024-02-14 call, David Kwan stated that the aerospace contract was still on track and that auto OEM orders were picking up slightly in February. [CRM:2024-02-14:MER]
- (communications) On a 2024-04-10 call, David Kwan disclosed that automotive OEM orders were down 8% YoY through March, worse than management expected. He stated the aerospace contract would offset this in Q2. The RM asked for updated projections; he said he would send them by end of month. The RM logged 'Did not receive projections.' [CRM:2024-04-10:MER, PERF:MER:2024-04]
- (communications) In the 2024-04-10 CRM log the RM wrote: 'Tone was measured but I sense more stress than prior calls.' [CRM:2024-04-10:MER]
- (communications) On 2024-05-14 the RM sent a follow-up email requesting the updated projections. The outcome was logged as 'No Response'. [CRM:2024-05-14:MER]
- (communications) The Q2 package cover note from David Kwan mentioned continuing automotive softness. The RM logged that aerospace revenues were not yet flowing, and her call to David on 2024-06-04 went to voicemail. In that log the RM wrote: 'This is a trend I need to watch closely.' [CRM:2024-06-04:MER]
- (communications) On a 2024-07-09 call, David Kwan stated the aerospace contract was delayed further, with first revenue now expected in Q3 rather than Q2. He framed 55% revolver utilization as a seasonal working capital need. In that log the RM wrote: 'I'm not sure I agree given the pattern.' The RM recorded that she flagged the account internally to Marcus Chen. [CRM:2024-07-09:MER, PERF:MER:2024-07]
- (communications) At the 2024-09-05 annual review (video call, 60 min) with David and Michelle Kwan, the RM logged that the aerospace contract was producing revenue with a slower ramp than projected. Michelle Kwan was described as confident in the aerospace pipeline. The RM wrote: 'I'm less confident.' The RM also logged that she would request updated projections. [CRM:2024-09-05:MER]
- (communications) On 2024-10-15 the RM emailed David Kwan about the DSCR result. He called back the same day and cited aerospace timing. [CRM:2024-10-15:MER]
- (communications) In a 2025-01-18 email submitting the Q4 2024 package, David Kwan stated the following: the delay was due to year-end close complications; the aerospace contract came through but its first delivery milestone was pushed to Q2 2025; the company is about 11 weeks behind on that contract; and an internal projection has the company back above the DSCR floor by Q3 2025. He offered to share updated projections on a call. [EMAIL:T1.1]
- (communications) On 2025-01-21 the RM acknowledged the package, proposed a call, and requested the signed management representation letter and the updated accounts receivable aging by Wednesday. She noted these were not in the package. [EMAIL:T1.2]
- (communications) On 2025-01-22 David Kwan agreed to a Thursday 11am call and committed to send the rep letter and AR aging by end of day Wednesday. He also stated three things: the AR aging would show larger balances in the 60-90 day bucket; two automotive customers went on extended payment terms at year-end, a December pattern he said was more pronounced this year; and 'Nothing we'd call collection risk at this point.' [EMAIL:T1.3]
- (communications) On 2025-01-22 the RM sent an internal summary to Marcus Chen and Priya Voss. On the AR aging she wrote: 'client says seasonal, we should verify.' She also wrote: 'If projections don't support a Q3 recovery path I think we need to start the modification conversation.' [EMAIL:T1.4]
- (communications) On 2025-01-23 Marcus Chen asked the RM to do two things: ask David Kwan whether the aerospace contract has a firm PO or is still conditional, and obtain the customer names on the 60-90 day AR items. [EMAIL:T1.5]
- (communications) On a 2025-01-23 call (35 min), the RM logged DSCR 1.10x and leverage 4.1x with 'breach confirmed', and that aerospace revenues were coming in but behind projections. David Kwan committed to a Q1 recovery path. Marcus Chen joined for the last 10 minutes and asked about a firm PO on the aerospace contract; David said he would send it. [CRM:2025-01-23:MER]
- (open_requests) Updated projections were first requested on 2024-04-10 (the CFO said end of April) and followed up on 2024-05-14 with no response. The RM noted on 2024-09-05 that she would request them. They were made a waiver condition on 2024-11-08 and discussed again in Jan 2025 emails. There is no record of written projections being received. [CRM:2024-04-10:MER, CRM:2024-05-14:MER, CRM:2024-09-05:MER, CRM:2024-11-08:MER, EMAIL:T1.1, EMAIL:T1.2]
- (open_requests) The signed management representation letter was requested on 2025-01-21 for delivery by Wednesday, and the CFO committed to end of day Wednesday. There is no record of receipt. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) The updated accounts receivable aging was requested on 2025-01-21, and the CFO committed to end of day Wednesday. There is no record of receipt. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) Documentation of a firm PO on the aerospace contract was requested on the 2025-01-23 call. The CRM log records it as 'Not received as of this log entry.' [CRM:2025-01-23:MER, EMAIL:T1.5]
- (open_requests) The customer names on the 60-90 day AR balances were requested internally by Marcus Chen on 2025-01-23. There is no record that they were obtained. [EMAIL:T1.5]
