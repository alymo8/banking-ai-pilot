# Northfield Bank: Claude pilot, two working workflows

Built on a synthetic data package for a fictional Northfield Bank (loan performance, RM activity,
emails, a compliance policy, RM personas). Everything here ran on that data. The exact
prompts are in `prompts/`, and every model call's input and output is saved under `runs/`.

| | Solution | Origin | Entry point |
|---|---|---|---|
| 1 | **Relationship review memo pipeline** | Rebuild of Tom's prompt #2 (ChatGPT, flagged by IT audit) | `python -m banking_pilot.memo_pipeline` |
| 2 | **Open-items ledger** (Sarah's Monday setup) | Found in the data: asks and promises that nobody tracks | `python -m banking_pilot.ledger_pipeline` |
| – | **MCP server** (policy-filtered data tools for Claude Desktop / Claude for Work) | Replaces copy-paste into the prompt | `python -m banking_pilot.mcp_server` |
| – | **Evaluation** against the criteria agreed upfront | | `python -m banking_pilot.evaluate` |

Every problem found during the build and how it was fixed: [notes/04-problems-and-fixes.md](notes/04-problems-and-fixes.md).
Cross-file data findings: [notes/01-data-findings.md](notes/01-data-findings.md).

## Setup

```bash
pip install anthropic pydantic mcp
```

Put `ANTHROPIC_API_KEY=...` in `.env` at the repo root (it's git-ignored). The model defaults to
`claude-opus-5-5`. Override it with `BANK_PILOT_MODEL`.

## Run

```bash
python -m banking_pilot.memo_pipeline meridian --as-of 2025-01-31 --rm-notes rm_input/meridian_2025-01-31.md
```

```bash
python -m banking_pilot.memo_pipeline meridian --as-of 2025-05-31
```

```bash
python -m banking_pilot.ledger_pipeline "Sarah Okonkwo" --as-of 2025-06-02 --drafts
```

```bash
python -m banking_pilot.evaluate
```

Each run writes `runs/<timestamp>-<name>/`. For every step it saves `NN_step.prompt.md` (the exact
system and user text sent), the output, and `meta.json` (tokens, seconds), plus the final
deliverable (`memo.md` + `rm_review_sheet.md`, or `open_items.md`).

## MCP server in Claude Desktop

Add this to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "northfield-bank": {
      "command": "python",
      "args": ["-m", "banking_pilot.mcp_server"],
      "env": { "PYTHONPATH": "<repo-root>" }
    }
  }
}
```

Tools: `list_borrowers`, `get_borrower_profile`, `get_monthly_performance`, `get_activity_log`,
`get_email_threads`, `get_prior_memo`. The policy filters run inside the server, so no prompt can
get around them.

Claude Desktop from the Microsoft Store reads its config from
`%LOCALAPPDATA%\Claude-Data\claude_<id>\claude_desktop_config.json`, not `%APPDATA%\Claude`.
Fully quit the app (tray icon → Quit) after editing it.

Check the server without Desktop (stdio, all tools, Special Assets refusal):

```bash
python scripts/mcp_smoke.py
```

Leading questions over the chat route, before vs after the limits rule (see
`notes/03-mcp-chat-finding.md`; about 5 min, 36 conversations):

```bash
python scripts/chat_route_eval.py --reps 3
```

## Layout

```
banking_pilot/data.py          one data layer; policy 2.1 redaction + policy 5 refusal live here
banking_pilot/llm.py           Claude client; logs every prompt/output to runs/
banking_pilot/memo_pipeline.py solution 1
banking_pilot/ledger_pipeline.py solution 2
banking_pilot/mcp_server.py    MCP tools over the same data layer
banking_pilot/evaluate.py      criteria C1–C5
scripts/mcp_smoke.py        MCP server check over stdio
scripts/chat_route_eval.py  chat route: leading questions, before vs after the limits rule
prompts/                    exact prompt text, one file per step (for compliance review, policy 7)
rm_input/                   RM-authored notes (the only source of credit judgment)
config/restricted_borrowers.json   Special Assets / litigation flags (prod: from core system)
data/                       synthetic CSVs; data/text/ = documents (emails, policy, memo, personas)
runs/                       real outputs
```

*Northfield Bank, its people, borrowers and data are fictional.*
