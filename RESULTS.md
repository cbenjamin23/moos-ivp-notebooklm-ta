# Benchmark Results

Status: complete. C01-C30, D01-D15, and K01-K15 are fully captured and graded for NotebookLM TA, ChatGPT 5.5 Thinking, ChatGPT 5.5 Instant, Claude, and Gemini. User-approved recaptures are treated as the regular stored answers.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points. Concrete hallucinations and invalid copy-pasteable MOOS-IvP details are penalized even when the surrounding answer is useful.

## Executive Summary

NotebookLM TA finished first overall and remained strongest in the intended product lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. ChatGPT 5.5 Thinking remained very strong, especially on readable explanations. ChatGPT 5.5 Instant was also strong, but the hallucination-focused sweep lowered its score for concrete MOOS-IvP mistakes in pShare routing, NODE_MESSAGE fields/process ownership, BHV_OpRegionV24 semantics, behavior `setParam()`, and ZAIC construction.

The evidence supports a narrow positioning: the notebook is a conceptual, documentation-grounded MOOS-IvP TA. It should not be marketed as an autonomous coding agent, though the code/config stress test suggests that RAG over curated MOOS-IvP sources can help with beginner configuration patterns.

## Headline Scores

| Model | Score % | Avg / 2 | Good % | Partial % | Bad % | Conceptual | Exact Docs | Code/Config | Pending |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 99.2% | 1.98 | 98.3% | 1.7% | 0.0% | 100.0% | 100.0% | 96.7% | 0 |
| ChatGPT 5.5 Thinking | 94.2% | 1.88 | 90.0% | 8.3% | 1.7% | 96.7% | 90.0% | 93.3% | 0 |
| ChatGPT 5.5 Instant | 91.7% | 1.83 | 86.7% | 10.0% | 3.3% | 95.0% | 93.3% | 83.3% | 0 |
| Gemini | 80.0% | 1.60 | 68.3% | 23.3% | 8.3% | 80.0% | 90.0% | 70.0% | 0 |
| Claude | 71.7% | 1.43 | 51.7% | 40.0% | 8.3% | 65.0% | 73.3% | 83.3% | 0 |

## Category Results

| Category | Prompt Count | NotebookLM TA | ChatGPT Thinking | ChatGPT Instant | Claude | Gemini | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Conceptual/debugging | 30 | 100.0% (2.00/2) | 96.7% (1.93/2) | 95.0% (1.90/2) | 65.0% (1.30/2) | 80.0% (1.60/2) | complete |
| Exact docs/parameters/tools | 15 | 100.0% (2.00/2) | 90.0% (1.80/2) | 93.3% (1.87/2) | 73.3% (1.47/2) | 90.0% (1.80/2) | complete |
| Code/config advice | 15 | 96.7% (1.93/2) | 93.3% (1.87/2) | 83.3% (1.67/2) | 83.3% (1.67/2) | 70.0% (1.40/2) | complete |

## Recapture Note

User-approved recaptures are treated as the regular stored answers. NotebookLM D02 preserves the original non-answer in `raw/D02.json` replacement metadata, but the scored answer is the recapture. Claude C16, C25, C26, D05, and D10 are also stored as primary answers after direct-answer recapture; scoring remains hallucination-sensitive, so C16 still scores `0` because the recaptured answer gives the wrong NODE_MESSAGE_LOCAL mental model.

## Hard/Notable Error Details

