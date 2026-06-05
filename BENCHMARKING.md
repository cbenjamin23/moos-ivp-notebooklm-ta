# Benchmarking Plan

This benchmark compares the NotebookLM MOOS-IvP TA against the normal beginner-tier browser experience in ChatGPT, Claude, and Gemini, plus two additional ChatGPT 5.5 rows. The main purpose is to test whether the NotebookLM TA is useful as a conceptual, documentation-grounded MOOS-IvP teaching assistant for students working through the MIT/OceanAI MOOS-IvP labs.

The benchmark should not market the notebook as a code generator. Code tasks are included as a stress-test category, not as the primary product claim.

## Positioning

Primary claim:

> A NotebookLM-based MOOS-IvP virtual TA for documentation-grounded conceptual help, lab guidance, tool explanations, and debugging workflows students encounter while completing the MOOS-IvP labs.

Explicit limitation:

> It is not intended to generate, validate, or repair C++ MOOS-IvP code without checking against the local `moos-ivp` source tree.

## Systems To Compare

Completed comparison:

- NotebookLM MOOS-IvP TA
- ChatGPT 5.5 Thinking in the normal signed-in browser UI
- ChatGPT 5.5 Instant in the normal signed-in browser UI
- ChatGPT 5.5 Low through an isolated CLI run
- Claude in the normal signed-in browser UI
- Gemini in the normal signed-in browser UI

## Benchmark Mode

The primary benchmark mode is an organic beginner-tier test:

- Use the standard browser UI a student would naturally use.
- Use the same prompt text for every model.
- Do not add special benchmark instructions such as "do not browse," "cite sources," or "answer concisely."
- Do not upload extra documents to ChatGPT, Claude, or Gemini for the primary run.
- Allow each platform to use its default available behavior, including web/search behavior if the product chooses to use it.
- NotebookLM uses the curated `MOOS-IvP Virtual TA` notebook because that is the product being evaluated.
- Record visible model/tool settings where practical, but do not tune them per prompt.

## Prompt Set

Use 60 fixed prompts grounded in the lab sequence:

- 30 conceptual/debugging prompts
- 15 exact documentation/parameter/tool prompts
- 15 code-advice/code-correction prompts

This split reflects the intended use case. The benchmark should mainly test conceptual TA value for lab students, while still measuring whether the notebook is better or worse than normal LLMs on code-adjacent MOOS-IvP tasks.

The draft fixed prompt set is in `BENCHMARK_PROMPTS.md`.

### Category 1: Conceptual/Debugging

These should be phrased as student questions inspired by lab work, without naming lab numbers in the prompt text. Examples:

- "I launched a MOOSDB and poked a variable, but uXMS does not show what I expected. What should I check?"
- "My pOdometry-style app subscribes to `NAV_X` and `NAV_Y`, but nothing is being published. How do I debug `OnNewMail()`, `RegisterVariables()`, and AppTick?"
- "I set `DEPLOY=true`, but pHelmIvP stays PARKED or produces no desired heading. What should I inspect?"
- "My two vehicle communities run on one laptop but shoreside does not see both vehicles. How do ports, community names, pShare, and NODE_REPORT fit together?"
- "My TSP app generates waypoints, but the vehicle does not follow them. What is the boundary between the app, updates, and BHV_Waypoint?"
- "My inter-vehicle message does not arrive. How should I trace it through uFldNodeBroker, uFldNodeComms, uFldShoreBroker, and uFldMessageHandler?"
- "My custom behavior appears configured but never runs. How should I inspect conditions, InfoBuffer variables, and helm life events?"
- "What changes when moving from simulation to a Heron/PABLO field deployment?"
- "My launch argument changed, but the generated mission still behaves like it has the old value. What should I inspect?"
- "A payload process posts useful data, but the vehicle behavior does not react to it. How should I trace the data path?"
- "The mission works on one laptop but fails across machines. What should I check about hosts, ports, and pShare?"

### Category 2: Exact Documentation/Parameter/Tool

These should still be framed as natural student questions, without asking for citations directly:

