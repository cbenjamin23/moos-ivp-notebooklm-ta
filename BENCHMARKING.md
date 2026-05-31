# Benchmarking Plan

This benchmark will compare the NotebookLM MOOS-IvP TA against the normal beginner-tier browser experience in ChatGPT, Claude, and Gemini. The main purpose is to test whether the NotebookLM TA is useful as a conceptual, documentation-grounded MOOS-IvP teaching assistant for students working through the MIT/OceanAI MOOS-IvP labs.

The benchmark should not market the notebook as a code generator. Code tasks are included as a stress-test category, not as the primary product claim.

## Positioning

Primary claim:

> A NotebookLM-based MOOS-IvP virtual TA for documentation-grounded conceptual help, lab guidance, tool explanations, and debugging workflows students encounter while completing the MOOS-IvP labs.

Explicit limitation:

> It is not intended to generate, validate, or repair C++ MOOS-IvP code without checking against the local `moos-ivp` source tree.

## Systems To Compare

Primary comparison:

- NotebookLM MOOS-IvP TA
- ChatGPT in the normal signed-in browser UI
- Claude in the normal signed-in browser UI
- Gemini in the normal signed-in browser UI

Optional later comparison:

- Controlled no-web versions of the same systems, if the UI makes that easy and repeatable.
- ChatGPT with uploaded PDFs
- Claude Project with uploaded PDFs
- Gemini/AI Studio with uploaded PDFs
- Codex with local `moos-ivp` source and MOOS-IvP skills

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

Use 50 fixed prompts grounded in the lab sequence:

- 30 conceptual/debugging prompts
- 10 exact documentation/parameter/tool prompts
- 10 code-advice/code-correction prompts

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

## Simple Grading

Each answer gets one score:

| Score | Label | Meaning |
|---:|---|---|
| 2 | Good | Correct, useful, specific enough, and no serious caveat. |
| 1 | Partially useful | Mostly helpful, but vague, incomplete, missing an important caveat, or needs source verification. |
| 0 | Bad | Wrong, misleading, unsafe, invented details, or likely to waste student time. |

Also mark hard failures separately:

| Field | Values |
|---|---|
| Hard failure | `yes` / `no` |
| Failure reason | Short text, only when hard failure is `yes` |

Hard failure examples:

- Invented MOOS variable, behavior parameter, utility option, or C++ API.
- Confuses `.moos` app configuration with `.bhv` behavior configuration.
- Advises a behavior to directly publish `DESIRED_HEADING` or `DESIRED_SPEED`.
- Omits a critical requirement such as `setPWT(m_priority_wt)` in a code-correction task.
- Claims certainty without logs/config/source when the prompt requires concrete debugging.
- Citation does not support the answer's claim.

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
4. Hard-failure table
5. Main interpretation
6. Prompt-by-prompt results for all 50 prompts
7. Appendix with grading notes and reference checks

The root `README.md` should only include a concise summary:

- benchmark date
- systems tested
- average scores
- hard failures
- headline conclusion
- link to `RESULTS.md`

## Summary Metrics

Report these metrics:

- Average score per model.
- Percent of answers scored `2`.
- Percent of answers scored `0`.
- Hard failures per model.
- Average score by category.
- Prompt wins/losses/ties.

Recommended headline table:

| Model | Avg Score | Good % | Bad % | Hard Failures | Conceptual Avg | Exact Docs Avg | Code Avg |
|---|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ChatGPT | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Claude | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Gemini | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Expected Interpretation

Expected outcome based on early validation:

- NotebookLM TA should be strongest on conceptual/debugging prompts that are well-covered by the uploaded MOOS-IvP docs and phrased like lab-student questions.
- NotebookLM TA should be useful but not authoritative on code-advice prompts.
- NotebookLM TA may make source-level C++ mistakes, especially around exact constructors, helper naming, and implementation details not cleanly represented in the PDFs.
- General LLMs may be smoother and better at code style, but are likely to invent MOOS-IvP-specific details more often without retrieval.

The most important comparison is not raw average score. It is whether NotebookLM reduces hard failures on conceptual MOOS-IvP questions.
