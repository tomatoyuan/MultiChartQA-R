# Code Utilities

This directory contains a lightweight public release of the benchmark utilities:

| File | Role |
| --- | --- |
| `data_utils.py` | Load the main benchmark and the extended benchmark |
| `prompts.py` | Prompt templates for Task 1-4 and the Task 2 rationale-to-code helper prompt |
| `parse_predictions.py` | Parse JSON-style model outputs |
| `inference_multiselect_api_template.py` | Minimal API inference template for Task 1-4 multi-select |
| `inference_generative_api_template.py` | Minimal API inference template for Task 3 / Task 4 generative setting |
| `eval_task1_accuracy.py` | Task 1 accuracy evaluator |
| `eval_task2_accuracy.py` | Task 2 answer-level accuracy evaluator |
| `eval_task34_strict_risk_aware.py` | Task 3/4 Strict Risk-Aware `MF_beta` evaluator |
| `eval_task34_generative_answer_extraction.py` | Primary generative evaluator for Task 3 / Task 4 |
| `evaluation.py` | Small end-to-end evaluation examples |

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
python inference_multiselect_api_template.py --model your-model-name --task 1 --language en --sample-index 0
python inference_multiselect_api_template.py --model your-model-name --task 4 --language en --sample-index 0
python inference_generative_api_template.py --model your-model-name --task 3 --language en --sample-index 0
python eval_task1_accuracy.py --result-file path/to/task1_predictions.jsonl
python eval_task2_accuracy.py --result-file path/to/task2_predictions.jsonl
python eval_task34_strict_risk_aware.py --result-file path/to/task3_or_task4_predictions.jsonl
python eval_task34_generative_answer_extraction.py --result-file path/to/task3_or_task4_generative_predictions.jsonl --judge-model your-judge-model
```
