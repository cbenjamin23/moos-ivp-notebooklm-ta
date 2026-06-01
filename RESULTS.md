# Benchmark Results

Status: partial results available. The conceptual/debugging category (C01-C30) is complete and has received a hallucination-sensitive revision pass. The exact documentation/tool category is incomplete because NotebookLM hit its daily chat quota at D03. The code/config category has not been run in the clean cross-model benchmark yet.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Detailed conceptual results:

- `reports/conceptual_debugging_benchmark_results.md`
- `reports/conceptual_debugging_benchmark_results.json`

## Executive Summary

For conceptual/debugging prompts based on the MOOS-IvP labs, NotebookLM TA now leads under the hallucination-sensitive `0/1/2` rubric: 2.00/2.00 with no hard failures across C01-C30. ChatGPT remains very strong at 1.93, but lost credit for two plausible-looking wrong `ProcessConfig = pAntler` examples that a beginner might copy into a mission.

The revision matters: the earlier coarse pass only asked whether an answer was broadly useful. This pass also penalizes concrete hallucinations, wrong copy-pasteable config snippets, invented MOOS-IvP app/parameter names, stale-context answers, and unsupported off-domain robotics details. Gemini was often useful but had several MOOS-specific drift problems. Claude had several severe failures caused by poor search/context handling or invented MOOS-adjacent details.

Primary question for the completed category:

> Is the NotebookLM TA competitive with normal beginner-tier AI browser tools for documentation-grounded conceptual MOOS-IvP help?

Answer for C01-C30: yes. On the stricter hallucination-sensitive scoring, it ranks first for the completed conceptual/debugging category.

Secondary question about exact docs and code/config remains open until those categories are complete.

## Headline Results

| Model | Avg Score | Good Answers | Partial Answers | Bad Answers | Hard Failures | Conceptual Avg | Exact Docs Avg | Code Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 2.00 | 30/30 (100.0%) | 0/30 (0.0%) | 0/30 (0.0%) | 0/30 (0.0%) | 2.00 | pending | pending |
| ChatGPT | 1.93 | 28/30 (93.3%) | 2/30 (6.7%) | 0/30 (0.0%) | 2/30 (6.7%) | 1.93 | pending | pending |
| Gemini | 1.60 | 20/30 (66.7%) | 8/30 (26.7%) | 2/30 (6.7%) | 5/30 (16.7%) | 1.60 | pending | pending |
| Claude | 1.20 | 11/30 (36.7%) | 14/30 (46.7%) | 5/30 (16.7%) | 8/30 (26.7%) | 1.20 | pending | pending |

## Category Results

| Category | Prompt Count | NotebookLM TA | ChatGPT | Claude | Gemini | Notes |
|---|---:|---:|---:|---:|---:|---|
| Conceptual/debugging | 30 | 2.00 | 1.93 | 1.20 | 1.60 | Complete; hallucination-sensitive revision pass applied. |
| Exact docs/parameters/tools | 10 | pending | pending | pending | pending | Incomplete; browser run stopped at NotebookLM daily quota on D03. |
| Code advice/correction | 10 | pending | pending | pending | pending | Not yet run in the clean cross-model benchmark. |

## Hard Failures

| Prompt ID | Model | Failure Type | Brief Explanation |
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

## Main Interpretation

The completed conceptual/debugging category supports the narrow product claim that the NotebookLM notebook can serve as a conceptual MOOS-IvP TA for lab students. The stricter revision also gives a reasonable rubric where NotebookLM beats ChatGPT: source-grounded reliability and lower hallucination risk on MOOS-IvP-specific conceptual/debugging prompts.

This does not prove NotebookLM is better at all MOOS-IvP assistance. ChatGPT often produced richer operational checklists and may still be better for broad interactive debugging. The current evidence also does not support marketing the notebook as a coding helper. The code/config section is still pending in the clean cross-model benchmark, and earlier local validation already suggested caution on exact C++ correction.

## Prompt-by-Prompt Results

Scoring:

- `2` = good and clean
- `1` = partially useful, incomplete, or hallucination-tainted
- `0` = bad

