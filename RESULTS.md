# Benchmark Results

Status: planned, not yet run.

This document is the target structure for the cross-model benchmark comparing the NotebookLM MOOS-IvP TA against the normal beginner-tier browser experience in ChatGPT, Claude, and Gemini on lab-grounded student questions.

## Executive Summary

TBD after benchmark run.

Planned comparison:

- NotebookLM MOOS-IvP TA
- ChatGPT
- Claude
- Gemini

Primary question:

> Is the NotebookLM TA better than the normal beginner-tier AI browser experience for documentation-grounded conceptual MOOS-IvP help?

Secondary question:

> How does it behave on MOOS-IvP code-advice and code-correction tasks, despite not being marketed as a coding tool?

## Headline Results

| Model | Avg Score | Good % | Bad % | Hard Failures | Conceptual Avg | Exact Docs Avg | Code Avg |
|---|---:|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ChatGPT | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Claude | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Gemini | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Category Results

| Category | Prompt Count | NotebookLM TA | ChatGPT | Claude | Gemini | Notes |
|---|---:|---:|---:|---:|---:|---|
| Conceptual/debugging | 30 | TBD | TBD | TBD | TBD | Intended core use case. |
| Exact docs/parameters/tools | 10 | TBD | TBD | TBD | TBD | Tests source-grounded specificity. |
| Code advice/correction | 10 | TBD | TBD | TBD | TBD | Stress test, not primary product claim. |

## Hard Failures

| Prompt ID | Model | Failure Type | Brief Explanation |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

Failure types:

- Invented variable/parameter/API
- Wrong `.moos` vs `.bhv` boundary
- Unsafe autonomy advice
- Unsupported certainty
- Bad or unsupported citation
- Source-level C++ error

## Main Interpretation

TBD after benchmark run.

Questions to answer:

- Did NotebookLM reduce MOOS-IvP-specific hallucinations?
- Did NotebookLM provide source-backed claims that actually checked out during grading?
- Did any normal LLM outperform NotebookLM on conceptual prompts?
- Were code prompts bad enough to exclude from product claims?
- Is the right marketing language "conceptual TA" rather than "coding helper"?

## Prompt-by-Prompt Results

Use this table for all 50 prompts.

Scoring:

- `2` = Good
- `1` = Partially useful
- `0` = Bad

| ID | Category | Prompt Short Name | Expected Key Facts | NotebookLM | ChatGPT | Claude | Gemini | Hard Failures | Notes |
|---|---|---|---|---:|---:|---:|---:|---|---|
| C01 | Conceptual/debugging | command not found after build | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C02 | Conceptual/debugging | version control before mission changes | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C03 | Conceptual/debugging | uXMS/uPokeDB confusion | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C04 | Conceptual/debugging | app not publishing | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C05 | Conceptual/debugging | pAntler did not start a process | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C06 | Conceptual/debugging | launch arguments not reaching config files | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C07 | Conceptual/debugging | helm remains PARKED | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C08 | Conceptual/debugging | no desired outputs | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C09 | Conceptual/debugging | vehicle moves in simulation but autonomy looks wrong | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C10 | Conceptual/debugging | multi-vehicle ports | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C11 | Conceptual/debugging | shoreside missing vehicle | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C12 | Conceptual/debugging | pShare route confusion | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C13 | Conceptual/debugging | TSP app/behavior boundary | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C14 | Conceptual/debugging | distributed route assignment problem | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C15 | Conceptual/debugging | multi-machine networking problem | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C16 | Conceptual/debugging | message does not arrive | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C17 | Conceptual/debugging | node names/destinations | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C18 | Conceptual/debugging | behavior never runs | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C19 | Conceptual/debugging | `.moos` vs `.bhv` mistake | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C20 | Conceptual/debugging | payload event not affecting autonomy | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C21 | Conceptual/debugging | simulation to Heron/PABLO | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C22 | Conceptual/debugging | field deployment sanity check | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C23 | Conceptual/debugging | rescue path planning | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C24 | Conceptual/debugging | adversarial rescue updates | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C25 | Conceptual/debugging | teammate messaging | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C26 | Conceptual/debugging | post-mission alog diagnosis | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C27 | Conceptual/debugging | pLogger produced no useful alog | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C28 | Conceptual/debugging | choosing debugging tools during a mission run | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C29 | Conceptual/debugging | pMarineViewer background/geodesy | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C30 | Conceptual/debugging | mission broke after several edits | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D01 | Exact docs/parameters/tools | pOdometry variables | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D02 | Exact docs/parameters/tools | pAntler process launching | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D03 | Exact docs/parameters/tools | uTimerScript usage | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D04 | Exact docs/parameters/tools | helm deploy variables | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D05 | Exact docs/parameters/tools | BHV_Waypoint params | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D06 | Exact docs/parameters/tools | BHV_OpRegionV24 semantics | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D07 | Exact docs/parameters/tools | viewer image/geodesy config | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D08 | Exact docs/parameters/tools | pShare configuration | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D09 | Exact docs/parameters/tools | uField broker comparison | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D10 | Exact docs/parameters/tools | pLogger and alog verification | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K01 | Code advice/correction | pOdometry mail handling | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K02 | Code advice/correction | missing registration pattern | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K03 | Code advice/correction | AppCasting config warnings | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K04 | Code advice/correction | uTimerScript trigger setup | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K05 | Code advice/correction | behavior config file boundary | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K06 | Code advice/correction | pShare route config | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K07 | Code advice/correction | inter-vehicle message payload | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K08 | Code advice/correction | `setParam()` pattern | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K09 | Code advice/correction | `addInfoVars()` / InfoBuffer | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| K10 | Code advice/correction | ZAIC speed function | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Per-Prompt Notes

### C01: command not found after build

- Prompt: TBD
- Expected answer: TBD
- Reference checks: TBD
- Grading notes: TBD

### C02: version control before mission changes

- Prompt: TBD
- Expected answer: TBD
- Reference checks: TBD
- Grading notes: TBD

### D01: pOdometry variables

- Prompt: TBD
- Expected answer: TBD
- Reference checks: TBD
- Grading notes: TBD

### K10: ZAIC speed function

- Prompt: TBD
- Expected answer: TBD
- Reference checks: local `lib_ivpbuild/ZAIC_PEAK.h` and `BHV_ConstantSpeed.cpp`
- Grading notes: TBD

## Appendix: Grading Method

Each answer receives:

- Score: `0`, `1`, or `2`
- Hard failure: `yes` or `no`
- Short grading note

Score meanings:

- `2`: correct, useful, specific enough, no serious caveat
- `1`: partially useful but incomplete, vague, or requiring verification
- `0`: wrong, misleading, unsafe, invented, or likely to waste time

Hard failure examples:

- invented MOOS-IvP API/parameter
- wrong file boundary
- unsafe direct-control advice
- unsupported certainty
- source-level C++ error

## Appendix: Existing Pre-Benchmark Evidence

Existing reports in `reports/` are not the cross-model benchmark, but they motivate the plan:

- `studio_and_stress_report.json`: 20/20 diagnostic stress prompts passed after manual review.
- `code_advice_test_report.json`: 8 pass, 2 caution, 0 fail on code-advice prompts.
- `code_correction_test_report.json`: 1 pass, 2 pass-with-caution, 2 fail on incorrect-code correction prompts.

Interpretation:

- Strong on conceptual/debugging answers.
- Useful but cautious on code architecture.
- Not reliable as an exact C++ correction engine.
