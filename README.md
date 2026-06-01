# MOOS-IvP NotebookLM TA

This repository contains the source packs, upload list, and validation reports for a NotebookLM-based MOOS-IvP virtual teaching assistant aimed at students working through the MIT/OceanAI MOOS-IvP labs.

The current NotebookLM notebook is named `MOOS-IvP Virtual TA` and was built from MIT/OceanAI MOOS-IvP documentation PDFs grouped into upload-friendly packs.

## Contents

- `assets/build_packs.py` - script used to build grouped PDF packs.
- `assets/packs/` - combined PDFs uploaded to NotebookLM.
- `assets/upload_files.txt` - absolute local paths for the current upload pack set.
- `assets/manifest.json` - generated source-pack manifest from the original build.
- `reports/` - validation, stress-test, code-advice, code-correction, and cross-model benchmark reports.
- `benchmark_runs/` - raw captured benchmark outputs.

## Current Notebook Source Set

The uploaded NotebookLM source set contains 49 PDFs:

- `00_moos_ivp_virtual_ta_guide.pdf`
- 47 grouped MIT/OceanAI MOOS-IvP documentation packs
- `48_chap_helm_as_moos.pdf`, added after replacing an earlier web source

The most important entry point for human review is:

- `assets/packs/00_moos_ivp_virtual_ta_guide.pdf`

## Benchmark Results

The clean cross-model benchmark compares NotebookLM TA with beginner-tier browser ChatGPT, Claude, and Gemini. Additional ChatGPT rows test GPT-5.5 Instant in the web app and GPT-5.5 Low through an isolated CLI run. Scores use a simple `0/1/2` rubric: `2` good, `1` partially useful, `0` bad. `Score %` is the average converted to a percentage.

Current status: all 360 model outputs are captured and graded. User-approved recaptures are treated as regular stored answers; scoring remains hallucination-sensitive and concrete MOOS-IvP hallucinations reduce the score.

| Model | Score % | Avg / 2 | Conceptual | Exact Docs | Code/Config | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 99.2% | 1.98 | 100.0% | 100.0% | 96.7% | 0 |
| ChatGPT 5.5 Thinking | 93.3% | 1.87 | 96.7% | 90.0% | 90.0% | 0 |
| ChatGPT 5.5 Instant | 91.7% | 1.83 | 95.0% | 93.3% | 83.3% | 0 |
| ChatGPT 5.5 Low CLI | 90.8% | 1.82 | 93.3% | 80.0% | 96.7% | 0 |
| Gemini | 80.0% | 1.60 | 80.0% | 90.0% | 70.0% | 0 |
| Claude | 71.7% | 1.43 | 65.0% | 73.3% | 83.3% | 0 |

Interpretation: NotebookLM TA currently ranks first overall and is strongest in its intended lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. The isolated GPT-5.5 Low CLI row is useful as a cleaner non-RAG comparison because it avoids browser memory and local Codex skills, but it still trails NotebookLM on exact MOOS-IvP source alignment.

Detailed results and rubric:

- `SCORING_RUBRIC.md`
- `RESULTS.md`
- `reports/conceptual_debugging_benchmark_results.md`
- `reports/exact_docs_tools_benchmark_results.md`
- `reports/code_config_benchmark_results.md`
- `reports/chatgpt_55_instant_benchmark_results.md`
- `reports/chatgpt_55_low_cli_benchmark_results.md`

## Validation Summary

Existing pre-benchmark reports:

- `reports/validation_report.json` - initial NotebookLM setup and 20-prompt validation sweep.
- `reports/studio_and_stress_report.json` - Studio feature notes plus 20 diagnostic stress prompts.
- `reports/code_advice_test_report.json` - 10 prompts asking for MOOS-IvP code advice, reviewed against local source.
- `reports/code_correction_test_report.json` - 5 prompts with intentionally incorrect MOOS-IvP code, reviewed against local source.

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
