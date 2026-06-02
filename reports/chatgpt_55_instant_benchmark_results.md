# ChatGPT 5.5 Instant Benchmark Addendum

Status: complete for C01-C30, D01-D15, and K01-K15 as a separate model from the original ChatGPT Thinking row.

Run folder: `benchmark_runs/main_benchmark`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; hallucinations and invalid MOOS-IvP-specific syntax are penalized.

## Headline Scores

| Category | Prompt Count | Score % | Avg / 2 | Good | Partial | Bad |
|---|---:|---:|---:|---:|---:|---:|
| Overall | 60 | 91.7% | 1.83 | 52/60 (86.7%) | 6/60 (10.0%) | 2/60 (3.3%) |
| Conceptual/debugging | 30 | 95.0% | 1.90 | 27/30 (90.0%) | 3/30 (10.0%) | 0/30 (0.0%) |
| Exact docs/parameters/tools | 15 | 93.3% | 1.87 | 14/15 (93.3%) | 0/15 (0.0%) | 1/15 (6.7%) |
| Code/config advice | 15 | 83.3% | 1.67 | 11/15 (73.3%) | 3/15 (20.0%) | 1/15 (6.7%) |

## Interpretation

GPT-5.5 Instant was strong overall but below the original ChatGPT Thinking run after the hallucination-focused sweep. The biggest losses were concrete MOOS-IvP details: pShare route ports, NODE_MESSAGE field names/process ownership, BHV_OpRegionV24 semantics, base behavior parameter delegation, and ZAIC domain construction.

## Hard/Notable Error Details

| Prompt ID | Failure Type | Brief Explanation |
|---|---|---|
| C11 | Wrong pShare destination port model | Said vehicle reports should be sent to the shoreside MOOSDB port; pShare output should target the receiving pShare route/input port. |
| C12 | Wrong pShare destination port model | Described pShare as sending directly to the remote MOOSDB at host:port rather than to the receiving pShare route/input port. |
| C16 | Wrong NODE_MESSAGE handling process | Described pNodeReporter as converting/unwrapping NODE_MESSAGE_LOCAL/NODE_MESSAGE; the lab/source path uses uFldNodeBroker/uFldMessageHandler style handling. |
| D06 | Wrong behavior semantics | Described BHV_OpRegionV24 as only a safety/constraint monitor and denied the V24 recovery/steering behavior. |
| K06 | Wrong pShare destination port model | Told the user to route to the shoreside MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | Wrong NODE_MESSAGE destination field | Explicitly replaced the documented dest_node field with dests=bravo, which would break the message format. |
| K08 | Missing base-class delegation in code | Validated the custom parameter but returned false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K10 | Invalid/incomplete ZAIC correction | Added shaping and setPWT but kept ZAIC_PEAK zaic("speed") without the IvP domain constructor argument. |

## Prompt-by-Prompt Results

