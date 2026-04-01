# MultiChartQA-R

**MultiChartQA-R: A Benchmark for Multi-Chart Question Answering in Real-World Reasoning Scenarios**

MultiChartQA-R is a benchmark for **multi-chart question answering**, designed to evaluate multimodal large language models (MLLMs) in realistic reasoning settings. It extends prior multi-chart resources with broader task coverage, multilingual data, a scalable data construction pipeline, and evaluation protocols for both **multi-select** and **generative** settings.

## Appendix

**Direct PDF access:** [Open the appendix PDF](./appendix.pdf)

The appendix includes detailed benchmark statistics, metric definitions, prompt templates, multilingual breakdowns, extended benchmark details, and supplementary analyses.

## Resources

- **Appendix PDF:** [appendix.pdf](./appendix.pdf)
- **Main benchmark:** `benchmark/`
- **Extended benchmark:** `benchmark-extended/`
- **Utility scripts:** `code/`

## Overview

MultiChartQA-R studies reasoning over **multiple related charts**, rather than isolated single-chart understanding. The benchmark is designed to cover a progression of abilities from basic cross-chart perception to decision-oriented reasoning.

Each language version currently contains:

- **180** multi-chart sets
- **695** chart-code pairs
- **2,160** QA pairs
- **4** task types

The benchmark currently supports **English**, **Chinese**, and **Spanish**, and is designed to be extendable to additional languages.

In addition, we provide an **extended benchmark** for retrieval-oriented analysis, built from **101** multi-chart articles with **1,212** QA pairs, to study how model performance changes as the number of charts and the amount of relevant information increase.

## JSON Format Notes

The main benchmark JSON files are stored under `benchmark/json/{cn,en,es}`. Each file contains a multi-chart set and its `qa_pairs`.

- **Task 1 / Task 2** entries include direct answers and, for Task 2, explanatory calculations in the `explanation` field.
- **Task 3 / Task 4** entries include the released multi-select supervision fields:
  - `label`: correct option set
  - `easy_error`: distractors corresponding to clearly unsupported or obviously incorrect choices
  - `hard_error`: distractors corresponding to more plausible but ultimately incorrect choices
- **Task 4** entries additionally include a `cot` field, which stores option-level explanations for why each option is correct or incorrect.

This makes the released JSON suitable not only for answer evaluation, but also for instruction construction, explanation analysis, and option-level supervision.

## Task Definition

MultiChartQA-R includes four progressively more complex task types:

1. **Cross-chart Trend Inference**  
   Determine whether trends or patterns across charts are aligned, divergent, or otherwise related.

2. **Complementary Data Integration**  
   Combine evidence from multiple charts to derive a missing value, comparison, or aggregated conclusion.

3. **Anomaly and Pattern Analysis**  
   Identify and explain non-trivial anomalies or patterns grounded in multi-chart evidence.

4. **Strategy Recommendation**  
   Produce decision-oriented recommendations supported by cross-chart analysis.

## Preview

![Visualization_3_01](readme.assets/Visualization_3_01.png)

## Data Construction Pipeline

![construction_process](readme.assets/construction_process.png)

MultiChartQA-R is built through a scalable pipeline that supports both realistic benchmark construction and multilingual extension:

- **Chart-code pair construction:** We collect multi-chart examples from real-world analytical sources and reconstruct chart-rendering code to preserve the underlying structured data.
- **Task-specific QA synthesis:** The four tasks are constructed with different strategies, ranging from direct manual annotation to model-assisted synthesis followed by human review and refinement.
- **Multilingual expansion:** We extend the benchmark to multiple languages at both the chart level and the QA level while maintaining consistency between chart content, terminology, and question-answer pairs.

## Repository Structure

```text
MultiChartQA-R/
├── benchmark/              # Main benchmark data
│   ├── images/
│   ├── images_info/
│   ├── code/
│   └── json/
├── benchmark-extended/     # Retrieval-oriented extended benchmark
├── code/                   # Public utilities: loaders, prompt templates, evaluators, inference template
├── readme.assets/          # README figures
└── appendix.pdf            # Appendix document
```

## Quick Start

### Load the main benchmark

```bash
cd code
python load_benchmark.py
```

This script loads the main benchmark and prints example QA items for Task 1-4.

### Load the extended benchmark

```bash
cd code
python load_exbenchmark.py
```

This script loads the extended benchmark and prints examples from its retrieval-oriented subsets.

### Run evaluation examples

```bash
cd code
python evaluation.py
```

This script contains minimal examples for the released evaluators used by the benchmark:

- Task 1: accuracy / normalized binary matching
- Task 2: answer-level accuracy with numeric tolerance
- Task 3: strict risk-aware multi-select evaluation
- Task 4: strict risk-aware multi-select evaluation

Additional public utilities are also provided in `code/`:

- `prompts.py`: official prompt templates for Task 1-4
- `eval_task1_accuracy.py`: Task 1 accuracy
- `eval_task2_accuracy.py`: Task 2 answer-level accuracy
- `eval_task34_strict_risk_aware.py`: Task 3/4 Strict Risk-Aware `MF_beta`
- `inference_api_template.py`: API inference template using environment variables instead of hardcoded credentials

### Prompt and evaluation utilities

```bash
cd code
python load_benchmark.py
python eval_task1_accuracy.py --result-file path/to/task1_predictions.jsonl
python eval_task2_accuracy.py --result-file path/to/task2_predictions.jsonl
python eval_task34_strict_risk_aware.py --result-file path/to/task3_or_task4_predictions.jsonl
```

For API-based inference, use environment variables rather than editing scripts:

```bash
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key
python inference_api_template.py --model your-model-name --task 3 --language en --sample-index 0
```

## Evaluation Protocol

For the main benchmark:

- **Task 1-2** use accuracy-based evaluation.
- **Task 3-4 (multi-select)** use a **Strict Risk-Aware** \( MF_{\beta} \) metric.
- **Task 3-4 (generative)** use a free-form generation protocol aligned with the benchmark’s option-level evaluation principle.

## Notes

- Some scripts still contain legacy comments using the earlier internal name **MultiChartQA-X**. The released benchmark name is **MultiChartQA-R**.
- The benchmark is intended for research on realistic multi-chart reasoning, including multilingual analysis, retrieval scalability, and decision-oriented evaluation.

## Citation

If you find MultiChartQA-R useful, please cite the project/paper once the final bibliographic information is available.