- "What are the actual BHV_Waypoint arrival/capture parameters I should use in my `.bhv` file?"
- "Does BHV_OpRegionV24 steer me back inside the polygon, or does it mainly detect/enforce region constraints?"
- "In a multi-vehicle messaging setup, what is the difference between uFldNodeBroker, uFldShoreBroker, and uFldNodeComms?"
- "How should I use pLogger output, aloggrep, alogview, and variable history to verify what happened after a mission?"
- "Why does pMarineViewer show vehicles in the wrong place relative to the background image?"
- "What determines whether pAntler launches a process, and how do I tell launch failure from registration failure?"
- "What variables and tools matter for a pOdometry-style app?"
- "What is uTimerScript useful for, and what are common initialization mistakes?"

### Category 3: Code Advice/Correction

These prompts should be small code-adjacent student questions, not requests for a full generated project:

- App lifecycle: `OnStartUp()`, `OnNewMail()`, `Iterate()`, AppCasting reports.
- pOdometry-style mail handling and state updates.
- Mission configuration snippets: uTimerScript setup, behavior blocks, pShare routes, and inter-vehicle message strings.
- Behavior `setParam()` and standard behavior params.
- `addInfoVars()` and missing/stale InfoBuffer data.
- Simple ZAIC / `OF_Coupler` / `setPWT(m_priority_wt)` correction.

## Prompt Rules

- Use the exact same prompt text for every model.
- Do not give one model extra hidden hints.
- Do not ask for citations in the prompt text; evaluate source grounding separately during grading.
- Allow each platform's normal/default tool behavior in the primary organic benchmark.
- Preserve raw model output.
- Grade only after all model outputs are collected for that prompt.
- Code answers should be graded against the local MOOS-IvP source tree, not just against citations.

## Scoring

Use the canonical rubric in `SCORING_RUBRIC.md`.

Benchmark-specific grading notes:

- For code/config prompts, use the local MOOS-IvP source tree as the final oracle.
- Report both `Score %` and `Avg / 2` in public tables.
- Keep hard/notable error details in audit sections, not as a headline score-table column.

## Reference Oracle

Use two reference levels:

- Documentation oracle: final NotebookLM upload PDFs in `assets/packs/`.
- Source oracle: local MOOS-IvP checkout, especially:
  - `ivp/src/lib_behaviors/`
  - `ivp/src/lib_behaviors-marine/`
  - `ivp/src/lib_ivpbuild/`
  - representative apps such as `pEchoVar`, `pNodeReporter`, `uFldMessageHandler`, and `pDeadManPost`

For conceptual prompts, the documentation oracle is usually enough.

For code prompts, the source oracle decides.

## Results Structure

The main benchmark output should be `RESULTS.md`.

It should contain:

1. Executive summary
2. Model score table
3. Score table by category
4. Hard/notable error audit section
5. Main interpretation
6. Prompt-by-prompt results for all 60 prompts
7. Appendix with grading notes and reference checks

The root `README.md` should only include a concise summary:

- benchmark date
- systems tested
- average scores
- headline conclusion
- link to `RESULTS.md`

## Summary Metrics

Report these metrics:

- Average score out of 2 per model.
- Public score percentage per model, calculated as total points divided by maximum possible points.
- Percent of answers scored `2`.
- Percent of answers scored `0`.
- Hard/notable error details in audit sections, reported separately from good/partial/bad answer categories.
- Score percentage by category.
- Prompt wins/losses/ties.

Recommended headline table:

| Model | Score % | Avg / 2 | Good % | Partial % | Bad % | Conceptual Score % | Exact Docs Score % | Code Score % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ChatGPT 5.5 Thinking | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ChatGPT 5.5 Instant | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ChatGPT 5.5 Low CLI | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Claude | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Gemini | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Expected Interpretation

Expected outcome based on early validation:

- NotebookLM TA should be strongest on conceptual/debugging prompts that are well-covered by the uploaded MOOS-IvP docs and phrased like lab-student questions.
- NotebookLM TA should be useful but not authoritative on code-advice prompts.
- NotebookLM TA may make source-level C++ mistakes, especially around exact constructors, helper naming, and implementation details not cleanly represented in the PDFs.
- General LLMs may be smoother and better at code style, but are likely to invent MOOS-IvP-specific details more often without retrieval.

The most important comparison is not raw average score. It is whether NotebookLM reduces MOOS-IvP-specific hallucinations on conceptual questions.
