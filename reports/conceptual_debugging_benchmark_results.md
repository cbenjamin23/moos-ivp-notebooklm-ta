# Conceptual / Debugging Benchmark Results

Status: complete for C01-C30; user-approved recaptures are treated as primary stored answers. GPT-5.5 Instant is scored as a separate model from the original ChatGPT Thinking run.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points. Concrete hallucinations and invalid copy-pasteable MOOS-IvP details are penalized even when the surrounding answer is useful.

## Headline Scores

| Model | Score % | Avg / 2 | Good Answers | Partial Answers | Bad Answers | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 100.0% | 2.00 | 30/30 (100.0%) | 0/30 (0.0%) | 0/30 (0.0%) | 0 |
| ChatGPT 5.5 Thinking | 96.7% | 1.93 | 28/30 (93.3%) | 2/30 (6.7%) | 0/30 (0.0%) | 0 |
| ChatGPT 5.5 Instant | 95.0% | 1.90 | 27/30 (90.0%) | 3/30 (10.0%) | 0/30 (0.0%) | 0 |
| Claude | 65.0% | 1.30 | 12/30 (40.0%) | 15/30 (50.0%) | 3/30 (10.0%) | 0 |
| Gemini | 80.0% | 1.60 | 20/30 (66.7%) | 8/30 (26.7%) | 2/30 (6.7%) | 0 |

## Interpretation

NotebookLM TA remains first in the conceptual/debugging section. GPT-5.5 Instant is still strong, but the hallucination-focused sweep downgraded answers that gave wrong pShare destination-port or NODE_MESSAGE process ownership details.

## Hard/Notable Error Details

These details are kept for audit, not as a headline scoring column. They may overlap with partial or bad answers.

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

## Prompt-by-Prompt Results

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
