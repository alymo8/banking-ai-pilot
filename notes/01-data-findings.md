# Northfield Bank: what the data says when you read across files

Sources: P = portfolio_reference.csv, L = loan_performance_monthly.csv, A = rm_activity_log.csv,
E = emails, M = Meridian memo, T = Tom's notes, C = compliance policy, R = personas.

## Meridian Fabrication (Sarah): the memo and the log tell different stories

- **The memo's commitments went nowhere.** M (Jan 31) sets a Feb 14 deadline for the aerospace PO,
  12-month projections and AR customer names, and says to start the watchlist discussion if they miss it.
  A has no entry about Feb 14. The next contact is Mar 14, a brief call with "no specific numbers", and
  it's the last logged contact.
- **Sarah's revolver cap was blown through.** M proposes restricting draws above 75%. L shows Feb 75%,
  Mar 78%, Apr 81%, May 85%.
- **The aerospace timeline moved at least 4 times, not twice.** A: Q1 2024 → Q2 2024 → Q3 2024;
  L: Q4 2024; E: Q2 2025. M says it "moved twice".
- **The sources disagree on whether aerospace revenue has started at all.** A (Sep 2024, Jan 2025,
  Mar 2025) says it is "producing revenue" / "coming in". E (Jan 2025) says the first delivery milestone
  slipped to Q2 2025. M treats it as not started.
- **Small factual errors in a 3–4 hour hand-written memo.** M says Jan 2024 DSCR was 1.41x; L says 1.45x
  (1.41x is March). M dates the waiver 11/22 (L agrees); A logs it approved on the 11/8 call.
- **The overdue notice went out early.** E: dated Apr 28, it calls the package "overdue" but gives the
  due date as Apr 30. P still shows next_covenant_due 2025-06-30.

## BlueLine Logistics (Sarah)

- **A "new disclosure" wasn't new.** Sarah's Apr 16 email to credit calls the 14% driver decline
  "a new disclosure; not previously reported". Her own Nov 12, 2024 site-visit log records 142 vs 165
  drivers and calls it "material". The information sat for 5 months.
- **A leverage breach nobody mentions.** L: Dec 2024 leverage 4.6x against a 4.5x max. Every email
  cites only DSCR.
- **The recovery projection has slipped.** L (Jan): the plan projects 1.25x by Q4 2025. E (Apr): 1.10x
  by Q3, "above floor" by Q4.
- **The dates don't line up.** A (Mar 5) says "new contracts producing revenue", but A (Apr 1) says the
  contracts were *signed* in March.
- **Special Assets risk.** Sarah's Apr 16 email raises moving to Special Assets. **C §5 bans AI on
  Special Assets borrowers**, so any workflow needs a hard stop for this.

## Crestwood Capital (Tom): the best credit is walking away over 35 bps

- **Three signals over 13 months were missed.** A Jan 2024: First Midwest approached him (deposits).
  A Jan 2025: Whitmore "had a meeting with First Midwest", and Tom writes "I did not follow up".
  E Feb 12: a term sheet at 4.90%.
- **Slow responses.** Tom took 14 days to send a vague reply, then missed the Mar 18 call, reconstructed
  from calendar data. Tom's offer of 5.05% came Apr 15. The client's 2-week deadline passed May 13
  with pricing still pending.
- **The records conflict.** L (May) says "no response from RM as of 5/31". A logs a Tom email on 5/12.
- **Tom's notes have their own problems.** Dated Mar 28, they describe the Apr 15 meeting ("when Whitmore
  said 2 weeks"), so the date and the content don't match. They also say a Crestwood memo went to Marcus
  Chen with no edits and "he didn't know I used AI". That breaks **C §5** (presenting AI content as your
  own work), and the IT audit didn't flag it.

## Arcadia Property Group (Tom): the draw ledger doesn't reconcile

- **There's no room in the facility for this draw.** P: facility $22.0M. L: balance $22.0M in Apr and
  May 2025. E: Draw #13 asks for $875K more, and Marcus Chen says "fund the draw". Nobody checks
  availability, which may sit in an interest reserve or budget reallocation, but it's undocumented.
- **The draw count is wrong.** L Jan 2024 says "Draw #3 of 12". Count the funded draws in L
  (Feb 2025 and the Mar balance move included) and this request is #14 or #15, not #13. It's also past
  the 12-draw plan.
- **The schedule story contradicts itself.** E: "end of July… ~90 days behind the original Q3 2025
  target", but July *is* Q3 2025. A (Dec): the new timeline is Q4 2025. L (Apr): "substantially
  complete". E: GC certified 91%.
- **Dates and follow-ups don't match.** A logs Draw #13 on Apr 9, but the submission email is Apr 22.
  Marcus Chen asked for a Liang call "this week", and A has no record of it.
- **This is Tom's own Workflow #1 (the draw letter).** His prompt takes the pasted email and never
  looks at the ledger.

## Summit Retail (Marcus Webb): quiet slide, thin notes

- **Every month of 2025 is below the same month of 2024.** Revenue Jan–May is down 4–12% and margins
  went from 9–10% to 7–8%. TTM DSCR has fallen 5 months straight (1.21 → 1.12, about −0.02/month)
  against a 1.10 minimum. The next package is due Jul 31.
- **The notes lag the data.** Marcus's log quality is mostly "Low" ("Numbers ok", "Looks fine").
  The Mar 2025 RM note in L flags the Location 3 lease risk. His A entry the same month says
  "Numbers look ok".
- **The persona quotes overlap.** Sarah's and Marcus's personas share the same "haven't called Summit
  in three weeks" line, though Summit is Marcus's borrower.

## Compliance traps that are built into the data

- P.credit_grade is an **internal credit rating, a prohibited input under C §2.1**. Retrieval has to
  strip it.
- Emails mention a **watchlist classification** (Marcus Chen, Meridian), also C §2.1. It needs to be
  redacted or excluded.
- Guarantors (the Kwans) are named. Their **personal financials are C §2.1**. A yes/no guarantee flag
  is a loan term and is fine.
- **Special Assets or litigation means AI is prohibited (C §5).** BlueLine may be heading there.
- **Credit language is C §4.2.** Tom's memo prompt has the AI write "Credit overview", "Key risks" and
  "Recommended action". The format itself is the problem, even with his 2–3 sentences in the input.
- **Running anything on a schedule is C §4.1**, which needs CCO approval. Running it on demand over
  RM-assembled data is §3.2/§3.3.
- **Borrower-facing content needs RM review (C §4.3)**. Nothing sends by itself.