| ID | Category | Prompt Short Name | Score | Notes |
|---|---|---|---:|---|
| C01 | conceptual_debugging | Command Not Found After Build | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C02 | conceptual_debugging | Version Control Before Mission Changes | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C03 | conceptual_debugging | uXMS/uPokeDB Confusion | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C04 | conceptual_debugging | App Not Publishing | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C05 | conceptual_debugging | pAntler Did Not Start A Process | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C06 | conceptual_debugging | Launch Arguments Not Reaching Config Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C07 | conceptual_debugging | Helm Remains PARKED | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C08 | conceptual_debugging | No Desired Outputs | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C09 | conceptual_debugging | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C10 | conceptual_debugging | Multi-Vehicle Ports | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C11 | conceptual_debugging | Shoreside Missing Vehicle | 1 | Partial: useful NODE_REPORT/pNodeReporter debugging path, but includes the wrong pShare-port mental model by saying vehicle reports should be sent to the shoreside MOOSDB port. |
| C12 | conceptual_debugging | pShare Route Confusion | 1 | Partial: good local-vs-shared variable framing, but incorrectly describes a pShare route as sending directly to the remote MOOSDB rather than to the receiving pShare route/input port. |
| C13 | conceptual_debugging | TSP App / Behavior Boundary | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C14 | conceptual_debugging | Distributed Route Assignment Problem | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C15 | conceptual_debugging | Multi-Machine Networking Problem | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C16 | conceptual_debugging | Message Does Not Arrive | 1 | Partial: useful NODE_MESSAGE_LOCAL / NODE_MESSAGE / dest_node / var_name debugging path, but wrongly assigns conversion/unwrapping to pNodeReporter rather than the uField broker/message-handler path. |
| C17 | conceptual_debugging | Node Names / Destinations | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C18 | conceptual_debugging | Behavior Never Runs | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C19 | conceptual_debugging | `.moos` vs `.bhv` Mistake | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C20 | conceptual_debugging | Payload Event Not Affecting Autonomy | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C21 | conceptual_debugging | Simulation to Heron/PABLO | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C22 | conceptual_debugging | Field Deployment Sanity Check | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C23 | conceptual_debugging | Rescue Path Planning | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C24 | conceptual_debugging | Adversarial Rescue Updates | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C25 | conceptual_debugging | Teammate Messaging | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C26 | conceptual_debugging | Post-Mission Alog Diagnosis | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C27 | conceptual_debugging | pLogger Produced No Useful Alog | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C28 | conceptual_debugging | Choosing Debugging Tools During A Mission Run | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C29 | conceptual_debugging | pMarineViewer Background / Geodesy | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| C30 | conceptual_debugging | Mission Broke After Several Edits | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D01 | exact_docs_tools | pOdometry Variables | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D02 | exact_docs_tools | pAntler Process Launching | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D03 | exact_docs_tools | uTimerScript Usage | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D04 | exact_docs_tools | Helm Deploy Variables | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D05 | exact_docs_tools | BHV_Waypoint Params | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D06 | exact_docs_tools | BHV_OpRegionV24 Semantics | 0 | Bad: repeats the legacy/wrong mental model that BHV_OpRegionV24 is only a safety monitor and denies the documented V24 recovery/steering behavior. |
| D07 | exact_docs_tools | Viewer Image / Geodesy Config | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D08 | exact_docs_tools | pShare Configuration | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D09 | exact_docs_tools | uField Broker Comparison | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D10 | exact_docs_tools | pLogger And Alog Verification | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D11 | exact_docs_tools | Generated Mission Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D12 | exact_docs_tools | pMarineViewer Action Buttons | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D13 | exact_docs_tools | uXMS, uQueryDB, and uPokeDB | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D14 | exact_docs_tools | pNodeReporter and NODE_REPORT | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| D15 | exact_docs_tools | Loiter and Station-Keep Behaviors | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K01 | code_config_advice | pOdometry Mail Handling | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K02 | code_config_advice | Missing Registration Pattern | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K03 | code_config_advice | AppCasting Config Warnings | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K04 | code_config_advice | uTimerScript Trigger Setup | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K05 | code_config_advice | Behavior Config File Boundary | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K06 | code_config_advice | pShare Route Config | 1 | Partial: correctly identifies localhost/source-variable/name issues, but incorrectly says the route should target the shoreside MOOSDB ServerPort rather than the receiving pShare route/input port. |
| K07 | code_config_advice | Inter-Vehicle Message Payload | 0 | Bad: the first line repeats the documented dest_node form, but the answer then explicitly says to replace it with dests=bravo, which is not the documented NODE_MESSAGE field. |
| K08 | code_config_advice | `setParam()` Pattern | 1 | Partial: lowercases and validates the custom parameter, but returns false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K09 | code_config_advice | `addInfoVars()` / InfoBuffer | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K10 | code_config_advice | ZAIC Speed Function | 1 | Partial: adds ZAIC shaping and setPWT, but the corrected code still uses ZAIC_PEAK zaic("speed") instead of ZAIC_PEAK zaic(m_domain, "speed"), so it is not a valid normal MOOS-IvP pattern. |
| K11 | code_config_advice | Reconnect-Safe Registration | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K12 | code_config_advice | Editing Templates But Launching Stale Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K13 | code_config_advice | pMarineViewer Button Posts | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K14 | code_config_advice | Behavior Updates Not Taking Effect | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
| K15 | code_config_advice | Duplicate Ports and Community Names | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-focused grading pass. |
