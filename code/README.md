# Code Utilities

This directory contains a lightweight public release of the benchmark utilities:

- `data_utils.py`: load the main benchmark and the extended benchmark.
- `prompts.py`: official prompt templates for Task 1-4 and the Task 2 rationale-to-code helper prompt.
- `parse_predictions.py`: helpers for parsing JSON-style model outputs.
- `eval_task1_accuracy.py`: Task 1 accuracy evaluator.
- `eval_task2_accuracy.py`: Task 2 answer-level accuracy evaluator.
- `eval_task34_strict_risk_aware.py`: Task 3/4 Strict Risk-Aware `MF_beta` evaluator.
- `inference_api_template.py`: minimal OpenAI-compatible inference template using environment variables.

## Safe API configuration

Do **not** hardcode API credentials in scripts. Use environment variables instead:

```bash
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key
```

## Examples

```bash
python load_benchmark.py
python load_exbenchmark.py
python eval_task1_accuracy.py --result-file path/to/task1_predictions.jsonl
python eval_task2_accuracy.py --result-file path/to/task2_predictions.jsonl
python eval_task34_strict_risk_aware.py --result-file path/to/task3_or_task4_predictions.jsonl
```
