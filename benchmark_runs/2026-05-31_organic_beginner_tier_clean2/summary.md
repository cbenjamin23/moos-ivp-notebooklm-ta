# Organic Beginner-Tier Benchmark Run

Run ID: 2026-05-31_organic_beginner_tier_clean2

Status: stopped at partial K09 - Claude quota notice before Gemini

Last updated: 2026-06-01T14:20:36Z

Mode: same prompt text only; normal browser UI/default platform behavior; clean prompt context where practical.

Counts: {"captured":195,"not_started":5}

| Prompt | Category | Title | NotebookLM | ChatGPT | Claude | Gemini |
|---|---|---|---|---|---|---|
| C01 | conceptual_debugging | Command Not Found After Build | captured | captured | captured | captured |
| C02 | conceptual_debugging | Version Control Before Mission Changes | captured | captured | captured | captured |
| C03 | conceptual_debugging | uXMS/uPokeDB Confusion | captured | captured | captured | captured |
| C04 | conceptual_debugging | App Not Publishing | captured | captured | captured | captured |
| C05 | conceptual_debugging | pAntler Did Not Start A Process | captured | captured | captured | captured |
| C06 | conceptual_debugging | Launch Arguments Not Reaching Config Files | captured | captured | captured | captured |
| C07 | conceptual_debugging | Helm Remains PARKED | captured | captured | captured | captured |
| C08 | conceptual_debugging | No Desired Outputs | captured | captured | captured | captured |
| C09 | conceptual_debugging | Vehicle Moves In Simulation But Autonomy Looks Wrong | captured | captured | captured | captured |
| C10 | conceptual_debugging | Multi-Vehicle Ports | captured | captured | captured | captured |
| C11 | conceptual_debugging | Shoreside Missing Vehicle | captured | captured | captured | captured |
| C12 | conceptual_debugging | pShare Route Confusion | captured | captured | captured | captured |
| C13 | conceptual_debugging | TSP App / Behavior Boundary | captured | captured | captured | captured |
| C14 | conceptual_debugging | Distributed Route Assignment Problem | captured | captured | captured | captured |
| C15 | conceptual_debugging | Multi-Machine Networking Problem | captured | captured | captured | captured |
| C16 | conceptual_debugging | Message Does Not Arrive | captured | captured | captured | captured |
| C17 | conceptual_debugging | Node Names / Destinations | captured | captured | captured | captured |
| C18 | conceptual_debugging | Behavior Never Runs | captured | captured | captured | captured |
| C19 | conceptual_debugging | `.moos` vs `.bhv` Mistake | captured | captured | captured | captured |
| C20 | conceptual_debugging | Payload Event Not Affecting Autonomy | captured | captured | captured | captured |
| C21 | conceptual_debugging | Simulation to Heron/PABLO | captured | captured | captured | captured |
| C22 | conceptual_debugging | Field Deployment Sanity Check | captured | captured | captured | captured |
| C23 | conceptual_debugging | Rescue Path Planning | captured | captured | captured | captured |
| C24 | conceptual_debugging | Adversarial Rescue Updates | captured | captured | captured | captured |
| C25 | conceptual_debugging | Teammate Messaging | captured | captured | captured | captured |
| C26 | conceptual_debugging | Post-Mission Alog Diagnosis | captured | captured | captured | captured |
| C27 | conceptual_debugging | pLogger Produced No Useful Alog | captured | captured | captured | captured |
| C28 | conceptual_debugging | Choosing Debugging Tools During A Mission Run | captured | captured | captured | captured |
| C29 | conceptual_debugging | pMarineViewer Background / Geodesy | captured | captured | captured | captured |
| C30 | conceptual_debugging | Mission Broke After Several Edits | captured | captured | captured | captured |
| D01 | exact_docs_tools | pOdometry Variables | captured | captured | captured | captured |
| D02 | exact_docs_tools | pAntler Process Launching | captured | captured | captured | captured |
| D03 | exact_docs_tools | uTimerScript Usage | captured | captured | captured | captured |
| D04 | exact_docs_tools | Helm Deploy Variables | captured | captured | captured | captured |
| D05 | exact_docs_tools | BHV_Waypoint Params | captured | captured | captured | captured |
| D06 | exact_docs_tools | BHV_OpRegionV24 Semantics | captured | captured | captured | captured |
| D07 | exact_docs_tools | Viewer Image / Geodesy Config | captured | captured | captured | captured |
| D08 | exact_docs_tools | pShare Configuration | captured | captured | captured | captured |
| D09 | exact_docs_tools | uField Broker Comparison | captured | captured | captured | captured |
| D10 | exact_docs_tools | pLogger And Alog Verification | captured | captured | captured | captured |
| K01 | code_config_advice | pOdometry Mail Handling | captured | captured | captured | captured |
| K02 | code_config_advice | Missing Registration Pattern | captured | captured | captured | captured |
| K03 | code_config_advice | AppCasting Config Warnings | captured | captured | captured | captured |
| K04 | code_config_advice | uTimerScript Trigger Setup | captured | captured | captured | captured |
| K05 | code_config_advice | Behavior Config File Boundary | captured | captured | captured | captured |
| K06 | code_config_advice | pShare Route Config | captured | captured | captured | captured |
| K07 | code_config_advice | Inter-Vehicle Message Payload | captured | captured | captured | captured |
| K08 | code_config_advice | `setParam()` Pattern | captured | captured | captured | captured |
| K09 | code_config_advice | `addInfoVars()` / InfoBuffer | captured | captured | captured | not_started |
| K10 | code_config_advice | ZAIC Speed Function | not_started | not_started | not_started | not_started |

## Current Position

C01-C30, D01-D10, and K01-K08 are complete for all four tools. K09 is partial: NotebookLM, ChatGPT, and Claude are captured; Gemini was not started. K10 is not started.

## Stop Reason

At 2026-06-01T14:20:36Z, Claude completed K09 and then showed: "You are out of free messages until 12:10 PM". Per the run rule, I stopped the whole benchmark and did not continue with a smaller subset of tools.

## Resume Point

Resume at K09 Gemini only after confirming Claude is available again, then continue to K10 for all four tools if no tool is blocked.
