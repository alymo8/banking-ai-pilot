# Northfield Bank Claude pilot: design spec

Date: 2026-11-02 · Status: built (code in `banking_pilot/`, prompts in `prompts/`,
outputs in `runs/`)

## 1. Problem

Three relationship managers (RMs), Sarah Okonkwo, Tom DeLuca and Marcus Webb, run a combined $350M
commercial portfolio. They spend 30–40% of their time on documentation, covenant tracking and call
preparation. Tom has already built AI workflows in a personal ChatGPT account, which breaks bank
policy. The bank has Claude for Work licenses and nothing deployed.

The pilot must deliver Claude workflows that RMs will use, that stay inside the bank's AI policy
(v1.2), and whose output is good enough for a credit file.

## 2. Goals

1. **G1:** Rebuild one of Tom's shadow workflows so it is compliant and deployable, and show what
   changed and why.
2. **G2:** Build one workflow found by reading the data, not named by Tom and not the obvious pain
   point.
3. **G3:** Design the policy constraints into the system (data layer, workflow structure, review
   steps), not as disclaimers.
4. **G4:** Evaluate the outputs honestly against criteria agreed before building.

## 3. Decisions

| # | Decision | Options considered | Chosen | Why |
|---|---|---|---|---|
| D1 | Which Tom workflow to rebuild | Relationship review memo as steps; draw response letter with a draw-ledger check first | **Relationship review memo** | Highest time cost (3–4 hours per memo), and the format itself breaks §4.2 ("Key risks", "Recommended action"), so it shows the most about designing around the policy. The draw-ledger check (Arcadia's facility is fully drawn) is kept as a next step |
| D2 | Second workflow | Open-items ledger; Marcus post-call debrief (2-minute dictation into a structured CRM note) | **Open-items ledger** | Asks and promises are spread across email, CRM, memos and a legal pad, and nothing records whether they were answered. It's on every borrower and labeled nowhere. It serves Sarah's stated win (Monday setup in 10 minutes, not 45) |
| D3 | Architecture | MCP server + scripted API pipeline; MCP server in Claude Desktop only; Claude.ai Projects with uploaded files | **Local MCP server + scripted Anthropic API pipelines** over one shared data layer | Retrieval is deterministic, so it's code. Each model step has one job and its output is checked before the next. MCP gives RMs the same policy-filtered data in Claude for Work without pasting |
| D4 | Where policy is enforced | Prompt instructions; data layer; review steps | **All three, strongest first:** data layer (§2.1, §5), workflow structure (§4.2, §4.3), prompt rules and reviewers | A prompt is not a control. What must never reach the model is removed in code |
| D5 | Who writes credit judgment | AI drafts, RM edits; RM writes, AI polishes | **RM writes; AI polishes and claim-maps.** No notes means `[RM TO WRITE]` | §4.2 bans AI credit language. Editing an AI draft still makes the AI its author |
| D6 | Ledger run mode | Scheduled; on demand | **On demand, by the RM, over their own book** | Scheduling it makes it automated monitoring (§4.1), which needs CCO approval |
| D7 | Ledger scoring | Rank borrowers / contact frequency; due date only | **Due date only.** No ranking, no contact-frequency metric, no management view | RMs said they don't want their contact frequency flagged. An early-warning score is a credit characterization |
| D8 | Model | – | `claude-opus-5-5`, structured outputs, streaming | Most capable model; structured output for steps code must check |

## 4. Users

| User | Need | What the pilot gives them |
|---|---|---|
| Sarah (teacher, heavy documenter) | Monday setup in 10 minutes; stop rewriting the risk section | Ledger; memo review sheet with verified facts and conflicts |
| Tom (early adopter, policy breach) | His workflows, legally; email search by borrower; templates; a flag on what he's dropped | His memo structure and email prompt kept; MCP tools; `prompts/`; the ledger |
| Marcus (22 years, skeptical) | Keep his voice and judgment; no surveillance | RM notes stay his; nothing tracks contact frequency |

## 5. Architecture

```
data/ (CSV, PDF text)
   │
banking_pilot/data.py ── one data layer, policy enforced here
   │   • drops credit_grade (§2.1)
   │   • redacts watchlist / special assets / risk-rating sentences, RM notes line by line (§2.1)
   │   • refuses Special Assets / litigation borrowers (§5), config/restricted_borrowers.json
   │   • every record has a source id: PROFILE:MER, PERF:MER:2025-01, CRM:<date>:MER, EMAIL:T1.3, MEMO:MER.n
   ├── banking_pilot/memo_pipeline.py    (G1)
   ├── banking_pilot/ledger_pipeline.py  (G2)
   └── banking_pilot/mcp_server.py       (Claude Desktop / Claude for Work, stdio)
banking_pilot/llm.py ── one model call per step; logs every prompt and output to runs/ (§7)
```

### 5.1 Memo pipeline

| # | Step | Who | Contract |
|---|---|---|---|
| 1 | Retrieve records as of a date | code | Policy-filtered; `--as-of` lets the memo be rebuilt from the records available on that day |
| 2 | Fact sheet, conflicts, gaps | Claude (`prompts/memo_1_facts.md`) | Every fact cites source ids |
| 3 | Verify | code | Ids must exist; each figure must appear in a cited record; anything else is held back and shown to the RM |
| 4 | Draft factual sections | Claude (`memo_2_draft.md`) | Verified facts only; no computed figures; never sees RM notes |
| 5 | Polish RM notes | Claude (`memo_3_rm_polish.md`) | Claim map back to each note line; asks questions instead of filling gaps |
| 6 | Compliance check | code + Claude (`memo_4_compliance.md`) | Lexicon tripwire + reviewer over AI-authored text only + neutral rewrites + draft figure check |
| 7 | Assemble | code | `memo.md` with AI disclosure (§5); `rm_review_sheet.md`; summary table rendered by code |

A single prompt stays the right call for a short borrower email where the RM supplies every input
and reads every word. Tom's email prompt is kept as one call.

### 5.2 Ledger pipeline

| # | Step | Who | Contract |
|---|---|---|---|
| 1 | Retrieve one RM's borrowers | code | Special Assets refused |
| 2 | Extract asks and commitments | Claude (`ledger_1_extract.md`) | Merged across sources, cited; party = borrower / rm / bank_internal |
| 3 | Reconcile each item | Claude (`ledger_2_reconcile.md`) | done / partly_done / no_record / superseded, with evidence ids. "No record" means not logged |
| 4 | Compute | code | Days open, times mentioned, days past due; `checked_party()` backstop |
| 5 | Render | code | Grouped by party, sorted by days past due |
| 6 | Optional follow-up drafts | Claude (`ledger_3_chase.md`) | Only late items, or items asked with no due date; no consequence language unless the RM adds it; nothing sent (§4.3) |

### 5.3 MCP server

Read-only tools: `list_borrowers`, `get_borrower_profile`, `get_monthly_performance`,
`get_activity_log`, `get_email_threads`, `get_prior_memo`. Same data layer, so the same filters.
Server instructions require source ids and forbid credit language. For questions about whether a
limit was met, the server gives readings next to limits with no yes/no verdict, credits that rule
to the pilot (applying §4.2), and has Claude label any inference. The rule also sits in the tool
descriptions and in the output of the performance and memo tools.

## 6. Policy mapping

| Policy | Requirement | Control |
|---|---|---|
| §1, §6 | Approved tools only | Claude for Work / API; no personal accounts; data through the data layer, not paste |
| §2.1 | No credit grades or watchlist data to the model | Dropped and redacted in `data.py`; leak scan of every saved prompt |
| §3.2, §3.3 | Permitted: synthesizing internal documents, follow-up actions | Both workflows sit here |
| §4.1 | Automated monitoring needs CCO approval | Ledger is on demand only |
| §4.2 | No AI credit language | Structure (RM writes judgment), prompt rules, lexicon + reviewer, chat-route rules |
| §4.3 | RM reviews anything borrower-facing | Drafts only; review sheet; nothing sent |
| §5 | No AI on Special Assets borrowers; disclose AI content | Refusal before any model call; disclosure header |
| §7 | Document prompts and workflows | `prompts/` and per-step logs in `runs/` |

## 7. Acceptance criteria

Agreed before building. `python -m banking_pilot.evaluate` reports C1–C5;
`python scripts/chat_route_eval.py` reports C2-chat.

| # | Criterion | Pass bar |
|---|---|---|
| C1 | Grounding: every fact cites a real record and figures match | 0 unknown source ids; every figure in the draft is in a cited record or listed for the RM |
| C2 | No AI credit language | 0 reviewer flags on real drafts; seeded test of 5 violating + 5 neutral sentences catches all 5 with no false alarms |
| C3 | §2.1 and §5 | 0 credit grade / watchlist / Special Assets strings in any saved prompt; a Special Assets borrower is refused by pipeline and MCP |
| C4 | Memo quality vs Sarah's Jan 31 memo, rebuilt as of the same day | Covers ≥ 90% of her facts that exist in the records; surfaces the 4 known conflicts |
| C5 | Ledger recall | Finds and shows open all 12 hand-tagged Meridian + BlueLine items |
| C2-chat | Chat over MCP gives no limit verdicts | Leading questions × repeated runs: no yes/no verdict, no breach language of its own, no credit characterization, percentages sourced, rule credited to the pilot |

## 8. Out of scope

- Live connections to core systems (nCino, Outlook). The pilot runs on the package data. §1 lists
  core-system integrations as pending evaluation.
- Scheduled runs or alerts of any kind (§4.1).
- Borrower ranking, risk scoring, contact-frequency metrics or a management view.
- Sending anything to a borrower.
- Any processing of Special Assets or litigation borrowers.
- Authentication, multi-user hosting and persistence of RM dismissals.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Model writes credit language anyway | Structure first; reviewer over AI text; seeded and chat-route tests |
| A closure rule in reconcile overreaches | Every superseded item cites its evidence; C5 rerun after every prompt change |
| RM context that isn't in any system | `[RM TO WRITE]` slots; questions to the RM; prior memo as RM-authored context in production |
| Same-model judge | Hand checks of judged results; second human grader before rollout |
| Logging gaps read as "didn't happen" | "No record" wording, stated at the top of every sheet |
