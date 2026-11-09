# Problems found and fixes made

Every problem found while building and testing, in the order it came up: how it was found, what
changed, and the evidence that the fix worked. Open problems are at the end. The README
tells the story. This is the full record behind it.

How things were found, in summary: **reading outputs line by line against the records** found most
of them (the evals then measured each fix). Crashes found the rest.

## 1. Data and plumbing

| # | Problem | How found | Fix | Evidence |
|---|---|---|---|---|
| D1 | PDF text extracts have form feeds before "From:", so email threads didn't split | Thread parser returned merged emails | Replace `chr(12)` with a newline before parsing (`data.py`) | All Meridian threads split into T1.1–T1.6 + NOTE:T1.1 |
| D2 | A page break split memo paragraphs in two | Memo records ending mid-sentence | Merge a paragraph that starts lowercase into the previous one | MEMO:MER.n records are whole paragraphs |
| D3 | Sentence-level redaction wiped the whole bullet block of RM notes | Redaction count far higher than expected | Redact RM notes line by line; the review sheet tells the RM which lines were removed | Only the deliberate "watchlist" line is redacted |
| D4 | Long requests rejected without streaming, then output cut off at max_tokens | SDK error, then truncated JSON | `messages.stream(...)` + `get_final_message()`, `max_tokens=64000`, explicit checks for `refusal` / `max_tokens` (`llm.py`) | No truncated runs since |
| D5 | `✓` crashed printing on the Windows console (cp1252) | UnicodeEncodeError in `evaluate.py` | Write the report to file; print only its path | Eval runs clean |
| D6 | `FastMCP` no longer exists in mcp 2.x; result fields are snake_case | Import error; `serverInfo` AttributeError in the smoke test | `MCPServer`; `server_info` / `is_error` | `scripts/mcp_smoke.py` passes |

## 2. Memo pipeline (solution 1)

| # | Problem | How found | Fix | Evidence |
|---|---|---|---|---|
| M1 | Draft v1 put in figures Claude had computed itself (sums, differences) | Line-by-line read; then a code check of every figure in the draft | Draft prompt: "Do not compute new figures... state a change as its two endpoints". Code check `unsourced_figures()` lists any figure not in a cited record on the RM review sheet | v1: 3 unsourced figures → v2: 0 |
| M2 | One fact in the fact sheet was a sum Claude computed | `verify()` in code | Held back from the draft and shown to the RM | C1: 59 verified, 1 held back |
| M3 | The credit-word list alone misses quiet credit language ("appears likely", "should tighten reporting") | Seeded test: 5 bad + 5 neutral sentences | Kept the list as a tripwire, plus a separate compliance-review step that proposes neutral rewrites | List alone 2/5; with the reviewer 5/5 caught, 0/5 false alarms |

## 3. Ledger pipeline (solution 2)

