# Reports

This directory keeps the benchmark reports and score metadata.

## Final Benchmark Reports

- `conceptual_debugging_benchmark_results.md` / `.json`
- `exact_docs_tools_benchmark_results.md` / `.json`
- `code_config_benchmark_results.md` / `.json`
- `chatgpt_55_instant_benchmark_results.md` / `.json`
- `chatgpt_55_low_cli_benchmark_results.md` / `.json`
- `hallucination_sweep_notes.md`

The JSON reports preserve grading metadata such as the scoring method, score legend, aggregate metrics, hard/notable failures, per-prompt scores, and per-prompt notes.

## Pre-Benchmark Checks

`pre_benchmark/` contains earlier setup validation, Studio feature checks, stress tests, and code-advice probes. These files are retained for audit history, but the root `README.md` and `RESULTS.md` should be treated as the current public summary.
