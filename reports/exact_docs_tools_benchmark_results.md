# Exact Documentation / Tool Benchmark Results

Status: complete for D01-D10.

Run folder: `benchmark_runs/2026-05-31_organic_beginner_tier_clean2`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; `Score %` is total points divided by possible points.

## Headline Scores

| Model | Score % | Avg / 2 | Good Answers | Partial Answers | Bad Answers | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 90.0% | 1.80 | 9/10 (90.0%) | 0/10 (0.0%) | 1/10 (10.0%) | 0 |
| ChatGPT | 90.0% | 1.80 | 9/10 (90.0%) | 0/10 (0.0%) | 1/10 (10.0%) | 0 |
| Claude | 50.0% | 1.00 | 3/10 (30.0%) | 4/10 (40.0%) | 3/10 (30.0%) | 0 |
| Gemini | 90.0% | 1.80 | 8/10 (80.0%) | 2/10 (20.0%) | 0/10 (0.0%) | 0 |

## Interpretation

NotebookLM TA, ChatGPT, and Gemini were tightly grouped on exact documentation/tool questions, but their failure modes differed. NotebookLM lost one point only because it failed to answer D02. ChatGPT had one serious wrong answer on BHV_OpRegionV24. Gemini was strong overall but lost credit for mixed/off-target pOdometry details and an inaccurate pShare syntax. Claude was much weaker in this section because several answers were off-domain, non-responsive, or framed around the wrong tool/configuration model.

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

## Prompt-by-Prompt Results

| ID | Prompt Short Name | NotebookLM | ChatGPT | Claude | Gemini | Hard/Notable Details | Notes |
|---|---|---:|---:|---:|---:|---|---|
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
