# Exact Documentation / Tool Benchmark Results

Run folder: `benchmark_runs/main_benchmark`

Scores use the canonical `0/1/2` rubric in `SCORING_RUBRIC.md`; hallucinations and invalid MOOS-IvP-specific syntax are penalized.

## Scores

| Model | Score % | Avg / 2 | Good | Partial | Bad | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 100.0% | 2.00 | 15/15 | 0/15 | 0/15 | 0 |
| ChatGPT 5.5 Thinking | 86.7% | 1.73 | 12/15 | 2/15 | 1/15 | 0 |
| ChatGPT 5.5 Instant | 93.3% | 1.87 | 14/15 | 0/15 | 1/15 | 0 |
| ChatGPT 5.5 Low CLI | 80.0% | 1.60 | 10/15 | 4/15 | 1/15 | 0 |
| Gemini | 90.0% | 1.80 | 12/15 | 3/15 | 0/15 | 0 |
| Claude | 73.3% | 1.47 | 8/15 | 6/15 | 1/15 | 0 |

## Hard/Notable Error Details

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| D01 | Claude | Off-domain ROS answer | Answered with ROS /odom, /joint_states, /imu/data topics instead of MOOS-IvP pOdometry variables. |
| D02 | Claude | Wrong pAntler launch framing | Treated generic ProcessConfig = AppName blocks as launch selectors; pAntler launch commands come from the ANTLER process configuration Run lines. |
| D06 | ChatGPT 5.5 Thinking | Wrong behavior semantics | Confidently described BHV_OpRegionV24 as only a safety monitor and denied the V24 recovery/steering objective behavior. |
| D08 | Claude | Wrong bridge/tool syntax | Answered primarily with pMOOSBridge SHARE syntax instead of the pShare configuration requested. |
| D08 | Gemini | Inaccurate pShare syntax | Used a nonstandard src_var/colon route form for pShare output in an exact syntax-oriented answer. |
| D12 | ChatGPT 5.5 Thinking | Wrong pMarineViewer button syntax | Used `action = ...` as the button syntax instead of the documented button_one/button_two action-button parameters. |
| D12 | Claude | Wrong pMarineViewer button syntax | Used a var/sval button form that does not match the documented pMarineViewer button_one/button_two syntax. |
| D12 | Gemini | Wrong pMarineViewer button parameter | Used a generic `BUTTON = ...` parameter instead of the documented numbered button parameters. |
| D14 | Claude | Wrong NODE_REPORT_LOCAL publication framing | Stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally, weakening the local-vs-shared report distinction. |
| D06 | ChatGPT 5.5 Instant | Wrong behavior semantics | Described BHV_OpRegionV24 as only a safety/constraint monitor and denied the V24 recovery/steering behavior. |
| D02 | ChatGPT 5.5 Low CLI | Invented/misspelled executable name | Used `pNodeReport` in an exact pAntler launch example; the app is `pNodeReporter`. |
| D05 | ChatGPT 5.5 Low CLI | Invented BHV_Waypoint parameter | Listed `capture_line_radius`, which is not parsed by BHV_Waypoint source. |
| D06 | ChatGPT 5.5 Low CLI | Wrong behavior semantics | Described BHV_OpRegionV24 as only a constraint/watchdog and denied the documented V24 save-poly recovery objective function. |
| D08 | ChatGPT 5.5 Low CLI | Wrong pShare destination port model | Said pShare remote host/port is usually the other community MOOSDB host/port; output routes should target the receiving pShare input/route port. |
| D14 | ChatGPT 5.5 Low CLI | Wrong pNodeReporter default output framing | Said pNodeReporter normally publishes NODE_REPORT; source defaults to NODE_REPORT_LOCAL. |
| D11 | ChatGPT 5.5 Thinking | Wrong pAntler configuration block phrase | Correct stale-nsplug workflow overall, but told the user to inspect `ProcessConfig = pAntler`; pAntler launch `Run` lines live under the `ProcessConfig = ANTLER` block. |

## Prompt-by-Prompt Results

