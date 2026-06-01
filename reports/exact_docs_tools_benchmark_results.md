# Exact Documentation / Tool Benchmark Results

Status: complete for D01-D15; NotebookLM D02 uses user-approved retry replacement.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points.

## Headline Scores

| Model | Score % | Avg / 2 | Good Answers | Partial Answers | Bad Answers | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 100.0% | 2.00 | 15/15 (100.0%) | 0/15 (0.0%) | 0/15 (0.0%) | 0 |
| ChatGPT | 90.0% | 1.80 | 13/15 (86.7%) | 1/15 (6.7%) | 1/15 (6.7%) | 0 |
| Claude | 60.0% | 1.20 | 6/15 (40.0%) | 6/15 (40.0%) | 3/15 (20.0%) | 0 |
| Gemini | 90.0% | 1.80 | 12/15 (80.0%) | 3/15 (20.0%) | 0/15 (0.0%) | 0 |

## Interpretation

NotebookLM TA remains strongest in the exact documentation/tool section after expanding from 10 to 15 prompts. The expansion exposed a useful distinction: general models often knew the broad MOOS-IvP concept, but were more likely to invent or substitute exact pMarineViewer syntax. NotebookLM preserved the correct documented syntax more consistently.

## Replacement Note

NotebookLM's first D02 answer was `The system was unable to answer.` The immediate retry produced a correct answer and, at the user's request, is treated as the replacement primary score. The original first-pass response is preserved in `benchmark_runs/2026-05-31_organic_beginner_tier_clean2/retries/D02_notebook_retry_replacement.json` and in `raw/D02.json` under `replacement_for`.

## Hard/Notable Error Details

These details are kept for audit, not as a headline scoring column. They may overlap with partial or bad answers.

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| D01 | Claude | Off-domain ROS answer | Answered with ROS /odom, /joint_states, /imu/data topics instead of MOOS-IvP pOdometry variables. |
| D02 | Claude | Wrong pAntler launch framing | Treated generic ProcessConfig = AppName blocks as launch selectors; pAntler launch commands come from the ANTLER process configuration Run lines. |
| D05 | Claude | Non-answer | Asked for the .bhv file instead of answering the actual BHV_Waypoint parameter question. |
| D06 | ChatGPT | Wrong behavior semantics | Confidently described BHV_OpRegionV24 as only a safety monitor and denied the V24 recovery/steering objective behavior. |
| D08 | Claude | Wrong bridge/tool syntax | Answered primarily with pMOOSBridge SHARE syntax instead of the pShare configuration requested. |
| D08 | Gemini | Inaccurate pShare syntax | Used a nonstandard src_var/colon route form for pShare output in an exact syntax-oriented answer. |
| D10 | Claude | Non-answer | Declined to answer and asked for context despite the prompt naming pLogger, aloggrep, and alogview. |
| D12 | ChatGPT | Wrong pMarineViewer button syntax | Used `action = ...` as the button syntax instead of the documented button_one/button_two action-button parameters. |
| D12 | Claude | Wrong pMarineViewer button syntax | Used a var/sval button form that does not match the documented pMarineViewer button_one/button_two syntax. |
| D12 | Gemini | Wrong pMarineViewer button parameter | Used a generic `BUTTON = ...` parameter instead of the documented numbered button parameters. |
| D14 | Claude | Wrong NODE_REPORT_LOCAL publication framing | Stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally, weakening the local-vs-shared report distinction. |

## Prompt-by-Prompt Results

