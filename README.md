# MOOS-IvP NotebookLM TA

This repository contains the source packs, upload list, benchmark captures, and evaluation reports for a NotebookLM-based MOOS-IvP virtual teaching assistant aimed at students working through the MIT/OceanAI MOOS-IvP labs.

The current NotebookLM notebook is named `MOOS-IvP Virtual TA` and was built from MIT/OceanAI MOOS-IvP documentation PDFs grouped into upload-friendly packs.

## Contents

- `assets/build_packs.py` - script used to build grouped PDF packs.
- `assets/packs/` - combined PDFs uploaded to NotebookLM.
- `assets/upload_files.txt` - absolute local paths for the current upload pack set.
- `assets/manifest.json` - generated source-pack manifest from the original build.
- `reports/` - final benchmark reports, score JSON, and hallucination-audit notes.
- `reports/pre_benchmark/` - earlier setup validation, Studio, stress-test, and code-advice checks.
- `benchmark_runs/` - raw captured benchmark outputs and collection status.

The only large directory is `assets/packs/`. Those PDFs are intentionally retained because they are the reproducible source set uploaded to NotebookLM.

## Current Notebook Source Set

The uploaded NotebookLM source set contains 49 PDFs:

- `00_moos_ivp_virtual_ta_guide.pdf`
- 47 grouped MIT/OceanAI MOOS-IvP documentation packs
- `48_chap_helm_as_moos.pdf`, added after replacing an earlier web source

The most important entry point for human review is:

- `assets/packs/00_moos_ivp_virtual_ta_guide.pdf`

## Benchmark Results

The clean cross-model benchmark compares six rows: NotebookLM TA, ChatGPT 5.5 Thinking, ChatGPT 5.5 Instant, ChatGPT 5.5 Low CLI, Gemini, and Claude. The browser rows reflect the normal beginner-tier product experience available during collection. The CLI row is an isolated GPT-5.5 Low run without browser memory, Codex skills, local files, local tools, or web access; it should still be read as a Codex CLI run rather than a pure browser ChatGPT-low substitute.

Scores use a simple `0/1/2` rubric: `2` good, `1` partially useful, `0` bad. `Score %` is the average converted to a percentage.

Current status: all 360 model outputs are captured and graded. User-approved recaptures are treated as regular stored answers; scoring remains hallucination-sensitive and concrete MOOS-IvP hallucinations reduce the score.

The headline table averages the three ChatGPT rows for a cleaner front-facing comparison. The averaged row combines ChatGPT 5.5 Thinking, ChatGPT 5.5 Instant, and ChatGPT 5.5 Low CLI; detailed individual rows remain in `RESULTS.md` and the report files.

| Model | Score % | Avg / 2 | Conceptual | Exact Docs | Code/Config | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 99.2% | 1.98 | 100.0% | 100.0% | 96.7% | 0 |
| ChatGPT average (3 runs) | 91.1% | 1.82 | 93.9% | 86.7% | 90.0% | 0 |
| Gemini | 76.7% | 1.53 | 75.0% | 90.0% | 66.7% | 0 |
| Claude | 69.2% | 1.38 | 61.7% | 73.3% | 80.0% | 0 |

Interpretation: NotebookLM TA currently ranks first overall and is strongest in its intended lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. The averaged ChatGPT row is strong but trails NotebookLM on the lab-grounded benchmark overall. The isolated GPT-5.5 Low CLI row remains useful as a no-memory/no-local-context comparison, but Codex CLI's coding-agent wrapper may make its code/config score less directly comparable to the browser rows.

Detailed results and rubric:

- `SCORING_RUBRIC.md`
- `RESULTS.md`
- `reports/conceptual_debugging_benchmark_results.md`
- `reports/exact_docs_tools_benchmark_results.md`
- `reports/code_config_benchmark_results.md`
- `reports/chatgpt_55_instant_benchmark_results.md`
- `reports/chatgpt_55_low_cli_benchmark_results.md`
- `reports/hallucination_sweep_notes.md`

## Grading Metadata

Yes, grading metadata is stored with the benchmark artifacts:

- `SCORING_RUBRIC.md` defines the `0/1/2` scoring rules and how hallucinations are penalized.
- `RESULTS.md` gives the public summary plus per-prompt notes and hard/notable error examples.
- `reports/*_benchmark_results.json` stores machine-readable scoring metadata, including fields such as `grading_method`, `score_legend`, `metrics`, `hard_failures`, per-prompt scores, winners, and notes.
- `benchmark_runs/2026-05-31_organic_beginner_tier_clean2/raw/` stores the raw model outputs used for scoring.

## Validation Summary

Existing pre-benchmark reports:

- `reports/pre_benchmark/validation_report.json` - initial NotebookLM setup and 20-prompt validation sweep.
- `reports/pre_benchmark/studio_and_stress_report.json` - Studio feature notes plus 20 diagnostic stress prompts.
- `reports/pre_benchmark/code_advice_test_report.json` - 10 prompts asking for MOOS-IvP code advice, reviewed against local source.
- `reports/pre_benchmark/code_correction_test_report.json` - 5 prompts with intentionally incorrect MOOS-IvP code, reviewed against local source.

High-level result:

- General MOOS-IvP TA/debugging prompts: strong.
- Code architecture advice: useful, with source-level caution.
- Exact C++ correction: not reliable without checking the local `moos-ivp` checkout.

## Benchmark Plan

The benchmark uses 60 fixed, lab-grounded prompts:

- 30 conceptual/debugging prompts
- 15 exact documentation/parameter/tool prompts
- 15 code-advice/code-correction prompts

Detailed methodology:

- `BENCHMARKING.md`
- `BENCHMARK_PROMPTS.md`

## Notes

NotebookLM itself is not exported in this repository. This repo preserves the source artifacts, raw benchmark captures, and evaluation notes needed to recreate or audit the notebook.
