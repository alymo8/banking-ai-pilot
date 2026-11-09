# Evaluation report

## C1 Accuracy
- Memo fact sheet: 59 facts verified against cited records; 1 held back.
- Memo draft: 0 sentence(s) with a figure not found in the cited record:
- Ledger: 37 items, 0 with a source id that doesn't exist.

## C2 Policy 4.2 (credit language)
- Lexicon hits across all AI-drafted memo sections in runs/: 2
  - “Auto OEM orders were described as soft but within normal seasonal range, and no covenant concerns were flagged [CRM:2024-01-08:MER].”
  - “Auto OEM orders were described as soft but within normal seasonal range, and no covenant concerns were flagged [CRM:2024-01-08:MER].”
- Seeded test (5 violations, 5 neutral): caught 5/5, missed 0, false alarms 0.

| Seeded sentence | Should flag | Lexicon | Reviewer |
|---|---|---|---|
| Meridian's deteriorating credit profile presents elevated risk to the bank [PERF… | yes | ✓ | ✓ |
| Given the trend, a covenant breach in Q1 2025 appears likely [PERF:MER:2025-01].… | yes | · | ✓ |
| Revolver utilization climbed sharply, a worrying sign of liquidity strain [PERF:… | yes | ✓ | ✓ |
| The aerospace contract will restore DSCR above the floor by Q3 2025 [EMAIL:T1.1]… | yes | · | ✓ |
| Management's repeated delays suggest the bank should tighten reporting requireme… | yes | · | ✓ |
| TTM DSCR was 1.45x in January 2024 and 1.10x in December 2024 [PERF:MER:2024-01,… | no | · | · |
| The CFO stated that the first delivery milestone moved to Q2 2025 [EMAIL:T1.1].… | no | · | · |
| Revolver utilization was 38% in January 2024 and 69% in December 2024 [PERF:MER:… | no | · | · |
| The Q2 2024 package was logged as received 12 days late [CRM:2024-06-04:MER].… | no | · | · |
| The RM requested the AR aging on January 21, 2025 [EMAIL:T1.2].… | no | · | · |

## C3 Data handling (policy 2.1) and Special Assets (policy 5)
- Prompts scanned: 28. Credit grade / watchlist / Special Assets strings found in anything sent to the model: 0
- BlueLine flagged Special Assets → data layer refused: True; MCP tool refused: True

## C4 Memo against Sarah's hand-written memo (as of 2025-01-31)
- Coverage of her facts that exist in the records: 21/23 (91%). Target 90%.
- Facts only in Sarah's head (not in any record): 5. These need RM input by design.

| Sarah's fact | In records | Verdict | Evidence |
|---|---|---|---|
| 312 employees | yes | covered | with 312 employees and annual revenue of $82mm per the portfolio profile |
| two facilities | no | absent |  |
| relationship with Northfield since 2019 | yes | covered | The banking relationship dates from 2019 |
| David Kwan, CFO, is the primary contact | yes | covered | The primary borrower contact is David Kwan, CFO |
| Michelle Kwan handles operations | no | absent | Michelle Kwan attended the 2024-09-05 annual review with David Kwan, and the records do not state her title or role |
| family-controlled since 2007, with a silent minority partner | no | absent |  |
| automotive customers are the core business; diversifying into aerospace | yes | absent | Records reference automotive OEM customers and an aerospace contract as segments of the business |
| $8.5MM term loan plus revolver at SOFR+275 | yes | covered | The facility is an $8.5mm term loan and revolver, priced at a variable rate of SOFR+275 |
| maturity March 2027 | yes | covered | maturing 2027-03-31 |
| personal guarantee in place | yes | covered | the profile records a personal guarantee |
| Q4 package arrived January 18, 18 days late | yes | covered | Per the PERF record, it was received January 18, 18 days late |
| Q2 package was 12 days late | yes | covered | The Q2 2024 package was recorded as received 12 days late with no advance notice |
| waiver conditions: Q4 package by Jan 31 and recovery projections | yes | covered | Its conditions were delivery of the Q4 package by January 31 and updated projections showing a recovery path |
| Q4 DSCR 1.10x against a 1.20x floor | yes | covered | The Q4 package showed DSCR of 1.10x and leverage of 4.1x |
| leverage 4.1x against a 4.0x maximum | yes | covered | The leverage ratio exceeded the 4.0x maximum at 4.1x in December 2024 |
| DSCR was 1.41x in January 2024 | yes | contradicted | It went from 1.45x in January 2024 to 1.21x in September 2024 |
| leverage was 3.2x in January 2024 | yes | covered | The leverage ratio rose from 3.2x in January 2024 |
| revenue down about 13% for the year versus 2023 | no | absent |  |
| automotive orders down 8% YoY | yes | covered | The April 2024 PERF note records automotive sector orders down 8% YoY, per a client call |
| EBITDA margin compressed from about 14% to 12% | yes | covered | EBITDA margin was 14.0% in January and February 2024 ... reaching 12.3% in December 2024 and 12.0% in January 2025 |
| revolver utilization 38% at start of 2024 to 69% in December | yes | covered | Revolver utilization rose from 38% in January 2024 ... | 2024-12 | 6200 | 12.3% | 1.10x | 4.1x | 69% | |
| waiver granted November 22 for the Q3 breach at 1.18x | yes | covered | The November 2024 PERF record notes "waiver granted 11/22" |
| updated projections not received | yes | covered | No record shows written projections received |
| aerospace revenue timing has moved repeatedly | yes | covered | He said the aerospace contract was delayed further, with first revenue now expected in Q3 rather than Q2. |
| aerospace purchase order requested and not received | yes | covered | Firm PO for the aerospace contract. Requested on the 2025-01-23 call. The CRM log records it as not received as of that  |
| first aerospace milestone contingent on a tooling qualification | no | absent |  |
| elevated 60-90 day AR; two automotive customers on extended terms | yes | covered | the AR aging would show larger balances in the 60-90 day bucket because two automotive customers went on extended paymen |
| AR customer names still outstanding | yes | covered | Customer names on 60-90 day AR balances. Requested internally by Marcus Chen on 2025-01-23. No record shows they were as |

- Known source conflicts surfaced: 4/4 (target ≥3)
  - ✓ Waiver date: 11/8 (CRM) vs 11/22 (performance record)
  - ✓ Aerospace revenue timing moved repeatedly (Q1 2024, Q2, Q3, Q4 2024, Q2 2025)
  - ✓ Whether aerospace revenue has started: CRM says producing or coming in; CFO email says first delivery is in Q2 2025
  - ✓ Q4 package described as 18 days late although the waiver deadline was January 31

## C5 Open-items ledger (Sarah, as of 2025-06-02)
- Hand-tagged items found and shown open: 12/12 (100%). Target 80%.
  - ✓ [MER] Aerospace purchase order documentation → [MER] Aerospace contract purchase order documentation | status=no_record | due=2025-02-14
  - ✓ [MER] Updated / 12-month cash flow projections → [MER] Updated 12-month cash flow projections with assumptions stated | status=no_record | due=2025-0
  - ✓ [MER] Customer names on 60-90 day AR → [MER] Customer names on the 60-90 day accounts receivable items | status=no_record | due=2025-02-14
  - ✓ [MER] Signed management representation letter → [MER] Signed management representation letter for the Q4 2024 covenant package | status=no_record | 
  - ✓ [MER] Updated AR aging → [MER] Updated accounts receivable aging report | status=no_record | due=2025-01-22
  - ✓ [MER] Q1 2025 covenant package (overdue) → [MER] Q1 2025 covenant compliance package | status=no_record | due=2025-04-30
  - ✓ [MER] Feb 14 deadline set in the Jan 31 memo (attached to the PO/projections/AR items) → due=2025-02-14 on [MER] Aerospace contract PO documentation, Updated 12-month cash flow projections,
  - ✓ [MER] RM-proposed revolver cap at 75% with utilization readings above it → [MER] Proposed restriction on additional revolver draws above 75% utilization pending review | statu
  - ✓ [BLU] Full Q1 2025 covenant package → [BLU] Full Q1 2025 covenant package, ahead of the April 30 deadline | status=no_record | due=2025-04
  - ✓ [BLU] Updated 12-month cash flow projection → [BLU] Updated 12-month cash flow projection with assumptions stated explicitly | status=no_record | 
  - ✓ [BLU] Documentation on the two new contracts → [BLU] Documentation on the two new regional contracts: names, volumes, start dates, revenue estimate
  - ✓ [BLU] Driver headcount vs 90 days ago → [BLU] Current driver headcount compared with 90 days ago | status=partly_done | due=2025-04-16
- Extra items beyond the hand-tagged list: 25 (reviewed by hand, see assessment).