| ID | Prompt Short Name | NotebookLM | ChatGPT | Claude | Gemini | Hard/Notable Details | Notes |
|---|---|---:|---:|---:|---:|---|---|
| D01 | pOdometry Variables | 2 | 2 | 0 | 1 | Claude | NotebookLM and ChatGPT gave the expected NAV_X/NAV_Y to ODOMETRY_DIST path; Claude answered as ROS odometry; Gemini mixed MOOS-IvP with generic robotics/ROS signals. |
| D02 | pAntler Process Launching | 2 | 2 | 1 | 2 | Claude | NotebookLM retry replacement, ChatGPT, and Gemini correctly centered ProcessConfig = ANTLER and Run lines. The first NotebookLM pass returned only “The system was unable to answer,” but the user requested treating the immediate retry as the primary result. Claude was useful but framed launch discovery around generic ProcessConfig = AppName blocks instead of the ANTLER launch block. |
| D03 | uTimerScript Usage | 2 | 2 | 2 | 2 | none | All four answers gave a usable uTimerScript mental model: timed MOOS posts for initialization, triggers, simulation proxies, and checks in uXMS. |
| D04 | Helm Deploy Variables | 2 | 2 | 2 | 2 | none | All four answers correctly described DEPLOY, MOOS_MANUAL_OVERRIDE, and helm state gating for autonomous behavior. |
| D05 | BHV_Waypoint Params | 2 | 2 | 0 | 2 | Claude | NotebookLM, ChatGPT, and Gemini rejected the invented parameter and identified capture_radius/radius, slip_radius/nm_radius, and capture_line. Claude did not answer without an uploaded file. |
| D06 | BHV_OpRegionV24 Semantics | 2 | 0 | 2 | 2 | ChatGPT | NotebookLM, Claude, and Gemini described the V24 core/save/halt model and active recovery influence. ChatGPT gave the legacy OpRegion mental model and incorrectly denied steering/recovery behavior. |
| D07 | Viewer Image / Geodesy Config | 2 | 2 | 1 | 2 | none | NotebookLM and ChatGPT gave strong viewer/image/datum checks; Gemini was also usable. Claude identified the right general issue but placed datum settings in questionable app blocks and used imprecise viewer parameter framing. |
| D08 | pShare Configuration | 2 | 2 | 1 | 1 | Claude, Gemini | NotebookLM and ChatGPT gave the cleanest pShare routing model. Claude mostly answered with pMOOSBridge syntax. Gemini had the right idea but used an inaccurate pShare output syntax for an exact-docs prompt. |
| D09 | uField Broker Comparison | 2 | 2 | 1 | 2 | none | NotebookLM, ChatGPT, and Gemini gave a usable comparison of brokers, pShare bridging, node comms, and message handling. Claude was broadly useful but overstated node reports and used imprecise bridge terminology. |
| D10 | pLogger And Alog Verification | 2 | 2 | 0 | 2 | Claude | NotebookLM, ChatGPT, and Gemini gave a usable alog/pLogger verification workflow. Claude declined to answer without additional context. |
| D11 | Stale nsplug Generated Files | 2 | 2 | 2 | 2 | none | All four answers correctly identified the template-to-target-file workflow: inspect generated targ_/target .moos/.bhv files, rerun nsplug after template or launch-argument changes, and verify that pAntler is launching the regenerated file. |
| D12 | pMarineViewer Action Buttons | 2 | 1 | 1 | 1 | ChatGPT, Claude, Gemini | NotebookLM gave the documented button_one/button_two style. ChatGPT, Claude, and Gemini explained the right control variables but used wrong or nonstandard exact button syntax (`action =`, var/sval forms, or `BUTTON =`), so their answers would need correction before copying. |
| D13 | uXMS vs uQueryDB vs uPokeDB | 2 | 2 | 2 | 2 | none | All four answers separated live scoping/observation, one-shot or condition-oriented querying, and active poking well enough for a student debugging a running MOOSDB. |
| D14 | pNodeReporter Local vs Shared Reports | 2 | 2 | 1 | 2 | Claude | NotebookLM, ChatGPT, and Gemini correctly centered NODE_REPORT_LOCAL as the local ownship report and NODE_REPORT as the shared/received report. Claude gave useful topology advice but incorrectly stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally. |
| D15 | BHV_Loiter vs BHV_StationKeep | 2 | 2 | 2 | 2 | none | All four answers gave a useful distinction between continuous polygon loitering and point/radius station keeping, with enough parameters and symptoms to guide a lab student. |
