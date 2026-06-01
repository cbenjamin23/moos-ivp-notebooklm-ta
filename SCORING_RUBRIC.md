# Scoring Rubric

This benchmark uses one simple score per answer. Hard/notable errors are retained as audit details, not as a separate public score column.

## Score

| Score | Public Percentage | Label | Meaning |
|---:|---:|---|---|
| 2 | 100% | Good | Correct, useful, specific enough, and no notable hallucination or serious caveat. |
| 1 | 50% | Partially useful | Mostly helpful, but vague, incomplete, off-domain in places, missing an important caveat, or containing a concrete factual slip/hallucination that must be corrected before use. |
| 0 | 0% | Bad | Wrong, misleading, unsafe, non-responsive, stale-context, invented/off-domain in a way likely to waste student time, or unusable for the task. |

The public average score is reported both as an average out of 2 and as a percentage of possible points:

```text
average_score = total_points / prompt_count
score_percent = total_points / (2 * prompt_count) * 100
```

## Audit Details

Hard/notable errors are tracked separately from the score for auditability. They are not an additional answer category, so they may overlap with partial or bad answers.

Examples:

- Invented MOOS-IvP utility, app, variable, behavior parameter, or C++ API.
- Wrong copy-pasteable `.moos` or `.bhv` configuration snippet.
- Confusing `.moos` app/process configuration with `.bhv` behavior configuration.
- Advising a behavior to directly publish `DESIRED_HEADING` or `DESIRED_SPEED`.
- Omitting a critical code-correction requirement such as `setPWT(m_priority_wt)`.
- Unsupported Heron/PABLO interface app names.
- Off-domain ROS/Gazebo/PX4/V2X answer when the prompt is clearly MOOS-IvP-specific.
- Stale answer from a prior prompt.
- Claiming certainty when the prompt requires logs, config files, or source verification.
- Citation or source claim that does not support the answer.

For example, if a model has `28/30` good answers, `2/30` partial answers, and `2` hard/notable errors, those two hard/notable errors may be the same two partial answers. The answer-category counts still sum to 30.
