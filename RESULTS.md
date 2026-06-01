# Benchmark Results

Status: near-complete. C01-C30 and D01-D10 are fully captured and graded. K01-K09 are complete for all four tools, and K10 is graded for NotebookLM TA, ChatGPT, and Gemini. Claude K10 remains pending because Claude hit a quota stop and indicated availability at 12:10 PM.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points. Hard/notable errors are audit details, not a public score-table column.

## Executive Summary

NotebookLM TA is currently first overall on the captured benchmark outputs and is strongest in the intended product lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. ChatGPT remains very strong, especially on readable explanations, but lost credit for several fluent wrong MOOS-IvP-specific details. Gemini was competitive on exact documentation questions but much weaker on the code/config stress prompts. Claude remains provisional because one answer is pending; its captured outputs show the most severe context/search failures.

The evidence still supports a narrow positioning: the notebook is a conceptual, documentation-grounded MOOS-IvP TA. It should not be marketed as an autonomous coding agent, though the code/config stress test suggests it can sometimes outperform general tools on MOOS-IvP-specific configuration patterns.

## Headline Scores

| Model | Score % | Avg / 2 | Good % | Partial % | Bad % | Conceptual | Exact Docs | Code/Config | Pending |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 97.0% | 1.94 | 96.0% | 2.0% | 2.0% | 100.0% | 90.0% | 95.0% | 0 |
| ChatGPT | 94.0% | 1.88 | 90.0% | 8.0% | 2.0% | 96.7% | 90.0% | 90.0% | 0 |
| Gemini | 78.0% | 1.56 | 66.0% | 24.0% | 10.0% | 80.0% | 90.0% | 60.0% | 0 |
| Claude | 60.2% | 1.20 | 38.8% | 42.9% | 18.4% | 60.0% | 50.0% | 72.2% | 1 |

Claude's overall score is provisional because one code/config answer is pending. The denominator for Claude currently excludes K10; all other tools are scored across all 50 prompts.

## Category Results

| Category | Prompt Count | NotebookLM TA | ChatGPT | Claude | Gemini | Status |
|---|---:|---:|---:|---:|---:|---|
| Conceptual/debugging | 30 | 100.0% (2.00/2) | 96.7% (1.93/2) | 60.0% (1.20/2) | 80.0% (1.60/2) | complete |
| Exact docs/parameters/tools | 10 | 90.0% (1.80/2) | 90.0% (1.80/2) | 50.0% (1.00/2) | 90.0% (1.80/2) | complete |
| Code/config advice | 10 | 95.0% (1.90/2) | 90.0% (1.80/2) | 72.2% (1.44/2) | 60.0% (1.20/2) | partial: K10 Claude pending |

## Hard/Notable Error Details

