# ChatGPT 5.5 Low CLI Benchmark Addendum

Status: complete for C01-C30, D01-D15, and K01-K15 as a separate isolated CLI model from browser ChatGPT rows.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Collection used a temporary updated Codex CLI, ephemeral/read-only execution, fresh turn per prompt, ignored user config/rules, and an empty working directory. The retained raw JSON records contain answer text plus collection metadata, and the integrity scan found no suspicious events or local MOOS-IvP checkout path references in stored answers.

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; hallucinations and invalid MOOS-IvP-specific syntax are penalized.

## Headline Scores

| Category | Prompt Count | Score % | Avg / 2 | Good | Partial | Bad |
|---|---:|---:|---:|---:|---:|---:|
| Overall | 60 | 90.0% | 1.80 | 49/60 (81.7%) | 10/60 (16.7%) | 1/60 (1.7%) |
| Conceptual/debugging | 30 | 91.7% | 1.83 | 25/30 (83.3%) | 5/30 (16.7%) | 0/30 (0.0%) |
| Exact docs/parameters/tools | 15 | 80.0% | 1.60 | 10/15 (66.7%) | 4/15 (26.7%) | 1/15 (6.7%) |
| Code/config advice | 15 | 96.7% | 1.93 | 14/15 (93.3%) | 1/15 (6.7%) | 0/15 (0.0%) |

## Interpretation

GPT-5.5 Low CLI was strong overall, especially on code/config prompts, but it lost more ground on exact MOOS-IvP documentation details than the browser ChatGPT rows. Since this was collected through Codex CLI, the code/config score should be interpreted as an isolated no-local-context Codex CLI result, not as a pure browser ChatGPT-low result. The largest penalties were pHelmIvP behavior-file parameter naming, uField/NODE_MESSAGE process ownership, pShare port semantics, pNodeReporter report naming, and BHV_OpRegionV24 V24 recovery behavior.

## Hard/Notable Error Details

| Prompt ID | Failure Type | Brief Explanation |
|---|---|---|
| C08 | Wrong pHelmIvP behavior-file parameter | Used singular `behavior = file.bhv`; pHelmIvP parses the `Behaviors = ...` parameter or `.bhv` command-line files. |
| C11 | Wrong NODE_REPORT_LOCAL framing | Useful checklist, but repeatedly framed the vehicle-side source as `NODE_REPORT`; pNodeReporter normally publishes `NODE_REPORT_LOCAL`, which is then shared as `NODE_REPORT`. |
| C16 | Wrong NODE_MESSAGE handling process | Named pNodeReporter as a common NODE_MESSAGE_LOCAL handler; the relevant path is uFldNodeBroker/uFldNodeComms/uFldMessageHandler style messaging. |
| C19 | Wrong pHelmIvP behavior-file parameter | Correct file-boundary explanation but gave `behavior = filename.bhv` instead of `Behaviors = filename.bhv`. |
| C25 | Imprecise uField message transport | Described scout reports moving through uField broker/handler plumbing without clearly requiring NODE_MESSAGE payloads or explicit pShare/uField routes. |
| D02 | Invented/misspelled executable name | Used `pNodeReport` in an exact pAntler launch example; the app is `pNodeReporter`. |
| D05 | Invented BHV_Waypoint parameter | Listed `capture_line_radius`, which is not parsed by BHV_Waypoint source. |
| D06 | Wrong behavior semantics | Described BHV_OpRegionV24 as only a constraint/watchdog and denied the documented V24 save-poly recovery objective function. |
| D08 | Wrong pShare destination port model | Said pShare remote host/port is usually the other community MOOSDB host/port; output routes should target the receiving pShare input/route port. |
| D14 | Wrong pNodeReporter default output framing | Said pNodeReporter normally publishes NODE_REPORT; source defaults to NODE_REPORT_LOCAL. |
| K09 | Wrong behavior lifecycle framing | Put addInfoVars in onHelmStart/onIdleState instead of the normal constructor/config-time behavior pattern. |

## Prompt-by-Prompt Results