| ID | Prompt Short Name | NotebookLM TA | ChatGPT 5.5 Thinking | ChatGPT 5.5 Instant | ChatGPT 5.5 Low CLI | Gemini | Claude | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| D01 | pOdometry Variables | 2 | 2 | 2 | 2 | 1 | 0 | NotebookLM and ChatGPT gave the expected NAV_X/NAV_Y to ODOMETRY_DIST path; Claude answered as ROS odometry; Gemini mixed MOOS-IvP with generic robotics/ROS signals. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D02 | pAntler Process Launching | 2 | 2 | 2 | 1 | 2 | 1 | NotebookLM retry replacement, ChatGPT, and Gemini correctly centered ProcessConfig = ANTLER and Run lines. The first NotebookLM pass returned only “The system was unable to answer,” but the user requested treating the immediate retry as the primary result. Claude was useful but framed launch discovery around generic ProcessConfig = AppName blocks instead of the ANTLER launch block. ChatGPT 5.5 Low CLI: Partial: correctly explains ANTLER `Run = ...` launch lines and registration, but includes an invented/misspelled `pNodeReport` executable in the exact pAntler example. |
| D03 | uTimerScript Usage | 2 | 2 | 2 | 2 | 2 | 2 | All four answers gave a usable uTimerScript mental model: timed MOOS posts for initialization, triggers, simulation proxies, and checks in uXMS. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D04 | Helm Deploy Variables | 2 | 2 | 2 | 2 | 2 | 2 | All four answers correctly described DEPLOY, MOOS_MANUAL_OVERRIDE, and helm state gating for autonomous behavior. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D05 | BHV_Waypoint Params | 2 | 2 | 2 | 1 | 2 | 2 | All four final stored answers rejected the invented magic_arrival_radius parameter and identified real BHV_Waypoint arrival/capture parameters such as capture_radius/radius and slip_radius/nm_radius. ChatGPT 5.5 Low CLI: Partial: correctly rejects `magic_arrival_radius` and names real BHV_Waypoint parameters such as `capture_radius`, `slip_radius`/`nm_radius`, `capture_line`, `lead`, and `lead_damper`, but also invents `capture_line_radius` as a parameter. |
| D06 | BHV_OpRegionV24 Semantics | 2 | 0 | 0 | 0 | 2 | 2 | NotebookLM, Claude, and Gemini described the V24 core/save/halt model and active recovery influence. ChatGPT gave the legacy OpRegion mental model and incorrectly denied steering/recovery behavior. GPT-5.5 Instant: Bad: repeats the legacy/wrong mental model that BHV_OpRegionV24 is only a safety monitor and denies the documented V24 recovery/steering behavior. ChatGPT 5.5 Low CLI: Bad: repeats the legacy mental model that BHV_OpRegionV24 is only a monitor/constraint behavior and denies the V24 save-poly recovery objective function shown in source. |
| D07 | Viewer Image / Geodesy Config | 2 | 2 | 2 | 2 | 2 | 1 | NotebookLM and ChatGPT gave strong viewer/image/datum checks; Gemini was also usable. Claude identified the right general issue but placed datum settings in questionable app blocks and used imprecise viewer parameter framing. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D08 | pShare Configuration | 2 | 2 | 2 | 1 | 1 | 1 | NotebookLM and ChatGPT gave the cleanest pShare routing model. Claude mostly answered with pMOOSBridge syntax. Gemini had the right idea but used an inaccurate pShare output syntax for an exact-docs prompt. ChatGPT 5.5 Low CLI: Partial: useful route/host/variable debugging advice, but says pShare remote host/port is usually the other community MOOSDB host/port; the pShare output route should target the receiving pShare input/route port. |
| D09 | uField Broker Comparison | 2 | 2 | 2 | 2 | 2 | 1 | NotebookLM, ChatGPT, and Gemini gave a usable comparison of brokers, pShare bridging, node comms, and message handling. Claude was broadly useful but overstated node reports and used imprecise bridge terminology. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D10 | pLogger And Alog Verification | 2 | 2 | 2 | 2 | 2 | 2 | All four final stored answers gave a usable pLogger/aloggrep/alogview verification workflow. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D11 | Stale nsplug Generated Files | 2 | 1 | 2 | 2 | 2 | 2 | NotebookLM, Claude, Gemini, GPT-5.5 Instant, and GPT-5.5 Low CLI correctly identified the template-to-target workflow. ChatGPT was useful overall but lost credit for the wrong `ProcessConfig = pAntler` inspection phrase; pAntler launch lines are under `ProcessConfig = ANTLER`. |
| D12 | pMarineViewer Action Buttons | 2 | 1 | 2 | 2 | 1 | 1 | NotebookLM gave the documented button_one/button_two style. ChatGPT, Claude, and Gemini explained the right control variables but used wrong or nonstandard exact button syntax (`action =`, var/sval forms, or `BUTTON =`), so their answers would need correction before copying. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D13 | uXMS vs uQueryDB vs uPokeDB | 2 | 2 | 2 | 2 | 2 | 2 | All four answers separated live scoping/observation, one-shot or condition-oriented querying, and active poking well enough for a student debugging a running MOOSDB. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
| D14 | pNodeReporter Local vs Shared Reports | 2 | 2 | 2 | 1 | 2 | 1 | NotebookLM, ChatGPT, and Gemini correctly centered NODE_REPORT_LOCAL as the local ownship report and NODE_REPORT as the shared/received report. Claude gave useful topology advice but incorrectly stated or implied that pNodeReporter normally publishes NODE_REPORT directly/both locally. ChatGPT 5.5 Low CLI: Partial: explains the local-vs-shared report distinction, but starts by saying pNodeReporter normally publishes `NODE_REPORT`; source defaults to `NODE_REPORT_LOCAL`, with `NODE_REPORT` normally being the shared/received report. |
| D15 | BHV_Loiter vs BHV_StationKeep | 2 | 2 | 2 | 2 | 2 | 2 | All four answers gave a useful distinction between continuous polygon loitering and point/radius station keeping, with enough parameters and symptoms to guide a lab student. ChatGPT 5.5 Low CLI: Good: useful answer with no notable MOOS-IvP-specific error found in the hallucination-sensitive grading pass. |