| ID | Category | Prompt Short Name | NotebookLM | ChatGPT | Claude | Gemini | Hard Failures | Notes |
|---|---|---|---:|---:|---:|---:|---|---|
| C01 | Conceptual/debugging | Command Not Found After Build | 2 | 2 | 2 | 2 | none | All models identified PATH/build-location checks; Claude was less MOOS-specific but still useful. |
| C02 | Conceptual/debugging | Version Control Before Mission Changes | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave clean Git baseline and generated-file cautions; Claude was useful but drifted into generic robotics/ROS artifacts. |
| C03 | Conceptual/debugging | uXMS/uPokeDB Confusion | 2 | 2 | 2 | 2 | none | All models correctly centered the same-host/same-port/same-variable/uXMS registration debugging path. |
| C04 | Conceptual/debugging | App Not Publishing | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave a usable app lifecycle pipeline. Claude was mostly useful, but lost credit for suggesting pMarinePID/iGPS-style upstream NAV publishers in a way that could mislead a beginner. |
| C05 | Conceptual/debugging | pAntler Did Not Start A Process | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM/ChatGPT gave clean pAntler launch-vs-registration guidance. Claude and Gemini were useful but lost credit for imprecise or wrong ProcessConfig framing; Gemini used ProcessConfig = pAntler for Run lines. |
| C06 | Conceptual/debugging | Launch Arguments Not Reaching Config Files | 2 | 2 | 1 | 0 | Gemini | NotebookLM and ChatGPT directly described launch scripts, templates, generated files, and stale target files; Claude was generic ROS-like but partly useful; Gemini went off-domain. |
| C07 | Conceptual/debugging | Helm Remains PARKED | 2 | 2 | 2 | 1 | none | NotebookLM/ChatGPT/Claude gave correct helm-state/all-stop/deploy-variable diagnostics; Gemini was broadly helpful but less precise about helm state naming. |
| C08 | Conceptual/debugging | No Desired Outputs | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini covered helm state, behavior activation, NAV variables, .moos/.bhv boundaries; Claude had useful checks but wrong pHelmIvP casing and config details. |
| C09 | Conceptual/debugging | Vehicle Moves In Simulation But Autonomy Looks Wrong | 2 | 2 | 2 | 2 | none | All models separated simulator NAV output, helm inputs, behavior conditions, and viewer state well enough. |
| C10 | Conceptual/debugging | Multi-Vehicle Ports | 2 | 2 | 2 | 2 | none | All models correctly explained unique MOOSDB ports, community names, pShare ports/routes, and launch arguments. |
| C11 | Conceptual/debugging | Shoreside Missing Vehicle | 2 | 2 | 2 | 2 | none | All models traced pNodeReporter/NODE_REPORT through vehicle, bridge, shoreside, and viewer well enough. |
| C12 | Conceptual/debugging | pShare Route Confusion | 2 | 2 | 2 | 2 | none | All models gave a reasonable local-vs-shared variable boundary for pShare routes. |
| C13 | Conceptual/debugging | TSP App / Behavior Boundary | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini clearly separated planner output, behavior updates, and BHV_Waypoint steering; Claude was conceptually right but less exact on MOOS update naming. |
| C14 | Conceptual/debugging | Distributed Route Assignment Problem | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were specific to task generation, identities, route updates, and behavior activation; Claude/Gemini were more generic task-allocation answers. |
| C15 | Conceptual/debugging | Multi-Machine Networking Problem | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini gave good multi-machine host/port/firewall/pShare guidance; Claude was useful but used some imprecise MOOS_SERVER_HOST-style framing. |
| C16 | Conceptual/debugging | Message Does Not Arrive | 2 | 2 | 0 | 1 | Claude | NotebookLM/ChatGPT gave the expected NODE_MESSAGE_LOCAL to uField path; Claude did not answer; Gemini gave a generic messaging pipeline with only partial MOOS value. |
| C17 | Conceptual/debugging | Node Names / Destinations | 2 | 2 | 1 | 0 | Gemini | NotebookLM/ChatGPT addressed src_node/dest_node/var_name payload fields; Claude was generic multi-middleware; Gemini was off-domain V2X/ROS/MQTT. |
| C18 | Conceptual/debugging | Behavior Never Runs | 2 | 2 | 2 | 2 | none | All models gave usable behavior-state, condition, pwt, InfoBuffer, update, and uHelmScope guidance. |
| C19 | Conceptual/debugging | `.moos` vs `.bhv` Mistake | 2 | 2 | 2 | 2 | none | All models correctly distinguished .moos app/process config from .bhv behavior config. |
| C20 | Conceptual/debugging | Payload Event Not Affecting Autonomy | 2 | 2 | 2 | 2 | none | All models gave a usable data-path trace from payload publication through MOOSDB into helm conditions/updates/coordinating apps. |
| C21 | Conceptual/debugging | Simulation to Heron/PABLO | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM and ChatGPT gave the cleanest uSimMarine-to-Heron/PABLO transition framing. Claude and Gemini kept some useful safety/architecture points but lost credit for invented or unsupported Heron interface app names. |
| C22 | Conceptual/debugging | Field Deployment Sanity Check | 2 | 2 | 0 | 1 | Claude, Gemini | NotebookLM/ChatGPT were MOOS/PABLO-aware; Claude was generic ROS/Gazebo; Gemini was generic drone/autopilot deployment with little MOOS specificity. |
| C23 | Conceptual/debugging | Rescue Path Planning | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT were most aligned with MOOS rescue planner/route handoff; Claude/Gemini were generic SAR planning but still conceptually useful. |
| C24 | Conceptual/debugging | Adversarial Rescue Updates | 2 | 2 | 1 | 1 | none | NotebookLM/ChatGPT addressed dynamic rescue updates and replanning in the lab style; Claude/Gemini gave generic dynamic task-allocation answers. |
| C25 | Conceptual/debugging | Teammate Messaging | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini understood two-vehicle rescue/uField messaging; Claude asked for context and treated uField as unknown. |
| C26 | Conceptual/debugging | Post-Mission Alog Diagnosis | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini gave aloggrep/alogview/aloghelm-style post-run debugging; Claude returned an unrelated uField clarification from a prior prompt. |
| C27 | Conceptual/debugging | pLogger Produced No Useful Alog | 2 | 1 | 1 | 2 | ChatGPT, Claude | NotebookLM and Gemini gave useful pLogger/path/process guidance. ChatGPT was otherwise strong but used a wrong ProcessConfig = pAntler example; Claude included unsupported pLogger filtering/subscription claims. |
| C28 | Conceptual/debugging | Choosing Debugging Tools During A Mission Run | 2 | 2 | 1 | 2 | none | NotebookLM/ChatGPT/Gemini mapped tools to use cases well; Claude was useful but shallower and slightly imprecise on uQueryDB/pLogger roles. |
| C29 | Conceptual/debugging | pMarineViewer Background / Geodesy | 2 | 2 | 0 | 2 | Claude | NotebookLM/ChatGPT/Gemini covered image files, datum, local coordinates, and viewer config; Claude invented BackgroundFile-style parameter names. |
| C30 | Conceptual/debugging | Mission Broke After Several Edits | 2 | 1 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini gave usable triage order. ChatGPT was useful overall but lost credit for repeating a wrong ProcessConfig = pAntler launch-block example. |
| D01 | Exact docs/parameters/tools | pOdometry Variables | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D02 | Exact docs/parameters/tools | pAntler Process Launching | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D03 | Exact docs/parameters/tools | uTimerScript Usage | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D04 | Exact docs/parameters/tools | Helm Deploy Variables | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D05 | Exact docs/parameters/tools | BHV_Waypoint Params | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D06 | Exact docs/parameters/tools | BHV_OpRegionV24 Semantics | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D07 | Exact docs/parameters/tools | Viewer Image / Geodesy Config | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D08 | Exact docs/parameters/tools | pShare Configuration | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D09 | Exact docs/parameters/tools | uField Broker Comparison | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| D10 | Exact docs/parameters/tools | pLogger And Alog Verification | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K01 | Code advice/correction | pOdometry Mail Handling | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K02 | Code advice/correction | Missing Registration Pattern | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K03 | Code advice/correction | AppCasting Config Warnings | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K04 | Code advice/correction | uTimerScript Trigger Setup | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K05 | Code advice/correction | Behavior Config File Boundary | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K06 | Code advice/correction | pShare Route Config | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K07 | Code advice/correction | Inter-Vehicle Message Payload | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K08 | Code advice/correction | `setParam()` Pattern | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K09 | Code advice/correction | `addInfoVars()` / InfoBuffer | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |
| K10 | Code advice/correction | ZAIC Speed Function | pending | pending | pending | pending | pending | Category incomplete; left ungraded until the full section is captured. |