| ID | Category | Prompt Short Name | Score | Notes |
|---|---|---|---:|---|
| C01 | conceptual_debugging | Command Not Found After Build | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C02 | conceptual_debugging | Version Control Before Mission Changes | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C03 | conceptual_debugging | uXMS/uPokeDB Confusion | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C04 | conceptual_debugging | App Not Publishing | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C05 | conceptual_debugging | pAntler Did Not Start A Process | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C06 | conceptual_debugging | Launch Arguments Not Reaching Config Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C07 | conceptual_debugging | Helm Remains PARKED | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C08 | conceptual_debugging | No Desired Outputs | 1 | Partial: useful helm/nav/condition checks, but it says the pHelmIvP `.moos` setting is `behavior = your_file.bhv`; source and missions use the `Behaviors = ...` parameter, so the behavior-file check is copy-paste risky. |
| C09 | conceptual_debugging | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C10 | conceptual_debugging | Multi-Vehicle Ports | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C11 | conceptual_debugging | Shoreside Missing Vehicle | 1 | Partial: useful checklist, but it repeatedly frames the vehicle-side report as `NODE_REPORT`; pNodeReporter normally publishes `NODE_REPORT_LOCAL`, which is then shared outward as `NODE_REPORT`. |
| C12 | conceptual_debugging | pShare Route Confusion | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C13 | conceptual_debugging | TSP App / Behavior Boundary | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C14 | conceptual_debugging | Distributed Route Assignment Problem | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C15 | conceptual_debugging | Multi-Machine Networking Problem | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C16 | conceptual_debugging | Message Does Not Arrive | 1 | Partial: mostly correct NODE_MESSAGE_LOCAL to NODE_MESSAGE to payload-variable trace, but it incorrectly names pNodeReporter as a common sender-side handler for NODE_MESSAGE_LOCAL instead of keeping the uField broker/message-handler path clean. |
| C17 | conceptual_debugging | Node Names / Destinations | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C18 | conceptual_debugging | Behavior Never Runs | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C19 | conceptual_debugging | `.moos` vs `.bhv` Mistake | 1 | Partial: correctly separates `.moos` app config from `.bhv` behavior config, but gives `behavior = filename.bhv` as the pHelmIvP config pattern rather than the documented `Behaviors = filename.bhv` parameter. |
| C20 | conceptual_debugging | Payload Event Not Affecting Autonomy | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C21 | conceptual_debugging | Simulation to Heron/PABLO | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C22 | conceptual_debugging | Field Deployment Sanity Check | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C23 | conceptual_debugging | Rescue Path Planning | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C24 | conceptual_debugging | Adversarial Rescue Updates | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C25 | conceptual_debugging | Teammate Messaging | 1 | Partial: good teammate/scout/rescue mental model, but the uField transport explanation implies a generic SCOUT_REPORT can move through broker/message-handler plumbing without clearly using the NODE_MESSAGE envelope or explicit sharing route. |
| C26 | conceptual_debugging | Post-Mission Alog Diagnosis | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C27 | conceptual_debugging | pLogger Produced No Useful Alog | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C28 | conceptual_debugging | Choosing Debugging Tools During A Mission Run | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C29 | conceptual_debugging | pMarineViewer Background / Geodesy | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| C30 | conceptual_debugging | Mission Broke After Several Edits | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D01 | exact_docs_tools | pOdometry Variables | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D02 | exact_docs_tools | pAntler Process Launching | 1 | Partial: correctly explains ANTLER `Run = ...` launch lines and registration, but includes an invented/misspelled `pNodeReport` executable in the exact pAntler example. |
| D03 | exact_docs_tools | uTimerScript Usage | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D04 | exact_docs_tools | Helm Deploy Variables | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D05 | exact_docs_tools | BHV_Waypoint Params | 1 | Partial: correctly rejects `magic_arrival_radius` and names real BHV_Waypoint parameters such as `capture_radius`, `slip_radius`/`nm_radius`, `capture_line`, `lead`, and `lead_damper`, but also invents `capture_line_radius` as a parameter. |
| D06 | exact_docs_tools | BHV_OpRegionV24 Semantics | 0 | Bad: repeats the legacy mental model that BHV_OpRegionV24 is only a monitor/constraint behavior and denies the V24 save-poly recovery objective function shown in source. |
| D07 | exact_docs_tools | Viewer Image / Geodesy Config | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D08 | exact_docs_tools | pShare Configuration | 1 | Partial: useful route/host/variable debugging advice, but says pShare remote host/port is usually the other community MOOSDB host/port; the pShare output route should target the receiving pShare input/route port. |
| D09 | exact_docs_tools | uField Broker Comparison | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D10 | exact_docs_tools | pLogger And Alog Verification | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D11 | exact_docs_tools | Generated Mission Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D12 | exact_docs_tools | pMarineViewer Action Buttons | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D13 | exact_docs_tools | uXMS, uQueryDB, and uPokeDB | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D14 | exact_docs_tools | pNodeReporter and NODE_REPORT | 1 | Partial: explains the local-vs-shared report distinction, but starts by saying pNodeReporter normally publishes `NODE_REPORT`; source defaults to `NODE_REPORT_LOCAL`, with `NODE_REPORT` normally being the shared/received report. |
| D15 | exact_docs_tools | Loiter and Station-Keep Behaviors | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K01 | code_config_advice | pOdometry Mail Handling | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K02 | code_config_advice | Missing Registration Pattern | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K03 | code_config_advice | AppCasting Config Warnings | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K04 | code_config_advice | uTimerScript Trigger Setup | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K05 | code_config_advice | Behavior Config File Boundary | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K06 | code_config_advice | pShare Route Config | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K07 | code_config_advice | Inter-Vehicle Message Payload | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K08 | code_config_advice | `setParam()` Pattern | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K09 | code_config_advice | `addInfoVars()` / InfoBuffer | 1 | Partial: correctly uses `addInfoVars()` and `getBufferDoubleVal(..., ok)`, but places InfoVar registration in `onHelmStart()`/`onIdleState()` instead of the normal constructor/config-time behavior pattern used throughout the MOOS-IvP behavior source. |
| K10 | code_config_advice | ZAIC Speed Function | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K11 | code_config_advice | Reconnect-Safe Registration | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K12 | code_config_advice | Editing Templates But Launching Stale Files | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K13 | code_config_advice | pMarineViewer Button Posts | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K14 | code_config_advice | Behavior Updates Not Taking Effect | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| K15 | code_config_advice | Duplicate Ports and Community Names | 2 | Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
