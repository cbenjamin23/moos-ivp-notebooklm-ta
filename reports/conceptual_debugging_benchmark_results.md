# Conceptual/Debugging Benchmark Results

Status: complete for C01-C30 only. The exact documentation/tool and code/config categories are still incomplete because NotebookLM hit its daily chat quota at D03.

Run: `2026-05-31_organic_beginner_tier_clean2`

Grading method: Manual Codex review against the simple rubric in BENCHMARKING.md, revised to penalize concrete hallucinations, invented MOOS-IvP details, wrong copy-pasteable config snippets, and unsupported product-specific claims even when the surrounding answer was useful.

## Summary

Under the hallucination-sensitive `0/1/2` rubric, NotebookLM TA now leads the completed conceptual/debugging category. The earlier coarse pass treated all broadly useful answers as `2`; this revision drops answers to `1` when they include concrete wrong MOOS-IvP details a student might copy, such as an incorrect pAntler launch block or invented Heron interface app names.

NotebookLM remained clean across C01-C30. ChatGPT was still very strong, but lost credit on two prompts for plausible-looking wrong `ProcessConfig = pAntler` examples. Gemini was usually helpful but had several off-domain or invented-detail failures. Claude had the most reliability issues, including stale-context answers and unsupported MOOS-adjacent details.

## Headline Metrics

| Model | Avg Score | Good Answers | Partial Answers | Bad Answers | Hard Failures | Tied Top Prompts |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 2.00 | 30/30 (100.0%) | 0/30 (0.0%) | 0/30 (0.0%) | 0/30 (0.0%) | 30/30 |
| ChatGPT | 1.93 | 28/30 (93.3%) | 2/30 (6.7%) | 0/30 (0.0%) | 2/30 (6.7%) | 28/30 |
| Gemini | 1.60 | 20/30 (66.7%) | 8/30 (26.7%) | 2/30 (6.7%) | 5/30 (16.7%) | 20/30 |
| Claude | 1.20 | 11/30 (36.7%) | 14/30 (46.7%) | 5/30 (16.7%) | 8/30 (26.7%) | 11/30 |

## Ranking

1. NotebookLM TA: averaged 2.00 with no partial answers and no hard failures.
2. ChatGPT: averaged 1.93; still high quality, but the stricter pass found two wrong copy-pasteable pAntler config examples.
3. Gemini: averaged 1.60; useful on many prompts, but less reliable on MOOS-specific deployment and messaging details.
4. Claude: averaged 1.20; several answers were generic, stale, or contained invented MOOS-adjacent details.

Interpretation: for the intended conceptual TA use case, the current NotebookLM source set is competitive with normal beginner-tier AI tools and shows lower hallucination risk on this MOOS-IvP lab-grounded prompt set. This completed category still does not support marketing the notebook as a coding helper.

## Notable Revision Changes

| Prompt | Model | Change | Reason |
|---|---|---:|---|
| C04 | Claude | 2 -> 1 | Mostly useful lifecycle advice, but included a misleading upstream NAV publisher example. |
| C05 | Gemini | 2 -> 1 | Useful pAntler debugging shape, but wrong ProcessConfig = pAntler launch-block framing. |
| C21 | Gemini | 2 -> 1 | Useful deployment framing, but invented/unsupported Heron interface app names. |
| C27 | ChatGPT | 2 -> 1 | Useful pLogger advice, but wrong ProcessConfig = pAntler example. |
| C27 | Claude | 2 -> 1 | Useful checklist mixed with unsupported pLogger filtering/subscription claims. |
| C30 | ChatGPT | 2 -> 1 | Useful triage answer, but repeated wrong ProcessConfig = pAntler example. |

## Hard Failures

| Prompt | Model | Failure Type | Explanation |
|---|---|---|---|
| C05 | Claude | Wrong pAntler configuration block framing | Suggested looking for ProcessConfig = pAntler around launch entries; the pAntler launch list is read from the ANTLER/Antler process configuration block. |
| C05 | Gemini | Wrong pAntler configuration block framing | Told the user to look for Run lines inside ProcessConfig = pAntler; the pAntler launch block should be ANTLER/Antler, making the answer useful but copy-paste risky. |
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

## Prompt Scores

Scoring: `2` = good and clean, `1` = partially useful or hallucination-tainted, `0` = bad.

| ID | Prompt | NotebookLM | ChatGPT | Claude | Gemini | Hard Failures | Grading Note |
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
| C15 | Multi-Machine Networking Problem | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave good multi-machine host/port/firewall/pShare guidance; Claude was useful but used some imprecise MOOS_SERVER_HOST-style framing. |
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

## What This Supports

This completed category supports the narrow product claim: the NotebookLM notebook is a useful conceptual/debugging TA for students working through MOOS-IvP labs. The hallucination-sensitive revision strengthens that claim relative to ChatGPT for this category, because NotebookLM avoided the copy-pasteable MOOS-IvP configuration hallucinations found in the general LLM outputs. It does not yet support claims about exact parameter lookup or code/config correction, because those sections are not complete.
