# Code / Config Benchmark Results

Status: partial: K10 Claude remains pending due Claude quota; all other K outputs are captured and graded.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points.

## Headline Scores

| Model | Score % | Avg / 2 | Good Answers | Partial Answers | Bad Answers | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 95.0% | 1.90 | 9/10 (90.0%) | 1/10 (10.0%) | 0/10 (0.0%) | 0 |
| ChatGPT | 90.0% | 1.80 | 8/10 (80.0%) | 2/10 (20.0%) | 0/10 (0.0%) | 0 |
| Claude | 72.2% | 1.44 | 5/9 (55.6%) | 3/9 (33.3%) | 1/9 (11.1%) | 1 |
| Gemini | 60.0% | 1.20 | 5/10 (50.0%) | 2/10 (20.0%) | 3/10 (30.0%) | 0 |

## Interpretation

NotebookLM TA is currently leading the code/config stress section, but this should still be treated as a stress test rather than the product claim. The most important result is failure-mode shape: NotebookLM stayed close to MOOS-IvP source patterns, while general tools were more likely to produce fluent but wrong copy-pasteable details for pShare, NODE_MESSAGE payloads, behavior setParam delegation, or ZAIC construction. Claude will receive a final K score after K10 is captured.

## Hard/Notable Error Details

These details are kept for audit, not as a headline scoring column. They may overlap with partial or bad answers.

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| K03 | Gemini | Nonstandard AppCasting API | Used RegisterConfigWarning-style wording rather than the AppCasting warning/reporting pattern and did not fix reconnect registration. |
| K06 | ChatGPT | Wrong pShare destination port model | Told the user to route to the destination MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | Claude | Wrong NODE_MESSAGE fields | Claimed string_val/double_val are not recognized and replaced them with moos_var/moos_string, which is wrong for the documented NODE_MESSAGE payload. |
| K07 | Gemini | Wrong inter-vehicle messaging pattern | Recommended Notify("VISIT_POINT", ...) instead of using NODE_MESSAGE_LOCAL with var_name/string_val for the broker/message-handler path. |
| K08 | ChatGPT | Missing base-class delegation in code | The prose mentioned superclass parsing, but the actual correction returned false for unhandled parameters instead of delegating to IvPBehavior::setParam. |
| K09 | Claude | Wrong behavior lifecycle framing | Placed addInfoVars in an onSetParam/RegisterVariables-style flow and described MOOS app mail delivery rather than the helm InfoBuffer behavior pattern. |
| K09 | Gemini | Off-domain BehaviorTree.CPP answer | Answered with BehaviorTree.CPP ports, blackboard, getInput, and BT::NodeStatus rather than MOOS-IvP addInfoVars/InfoBuffer APIs. |
| K10 | Gemini | Invalid/incomplete ZAIC correction | Kept ZAIC_PEAK zaic("speed") without the IvP domain, omitted setPWT(m_priority_wt), and introduced an unsupported setValueAtSummit method. |

## Prompt-by-Prompt Results

| ID | Prompt Short Name | NotebookLM | ChatGPT | Claude | Gemini | Hard/Notable Details | Notes |
|---|---|---:|---:|---:|---:|---|---|
| K01 | pOdometry Mail Handling | 2 | 2 | 2 | 2 | none | All four answers separated mail/state updates from Iterate-time publication well enough for a pOdometry-style app. |
| K02 | Missing Registration Pattern | 2 | 2 | 2 | 2 | none | All four answers gave a usable reconnect-safe registration pattern, with registration repeated from OnConnectToServer or the local RegisterVariables helper. |
| K03 | AppCasting Config Warnings | 1 | 2 | 1 | 1 | Gemini | ChatGPT gave the cleanest AppCasting/startup pattern. NotebookLM, Claude, and Gemini were partially useful but missed or weakened the reconnect registration point or used nonstandard warning API language. |
| K04 | uTimerScript Trigger Setup | 2 | 2 | 1 | 1 | none | NotebookLM and ChatGPT gave robust timed-post/debugging advice. Claude and Gemini were useful but more generic and included less reliable trigger/config details. |
| K05 | Behavior Config File Boundary | 2 | 2 | 2 | 2 | none | All four correctly identified that behavior blocks belong in the .bhv behavior file, while pHelmIvP is launched/configured from the .moos mission file. |
| K06 | pShare Route Config | 2 | 1 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini gave usable pShare host/port/name guidance. ChatGPT incorrectly framed the destination as the shoreside MOOSDB ServerPort rather than the receiving pShare port. |
| K07 | Inter-Vehicle Message Payload | 2 | 2 | 0 | 0 | Claude, Gemini | NotebookLM and ChatGPT correctly used NODE_MESSAGE_LOCAL with src_node, dest_node, var_name, and quoted string_val. Claude replaced the documented field names with wrong moos_var/moos_string fields. Gemini recommended direct VISIT_POINT publishing rather than the inter-vehicle envelope. |
| K08 | `setParam()` Pattern | 2 | 1 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini preserved base-class setParam delegation. ChatGPT validated the custom parameter but its code returned false instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K09 | `addInfoVars()` / InfoBuffer | 2 | 2 | 1 | 0 | Claude, Gemini | NotebookLM and ChatGPT gave the normal addInfoVars plus getBufferDoubleVal ok-flag pattern. Claude had the right calls but wrong behavior lifecycle framing. Gemini answered as BehaviorTree.CPP, not MOOS-IvP. |
| K10 | ZAIC Speed Function | 2 | 2 | pending | 0 | Gemini | NotebookLM and ChatGPT corrected the normal ZAIC_PEAK pattern with m_domain and setPWT. Gemini omitted the IvP domain and priority weight and invented an unsupported ZAIC method. Claude is still pending due quota. |
