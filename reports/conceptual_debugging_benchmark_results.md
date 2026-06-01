# Conceptual/Debugging Benchmark Results

Status: complete for C01-C30 only. The exact documentation/tool and code/config categories are still incomplete because NotebookLM hit its daily chat quota at D03.

Run: `2026-05-31_organic_beginner_tier_clean2`

Grading method: manual Codex review against the simple rubric in `BENCHMARKING.md`, using preserved raw browser outputs in `benchmark_runs/2026-05-31_organic_beginner_tier_clean2/raw/`. This is a coarse pass/fail/usefulness rubric, not a fine-grained ranking among good answers.

## Summary

Under the coarse `0/1/2` rubric, NotebookLM TA and ChatGPT tied at the top on conceptual/debugging prompts. Both were consistently useful and had no hard failures. NotebookLM's answers were usually more documentation-shaped and concise; ChatGPT's were often more operationally detailed. Gemini was usually good but had several off-domain drifts. Claude had multiple blocking failures where the browser product either searched poorly, asked for context, repeated a stale answer, or invented MOOS-adjacent details.

## Headline Metrics

| Model | Avg Score | Good % | Bad % | Hard Failures | Tied Top Prompts |
|---|---:|---:|---:|---:|---:|
| NotebookLM TA | 2.00 | 100.0% | 0.0% | 0 | 30/30 |
| ChatGPT | 2.00 | 100.0% | 0.0% | 0 | 30/30 |
| Claude | 1.27 | 43.3% | 16.7% | 6 | 13/30 |
| Gemini | 1.67 | 73.3% | 6.7% | 3 | 22/30 |

## Ranking

1. NotebookLM TA and ChatGPT tied: both averaged 2.00 with no hard failures.
2. Gemini: averaged 1.67, usually helpful but less reliable on MOOS-specific naming and deployment context.
3. Claude: averaged 1.27, with several severe off-domain or stale-context failures.

Interpretation: for the intended conceptual TA use case, the current NotebookLM source set is competitive with ChatGPT and clearly stronger than the observed beginner-tier Claude/Gemini runs on MOOS-IvP-specific grounding. The simple rubric is not sensitive enough to choose between NotebookLM and ChatGPT when both are correct.

## Hard Failures

| Prompt | Model | Failure Type | Explanation |
|---|---|---|---|
| C06 | Gemini | Off-domain framework drift | Answered as ROS/ArduPilot/PX4/Gazebo caching rather than MOOS launch/nsplug/generated mission files. |
| C16 | Claude | No substantive answer | Asked clarifying questions instead of walking the NODE_MESSAGE_LOCAL delivery path. |
| C17 | Gemini | Off-domain messaging model | Answered as V2X/ROS/MQTT and missed MOOS NODE_MESSAGE fields. |
| C21 | Claude | Invented/uncertain MOOS-IvP app names | Suggested iGPS/iIMU/pNavManager/iHeron/iActuationKF instead of the documented Heron/PABLO interface framing. |
| C22 | Claude | Off-domain deployment checklist | Generic ROS/Gazebo/CARLA checklist with no MOOS-IvP variable/process specificity. |
| C22 | Gemini | Off-domain deployment checklist | Generic drone/autopilot/PX4-style checklist, only partially transferable to a Heron/PABLO MOOS mission. |
| C25 | Claude | Off-domain clarification | Treated uField as unknown and asked whether this was a game/competition instead of answering the MOOS-IvP setup. |
| C26 | Claude | Wrong prompt context | Repeated the unrelated uField clarification instead of answering the alog diagnosis prompt. |
| C29 | Claude | Invented viewer parameters | Used BackgroundFileX/BackgroundFileY/BackgroundFileScale style parameters rather than the MOOS-IvP TIFF/info/datum configuration model. |

## Prompt Scores

Scoring: `2` = good, `1` = partially useful, `0` = bad.