These details are kept for audit. A hard/notable error can be in an answer already counted as partial or bad.

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| C05 | Claude | Wrong pAntler configuration block framing | Suggested looking for ProcessConfig = pAntler around launch entries; the pAntler launch list is read from the ANTLER/Antler process configuration block. |
| C05 | Gemini | Wrong pAntler configuration block framing | Told the user to look for Run lines inside ProcessConfig = pAntler; the pAntler launch block should be ANTLER/Antler, making the answer useful but copy-paste risky. |
| C15 | Claude | Invented MOOS host variable | Introduced MOOS_SERVER_HOST as if it were a mission-file setting; the relevant MOOS configuration field is ServerHost, so the answer was useful but contained a concrete wrong variable name. |
| C06 | Gemini | Off-domain framework drift | Answered as ROS/ArduPilot/PX4/Gazebo caching rather than MOOS launch/nsplug/generated mission files. |
| C16 | Claude | No substantive answer | Asked clarifying questions instead of walking the NODE_MESSAGE_LOCAL delivery path. |
| C17 | Gemini | Off-domain messaging model | Answered as V2X/ROS/MQTT and missed MOOS NODE_MESSAGE fields. |
| C21 | Claude | Invented/uncertain MOOS-IvP app names | Suggested iGPS/iIMU/pNavManager/iHeron/iActuationKF instead of the documented Heron/PABLO interface framing. |
| C21 | Gemini | Invented/uncertain Heron interface app names | Suggested iHeron/iClearpath as the physical Heron front-seat interface, which is not supported by the curated MOOS-IvP TA source set. |
| C22 | Claude | Off-domain deployment checklist | Generic ROS/Gazebo/CARLA checklist with no MOOS-IvP variable/process specificity. |
| C22 | Gemini | Off-domain deployment checklist | Generic drone/autopilot/PX4-style checklist, only partially transferable to a Heron/PABLO MOOS mission. |
| C25 | Claude | Off-domain clarification | Treated uField as unknown and asked whether this was a game/competition instead of answering the MOOS-IvP setup. |
| C26 | Claude | Wrong prompt context | Repeated the unrelated uField clarification instead of answering the alog diagnosis prompt. |
| C27 | ChatGPT | Wrong pAntler configuration block example | Used ProcessConfig = pAntler for Run lines; the pAntler launch block should use the ANTLER process configuration, so the answer was useful but copy-paste risky. |
| C27 | Claude | Invented/imprecise pLogger filtering semantics | Described pLogger as logging only subscribed variables and referred to LogAuxSrc/LOG=false filtering in a way not supported by the curated source set. |
| C29 | Claude | Invented viewer parameters | Used BackgroundFileX/BackgroundFileY/BackgroundFileScale style parameters rather than the MOOS-IvP TIFF/info/datum configuration model. |
| C30 | ChatGPT | Wrong pAntler configuration block example | Again used ProcessConfig = pAntler around Run lines, a plausible-looking but wrong MOOS configuration detail. |
| D01 | Claude | Off-domain ROS answer | Answered with ROS /odom, /joint_states, /imu/data topics instead of MOOS-IvP pOdometry variables. |
| D02 | Claude | Wrong pAntler launch framing | Treated generic ProcessConfig = AppName blocks as launch selectors; pAntler launch commands come from the ANTLER process configuration Run lines. |
| D05 | Claude | Non-answer | Asked for the .bhv file instead of answering the actual BHV_Waypoint parameter question. |
| D06 | ChatGPT | Wrong behavior semantics | Confidently described BHV_OpRegionV24 as only a safety monitor and denied the V24 recovery/steering objective behavior. |
| D08 | Claude | Wrong bridge/tool syntax | Answered primarily with pMOOSBridge SHARE syntax instead of the pShare configuration requested. |
| D08 | Gemini | Inaccurate pShare syntax | Used a nonstandard src_var/colon route form for pShare output in an exact syntax-oriented answer. |
| D10 | Claude | Non-answer | Declined to answer and asked for context despite the prompt naming pLogger, aloggrep, and alogview. |
| K03 | Gemini | Nonstandard AppCasting API | Used RegisterConfigWarning-style wording rather than the AppCasting warning/reporting pattern and did not fix reconnect registration. |
| K06 | ChatGPT | Wrong pShare destination port model | Told the user to route to the destination MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | Claude | Wrong NODE_MESSAGE fields | Claimed string_val/double_val are not recognized and replaced them with moos_var/moos_string, which is wrong for the documented NODE_MESSAGE payload. |
| K07 | Gemini | Wrong inter-vehicle messaging pattern | Recommended Notify("VISIT_POINT", ...) instead of using NODE_MESSAGE_LOCAL with var_name/string_val for the broker/message-handler path. |
| K08 | ChatGPT | Missing base-class delegation in code | The prose mentioned superclass parsing, but the actual correction returned false for unhandled parameters instead of delegating to IvPBehavior::setParam. |
| K09 | Claude | Wrong behavior lifecycle framing | Placed addInfoVars in an onSetParam/RegisterVariables-style flow and described MOOS app mail delivery rather than the helm InfoBuffer behavior pattern. |
| K09 | Gemini | Off-domain BehaviorTree.CPP answer | Answered with BehaviorTree.CPP ports, blackboard, getInput, and BT::NodeStatus rather than MOOS-IvP addInfoVars/InfoBuffer APIs. |
| K10 | Gemini | Invalid/incomplete ZAIC correction | Kept ZAIC_PEAK zaic("speed") without the IvP domain, omitted setPWT(m_priority_wt), and introduced an unsupported setValueAtSummit method. |

## Main Interpretation

The strongest reasonable claim is not that NotebookLM is universally smarter than ChatGPT, Claude, or Gemini. The stronger claim is narrower and more defensible: when the question is grounded in MOOS-IvP lab concepts, documented tools, and common beginner debugging workflows, the curated NotebookLM TA produced fewer MOOS-specific hallucinations and more consistently stayed inside the correct toolchain.

The code/config results are useful but should remain secondary. They show that RAG over the MOOS-IvP source packs can help with exact local conventions, but exact C++ or mission-file correction still needs source-tree verification.

## Prompt-by-Prompt Results

Scoring: `2` = good, `1` = partially useful, `0` = bad, `pending` = not yet captured.

