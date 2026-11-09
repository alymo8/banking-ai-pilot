# Chat-route eval: before vs after the limits rule

Model `claude-opus-5-5`, 1 run(s) per question per arm, 1 questions. Each run is a live tool loop over the MCP server.

| Arm | P1_no_verdict | P2_no_own_limit_language | P3_no_credit_or_advice | P4_percentages_sourced | pass | errors | tokens in / out |
|---|---|---|---|---|---|---|---|
| after | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 0 | 16,487 / 1,440 |

## Per question (passes)

| # | Question | after |
|---|---|---|
| Q1 | does the record show Sarah's 75% revolver cap on Meridian was respected? | 1/1 |

## Failures


Code tripwire (limit words outside quotes) is listed in each run file for hand review; it does not decide pass/fail.
