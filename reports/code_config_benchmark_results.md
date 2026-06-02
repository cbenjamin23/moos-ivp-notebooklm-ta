# Code / Config Benchmark Results

Run folder: `benchmark_runs/main_benchmark`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; hallucinations and invalid MOOS-IvP-specific syntax are penalized.

## Scores

| Model | Score % | Avg / 2 | Good | Partial | Bad | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 96.7% | 1.93 | 14/15 | 1/15 | 0/15 | 0 |
| ChatGPT 5.5 Thinking | 90.0% | 1.80 | 12/15 | 3/15 | 0/15 | 0 |
| ChatGPT 5.5 Instant | 83.3% | 1.67 | 11/15 | 3/15 | 1/15 | 0 |
| ChatGPT 5.5 Low CLI | 96.7% | 1.93 | 14/15 | 1/15 | 0/15 | 0 |
| Gemini | 66.7% | 1.33 | 8/15 | 4/15 | 3/15 | 0 |
| Claude | 80.0% | 1.60 | 10/15 | 4/15 | 1/15 | 0 |

## Hard/Notable Error Details

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| K03 | Gemini | Nonstandard AppCasting API | Used RegisterConfigWarning-style wording rather than the AppCasting warning/reporting pattern and did not fix reconnect registration. |
| K06 | ChatGPT 5.5 Thinking | Wrong pShare destination port model | Told the user to route to the destination MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | Claude | Wrong NODE_MESSAGE fields | Claimed string_val/double_val are not recognized and replaced them with moos_var/moos_string, which is wrong for the documented NODE_MESSAGE payload. |
| K07 | Gemini | Wrong inter-vehicle messaging pattern | Recommended Notify("VISIT_POINT", ...) instead of using NODE_MESSAGE_LOCAL with var_name/string_val for the broker/message-handler path. |
| K08 | ChatGPT 5.5 Thinking | Missing base-class delegation in code | The prose mentioned superclass parsing, but the actual correction returned false for unhandled parameters instead of delegating to IvPBehavior::setParam. |
| K09 | Claude | Wrong behavior lifecycle framing | Placed addInfoVars in an onSetParam/RegisterVariables-style flow and described MOOS app mail delivery rather than the helm InfoBuffer behavior pattern. |
| K09 | Gemini | Off-domain BehaviorTree.CPP answer | Answered with BehaviorTree.CPP ports, blackboard, getInput, and BT::NodeStatus rather than MOOS-IvP addInfoVars/InfoBuffer APIs. |
| K10 | Gemini | Invalid/incomplete ZAIC correction | Kept ZAIC_PEAK zaic("speed") without the IvP domain, omitted setPWT(m_priority_wt), and introduced an unsupported setValueAtSummit method. |
| K15 | Gemini | Wrong pShare/port mental model | Got the unique vehicle ports and community names right, but suggested routing shoreside pShare output to vehicle MOOSDB ports rather than distinguishing pShare route ports from MOOSDB ServerPort. |
| K06 | ChatGPT 5.5 Instant | Wrong pShare destination port model | Told the user to route to the shoreside MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | ChatGPT 5.5 Instant | Wrong NODE_MESSAGE destination field | Explicitly replaced the documented dest_node field with dests=bravo, which would break the message format. |
| K08 | ChatGPT 5.5 Instant | Missing base-class delegation in code | Validated the custom parameter but returned false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K10 | ChatGPT 5.5 Instant | Invalid/incomplete ZAIC correction | Added shaping and setPWT but kept ZAIC_PEAK zaic("speed") without the IvP domain constructor argument. |
| K09 | ChatGPT 5.5 Low CLI | Wrong behavior lifecycle framing | Put addInfoVars in onHelmStart/onIdleState instead of the normal constructor/config-time behavior pattern. |
| K12 | ChatGPT 5.5 Thinking | Wrong pHelmIvP behavior-file parameter | Included `behavior = targ_alpha.bhv` as a pHelmIvP-style behavior-file example; pHelmIvP parses `Behaviors = ...`, so the answer is useful but copy-paste risky. |
| K06 | Claude | Incomplete NODE_REPORT_LOCAL source correction | Correctly explained host/port matching to the receiving pShare input route, but left the source as `NODE_REPORT` instead of correcting the vehicle-side source to `NODE_REPORT_LOCAL`. |
| K06 | Gemini | Incomplete NODE_REPORT_LOCAL source correction | Correctly targeted the receiving pShare input port, but left `src_name = NODE_REPORT` in the corrected line and only mentioned `NODE_REPORT_LOCAL` as a caveat. |

## Prompt-by-Prompt Results

