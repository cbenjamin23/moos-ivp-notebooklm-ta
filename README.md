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

The clean cross-model benchmark compares NotebookLM TA with the normal beginner-tier browser experience in ChatGPT, Claude, and Gemini. Scores use a simple `0/1/2` rubric: `2` good, `1` partially useful, `0` bad. `Score %` is the average converted to a percentage.

Current status: 199 of 200 model outputs are captured and graded. Claude K10 is pending after a quota stop. NotebookLM D02 uses a user-approved retry replacement after an initial non-answer.

| Model | Score % | Avg / 2 | Conceptual | Exact Docs | Code/Config | Pending |
|---|---:|---:|---:|---:|---:|---:|
| NotebookLM TA | 99.0% | 1.98 | 100.0% | 100.0% | 95.0% | 0 |
| ChatGPT | 94.0% | 1.88 | 96.7% | 90.0% | 90.0% | 0 |
| Gemini | 78.0% | 1.56 | 80.0% | 90.0% | 60.0% | 0 |
| Claude | 60.2% | 1.20 | 60.0% | 50.0% | 72.2% | 1 |

Interpretation: NotebookLM TA currently ranks first overall and is strongest in its intended lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. The repo should still position it as a conceptual TA, not as a standalone MOOS-IvP coding agent.

Detailed results and rubric:

- `SCORING_RUBRIC.md`
- `RESULTS.md`
- `reports/conceptual_debugging_benchmark_results.md`
- `reports/exact_docs_tools_benchmark_results.md`
- `reports/code_config_benchmark_results.md`

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

The benchmark uses 50 fixed, lab-grounded prompts:

- 30 conceptual/debugging prompts
- 10 exact documentation/parameter/tool prompts
- 10 code-advice/code-correction prompts

Detailed methodology:

- `BENCHMARKING.md`
- `BENCHMARK_PROMPTS.md`

## Notes

NotebookLM itself is not exported in this repository. This repo preserves the source artifacts, raw benchmark captures, and evaluation notes needed to recreate or audit the notebook.