These details are kept for audit. A hard/notable error can be in an answer already counted as partial or bad.

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| C05 | Claude | Wrong pAntler configuration block framing | Suggested looking for ProcessConfig = pAntler around launch entries; the pAntler launch list is read from the ANTLER/Antler process configuration block. |
| C05 | Gemini | Wrong pAntler configuration block framing | Told the user to look for Run lines inside ProcessConfig = pAntler; the pAntler launch block should be ANTLER/Antler, making the answer useful but copy-paste risky. |
| C15 | Claude | Invented MOOS host variable | Introduced MOOS_SERVER_HOST as if it were a mission-file setting; the relevant MOOS configuration field is ServerHost, so the answer was useful but contained a concrete wrong variable name. |
| C06 | Gemini | Off-domain framework drift | Answered as ROS/ArduPilot/PX4/Gazebo caching rather than MOOS launch/nsplug/generated mission files. |
| C17 | Gemini | Off-domain messaging model | Answered as V2X/ROS/MQTT and missed MOOS NODE_MESSAGE fields. |
| C21 | Claude | Invented/uncertain MOOS-IvP app names | Suggested iGPS/iIMU/pNavManager/iHeron/iActuationKF instead of the documented Heron/PABLO interface framing. |
| C21 | Gemini | Invented/uncertain Heron interface app names | Suggested iHeron/iClearpath as the physical Heron front-seat interface, which is not supported by the curated MOOS-IvP TA source set. |
| C22 | Claude | Off-domain deployment checklist | Generic ROS/Gazebo/CARLA checklist with no MOOS-IvP variable/process specificity. |
| C22 | Gemini | Off-domain deployment checklist | Generic drone/autopilot/PX4-style checklist, only partially transferable to a Heron/PABLO MOOS mission. |
| C27 | ChatGPT 5.5 Thinking | Wrong pAntler configuration block example | Used ProcessConfig = pAntler for Run lines; the pAntler launch block should use the ANTLER process configuration, so the answer was useful but copy-paste risky. |
| C27 | Claude | Invented/imprecise pLogger filtering semantics | Described pLogger as logging only subscribed variables and referred to LogAuxSrc/LOG=false filtering in a way not supported by the curated source set. |
| C29 | Claude | Invented viewer parameters | Used BackgroundFileX/BackgroundFileY/BackgroundFileScale style parameters rather than the MOOS-IvP TIFF/info/datum configuration model. |
| C30 | ChatGPT 5.5 Thinking | Wrong pAntler configuration block example | Again used ProcessConfig = pAntler around Run lines, a plausible-looking but wrong MOOS configuration detail. |
| C16 | Claude | Wrong NODE_MESSAGE_LOCAL semantics | The recaptured answer was substantive but incorrectly described NODE_MESSAGE_LOCAL as same-process/local-only rather than the MOOS-IvP local report that should be brokered through the uField messaging path. |
| C11 | ChatGPT 5.5 Instant | Wrong pShare destination port model | Said vehicle reports should be sent to the shoreside MOOSDB port; pShare output should target the receiving pShare route/input port. |
| C12 | ChatGPT 5.5 Instant | Wrong pShare destination port model | Described pShare as sending directly to the remote MOOSDB at host:port rather than to the receiving pShare route/input port. |
| C16 | ChatGPT 5.5 Instant | Wrong NODE_MESSAGE handling process | Described pNodeReporter as converting/unwrapping NODE_MESSAGE_LOCAL/NODE_MESSAGE; the lab/source path uses uFldNodeBroker/uFldMessageHandler style handling. |
| D01 | Claude | Off-domain ROS answer | Answered with ROS /odom, /joint_states, /imu/data topics instead of MOOS-IvP pOdometry variables. |
| D02 | Claude | Wrong pAntler launch framing | Treated generic ProcessConfig = AppName blocks as launch selectors; pAntler launch commands come from the ANTLER process configuration Run lines. |
| D06 | ChatGPT | Wrong behavior semantics | Confidently described BHV_OpRegionV24 as only a safety monitor and denied the V24 recovery/steering objective behavior. |
| D08 | Claude | Wrong bridge/tool syntax | Answered primarily with pMOOSBridge SHARE syntax instead of the pShare configuration requested. |
| D08 | Gemini | Inaccurate pShare syntax | Used a nonstandard src_var/colon route form for pShare output in an exact syntax-oriented answer. |
| D12 | ChatGPT | Wrong pMarineViewer button syntax | Used `action = ...` as the button syntax instead of the documented button_one/button_two action-button parameters. |
| D12 | Claude | Wrong pMarineViewer button syntax | Used a var/sval button form that does not match the documented pMarineViewer button_one/button_two syntax. |
| D12 | Gemini | Wrong pMarineViewer button parameter | Used a generic `BUTTON = ...` parameter instead of the documented numbered button parameters. |
| D14 | Claude | Wrong NODE_REPORT_LOCAL publication framing | Stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally, weakening the local-vs-shared report distinction. |
| D06 | ChatGPT 5.5 Instant | Wrong behavior semantics | Described BHV_OpRegionV24 as only a safety/constraint monitor and denied the V24 recovery/steering behavior. |
| K03 | Gemini | Nonstandard AppCasting API | Used RegisterConfigWarning-style wording rather than the AppCasting warning/reporting pattern and did not fix reconnect registration. |
| K06 | ChatGPT | Wrong pShare destination port model | Told the user to route to the destination MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | Claude | Wrong NODE_MESSAGE fields | Claimed string_val/double_val are not recognized and replaced them with moos_var/moos_string, which is wrong for the documented NODE_MESSAGE payload. |
| K07 | Gemini | Wrong inter-vehicle messaging pattern | Recommended Notify("VISIT_POINT", ...) instead of using NODE_MESSAGE_LOCAL with var_name/string_val for the broker/message-handler path. |
| K08 | ChatGPT | Missing base-class delegation in code | The prose mentioned superclass parsing, but the actual correction returned false for unhandled parameters instead of delegating to IvPBehavior::setParam. |
| K09 | Claude | Wrong behavior lifecycle framing | Placed addInfoVars in an onSetParam/RegisterVariables-style flow and described MOOS app mail delivery rather than the helm InfoBuffer behavior pattern. |
| K09 | Gemini | Off-domain BehaviorTree.CPP answer | Answered with BehaviorTree.CPP ports, blackboard, getInput, and BT::NodeStatus rather than MOOS-IvP addInfoVars/InfoBuffer APIs. |
| K10 | Gemini | Invalid/incomplete ZAIC correction | Kept ZAIC_PEAK zaic("speed") without the IvP domain, omitted setPWT(m_priority_wt), and introduced an unsupported setValueAtSummit method. |
| K15 | Gemini | Wrong pShare/port mental model | Got the unique vehicle ports and community names right, but suggested routing shoreside pShare output to vehicle MOOSDB ports rather than distinguishing pShare route ports from MOOSDB ServerPort. |
| K06 | ChatGPT 5.5 Instant | Wrong pShare destination port model | Told the user to route to the shoreside MOOSDB ServerPort; pShare output should target the receiving pShare route/input port. |
| K07 | ChatGPT 5.5 Instant | Wrong NODE_MESSAGE destination field | Explicitly replaced the documented dest_node field with dests=bravo, which would break the message format. |
| K08 | ChatGPT 5.5 Instant | Missing base-class delegation in code | Validated the custom parameter but returned false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K10 | ChatGPT 5.5 Instant | Invalid/incomplete ZAIC correction | Added shaping and setPWT but kept ZAIC_PEAK zaic("speed") without the IvP domain constructor argument. |