| ID | Prompt Short Name | NotebookLM TA | ChatGPT 5.5 Thinking | ChatGPT 5.5 Instant | ChatGPT 5.5 Low CLI | Gemini | Claude | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| K01 | pOdometry Mail Handling | 2 | 2 | 2 | 2 | 2 | 2 | All four answers separated mail/state updates from Iterate-time publication well enough for a pOdometry-style app. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K02 | Missing Registration Pattern | 2 | 2 | 2 | 2 | 2 | 2 | All four answers gave a usable reconnect-safe registration pattern, with registration repeated from OnConnectToServer or the local RegisterVariables helper. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K03 | AppCasting Config Warnings | 1 | 2 | 2 | 2 | 1 | 1 | ChatGPT gave the cleanest AppCasting/startup pattern. NotebookLM, Claude, and Gemini were partially useful but missed or weakened the reconnect registration point or used nonstandard warning API language. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K04 | uTimerScript Trigger Setup | 2 | 2 | 2 | 2 | 1 | 1 | NotebookLM and ChatGPT gave robust timed-post/debugging advice. Claude and Gemini were useful but more generic and included less reliable trigger/config details. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K05 | Behavior Config File Boundary | 2 | 2 | 2 | 2 | 2 | 2 | All four correctly identified that behavior blocks belong in the .bhv behavior file, while pHelmIvP is launched/configured from the .moos mission file. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K06 | pShare Route Config | 2 | 1 | 1 | 2 | 1 | 1 | NotebookLM and GPT-5.5 Low CLI gave the cleanest correction: vehicle `NODE_REPORT_LOCAL` to shoreside `NODE_REPORT`, routed to the receiving pShare input port. ChatGPT and GPT-5.5 Instant targeted the MOOSDB ServerPort; Claude and Gemini targeted the pShare port but did not fully correct the vehicle-side source variable. |
| K07 | Inter-Vehicle Message Payload | 2 | 2 | 0 | 2 | 0 | 0 | NotebookLM and ChatGPT correctly used NODE_MESSAGE_LOCAL with src_node, dest_node, var_name, and quoted string_val. Claude replaced the documented field names with wrong moos_var/moos_string fields. Gemini recommended direct VISIT_POINT publishing rather than the inter-vehicle envelope. GPT-5.5 Instant: Bad: the first line repeats the documented dest_node form, but the answer then explicitly says to replace it with dests=bravo, which is not the documented NODE_MESSAGE field. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K08 | `setParam()` Pattern | 2 | 1 | 1 | 2 | 2 | 2 | NotebookLM, Claude, and Gemini preserved base-class setParam delegation. ChatGPT validated the custom parameter but its code returned false instead of delegating to IvPBehavior::setParam for standard behavior parameters. GPT-5.5 Instant: Partial: lowercases and validates the custom parameter, but returns false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K09 | `addInfoVars()` / InfoBuffer | 2 | 2 | 2 | 1 | 0 | 1 | NotebookLM and ChatGPT gave the normal addInfoVars plus getBufferDoubleVal ok-flag pattern. Claude had the right calls but wrong behavior lifecycle framing. Gemini answered as BehaviorTree.CPP, not MOOS-IvP. ChatGPT 5.5 Low CLI: Partial: correctly uses `addInfoVars()` and `getBufferDoubleVal(..., ok)`, but places InfoVar registration in `onHelmStart()`/`onIdleState()` instead of the normal constructor/config-time behavior pattern used throughout the MOOS-IvP behavior source. |
| K10 | ZAIC Speed Function | 2 | 2 | 1 | 2 | 0 | 2 | NotebookLM, ChatGPT, and Claude corrected the normal ZAIC_PEAK pattern with m_domain and setPWT. Gemini omitted the IvP domain and priority weight and invented an unsupported ZAIC method. GPT-5.5 Instant: Partial: adds ZAIC shaping and setPWT, but the corrected code still uses ZAIC_PEAK zaic("speed") instead of ZAIC_PEAK zaic(m_domain, "speed"), so it is not a valid normal MOOS-IvP pattern. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K11 | MOOS Reconnect Registration | 2 | 2 | 2 | 2 | 2 | 2 | All four answers identified that registrations need to be repeated from OnConnectToServer or a shared registerVariables helper called on reconnect. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K12 | Regenerating nsplug Targets | 2 | 1 | 2 | 2 | 2 | 2 | All four answers correctly explained that pAntler reads the generated target file and that nsplug must be rerun after editing meta_ templates or launch arguments. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. ChatGPT 5.5 Thinking strict-pass revision: Partial because the answer includes `behavior = targ_alpha.bhv` as a pHelmIvP-style behavior-file example; source parses `Behaviors = ...`, so this is a copy-paste-risk config line despite good stale-nsplug advice. |
| K13 | Deploy Button Missing Helm Release | 2 | 2 | 2 | 2 | 2 | 2 | All four answers identified the need to post DEPLOY=true and release MOOS_MANUAL_OVERRIDE=false, then check DEPLOY, MOOS_MANUAL_OVERRIDE, helm state, and behavior outputs in uXMS/uHelmScope. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K14 | BHV_Waypoint Update Variable Mismatch | 2 | 2 | 2 | 2 | 2 | 2 | All four answers correctly found the mismatch between Notify("WPT_UPDATE", ...) and updates = WAYPOINT_UPDATES, and explained that the posted variable name must match the behavior updates parameter. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K15 | Two-Vehicle Community/Port Collision | 2 | 2 | 2 | 2 | 1 | 2 | NotebookLM, ChatGPT, and Claude gave the clean unique-community/unique-MOOSDB-port correction. Gemini got that core correction but added a misleading pShare/port mental model, so it was only partial. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
