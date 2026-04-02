# Code Utilities

This directory contains a lightweight public release of the benchmark utilities:

- `data_utils.py`: load the main benchmark and the extended benchmark
- `prompts.py`: prompt templates for Task 1-4 and the Task 2 rationale-to-code helper prompt
- `parse_predictions.py`: parse JSON-style model outputs
- `inference_multiselect_api_template.py`: minimal API inference template for Task 1-4 multi-select
- `inference_generative_api_template.py`: minimal API inference template for Task 3 / Task 4 generative setting
- `eval_task1_accuracy.py`: Task 1 accuracy evaluator
- `eval_task2_accuracy.py`: Task 2 answer-level accuracy evaluator
- `eval_task34_strict_risk_aware.py`: Task 3/4 Strict Risk-Aware `MF_beta` evaluator
- `eval_task34_generative_answer_extraction.py`: primary generative evaluator for Task 3 / Task 4
- `evaluation.py`: small end-to-end evaluation examples

## Safe API configuration

Do **not** hardcode API credentials in scripts. Use environment variables instead:

```bash
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key
```

## Usage

### 1. Load the datasets

```bash
cd code
python load_benchmark.py
python load_exbenchmark.py
```

### 2. Run inference for Task 1-4

For multi-select / standard inference:

```bash
cd code
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key

python inference_multiselect_api_template.py --model your-model-name --task 1 --language en --sample-index 0
python inference_multiselect_api_template.py --model your-model-name --task 2 --language en --sample-index 0
python inference_multiselect_api_template.py --model your-model-name --task 3 --language en --sample-index 0
python inference_multiselect_api_template.py --model your-model-name --task 4 --language en --sample-index 0
```

For generative inference on Task 3 / Task 4:

```bash
cd code
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key

python inference_generative_api_template.py --model your-model-name --task 3 --language en --sample-index 0
python inference_generative_api_template.py --model your-model-name --task 4 --language en --sample-index 0
```

### 3. Evaluate predictions for all tasks

```bash
cd code
python eval_task1_accuracy.py --result-file path/to/task1_predictions.jsonl
python eval_task2_accuracy.py --result-file path/to/task2_predictions.jsonl
python eval_task34_strict_risk_aware.py --result-file path/to/task3_multiselect_predictions.jsonl
python eval_task34_strict_risk_aware.py --result-file path/to/task4_multiselect_predictions.jsonl
```

For primary generative evaluation of Task 3 / Task 4:

```bash
export OPENAI_BASE_URL=https://your-endpoint/v1
export OPENAI_API_KEY=your_api_key
python eval_task34_generative_answer_extraction.py --result-file path/to/task3_generative_predictions.jsonl --judge-model your-judge-model
python eval_task34_generative_answer_extraction.py --result-file path/to/task4_generative_predictions.jsonl --judge-model your-judge-model
```