| ID | Prompt | NotebookLM | ChatGPT | Claude | Gemini | Hard Failures | Grading Note |
|---|---|---:|---:|---:|---:|---|---|
| C01 | Command Not Found After Build | 2 | 2 | 2 | 2 | none | All models identified PATH/build-location checks; Claude was less MOOS-specific but still useful. |
| C02 | Version Control Before Mission Changes | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave clean Git baseline and generated-file cautions; Claude was useful but drifted into generic robotics/ROS artifacts. |
| C03 | uXMS/uPokeDB Confusion | 2 | 2 | 2 | 2 | none | All models correctly centered the same-host/same-port/same-variable/uXMS registration debugging path. |
| C04 | App Not Publishing | 2 | 2 | 2 | 2 | none | All models gave a usable app lifecycle pipeline: register/subscribe, OnNewMail state update, Iterate cadence, Notify, and uXMS checks. |
| C05 | pAntler Did Not Start A Process | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini covered pAntler launch vs MOOSDB registration well; Claude was helpful but had imprecise ProcessConfig/launch terminology. |
| C06 | Launch Arguments Not Reaching Config Files | 2 | 2 | 1 | 0 | Gemini | NotebookLM and ChatGPT directly described launch scripts, templates, generated files, and stale target files; Claude was generic ROS-like but partly useful; Gemini went off-domain. |
| C07 | Helm Remains PARKED | 2 | 2 | 2 | 1 | none | NotebookLM/ChatGPT/Claude gave correct helm-state/all-stop/deploy-variable diagnostics; Gemini was broadly helpful but less precise about helm state naming. |
| C08 | No Desired Outputs | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini covered helm state, behavior activation, NAV variables, .moos/.bhv boundaries; Claude had useful checks but wrong pHelmIvP casing and config details. |
| C09 | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | 2 | 2 | 2 | none | All models separated simulator NAV output, helm inputs, behavior conditions, and viewer state well enough. |
| C10 | Multi-Vehicle Ports | 2 | 2 | 2 | 2 | none | All models correctly explained unique MOOSDB ports, community names, pShare ports/routes, and launch arguments. |
| C11 | Shoreside Missing Vehicle | 2 | 2 | 2 | 2 | none | All models traced pNodeReporter/NODE_REPORT through vehicle, bridge, shoreside, and viewer well enough. |
| C12 | pShare Route Confusion | 2 | 2 | 2 | 2 | none | All models gave a reasonable local-vs-shared variable boundary for pShare routes. |
| C13 | TSP App / Behavior Boundary | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini clearly separated planner output, behavior updates, and BHV_Waypoint steering; Claude was conceptually right but less exact on MOOS update naming. |
| C14 | Distributed Route Assignment Problem | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were specific to task generation, identities, route updates, and behavior activation; Claude/Gemini were more generic task-allocation answers. |
| C15 | Multi-Machine Networking Problem | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave good multi-machine host/port/firewall/pShare guidance; Claude was useful but used some imprecise MOOS_SERVER_HOST-style framing. |
| C16 | Message Does Not Arrive | 2 | 2 | 0 | 1 | Claude | NotebookLM/ChatGPT gave the expected NODE_MESSAGE_LOCAL to uField path; Claude did not answer; Gemini gave a generic messaging pipeline with only partial MOOS value. |
| C17 | Node Names / Destinations | 2 | 2 | 1 | 0 | Gemini | NotebookLM/ChatGPT addressed src_node/dest_node/var_name payload fields; Claude was generic multi-middleware; Gemini was off-domain V2X/ROS/MQTT. |
| C18 | Behavior Never Runs | 2 | 2 | 2 | 2 | none | All models gave usable behavior-state, condition, pwt, InfoBuffer, update, and uHelmScope guidance. |
| C19 | `.moos` vs `.bhv` Mistake | 2 | 2 | 2 | 2 | none | All models correctly distinguished .moos app/process config from .bhv behavior config. |
| C20 | Payload Event Not Affecting Autonomy | 2 | 2 | 2 | 2 | none | All models gave a usable data-path trace from payload publication through MOOSDB into helm conditions/updates/coordinating apps. |
| C21 | Simulation to Heron/PABLO | 2 | 2 | 1 | 2 | Claude | NotebookLM/ChatGPT/Gemini handled uSimMarine-to-Heron/PABLO transition; Claude had good safety framing but invented/uncertain Heron interface app names. |
| C22 | Field Deployment Sanity Check | 2 | 2 | 0 | 1 | Claude, Gemini | NotebookLM/ChatGPT were MOOS/PABLO-aware; Claude was generic ROS/Gazebo; Gemini was generic drone/autopilot deployment with little MOOS specificity. |
| C23 | Rescue Path Planning | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were most aligned with MOOS rescue planner/route handoff; Claude/Gemini were generic SAR planning but still conceptually useful. |
| C24 | Adversarial Rescue Updates | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT addressed dynamic rescue updates and replanning in the lab style; Claude/Gemini gave generic dynamic task-allocation answers. |
| C25 | Teammate Messaging | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini understood two-vehicle rescue/uField messaging; Claude asked for context and treated uField as unknown. |
| C26 | Post-Mission Alog Diagnosis | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini gave aloggrep/alogview/aloghelm-style post-run debugging; Claude returned an unrelated uField clarification from a prior prompt. |
| C27 | pLogger Produced No Useful Alog | 2 | 2 | 2 | 2 | none | All models gave a useful pLogger/pAntler/path/process/config checklist. |
| C28 | Choosing Debugging Tools During A Mission Run | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini mapped tools to use cases well; Claude was useful but shallower and slightly imprecise on uQueryDB/pLogger roles. |
| C29 | pMarineViewer Background / Geodesy | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini covered image files, datum, local coordinates, and viewer config; Claude invented BackgroundFile-style parameter names. |
| C30 | Mission Broke After Several Edits | 2 | 2 | 2 | 2 | none | All models gave usable triage order and artifact requests after mission edits. |

## What This Supports

This completed category supports the narrow product claim: the NotebookLM notebook is a useful conceptual/debugging TA for students working through MOOS-IvP labs. It does not yet support claims about exact parameter lookup or code/config correction, because those sections are not complete.
