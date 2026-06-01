# MOOS-IvP NotebookLM TA

This repository contains the source packs, upload list, and validation reports for a NotebookLM-based MOOS-IvP virtual teaching assistant aimed at students working through the MIT/OceanAI MOOS-IvP labs.

The current NotebookLM notebook is named `MOOS-IvP Virtual TA` and was built from MIT/OceanAI MOOS-IvP documentation PDFs grouped into upload-friendly packs.

## Contents

- `assets/build_packs.py` - script used to build grouped PDF packs.
- `assets/packs/` - combined PDFs uploaded to NotebookLM.
- `assets/upload_files.txt` - absolute local paths for the current upload pack set.
- `assets/manifest.json` - generated source-pack manifest from the original build.
- `reports/` - validation, stress-test, code-advice, and code-correction reports.

## Current Notebook Source Set

The uploaded NotebookLM source set contains 49 PDFs:

- `00_moos_ivp_virtual_ta_guide.pdf`
- 47 grouped MIT/OceanAI MOOS-IvP documentation packs
- `48_chap_helm_as_moos.pdf`, added after replacing an earlier web source

The most important entry point for human review is:

- `assets/packs/00_moos_ivp_virtual_ta_guide.pdf`

## Validation Summary

Existing reports:

- `reports/validation_report.json` - initial NotebookLM setup and 20-prompt validation sweep.
- `reports/studio_and_stress_report.json` - Studio feature notes plus 20 diagnostic stress prompts.
- `reports/code_advice_test_report.json` - 10 prompts asking for MOOS-IvP code advice, reviewed against local source.
- `reports/code_correction_test_report.json` - 5 prompts with intentionally incorrect MOOS-IvP code, reviewed against local source.

High-level result:

- General MOOS-IvP TA/debugging prompts: strong.
- Code architecture advice: useful, with source-level caution.
- Exact C++ correction: not reliable without checking the local `moos-ivp` checkout.

## Benchmark Results

The clean cross-model benchmark is partially complete. The conceptual/debugging section (`C01-C30`) has been captured and graded independently from the unfinished sections. A hallucination-sensitive revision pass has been applied, so plausible-looking wrong MOOS-IvP details reduce the score.

Scores use a `0/1/2` rubric; `Score %` is the average converted to a percentage.

Conceptual/debugging scores:

| Model | Score % | Avg / 2 | Good Answers | Partial Answers | Bad Answers |
|---|---:|---:|---:|---:|---:|
| NotebookLM TA | 100.0% | 2.00 | 30/30 (100.0%) | 0/30 (0.0%) | 0/30 (0.0%) |
| ChatGPT | 96.7% | 1.93 | 28/30 (93.3%) | 2/30 (6.7%) | 0/30 (0.0%) |
| Gemini | 80.0% | 1.60 | 20/30 (66.7%) | 8/30 (26.7%) | 2/30 (6.7%) |
| Claude | 60.0% | 1.20 | 11/30 (36.7%) | 14/30 (46.7%) | 5/30 (16.7%) |

Interpretation: NotebookLM TA ranks first on the completed conceptual/debugging section under the hallucination-sensitive rubric. ChatGPT remains very strong, but lost credit for two wrong copy-pasteable pAntler config examples. Exact documentation/tool prompts and code/config prompts remain pending in the clean benchmark.

Detailed results and rubric:

- `SCORING_RUBRIC.md`
- `RESULTS.md`
- `reports/conceptual_debugging_benchmark_results.md`
- `reports/conceptual_debugging_benchmark_results.json`
- `reports/hallucination_sweep_notes.md`

## Benchmark Plan

The cross-model benchmark compares the NotebookLM MOOS-IvP TA against the normal beginner-tier browser experience in ChatGPT, Claude, and Gemini on questions a student might naturally ask while working through the MOOS-IvP labs.

The intended product claim is narrow:

> The NotebookLM TA is a conceptual, documentation-grounded MOOS-IvP answering machine for labs, tools, behaviors, debugging workflows, and mission structure.

It should not be marketed as a MOOS-IvP coding agent.

The benchmark uses 50 fixed, lab-grounded prompts:

- 30 conceptual/debugging prompts
- 10 exact documentation/parameter/tool prompts
- 10 code-advice/code-correction prompts

Detailed methodology:

- `SCORING_RUBRIC.md`
- `BENCHMARKING.md`

Draft fixed prompt set:

- `BENCHMARK_PROMPTS.md`

Full results template:

- `RESULTS.md`

## Notes

NotebookLM itself is not exported in this repository. This repo preserves the source artifacts and evaluation notes needed to recreate or audit the notebook.