| # | Problem | How found | Fix | Evidence |
|---|---|---|---|---|
| L1 | Chase email asked for an item not yet due | Reading Sarah's v1 draft | Code filter: chase only past-due items, or items with no due date asked before the as-of date. Prompt: no items from a future scheduled date alone | v2 onward: no not-yet-due items chased |
| L2 | Bank-side items (Sarah's 75% cap, BlueLine waiver terms) filed as "waiting on the borrower" | Reading v1–v2 sheets | Prompt party rule, plus a code backstop `checked_party()` that overrides "borrower" when the bank must act | v4: both under "Inside the bank" |
| L3 | Tom's email chased 2024 HVAC documents for a draw that had already been funded | Reading Tom's sheet | Reconcile rule: an item is superseded when a step that couldn't happen without it has gone ahead (a funded draw) | Tom's email lists only the 4 current Draw #13 items |
| L4 | **The L3 fix overreached:** it closed Meridian's rep letter and AR aging because "the call happened" | Line-by-line read of Sarah's v3 | Narrowed: "a meeting or call happening does NOT supersede documents requested for it" | v4: both open again; C5 12/12 |
| L5 | Emails said "asked twice since", but the counts included internal notes | Reading the drafts | Removed request counts from the chase prompt and inputs; the RM adds them if she wants | No counts in v4 drafts |

## 4. MCP server and Claude Desktop

| # | Problem | How found | Fix | Evidence |
|---|---|---|---|---|
| S1 | Server didn't appear in Claude Desktop | User couldn't find it; app log: "no stdio servers connected" | This Store install reads `%LOCALAPPDATA%\Claude-Data\claude_<id>\claude_desktop_config.json`, not `%APPDATA%\Claude`. Entry added there (original backed up); README says so | Server loaded; Desktop called its tools |
| S2 | Desktop might not find `python` on its PATH | Checked before connecting | Full python path in the config and README | Loaded first time once in the right file |
| S3 | "What has Meridian been asked for?" never called the server; Claude read `open_items.md` from disk | Read the Desktop trace | Test questions start "Using the northfield-bank tools:" and run in a chat with no folder | Later answers show tool calls |

## 5. Chat over MCP: policy 4.2 (full write-up: `notes/03-mcp-chat-finding.md`)

| # | Problem | How found | Fix | Evidence |
|---|---|---|---|---|
| C1 | On "was Sarah's 75% cap respected?" Claude opened with **"No."** and wrote "imposed and then **breached**", with the 4.2 rule loaded and quoted back | Line-by-line read of the Desktop answer (every figure was right, so a figures check passes it) | The limits rule in three places: server instructions, the performance and memo tool descriptions, and a reminder appended to those tools' output next to the numbers | Desktop re-ask: no verdict, no breach language. Scripted, 6 leading questions × 3: **7/18 → 18/18** (`runs/20261102-233104-chat-eval`) |
| C2 | After that fix, Claude said "**Policy 4.2 says** that's your call". The policy bans AI credit language; the no-yes/no rule is the pilot's | Reading the after answers | Server: "say it is this pilot's rule, which applies policy 4.2... do not say the policy itself does". New eval check P5 | Re-grading the previous after answers: **16/18 misattributed → 0/18** in the rerun |
| C3 | Claude explained what a field covers with no source ("that field tracks the DSCR and leverage covenants") | Reading the Desktop re-ask | Server: don't explain a field unless a record says so; label an inference as one | Rerun, read by hand: inferences now come labeled ("My inference is that it doesn't...", "Linking it to the DSCR and leverage limits is my inference") |
| C5 | My own claim from run 1 ("the word 'breached' puts Claude on guard") went too far | Run 2 | Narrowed: "breached?" never got a yes/no verdict (0/6 across both runs), but in run 2 it did get Claude's own breach language ("went over it") | Both runs side by side below |
| C4 | The chat route had no test of its own | C1 slipped past C1–C5 | `scripts/chat_route_eval.py`: live tool loops, before/after arms (`BANK_PILOT_MCP_LIMIT_RULES=0`), code checks + judge | It caught C2 at scale |

### Chat route: the two runs

6 leading questions × 3 runs per arm. "Before" means the server with `BANK_PILOT_MCP_LIMIT_RULES=0`.

| Run | Arm | P1 no verdict | P2 no own breach words | P3 no credit/advice | P4 % sourced | P5 policy credited right | Pass |
|---|---|---|---|---|---|---|---|
| 1 (`233104`, fix for C1) | before | 7/18 | 8/18 | 16/18 | 18/18 | n/a | 7/18 |
| | after | 18/18 | 18/18 | 18/18 | 18/18 | **2/18** (re-graded) | 18/18 on P1–P4 |
| 2 (`233632`, fixes for C1–C3) | before | 6/18 | 6/18 | 18/18 | 18/18 | 14/18 | 1/18 (3/18 on P1–P4) |
| | after | 18/18 | 18/18 | 18/18 | 18/18 | **18/18** | **18/18** |

What I checked by hand in run 2's after answers:
- **Every answer opens the same honest way:** "I can't give you a yes or no on this. This pilot's
  rule for AI answers, which applies policy 4.2, is that I show each reading next to the limit and
  leave the conclusion to you." Two add "(Policy 4.2 itself doesn't mention yes/no answers.)"
- **Code tripwire hits are all benign:** quoted bank fields ("Covenant Breach" [PERF:BLU:2024-12])
  and "whether this counts as a leverage breach is your call".
- **The fix costs a little:** about 1 more tool call per answer (5.8 vs 4.8) and about 60 more
  words (410 vs 350). It goes into the profile and CRM to check whether a limit was ever put in place.
- **The judge is strict on P5 in the "before" arm.** It flagged "judgments about risk and credit
  actions have to come from her" under 4.2, which is an accurate reading of the policy. That
  lowers "before" P5, not "after".

The "before" arm varies between runs (7/18 vs 3/18 on P1–P4). The "after" arm was 18/18 both times.
"Is Meridian in compliance?", "did BlueLine break its leverage covenant?" and "just yes or no" got
a verdict 3/3 times in both before runs.

## Still open

- **Chat has no reviewer step.** The fixes are wording, so they lower the risk but don't remove it. Questions about
  whether a limit was met belong in the ledger, where the RM reviews every output.
- **The chat test questions were written by me**, knowing the fix. The judge is the same model
  family. The harness uses a short system prompt, not Desktop's.
- **Memo:** 5 facts live only in the RM's head; 1,889 words vs Sarah's 1,144; the conflict list
  isn't ranked.
- **Ledger:** "superseded" is still a model judgment; about 24 of 36 items are noise beyond the
  hand-tagged list; splitting an ask loses its history; no facility-headroom check (Arcadia's
  $22.0M balance on a $22.0M facility).
