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

## Benchmark Plan

The planned cross-model benchmark will compare the NotebookLM MOOS-IvP TA against non-RAG ChatGPT, Claude, and Gemini outputs on questions a student might naturally ask while working through the MOOS-IvP labs.

The intended product claim is narrow:

> The NotebookLM TA is a conceptual, documentation-grounded MOOS-IvP answering machine for labs, tools, behaviors, debugging workflows, and mission structure.

It should not be marketed as a MOOS-IvP coding agent.

The planned benchmark uses 30 fixed, lab-grounded prompts:

- 20 conceptual/debugging prompts
- 5 exact documentation/parameter/tool prompts
- 5 code-advice/code-correction prompts

Each answer will be graded with a simple score:

- `2` = good
- `1` = partially useful
- `0` = bad

Hard failures will be tracked separately for invented APIs, wrong parameters, unsafe advice, `.moos`/`.bhv` confusion, unsupported certainty, bad citations, and source-level C++ errors.

Detailed methodology:

- `BENCHMARKING.md`

Draft fixed prompt set:

- `BENCHMARK_PROMPTS.md`

Full results template:

- `RESULTS.md`

## Notes

NotebookLM itself is not exported in this repository. This repo preserves the source artifacts and evaluation notes needed to recreate or audit the notebook.
