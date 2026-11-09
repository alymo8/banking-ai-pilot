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
As-of date: 2025-01-31

VERIFIED FACT SHEET:
- (business) Meridian Fabrication LLC is an Industrial Manufacturing company headquartered in Ohio with an employee count of 312 and annual revenue of $82mm, per the portfolio profile. [PROFILE:MER]
- (business) The banking relationship dates from 2019. The relationship tier is Core and the RM is Sarah Okonkwo. [PROFILE:MER]
- (business) The primary borrower contact is David Kwan, CFO. [PROFILE:MER, EMAIL:T1.1]
- (business) Michelle Kwan attended the 2024-09-05 annual review alongside David Kwan. Her title and role are not stated in the records. [CRM:2024-09-05:MER]
- (business) Records reference automotive OEM customers and an aerospace contract as segments of the borrower's business. [CRM:2024-01-08:MER, CRM:2024-04-10:MER, EMAIL:T1.1]
- (business) Bank personnel involved: Marcus Chen (Senior Credit Officer) and Priya Voss (copied on the 2025-01-22 internal email). [EMAIL:T1.4, EMAIL:T1.5]
- (facility) The facility is a Term Loan + Revolver totaling $8.5mm, priced at a variable rate of SOFR+275, maturing 2027-03-31. [PROFILE:MER]
- (facility) The loan purpose is equipment expansion and working capital. [PROFILE:MER]
- (facility) Collateral is Machinery & Equipment + A/R. The profile records personal_guarantee=Yes. [PROFILE:MER]
- (facility) The loan balance was $8.3mm in Jan 2024 and $7.8mm in Dec 2024 and Jan 2025. [PERF:MER:2024-01, PERF:MER:2024-12, PERF:MER:2025-01]
- (facility) The profile lists next_covenant_due=2025-06-30 and last_annual_review=2024-09-15. [PROFILE:MER]
- (financial_performance) Monthly revenue was $7,100k (Jan 2024), $7,400k (Mar 2024, the high in the series), $6,850k (Sep 2024), $6,200k (Dec 2024) and $6,000k (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-09, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) Monthly EBITDA was $994k (Jan 2024), $1,010k (Mar 2024), $878k (Sep 2024), $760k (Dec 2024) and $720k (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-09, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) EBITDA margin was 14.0% in Jan and Feb 2024. It was lower in each subsequent month, reaching 12.3% in Dec 2024 and 12.0% in Jan 2025. [PERF:MER:2024-01, PERF:MER:2024-02, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) TTM DSCR was lower in each month of the series. Values: 1.45x (Jan 2024), 1.41x (Mar 2024), 1.33x (Jun 2024), 1.21x (Sep 2024), 1.18x (Oct 2024), 1.14x (Nov 2024), 1.10x (Dec 2024), 1.08x (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-03, PERF:MER:2024-06, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) The leverage ratio was 3.2x (Jan 2024), 3.6x (Jun 2024), 3.8x (Sep 2024), 4.0x (Nov 2024), 4.1x (Dec 2024) and 4.2x (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-06, PERF:MER:2024-09, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) The current ratio was 1.8 (Jan 2024), 1.5 (Sep 2024), 1.4 (Dec 2024) and 1.3 (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-09, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) Revolver utilization was 38% (Jan 2024), 51% (Jun 2024), 55% (Jul 2024), 58% (Aug 2024), 52% (Sep 2024), 60% (Oct 2024), 65% (Nov 2024), 69% (Dec 2024) and 72% (Jan 2025). [PERF:MER:2024-01, PERF:MER:2024-06, PERF:MER:2024-07, PERF:MER:2024-08, PERF:MER:2024-09, PERF:MER:2024-10, PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (financial_performance) Days past due was 0 in every monthly record from Jan 2024 through Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (financial_performance) The PERF note for Apr 2024 records automotive sector orders down 8% YoY per a client call. [PERF:MER:2024-04]
- (covenant_history) The covenant DSCR minimum was 1.20x and the covenant leverage maximum was 4.0x in every monthly record from Jan 2024 through Jan 2025. [PERF:MER:2024-01, PERF:MER:2025-01]
- (covenant_history) Covenant status was Compliant from Jan 2024 through Sep 2024. [PERF:MER:2024-01, PERF:MER:2024-09]
- (covenant_history) Covenant status was Covenant Watch in Oct 2024. The PERF note reads 'DSCR below minimum — RM notified; waiver discussion initiated'. [PERF:MER:2024-10]
- (covenant_history) Covenant status was Covenant Breach in Nov 2024, Dec 2024 and Jan 2025. The Nov 2024 note reads 'Leverage at covenant max; DSCR below min'. [PERF:MER:2024-11, PERF:MER:2024-12, PERF:MER:2025-01]
- (covenant_history) The leverage ratio exceeded the 4.0x maximum at 4.1x (Dec 2024) and 4.2x (Jan 2025). [PERF:MER:2024-12, PERF:MER:2025-01]
- (covenant_history) The Q1 2024 covenant package was recorded as submitted on time. The CRM logged receipt on 2024-03-05 showing DSCR 1.41x and leverage 3.3x, both compliant. [PERF:MER:2024-03, CRM:2024-03-05:MER]
- (covenant_history) The Q2 2024 covenant package was recorded as received 12 days late with no advance notice. The CRM entry is dated 2024-06-04 and shows DSCR 1.33x and leverage 3.6x. [PERF:MER:2024-06, CRM:2024-06-04:MER]
- (covenant_history) The Q3 2024 covenant package was logged on 2024-10-15 as received on time, showing DSCR 1.18x against the 1.20x minimum and leverage 3.9x. The RM log describes this as 'the first formal breach'. [CRM:2024-10-15:MER]
- (covenant_history) A waiver was approved on a 2024-11-08 call with David Kwan and Marcus Chen. Conditions: the Q4 package by Jan 31, and updated projections showing a recovery path. David Kwan committed to both. [CRM:2024-11-08:MER]
- (covenant_history) The PERF record for Nov 2024 notes 'waiver granted 11/22'. [PERF:MER:2024-11]
- (covenant_history) The Q4 2024 covenant package was not received as of 12/31. The PERF record states it was received 1/18 and was 18 days late. [PERF:MER:2024-12, PERF:MER:2025-01, EMAIL:T1.1]
- (covenant_history) The Q4 2024 package showed DSCR 1.10x and leverage 4.1x. The RM logged 'breach confirmed' on 2025-01-23. [CRM:2025-01-23:MER, EMAIL:T1.4]
- (covenant_history) The RM's internal email of 2025-01-22 describes Q4 DSCR as the 'second consecutive quarter in breach'. [EMAIL:T1.4]
- (communications) On 2024-01-08 the CRM log records that David Kwan said the Q4 pipeline looked solid per management and that the aerospace contract was expected to contribute starting Q1. Auto OEM orders were described as soft but within normal seasonal range. No covenant concerns were flagged, and the follow-up was to request the Q1 package by end of April. [CRM:2024-01-08:MER]
- (communications) On 2024-02-14 the CRM log records that David Kwan said the aerospace contract was still on track and auto OEM orders were picking up slightly in February. [CRM:2024-02-14:MER]
- (communications) On 2024-04-10 David Kwan disclosed that automotive OEM orders were down 8% YoY through March, worse than expected, and said the aerospace contract would offset in Q2. The RM asked for updated projections; he said he would send them by end of month. The log notes they were not received. [CRM:2024-04-10:MER]
- (communications) In the CRM log for 2024-04-10 the RM wrote: 'Tone was measured but I sense more stress than prior calls.' [CRM:2024-04-10:MER]
- (communications) On 2024-05-14 the RM sent a follow-up email requesting the updated projections mentioned in the April call. No response was received. [CRM:2024-05-14:MER]
- (communications) On 2024-06-04 David Kwan's cover note to the Q2 package mentioned continuing automotive softness, and the RM logged that aerospace revenues were still not flowing. The RM's call to David went to voicemail. [CRM:2024-06-04:MER]
- (communications) In the CRM log for 2024-06-04 the RM wrote: 'This is a trend I need to watch closely.' [CRM:2024-06-04:MER]
- (communications) On 2024-07-09 David Kwan said the aerospace contract was delayed further, with first revenue now expected in Q3 rather than Q2. He framed revolver utilization of 55% as a seasonal working capital need. The RM flagged the account internally to Marcus Chen. [CRM:2024-07-09:MER]
- (communications) In the CRM log for 2024-07-09 the RM wrote: 'I'm not sure I agree given the pattern.' [CRM:2024-07-09:MER]
- (communications) At the 2024-09-05 annual review (video call, 60 min), David and Michelle Kwan walked through Q3 financials. They stated the aerospace contract was producing revenue with a slower ramp than projected. Michelle Kwan expressed confidence in the aerospace pipeline. The RM noted she would request updated projections. [CRM:2024-09-05:MER]
- (communications) In the CRM log for 2024-09-05 the RM wrote: 'I'm less confident.' She also wrote that revolver utilization at 52% was 'up significantly from last year.' [CRM:2024-09-05:MER]
- (communications) On 2024-10-15 the RM emailed David Kwan about the Q3 DSCR result. He called back the same day and cited aerospace timing; the RM logged him as 'very apologetic'. Waiver discussion was initiated. [CRM:2024-10-15:MER]
- (communications) In his 2025-01-18 email, David Kwan attributed the delay in the Q4 package to year-end close complications. He stated that the aerospace contract's first delivery milestone was pushed to Q2 2025, that the expected Q4 revenue benefit did not occur, and that the contract was tracking about 11 weeks behind. [EMAIL:T1.1]
- (communications) In the same 2025-01-18 email, David Kwan stated that the company's internal projection has it back above the DSCR floor by Q3 2025. He offered to share updated projections on a call. [EMAIL:T1.1]
- (communications) On 2025-01-21 the RM replied that she had logged the package and asked for a call. She requested the signed management representation letter and updated accounts receivable aging, which were not in the package, by Wednesday. [EMAIL:T1.2]
- (communications) On 2025-01-22 David Kwan confirmed a Thursday 11am call and said he would send the rep letter and AR aging by end of day Wednesday. [EMAIL:T1.3]
- (communications) In the same 2025-01-22 email, David Kwan stated the AR aging would show larger balances in the 60-90 day bucket because two automotive customers went on extended payment terms at year-end. He described this as a pattern seen every December but more pronounced this year, and said it was 'Nothing we'd call collection risk at this point.' [EMAIL:T1.3]
- (communications) On 2025-01-22 the RM emailed Marcus Chen and Priya Voss with a summary ahead of the formal credit review. The summary noted the client says the AR concentration is seasonal and 'we should verify'. [EMAIL:T1.4]
- (communications) In the 2025-01-22 internal email the RM wrote: 'If projections don't support a Q3 recovery path I think we need to start the modification conversation.' [EMAIL:T1.4]
- (communications) On 2025-01-23 Marcus Chen asked the RM to ask David directly whether the aerospace contract has a firm PO or is still conditional. He also asked her to get the customer names on the 60-90 day AR items. [EMAIL:T1.5]
- (communications) On the 2025-01-23 call, the RM logged that David Kwan said aerospace revenues are coming in but behind projections, and that he committed to a Q1 recovery path. Marcus Chen asked about a firm PO on the aerospace contract and David said he would send it. [CRM:2025-01-23:MER]
- (open_requests) Updated projections were requested on 2024-04-10 (promised by end of April), on 2024-05-14 by email (no response), and noted as to-be-requested on 2024-09-05. They were also a waiver condition on 2024-11-08 and the RM asked to hear them on the call (2025-01-21). No record shows written projections received. [CRM:2024-04-10:MER, CRM:2024-05-14:MER, CRM:2024-09-05:MER, CRM:2024-11-08:MER, EMAIL:T1.1, EMAIL:T1.2]
- (open_requests) The signed management representation letter was requested on 2025-01-21 and promised by end of day 2025-01-22. No record shows receipt. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) The updated accounts receivable aging was requested on 2025-01-21 and promised by end of day 2025-01-22. No record shows receipt. [EMAIL:T1.2, EMAIL:T1.3]
- (open_requests) The firm PO for the aerospace contract was requested on the 2025-01-23 call. The CRM log records it as not received as of that entry. [CRM:2025-01-23:MER, EMAIL:T1.5]
- (open_requests) Customer names on the 60-90 day AR balances were requested internally by Marcus Chen on 2025-01-23. No record shows they were asked of or received from the borrower. [EMAIL:T1.5]