## Main Interpretation

The strongest reasonable claim is not that NotebookLM is universally smarter than ChatGPT, Claude, or Gemini. The stronger claim is narrower and more defensible: when the question is grounded in MOOS-IvP lab concepts, documented tools, and common beginner debugging workflows, the curated NotebookLM TA produced fewer MOOS-specific hallucinations and more consistently stayed inside the correct toolchain.

The expanded exact-doc and code/config prompts reinforced the same pattern. General models often understood the broad concept, but were more likely to produce plausible-looking syntax or routing details that would waste a student’s time if copied directly. NotebookLM was not perfect, but it was more conservative and source-aligned.

## Prompt-by-Prompt Results

Scoring: `2` = good, `1` = partially useful, `0` = bad.

| ID | Prompt Short Name | NotebookLM | ChatGPT Thinking | ChatGPT Instant | Claude | Gemini | Hard/Notable Details | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| C01 | Command Not Found After Build | 2 | 2 | 2 | 2 | 2 | none | All models identified PATH/build-location checks; Claude was less MOOS-specific but still useful. |
| C02 | Version Control Before Mission Changes | 2 | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave clean Git baseline and generated-file cautions; Claude was useful but drifted into generic robotics/ROS artifacts. |
| C03 | uXMS/uPokeDB Confusion | 2 | 2 | 2 | 2 | 2 | none | All models correctly centered the same-host/same-port/same-variable/uXMS registration debugging path. |
| C04 | App Not Publishing | 2 | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave a usable app lifecycle pipeline. Claude was mostly useful, but lost credit for suggesting pMarinePID/iGPS-style upstream NAV publishers in a way that could mislead a beginner. |
| C05 | pAntler Did Not Start A Process | 2 | 2 | 2 | 1 | 1 | claude, gemini | NotebookLM/ChatGPT gave clean pAntler launch-vs-registration guidance. Claude and Gemini were useful but lost credit for imprecise or wrong ProcessConfig framing; Gemini used ProcessConfig = pAntler for Run lines. |
| C06 | Launch Arguments Not Reaching Config Files | 2 | 2 | 2 | 1 | 0 | gemini | NotebookLM and ChatGPT directly described launch scripts, templates, generated files, and stale target files; Claude was generic ROS-like but partly useful; Gemini went off-domain. |
| C07 | Helm Remains PARKED | 2 | 2 | 2 | 2 | 1 | none | NotebookLM/ChatGPT/Claude gave correct helm-state/all-stop/deploy-variable diagnostics; Gemini was broadly helpful but less precise about helm state naming. |
| C08 | No Desired Outputs | 2 | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini covered helm state, behavior activation, NAV variables, .moos/.bhv boundaries; Claude had useful checks but wrong pHelmIvP casing and config details. |
| C09 | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | 2 | 2 | 2 | 2 | none | All models separated simulator NAV output, helm inputs, behavior conditions, and viewer state well enough. |
| C10 | Multi-Vehicle Ports | 2 | 2 | 2 | 2 | 2 | none | All models correctly explained unique MOOSDB ports, community names, pShare ports/routes, and launch arguments. |
| C11 | Shoreside Missing Vehicle | 2 | 2 | 1 | 2 | 2 | ChatGPT 5.5 Instant | All models traced pNodeReporter/NODE_REPORT through vehicle, bridge, shoreside, and viewer well enough. GPT-5.5 Instant: Partial: useful NODE_REPORT/pNodeReporter debugging path, but includes the wrong pShare-port mental model by saying vehicle reports should be sent to the shoreside MOOSDB port. |
| C12 | pShare Route Confusion | 2 | 2 | 1 | 2 | 2 | ChatGPT 5.5 Instant | All models gave a reasonable local-vs-shared variable boundary for pShare routes. GPT-5.5 Instant: Partial: good local-vs-shared variable framing, but incorrectly describes a pShare route as sending directly to the remote MOOSDB rather than to the receiving pShare route/input port. |
| C13 | TSP App / Behavior Boundary | 2 | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini clearly separated planner output, behavior updates, and BHV_Waypoint steering; Claude was conceptually right but less exact on MOOS update naming. |
| C14 | Distributed Route Assignment Problem | 2 | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were specific to task generation, identities, route updates, and behavior activation; Claude/Gemini were more generic task-allocation answers. |
| C15 | Multi-Machine Networking Problem | 2 | 2 | 2 | 1 | 2 | claude | NotebookLM/ChatGPT/Gemini gave good multi-machine host/port/firewall/pShare guidance. Claude was useful but introduced a wrong MOOS_SERVER_HOST-style variable name where ServerHost is the relevant mission-file setting. |
| C16 | Message Does Not Arrive | 2 | 2 | 1 | 0 | 1 | Claude, ChatGPT 5.5 Instant | NotebookLM and ChatGPT gave the expected NODE_MESSAGE_LOCAL to uField path. The recaptured Claude answer was substantive but still wrong about NODE_MESSAGE_LOCAL scoping, so it remains bad. Gemini gave a generic messaging pipeline with only partial MOOS value. GPT-5.5 Instant: Partial: useful NODE_MESSAGE_LOCAL / NODE_MESSAGE / dest_node / var_name debugging path, but wrongly assigns conversion/unwrapping to pNodeReporter rather than the uField broker/message-handler path. |
| C17 | Node Names / Destinations | 2 | 2 | 2 | 1 | 0 | gemini | NotebookLM/ChatGPT addressed src_node/dest_node/var_name payload fields; Claude was generic multi-middleware; Gemini was off-domain V2X/ROS/MQTT. |
| C18 | Behavior Never Runs | 2 | 2 | 2 | 2 | 2 | none | All models gave usable behavior-state, condition, pwt, InfoBuffer, update, and uHelmScope guidance. |
| C19 | `.moos` vs `.bhv` Mistake | 2 | 2 | 2 | 2 | 2 | none | All models correctly distinguished .moos app/process config from .bhv behavior config. |
| C20 | Payload Event Not Affecting Autonomy | 2 | 2 | 2 | 2 | 2 | none | All models gave a usable data-path trace from payload publication through MOOSDB into helm conditions/updates/coordinating apps. |
| C21 | Simulation to Heron/PABLO | 2 | 2 | 2 | 1 | 1 | claude, gemini | NotebookLM and ChatGPT gave the cleanest uSimMarine-to-Heron/PABLO transition framing. Claude and Gemini kept some useful safety/architecture points but lost credit for invented or unsupported Heron interface app names. |
| C22 | Field Deployment Sanity Check | 2 | 2 | 2 | 0 | 1 | claude, gemini | NotebookLM/ChatGPT were MOOS/PABLO-aware; Claude was generic ROS/Gazebo; Gemini was generic drone/autopilot deployment with little MOOS specificity. |
| C23 | Rescue Path Planning | 2 | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were most aligned with MOOS rescue planner/route handoff; Claude/Gemini were generic SAR planning but still conceptually useful. |
| C24 | Adversarial Rescue Updates | 2 | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT addressed dynamic rescue updates and replanning in the lab style; Claude/Gemini gave generic dynamic task-allocation answers. |
| C25 | Teammate Messaging | 2 | 2 | 2 | 1 | 2 | none | NotebookLM, ChatGPT, and Gemini understood two-vehicle rescue/uField messaging. The recaptured Claude answer was operationally useful but generic and weak on the uField-specific messaging path. |
| C26 | Post-Mission Alog Diagnosis | 2 | 2 | 2 | 2 | 2 | none | All four final stored answers gave useful post-run diagnosis guidance; the recaptured Claude answer covered aloggrep, IVPHELM_SUMMARY, condition variables, and behavior-state tracing. |
| C27 | pLogger Produced No Useful Alog | 2 | 1 | 2 | 1 | 2 | chatgpt, claude | NotebookLM and Gemini gave useful pLogger/path/process guidance. ChatGPT was otherwise strong but used a wrong ProcessConfig = pAntler example; Claude included unsupported pLogger filtering/subscription claims. |
| C28 | Choosing Debugging Tools During A Mission Run | 2 | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini mapped tools to use cases well; Claude was useful but shallower and slightly imprecise on uQueryDB/pLogger roles. |
| C29 | pMarineViewer Background / Geodesy | 2 | 2 | 2 | 0 | 2 | claude | NotebookLM/ChatGPT/Gemini covered image files, datum, local coordinates, and viewer config; Claude invented BackgroundFile-style parameter names. |
| C30 | Mission Broke After Several Edits | 2 | 1 | 2 | 2 | 2 | chatgpt | NotebookLM, Claude, and Gemini gave usable triage order. ChatGPT was useful overall but lost credit for repeating a wrong ProcessConfig = pAntler launch-block example. |
| D01 | pOdometry Variables | 2 | 2 | 2 | 0 | 1 | Claude | NotebookLM and ChatGPT gave the expected NAV_X/NAV_Y to ODOMETRY_DIST path; Claude answered as ROS odometry; Gemini mixed MOOS-IvP with generic robotics/ROS signals. |
| D02 | pAntler Process Launching | 2 | 2 | 2 | 1 | 2 | Claude | NotebookLM retry replacement, ChatGPT, and Gemini correctly centered ProcessConfig = ANTLER and Run lines. The first NotebookLM pass returned only “The system was unable to answer,” but the user requested treating the immediate retry as the primary result. Claude was useful but framed launch discovery around generic ProcessConfig = AppName blocks instead of the ANTLER launch block. |
| D03 | uTimerScript Usage | 2 | 2 | 2 | 2 | 2 | none | All four answers gave a usable uTimerScript mental model: timed MOOS posts for initialization, triggers, simulation proxies, and checks in uXMS. |
| D04 | Helm Deploy Variables | 2 | 2 | 2 | 2 | 2 | none | All four answers correctly described DEPLOY, MOOS_MANUAL_OVERRIDE, and helm state gating for autonomous behavior. |
| D05 | BHV_Waypoint Params | 2 | 2 | 2 | 2 | 2 | none | All four final stored answers rejected the invented magic_arrival_radius parameter and identified real BHV_Waypoint arrival/capture parameters such as capture_radius/radius and slip_radius/nm_radius. |
| D06 | BHV_OpRegionV24 Semantics | 2 | 0 | 0 | 2 | 2 | ChatGPT, ChatGPT 5.5 Instant | NotebookLM, Claude, and Gemini described the V24 core/save/halt model and active recovery influence. ChatGPT gave the legacy OpRegion mental model and incorrectly denied steering/recovery behavior. GPT-5.5 Instant: Bad: repeats the legacy/wrong mental model that BHV_OpRegionV24 is only a safety monitor and denies the documented V24 recovery/steering behavior. |
| D07 | Viewer Image / Geodesy Config | 2 | 2 | 2 | 1 | 2 | none | NotebookLM and ChatGPT gave strong viewer/image/datum checks; Gemini was also usable. Claude identified the right general issue but placed datum settings in questionable app blocks and used imprecise viewer parameter framing. |
| D08 | pShare Configuration | 2 | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM and ChatGPT gave the cleanest pShare routing model. Claude mostly answered with pMOOSBridge syntax. Gemini had the right idea but used an inaccurate pShare output syntax for an exact-docs prompt. |
| D09 | uField Broker Comparison | 2 | 2 | 2 | 1 | 2 | none | NotebookLM, ChatGPT, and Gemini gave a usable comparison of brokers, pShare bridging, node comms, and message handling. Claude was broadly useful but overstated node reports and used imprecise bridge terminology. |
| D10 | pLogger And Alog Verification | 2 | 2 | 2 | 2 | 2 | none | All four final stored answers gave a usable pLogger/aloggrep/alogview verification workflow. |
| D11 | Stale nsplug Generated Files | 2 | 2 | 2 | 2 | 2 | none | All four answers correctly identified the template-to-target-file workflow: inspect generated targ_/target .moos/.bhv files, rerun nsplug after template or launch-argument changes, and verify that pAntler is launching the regenerated file. |
| D12 | pMarineViewer Action Buttons | 2 | 1 | 2 | 1 | 1 | ChatGPT, Claude, Gemini | NotebookLM gave the documented button_one/button_two style. ChatGPT, Claude, and Gemini explained the right control variables but used wrong or nonstandard exact button syntax (`action =`, var/sval forms, or `BUTTON =`), so their answers would need correction before copying. |
| D13 | uXMS vs uQueryDB vs uPokeDB | 2 | 2 | 2 | 2 | 2 | none | All four answers separated live scoping/observation, one-shot or condition-oriented querying, and active poking well enough for a student debugging a running MOOSDB. |
| D14 | pNodeReporter Local vs Shared Reports | 2 | 2 | 2 | 1 | 2 | Claude | NotebookLM, ChatGPT, and Gemini correctly centered NODE_REPORT_LOCAL as the local ownship report and NODE_REPORT as the shared/received report. Claude gave useful topology advice but incorrectly stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally. |
| D15 | BHV_Loiter vs BHV_StationKeep | 2 | 2 | 2 | 2 | 2 | none | All four answers gave a useful distinction between continuous polygon loitering and point/radius station keeping, with enough parameters and symptoms to guide a lab student. |
| K01 | pOdometry Mail Handling | 2 | 2 | 2 | 2 | 2 | none | All four answers separated mail/state updates from Iterate-time publication well enough for a pOdometry-style app. |
| K02 | Missing Registration Pattern | 2 | 2 | 2 | 2 | 2 | none | All four answers gave a usable reconnect-safe registration pattern, with registration repeated from OnConnectToServer or the local RegisterVariables helper. |
| K03 | AppCasting Config Warnings | 1 | 2 | 2 | 1 | 1 | Gemini | ChatGPT gave the cleanest AppCasting/startup pattern. NotebookLM, Claude, and Gemini were partially useful but missed or weakened the reconnect registration point or used nonstandard warning API language. |
| K04 | uTimerScript Trigger Setup | 2 | 2 | 2 | 1 | 1 | none | NotebookLM and ChatGPT gave robust timed-post/debugging advice. Claude and Gemini were useful but more generic and included less reliable trigger/config details. |
| K05 | Behavior Config File Boundary | 2 | 2 | 2 | 2 | 2 | none | All four correctly identified that behavior blocks belong in the .bhv behavior file, while pHelmIvP is launched/configured from the .moos mission file. |
| K06 | pShare Route Config | 2 | 1 | 1 | 2 | 2 | ChatGPT, ChatGPT 5.5 Instant | NotebookLM, Claude, and Gemini gave usable pShare host/port/name guidance. ChatGPT incorrectly framed the destination as the shoreside MOOSDB ServerPort rather than the receiving pShare port. GPT-5.5 Instant: Partial: correctly identifies localhost/source-variable/name issues, but incorrectly says the route should target the shoreside MOOSDB ServerPort rather than the receiving pShare route/input port. |
| K07 | Inter-Vehicle Message Payload | 2 | 2 | 0 | 0 | 0 | Claude, Gemini, ChatGPT 5.5 Instant | NotebookLM and ChatGPT correctly used NODE_MESSAGE_LOCAL with src_node, dest_node, var_name, and quoted string_val. Claude replaced the documented field names with wrong moos_var/moos_string fields. Gemini recommended direct VISIT_POINT publishing rather than the inter-vehicle envelope. GPT-5.5 Instant: Bad: the first line repeats the documented dest_node form, but the answer then explicitly says to replace it with dests=bravo, which is not the documented NODE_MESSAGE field. |
| K08 | `setParam()` Pattern | 2 | 1 | 1 | 2 | 2 | ChatGPT, ChatGPT 5.5 Instant | NotebookLM, Claude, and Gemini preserved base-class setParam delegation. ChatGPT validated the custom parameter but its code returned false instead of delegating to IvPBehavior::setParam for standard behavior parameters. GPT-5.5 Instant: Partial: lowercases and validates the custom parameter, but returns false for unhandled parameters instead of delegating to IvPBehavior::setParam for standard behavior parameters. |
| K09 | `addInfoVars()` / InfoBuffer | 2 | 2 | 2 | 1 | 0 | Claude, Gemini | NotebookLM and ChatGPT gave the normal addInfoVars plus getBufferDoubleVal ok-flag pattern. Claude had the right calls but wrong behavior lifecycle framing. Gemini answered as BehaviorTree.CPP, not MOOS-IvP. |
| K10 | ZAIC Speed Function | 2 | 2 | 1 | 2 | 0 | Gemini, ChatGPT 5.5 Instant | NotebookLM, ChatGPT, and Claude corrected the normal ZAIC_PEAK pattern with m_domain and setPWT. Gemini omitted the IvP domain and priority weight and invented an unsupported ZAIC method. GPT-5.5 Instant: Partial: adds ZAIC shaping and setPWT, but the corrected code still uses ZAIC_PEAK zaic("speed") instead of ZAIC_PEAK zaic(m_domain, "speed"), so it is not a valid normal MOOS-IvP pattern. |
| K11 | MOOS Reconnect Registration | 2 | 2 | 2 | 2 | 2 | none | All four answers identified that registrations need to be repeated from OnConnectToServer or a shared registerVariables helper called on reconnect. |
| K12 | Regenerating nsplug Targets | 2 | 2 | 2 | 2 | 2 | none | All four answers correctly explained that pAntler reads the generated target file and that nsplug must be rerun after editing meta_ templates or launch arguments. |
| K13 | Deploy Button Missing Helm Release | 2 | 2 | 2 | 2 | 2 | none | All four answers identified the need to post DEPLOY=true and release MOOS_MANUAL_OVERRIDE=false, then check DEPLOY, MOOS_MANUAL_OVERRIDE, helm state, and behavior outputs in uXMS/uHelmScope. |
| K14 | BHV_Waypoint Update Variable Mismatch | 2 | 2 | 2 | 2 | 2 | none | All four answers correctly found the mismatch between Notify("WPT_UPDATE", ...) and updates = WAYPOINT_UPDATES, and explained that the posted variable name must match the behavior updates parameter. |
| K15 | Two-Vehicle Community/Port Collision | 2 | 2 | 2 | 2 | 1 | Gemini | NotebookLM, ChatGPT, and Claude gave the clean unique-community/unique-MOOSDB-port correction. Gemini got that core correction but added a misleading pShare/port mental model, so it was only partial. |