| ID | Prompt Short Name | NotebookLM | ChatGPT | Claude | Gemini | Hard/Notable Details | Notes |
|---|---|---:|---:|---:|---:|---|---|
| C01 | Command Not Found After Build | 2 | 2 | 2 | 2 | none | All models identified PATH/build-location checks; Claude was less MOOS-specific but still useful. |
| C02 | Version Control Before Mission Changes | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave clean Git baseline and generated-file cautions; Claude was useful but drifted into generic robotics/ROS artifacts. |
| C03 | uXMS/uPokeDB Confusion | 2 | 2 | 2 | 2 | none | All models correctly centered the same-host/same-port/same-variable/uXMS registration debugging path. |
| C04 | App Not Publishing | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave a usable app lifecycle pipeline. Claude was mostly useful, but lost credit for suggesting pMarinePID/iGPS-style upstream NAV publishers in a way that could mislead a beginner. |
| C05 | pAntler Did Not Start A Process | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM/ChatGPT gave clean pAntler launch-vs-registration guidance. Claude and Gemini were useful but lost credit for imprecise or wrong ProcessConfig framing; Gemini used ProcessConfig = pAntler for Run lines. |
| C06 | Launch Arguments Not Reaching Config Files | 2 | 2 | 1 | 0 | Gemini | NotebookLM and ChatGPT directly described launch scripts, templates, generated files, and stale target files; Claude was generic ROS-like but partly useful; Gemini went off-domain. |
| C07 | Helm Remains PARKED | 2 | 2 | 2 | 1 | none | NotebookLM/ChatGPT/Claude gave correct helm-state/all-stop/deploy-variable diagnostics; Gemini was broadly helpful but less precise about helm state naming. |
| C08 | No Desired Outputs | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini covered helm state, behavior activation, NAV variables, .moos/.bhv boundaries; Claude had useful checks but wrong pHelmIvP casing and config details. |
| C09 | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | 2 | 2 | 2 | none | All models separated simulator NAV output, helm inputs, behavior conditions, and viewer state well enough. |
| C10 | Multi-Vehicle Ports | 2 | 2 | 2 | 2 | none | All models correctly explained unique MOOSDB ports, community names, pShare ports/routes, and launch arguments. |
| C11 | Shoreside Missing Vehicle | 2 | 2 | 2 | 2 | none | All models traced pNodeReporter/NODE_REPORT through vehicle, bridge, shoreside, and viewer well enough. |
| C12 | pShare Route Confusion | 2 | 2 | 2 | 2 | none | All models gave a reasonable local-vs-shared variable boundary for pShare routes. |
| C13 | TSP App / Behavior Boundary | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini clearly separated planner output, behavior updates, and BHV_Waypoint steering; Claude was conceptually right but less exact on MOOS update naming. |
| C14 | Distributed Route Assignment Problem | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were specific to task generation, identities, route updates, and behavior activation; Claude/Gemini were more generic task-allocation answers. |
| C15 | Multi-Machine Networking Problem | 2 | 2 | 1 | 2 | Claude | NotebookLM/ChatGPT/Gemini gave good multi-machine host/port/firewall/pShare guidance. Claude was useful but introduced a wrong MOOS_SERVER_HOST-style variable name where ServerHost is the relevant mission-file setting. |
| C16 | Message Does Not Arrive | 2 | 2 | 0 | 1 | Claude | NotebookLM/ChatGPT gave the expected NODE_MESSAGE_LOCAL to uField path; Claude did not answer; Gemini gave a generic messaging pipeline with only partial MOOS value. |
| C17 | Node Names / Destinations | 2 | 2 | 1 | 0 | Gemini | NotebookLM/ChatGPT addressed src_node/dest_node/var_name payload fields; Claude was generic multi-middleware; Gemini was off-domain V2X/ROS/MQTT. |
| C18 | Behavior Never Runs | 2 | 2 | 2 | 2 | none | All models gave usable behavior-state, condition, pwt, InfoBuffer, update, and uHelmScope guidance. |
| C19 | `.moos` vs `.bhv` Mistake | 2 | 2 | 2 | 2 | none | All models correctly distinguished .moos app/process config from .bhv behavior config. |
| C20 | Payload Event Not Affecting Autonomy | 2 | 2 | 2 | 2 | none | All models gave a usable data-path trace from payload publication through MOOSDB into helm conditions/updates/coordinating apps. |
| C21 | Simulation to Heron/PABLO | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM and ChatGPT gave the cleanest uSimMarine-to-Heron/PABLO transition framing. Claude and Gemini kept some useful safety/architecture points but lost credit for invented or unsupported Heron interface app names. |
| C22 | Field Deployment Sanity Check | 2 | 2 | 0 | 1 | Claude, Gemini | NotebookLM/ChatGPT were MOOS/PABLO-aware; Claude was generic ROS/Gazebo; Gemini was generic drone/autopilot deployment with little MOOS specificity. |
| C23 | Rescue Path Planning | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were most aligned with MOOS rescue planner/route handoff; Claude/Gemini were generic SAR planning but still conceptually useful. |
| C24 | Adversarial Rescue Updates | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT addressed dynamic rescue updates and replanning in the lab style; Claude/Gemini gave generic dynamic task-allocation answers. |
| C25 | Teammate Messaging | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini understood two-vehicle rescue/uField messaging; Claude asked for context and treated uField as unknown. |
| C26 | Post-Mission Alog Diagnosis | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini gave aloggrep/alogview/aloghelm-style post-run debugging; Claude returned an unrelated uField clarification from a prior prompt. |
| C27 | pLogger Produced No Useful Alog | 2 | 1 | 1 | 2 | ChatGPT, Claude | NotebookLM and Gemini gave useful pLogger/path/process guidance. ChatGPT was otherwise strong but used a wrong ProcessConfig = pAntler example; Claude included unsupported pLogger filtering/subscription claims. |
| C28 | Choosing Debugging Tools During A Mission Run | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini mapped tools to use cases well; Claude was useful but shallower and slightly imprecise on uQueryDB/pLogger roles. |
| C29 | pMarineViewer Background / Geodesy | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini covered image files, datum, local coordinates, and viewer config; Claude invented BackgroundFile-style parameter names. |
| C30 | Mission Broke After Several Edits | 2 | 1 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini gave usable triage order. ChatGPT was useful overall but lost credit for repeating a wrong ProcessConfig = pAntler launch-block example. |
| D01 | pOdometry Variables | 2 | 2 | 0 | 1 | Claude | NotebookLM and ChatGPT gave the expected NAV_X/NAV_Y to ODOMETRY_DIST path; Claude answered as ROS odometry; Gemini mixed MOOS-IvP with generic robotics/ROS signals. |
| D02 | pAntler Process Launching | 0 | 2 | 1 | 2 | Claude | ChatGPT and Gemini correctly centered ProcessConfig = ANTLER and Run lines. NotebookLM failed to answer. Claude was useful but framed launch discovery around generic ProcessConfig = AppName blocks instead of the ANTLER launch block. |
| D03 | uTimerScript Usage | 2 | 2 | 2 | 2 | none | All four answers gave a usable uTimerScript mental model: timed MOOS posts for initialization, triggers, simulation proxies, and checks in uXMS. |
| D04 | Helm Deploy Variables | 2 | 2 | 2 | 2 | none | All four answers correctly described DEPLOY, MOOS_MANUAL_OVERRIDE, and helm state gating for autonomous behavior. |
| D05 | BHV_Waypoint Params | 2 | 2 | 0 | 2 | Claude | NotebookLM, ChatGPT, and Gemini rejected the invented parameter and identified capture_radius/radius, slip_radius/nm_radius, and capture_line. Claude did not answer without an uploaded file. |
| D06 | BHV_OpRegionV24 Semantics | 2 | 0 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini described the V24 core/save/halt model and active recovery influence. ChatGPT gave the legacy OpRegion mental model and incorrectly denied steering/recovery behavior. |
| D07 | Viewer Image / Geodesy Config | 2 | 2 | 1 | 2 | none | NotebookLM and ChatGPT gave strong viewer/image/datum checks; Gemini was also usable. Claude identified the right general issue but placed datum settings in questionable app blocks and used imprecise viewer parameter framing. |
| D08 | pShare Configuration | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM and ChatGPT gave the cleanest pShare routing model. Claude mostly answered with pMOOSBridge syntax. Gemini had the right idea but used an inaccurate pShare output syntax for an exact-docs prompt. |
| D09 | uField Broker Comparison | 2 | 2 | 1 | 2 | none | NotebookLM, ChatGPT, and Gemini gave a usable comparison of brokers, pShare bridging, node comms, and message handling. Claude was broadly useful but overstated node reports and used imprecise bridge terminology. |
| D10 | pLogger And Alog Verification | 2 | 2 | 0 | 2 | Claude | NotebookLM, ChatGPT, and Gemini gave a usable alog/pLogger verification workflow. Claude declined to answer without additional context. |
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

## Appendix: Detailed Reports

- `reports/conceptual_debugging_benchmark_results.md`
- `reports/exact_docs_tools_benchmark_results.md`
- `reports/code_config_benchmark_results.md`
- `reports/hallucination_sweep_notes.md`

## Appendix: Grading Method

See `SCORING_RUBRIC.md` for the concise scoring rubric. Conceptual and exact-doc answers were checked against the curated NotebookLM source packs and known MOOS-IvP documentation semantics. Code/config answers were checked against the local MOOS-IvP checkout at `/Users/charlesbenjamin/moos-ivp`, especially behavior examples, pShare/uField message tooling, and IvP behavior/ZAIC APIs.
