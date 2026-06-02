# MOOS-IvP NotebookLM TA

This project explores whether a curated NotebookLM notebook can serve as a practical MOOS-IvP virtual teaching assistant for students working through the MIT 2.680 labs. The focus is documentation-grounded conceptual help: mission setup, autonomy concepts, tool usage, and beginner debugging workflows.

The repository preserves the source packs, benchmark prompts, raw captures, and scoring reports needed to recreate and audit the notebook.

## Benchmark Results

The benchmark uses 60 fixed, lab-grounded prompts across conceptual/debugging, exact documentation, and code/config categories. Scores are out of 2: `2` means good, `1` means partially useful, and `0` means bad. `Score %` converts that average to a percentage.

| Model | Score % | Avg / 2 | Conceptual | Exact Docs | Code/Config |
|---|---:|---:|---:|---:|---:|
| NotebookLM TA | 99.2% | 1.98 | 100.0% | 100.0% | 96.7% |
| ChatGPT | 91.1% | 1.82 | 93.9% | 86.7% | 90.0% |
| Gemini | 76.7% | 1.53 | 75.0% | 90.0% | 66.7% |
| Claude | 69.2% | 1.38 | 61.7% | 73.3% | 80.0% |

NotebookLM TA ranks first overall and is strongest in its intended lane: source-grounded conceptual/debugging help for MOOS-IvP lab students. Students are generally encouraged to use the virtual TA as a conceptual aid and not a reliable code generation tool. Contact Charles Benjamin to inquire about developer-level MOOS-IvP code generation when you are proficient. Detailed reports preserve the individual model runs behind the headline rows and can be found in the sources below.

Detailed results:

- `RESULTS.md`
- `SCORING_RUBRIC.md`
- `reports/conceptual_debugging_benchmark_results.md`
- `reports/exact_docs_tools_benchmark_results.md`
- `reports/code_config_benchmark_results.md`
- `reports/chatgpt_55_instant_benchmark_results.md`
- `reports/chatgpt_55_low_cli_benchmark_results.md`
- `reports/hallucination_sweep_notes.md`

## Repository Contents

- `assets/packs/` - 49 PDFs uploaded to NotebookLM, including the TA guide and grouped MIT/OceanAI source packs.
- `assets/build_packs.py` - script used to build grouped PDF packs.
- `assets/upload_files.txt` - absolute local paths for the current upload pack set.
- `assets/manifest.json` - generated source-pack manifest.
- `benchmark_runs/` - raw captured benchmark outputs.
- `reports/` - final reports, score JSON, hallucination-audit notes, and pre-benchmark checks.

The only large directory is `assets/packs/`; those PDFs are intentionally retained because they are the reproducible NotebookLM source set. The most useful human-review entry point is `assets/packs/00_moos_ivp_virtual_ta_guide.pdf`.

## Grading Evidence

- `SCORING_RUBRIC.md` defines the scoring rules.
- `RESULTS.md` gives per-prompt scores, notes, and hard/notable error examples.
- `reports/*_benchmark_results.json` stores machine-readable scoring metadata, including fields such as `grading_method`, `score_legend`, `metrics`, `hard_failures`, per-prompt scores, winners, and notes.
- `benchmark_runs/main_benchmark/raw/` stores the raw model outputs used for scoring.

## Benchmark Plan

- `BENCHMARKING.md`
- `BENCHMARK_PROMPTS.md`

## Notes

NotebookLM itself is not exported in this repository. This repo preserves the source artifacts, raw benchmark captures, and evaluation notes needed to recreate or audit the notebook.
