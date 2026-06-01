# Hallucination Sweep Notes

Scope: captured raw outputs in `benchmark_runs/2026-05-31_organic_beginner_tier_clean2/raw/`.

The sweep searched for wrong copy-pasteable MOOS config, invented MOOS/PABLO app names, off-domain robotics frameworks, unsupported viewer/geodesy parameters, questionable pLogger claims, and stale-context answers.

## Material Conceptual Findings

| Prompt | Model | Disposition | Note |
|---|---|---|---|
| C05 | Claude | Counted | Wrong pAntler launch-block framing around `ProcessConfig = pAntler`; docs show pAntler reads `Run` entries from `ProcessConfig=ANTLER`/`Antler`. |
| C05 | Gemini | Counted | Same wrong `ProcessConfig = pAntler` launch-block framing. |
| C15 | Claude | Counted | Introduced `MOOS_SERVER_HOST` as if it were a `.moos` setting; the relevant mission-file setting is `ServerHost`. |
| C21 | Claude | Counted | Invented or unsupported Heron/PABLO interface app names. |
| C21 | Gemini | Counted | Invented or unsupported `iHeron`/`iClearpath` Heron interface app names. |
| C27 | ChatGPT | Counted | Wrong `ProcessConfig = pAntler` launch-block example. |
| C27 | Claude | Counted | Mixed useful pLogger advice with unsupported/imprecise filtering claims. |
| C29 | Claude | Counted | Invented `BackgroundFileX`/`BackgroundFileY`/`BackgroundFileScale`-style viewer parameters. |
| C30 | ChatGPT | Counted | Repeated wrong `ProcessConfig = pAntler` launch-block example. |

## Non-Material Or Already Reflected

| Prompt | Model | Disposition | Note |
|---|---|---|---|
| C02 | Claude | Already reflected | Generic robotics/ROS artifacts contributed to the existing partial score. |
| C04 | Claude | Already reflected | Mostly useful app lifecycle advice, but a misleading `iGPS`-style upstream NAV example contributed to the partial score. |
| C06 | Claude | Already reflected | Generic ROS-like launch advice contributed to the partial score. |
| C06 | Gemini | Already reflected | Off-domain framework answer already scored `0` with a hard/notable error. |
| C08 | Claude | Already reflected | Wrong `pHelmIVP` casing/config precision contributed to the partial score. |
| C16 | Gemini | Already reflected | Generic messaging/framework drift contributed to the partial score. |
| C17 | Claude | Already reflected | Generic multi-middleware framing contributed to the partial score. |
| C17 | Gemini | Already reflected | Off-domain V2X/ROS/MQTT answer already scored `0` with a hard/notable error. |
| C22 | Claude | Already reflected | Generic ROS/Gazebo deployment checklist already scored `0` with a hard/notable error. |
| C22 | Gemini | Already reflected | Generic drone/autopilot deployment checklist already flagged. |
| C25 | NotebookLM TA | Not counted | The scanner hit wording about swimmer reports; the answer remained on-topic. |
| C27 | NotebookLM TA | Not counted | `AsyncLog` and `WildCardLogging` advice is supported by the pLogger source PDF. |
| C27 | Gemini | Not counted | `AsyncLog` and `WildCardLogging` advice is supported by the pLogger source PDF. |

## Captured But Ungraded Category Notes

D01-D02 were captured before NotebookLM quota stopped the exact-docs category, but the category remains ungraded until the full section is captured.

| Prompt | Model | Note |
|---|---|---|
| D01 | Claude | Off-domain ROS `/odom`, `/cmd_vel`, `ros2 topic`, and Gazebo framing. |
| D01 | Gemini | Mixed MOOS-IvP with ROS/ROS2 odometry tooling. |

These D-section observations should be reviewed again when the exact documentation/tool category is completed and graded.

## 2026-06-01 Strict Source/Docs Audit Pass

Ground truth for this pass was the local MOOS-IvP source tree plus upstream/curated MOOS-IvP documentation. The pass downgraded useful answers when they contained concrete copy-paste-risk MOOS-IvP errors such as wrong pShare syntax, wrong `NODE_REPORT_LOCAL` framing, wrong pAntler block names, or incorrect process responsibilities.

| Prompt | Model | Counted Issue |
|---|---|---|
| C10 | Gemini | Nonstandard pShare output syntax: Gave the right unique-port/community mental model, but used arrow-style pShare output examples rather than the documented `output = src_name=..., dest_name=..., route=...` form. |
| C11 | Claude | Nonstandard pShare/viewer config syntax: Used `SHARE = ...`/LISTEN-style pShare syntax and an uppercase `STALE_REPORT_THRESH`; source examples use pShare input/output routes and pMarineViewer `stale_report_thresh`. |
| C11 | Gemini | Wrong pShare route syntax/port model: Used an arrow-style pShare output example and said the route port should match the shoreside MOOSDB `ServerPort`; it should target the receiving pShare input route port. |
| C11 | ChatGPT 5.5 Low CLI | Wrong NODE_REPORT_LOCAL framing: Useful checklist, but repeatedly framed the vehicle-side source as `NODE_REPORT`; pNodeReporter normally publishes `NODE_REPORT_LOCAL`, which is then shared as `NODE_REPORT`. |
| C12 | ChatGPT 5.5 Thinking | Wrong NODE_REPORT_LOCAL framing: Useful pShare boundary advice, but it repeatedly described the vehicle-local report as `NODE_REPORT` rather than the normal `NODE_REPORT_LOCAL -> NODE_REPORT` sharing pattern. |
| C12 | Claude | Nonstandard pShare syntax and report-source framing: Used `[SHARE]`/arrow-style route examples and treated `NODE_REPORT` as the vehicle-side source instead of the normal `NODE_REPORT_LOCAL` source. |
| C20 | Gemini | Wrong pNodeReporter output role: Mostly useful tracing workflow, but listed pNodeReporter as the tool to check `DESIRED_THRUST`, `DESIRED_RUDDER`, or `DESIRED_SPEED`; those are helm/PID/control-path variables, not pNodeReporter outputs. |
| D11 | ChatGPT 5.5 Thinking | Wrong pAntler configuration block phrase: Correct stale-nsplug workflow overall, but told the user to inspect `ProcessConfig = pAntler`; pAntler launch `Run` lines live under the `ProcessConfig = ANTLER` block. |
| K06 | Claude | Incomplete NODE_REPORT_LOCAL source correction: Correctly explained host/port matching to the receiving pShare input route, but left the source as `NODE_REPORT` instead of correcting the vehicle-side source to `NODE_REPORT_LOCAL`. |
| K06 | Gemini | Incomplete NODE_REPORT_LOCAL source correction: Correctly targeted the receiving pShare input port, but left `src_name = NODE_REPORT` in the corrected line and only mentioned `NODE_REPORT_LOCAL` as a caveat. |
