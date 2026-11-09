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
- Do not compute new figures (differences, percentage changes, averages). State a change as its two endpoints with dates. Give the start, the end and any turning point, not every monthly value.
- Where the fact sheet marks a fact UNVERIFIED, leave it out. The RM will see it in the review notes.

Hard rules (bank AI policy section 4.2). Breaking any one makes the draft unusable:
- Do not characterize the borrower's creditworthiness, risk, outlook, or management quality, in any words, even implicitly. "The borrower faces significant headwinds" counts. "Results declined for four consecutive quarters" is fine.
- Do not state or imply a credit recommendation, covenant change, waiver decision, classification, or next credit step.
- Do not write a conclusion, summary of concerns, or "key risks" paragraph. The RM's sections follow yours.
- Do not mention the RM's assessment.


# USER

Borrower: Meridian Fabrication LLC
As-of date: 2025-05-31

VERIFIED FACT SHEET:
- (business) Meridian Fabrication LLC is classified in the Industrial Manufacturing industry, is headquartered in Ohio, and has 312 employees. [PROFILE:MER]
- (business) The banking relationship dates from 2019. The relationship tier is Core, and the relationship manager is Sarah Okonkwo. [PROFILE:MER]
- (business) The primary borrower contact is David Kwan, CFO. [PROFILE:MER, EMAIL:T1.1]
- (business) Michelle Kwan attended the 2024-09-05 annual review alongside David Kwan. Her title and role are not stated in the records. [CRM:2024-09-05:MER]
- (business) Per borrower discussions logged in CRM, the company serves automotive OEM customers and has an aerospace contract. [CRM:2024-01-08:MER, CRM:2024-04-10:MER, EMAIL:T1.1]
- (business) Bank personnel involved with the account include Marcus Chen (Senior Credit Officer) and Priya Voss, whose title is not stated. [EMAIL:T1.4, EMAIL:T1.5]
- (facility) The facility is a Term Loan + Revolver with a total facility size of $8.5mm. [PROFILE:MER]
- (facility) The facility carries a variable rate of SOFR+275. [PROFILE:MER]
- (facility) The facility matures on 2027-03-31. [PROFILE:MER]
- (facility) The stated loan purpose is equipment expansion and working capital. [PROFILE:MER]
- (facility) Collateral is Machinery & Equipment plus A/R, and the facility carries a personal guarantee (personal_guarantee=Yes). [PROFILE:MER]
- (facility) The loan balance fell from $8.3mm (Jan 2024) to $7.6mm (Apr and May 2025). [PERF:MER:2024-01, PERF:MER:2025-04, PERF:MER:2025-05]
- (facility) PROFILE lists the last annual review as 2024-09-15 and the next covenant due date as 2025-06-30. [PROFILE:MER]
- (financial_performance) Monthly revenue was $7,100k in Jan 2024, peaked at $7,400k in Mar 2024, and was $5,600k in May 2025. [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2025-05]
- (financial_performance) Monthly revenue declined in each month from Sep 2024 ($6,850k) through May 2025 ($5,600k). The intervening figures were $6,600k, $6,400k, $6,200k, $6,000k, $5,900k, $5,800k and $5,700k. [PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01, PERF:MER:2025-02, PERF:MER:2025-03, PERF:MER:2025-04, PERF:MER:2025-05]
- (financial_performance) Monthly EBITDA fell from $994k (Jan 2024) to $605k (May 2025). It was $1,010k in Mar 2024 and $760k in Dec 2024. [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-12, PERF:MER:2025-05]
- (financial_performance) EBITDA margin fell from 14.0% (Jan and Feb 2024) to 12.3% (Dec 2024) and then to 10.8% (May 2025). [PERF:MER:2024-01, PERF:MER:2024-02, PERF:MER:2024-12, PERF:MER:2025-05]
- (financial_performance) TTM DSCR declined every month from 1.45x (Jan 2024) to 1.03x (May 2025). Selected readings were 1.33x (Jun 2024), 1.21x (Sep 2024), 1.18x (Oct 2024), 1.10x (Dec 2024) and 1.04x (Apr 2025). [PERF:MER:2024-01, PERF:MER:2024-06, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-12, PERF:MER:2025-04, PERF:MER:2025-05]
- (financial_performance) The leverage ratio rose from 3.2x (Jan 2024) to 4.0x (Nov 2024), 4.1x (Dec 2024) and 4.5x (May 2025). [PERF:MER:2024-01, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-05]
- (financial_performance) The current ratio fell from 1.8 (Jan 2024) to 1.2 (Apr and May 2025). [PERF:MER:2024-01, PERF:MER:2025-04, PERF:MER:2025-05]
- (financial_performance) Revolver utilization was 38% in Jan 2024 and rose to 58% in Aug 2024. It dipped to 52% in Sep 2024. [PERF:MER:2024-01, PERF:MER:2024-08, PERF:MER:2024-09]
- (financial_performance) After Sep 2024, revolver utilization rose every month to 85% in May 2025. [PERF:MER:2024-09, PERF:MER:2025-05]
- (financial_performance) Days past due were 0 in every month from Jan 2024 through May 2025. [PERF:MER:2024-01, PERF:MER:2025-05]
- (financial_performance) The PERF 2024-04 note records automotive sector orders down 8% YoY per a client call. [PERF:MER:2024-04, CRM:2024-04-10:MER]
- (covenant_history) The covenant minimum DSCR is 1.20x and the covenant maximum leverage is 4.0x. Both levels are unchanged in every PERF record from Jan 2024 through May 2025. [PERF:MER:2024-01, PERF:MER:2025-05]
- (covenant_history) Covenant status was reported as Compliant for each month from Jan 2024 through Sep 2024. [PERF:MER:2024-01, PERF:MER:2024-09]
- (covenant_history) For Oct 2024, covenant status was reported as Covenant Watch with TTM DSCR at 1.18x. The note reads: 'DSCR below minimum — RM notified; waiver discussion initiated'. [PERF:MER:2024-10]
- (covenant_history) Covenant status was reported as Covenant Breach for each month from Nov 2024 through May 2025. [PERF:MER:2024-11, PERF:MER:2025-05]
- (covenant_history) TTM DSCR has been below the 1.20x minimum in every month from Oct 2024 (1.18x) through May 2025 (1.03x). [PERF:MER:2024-10, PERF:MER:2025-05]
- (covenant_history) Leverage equalled the 4.0x maximum in Nov 2024. It has exceeded the maximum in every month from Dec 2024 (4.1x) through May 2025 (4.5x). [PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-05]
- (covenant_history) A waiver was granted in November 2024. The CRM log records the conditions as: Q4 package by Jan 31 and updated projections showing a recovery path. [CRM:2024-11-08:MER, PERF:MER:2024-11]
- (covenant_history) The RM's 2025-04-28 email to the CFO states: 'Per the terms of the November waiver, late submission triggers a reporting default.' [EMAIL:T1.6]
- (covenant_history) The Q1 2024 covenant package was recorded as submitted/received on time. [PERF:MER:2024-03, CRM:2024-03-05:MER]
- (covenant_history) The Q2 2024 covenant package was received 12 days late, with no advance notice per the CRM log. [PERF:MER:2024-06, CRM:2024-06-04:MER]
- (covenant_history) The Q3 2024 covenant package was recorded as received on time. The CRM log entry is dated 2024-10-15. [CRM:2024-10-15:MER, PERF:MER:2024-09]
- (covenant_history) The Q4 2024 covenant package had not been received as of 12/31/2024. It was received 1/18/2025, recorded as 18 days late. [PERF:MER:2024-12, PERF:MER:2025-01, EMAIL:T1.1]
- (covenant_history) The Q1 2025 covenant package was due 4/30/2025. It was recorded as overdue as of 5/1/2025, and no response had been received as of 2025-05-12. [PERF:MER:2025-03, EMAIL:T1.6, PERF:MER:2025-05, NOTE:T1.1]
- (covenant_history) The records contain no waiver for covenant periods after the November 2024 waiver. [CRM:2024-11-08:MER, PERF:MER:2025-05]
- (communications) On 2024-01-08, the CRM log records that the CFO described the Q4 pipeline as solid. It also records that the aerospace contract was expected to contribute starting Q1, and that auto OEM orders were soft but within the normal seasonal range. The RM planned to request the Q1 package by end of April. [CRM:2024-01-08:MER]
- (communications) On 2024-02-14, the CRM log records that the CFO said the aerospace contract was still on track and that auto OEM orders were picking up slightly in February. [CRM:2024-02-14:MER]
- (communications) On 2024-04-10, the CFO disclosed that automotive OEM orders were down 8% YoY through March. He stated the aerospace contract would offset this in Q2. [CRM:2024-04-10:MER]
- (communications) On 2024-04-10, the RM asked the CFO for updated projections, and he said he would send them by end of month. In the CRM log the RM wrote: 'Tone was measured but I sense more stress than prior calls.' [CRM:2024-04-10:MER]
- (communications) On 2024-05-14, the RM sent a follow-up email requesting the updated projections. No response was received. [CRM:2024-05-14:MER]
- (communications) On 2024-06-04, the Q2 package cover note from the CFO mentioned continuing automotive softness. The RM's call to the CFO went to voicemail. [CRM:2024-06-04:MER]
- (communications) In the 2024-06-04 CRM log the RM wrote: 'This is a trend I need to watch closely.' [CRM:2024-06-04:MER]
- (communications) On 2024-07-09, the CFO stated that first aerospace revenue was now expected in Q3, not Q2. He framed the 55% revolver utilization as a seasonal working capital need. [CRM:2024-07-09:MER]
- (communications) In the 2024-07-09 CRM log the RM wrote: 'I'm not sure I agree given the pattern.' The RM flagged the account internally to Marcus Chen. [CRM:2024-07-09:MER]
- (communications) At the 2024-09-05 annual review (60-minute video call), management stated that the aerospace contract was producing revenue but on a slower ramp than projected. The CRM log records that Michelle Kwan was confident in the aerospace pipeline. [CRM:2024-09-05:MER]
- (communications) In the 2024-09-05 CRM log the RM wrote: 'I'm less confident.' The RM noted she would request updated projections. [CRM:2024-09-05:MER]
- (communications) On 2024-10-15, after the Q3 package showed DSCR at 1.18x, the RM emailed the CFO. He called back the same day and cited aerospace timing. [CRM:2024-10-15:MER]
- (communications) On 2024-11-08, a waiver call was held with the CFO, with Marcus Chen attending internally. The CFO committed to delivering the Q4 package by Jan 31 and updated projections. [CRM:2024-11-08:MER]
- (communications) In his 2025-01-18 email, the CFO attributed the Q4 package delay to year-end close complications. He stated that the aerospace contract's first delivery milestone was pushed to Q2 2025 and that the contract was about 11 weeks behind. [EMAIL:T1.1]
- (communications) In the same 2025-01-18 email, the CFO stated that the internal projection showed DSCR back above the floor by Q3 2025. He offered to share updated projections on a call. [EMAIL:T1.1]
- (communications) On 2025-01-21, the RM requested the signed management representation letter and the updated A/R aging, which were not in the Q4 package. She asked for them by Wednesday. [EMAIL:T1.2]
- (communications) On 2025-01-22, the CFO stated he would send the rep letter and A/R aging by end of day Wednesday. [EMAIL:T1.3]
- (communications) In the 2025-01-22 email, the CFO stated that the A/R aging would show larger balances in the 60-90 day bucket because two automotive customers went on extended payment terms at year-end. He said 'Nothing we'd call collection risk at this point.' [EMAIL:T1.3]
- (communications) On 2025-01-22, the RM briefed Marcus Chen and Priya Voss. She noted the client said the A/R concentration was seasonal and wrote 'we should verify'. [EMAIL:T1.4]
- (communications) In the 2025-01-22 internal email the RM wrote: 'If projections don't support a Q3 recovery path I think we need to start the modification conversation.' [EMAIL:T1.4]
- (communications) On 2025-01-23, Marcus Chen asked the RM to ask the CFO whether the aerospace contract has a firm PO or is still conditional. He also asked her to obtain customer names for the 60-90 day A/R items. [EMAIL:T1.5]
- (communications) On the 2025-01-23 call, the CFO committed to a Q1 recovery path. Marcus Chen asked about a firm PO on the aerospace contract, and the CFO said he would send it. [CRM:2025-01-23:MER]
- (communications) On 2025-03-14, the CFO stated that Q1 was tracking better than Q4 and that aerospace revenues were coming in. He provided no specific numbers and said the Q1 package would be on time. [CRM:2025-03-14:MER]
- (communications) On 2025-04-28, the RM sent a formal overdue notice on the Q1 2025 package and requested a response by end of day Thursday. No response was received as of 2025-05-12. [EMAIL:T1.6, CRM:2025-04-28:MER, NOTE:T1.1]
- (communications) The 2025-03-14 call is recorded as the last logged two-way contact with the borrower as of May 2025. [CRM:2025-03-14:MER, NOTE:T1.1]
- (open_requests) Updated projections have no record of receipt. They were requested 2024-04-10 and 2024-05-14, intended to be requested 2024-09-05, made a waiver condition 2024-11-08, and offered by the CFO 2025-01-18. [CRM:2024-04-10:MER, CRM:2024-05-14:MER, CRM:2024-09-05:MER, CRM:2024-11-08:MER, EMAIL:T1.1, EMAIL:T1.2]
- (open_requests) The signed management representation letter for Q4 2024 has no record of receipt. It was requested 2025-01-21 and promised by end of day Wednesday 2025-01-22. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) The updated A/R aging has no record of receipt. It was requested 2025-01-21 and promised by end of day Wednesday 2025-01-22. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) A firm PO for the aerospace contract has no record of receipt. It was requested 2025-01-23, and the CRM log states it was not received as of that entry. [CRM:2025-01-23:MER, EMAIL:T1.5]
- (open_requests) The Q1 2025 covenant package was due 4/30/2025 and has no record of receipt. An overdue notice was sent 2025-04-28, and no response had been received as of 2025-05-12. [EMAIL:T1.6, CRM:2025-04-28:MER, PERF:MER:2025-05, NOTE:T1.1]