## Appendix: Grading Method

Each answer receives:

- Score: `0`, `1`, or `2`
- Hard failure: `yes` or `no`
- Short grading note

Score meanings:

- `2`: correct, useful, specific enough, and no notable hallucination or serious caveat
- `1`: mostly helpful, but vague, incomplete, off-domain in places, or includes a concrete factual slip/hallucination that requires correction before use
- `0`: wrong, misleading, non-responsive, stale-context, invented/off-domain in a way likely to waste student time, or unsafe for the task

Hard failure examples used here:

- invented MOOS-IvP utility, app, API, variable, or parameter
- wrong copy-pasteable MOOS configuration snippets
- off-domain ROS/Gazebo/PX4/V2X answer when the prompt was clearly MOOS-IvP-specific
- stale answer from a prior prompt
- no substantive answer
- citation or source claim does not support the answer

## Appendix: Existing Pre-Benchmark Evidence

Existing reports in `reports/` are not the cross-model benchmark, but they motivate the plan:

- `studio_and_stress_report.json`: 20/20 diagnostic stress prompts passed after manual review.
- `code_advice_test_report.json`: 8 pass, 2 caution, 0 fail on code-advice prompts.
- `code_correction_test_report.json`: 1 pass, 2 pass-with-caution, 2 fail on incorrect-code correction prompts.

Interpretation:

- Strong on conceptual/debugging answers.
- Useful but cautious on code architecture.
- Not reliable as an exact C++ correction engine.
