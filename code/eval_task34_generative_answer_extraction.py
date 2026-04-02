from __future__ import annotations

import argparse
import json
import os
from typing import Dict, List

import requests

from eval_task34_strict_risk_aware import evaluate_question_strict_risk_aware
from parse_predictions import parse_prediction_json, normalize_option_answer


ANSWER_EXTRACTION_PROMPT = """You are given a multi-chart question, its answer choices, and a model-generated free-form analysis.\nDetermine which option letters are implicitly supported by the analysis.\nReturn valid JSON only in the following format:\n{\"answer\": [\"A\", \"C\"]}\nIf the analysis does not clearly support any option, return {\"answer\": []}."""


def dict_to_choices(answer_dict: Dict[str, str]) -> str:
    return "\n".join(f"{k}: {v}" for k, v in sorted(answer_dict.items()))


def call_judge(model_name: str, prompt: str) -> Dict:
    base_url = os.environ["OPENAI_BASE_URL"].rstrip("/")
    api_key = os.environ["OPENAI_API_KEY"]
    response = requests.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "max_tokens": 512,
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()


def extract_predicted_options(item: Dict, judge_model: str) -> List[str]:
    raw_prediction = item.get("predict_answer", "")
    parsed = parse_prediction_json(raw_prediction)
    free_form_answer = parsed.get("answer") if parsed else raw_prediction

    prompt = (
        ANSWER_EXTRACTION_PROMPT
        + "\n\nQuestion:\n"
        + item["question"]
        + "\n\nOptions:\n"
        + dict_to_choices(item["answer"])
        + "\n\nGenerated analysis:\n"
        + str(free_form_answer)
    )
    judge_response = call_judge(judge_model, prompt)
    content = judge_response["choices"][0]["message"]["content"]
    judge_parsed = parse_prediction_json(content)
    return normalize_option_answer(judge_parsed.get("answer") if judge_parsed else [])


def evaluate_file(result_file: str, judge_model: str, limit: int | None = None) -> Dict[str, float]:
    f_scores: List[float] = []
    precisions: List[float] = []
    recalls: List[float] = []

    with open(result_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if limit is not None and idx > limit:
                break
            item = json.loads(line)
            pred = extract_predicted_options(item, judge_model)
            scores = evaluate_question_strict_risk_aware(
                pred_answer=pred,
                label=item.get("label", []),
                easy_error=item.get("easy_error", []),
                hard_error=item.get("hard_error", []),
                beta=1.0,
                easy_weight=1.0,
                hard_weight=0.5,
            )
            f_scores.append(scores["f_beta"])
            precisions.append(scores["strict_precision"])
            recalls.append(scores["recall"])

    if not f_scores:
        return {"strict_f1": 0.0, "strict_precision": 0.0, "recall": 0.0}
    return {
        "strict_f1": sum(f_scores) / len(f_scores),
        "strict_precision": sum(precisions) / len(precisions),
        "recall": sum(recalls) / len(recalls),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Primary generative evaluation for Task 3/4 via answer extraction.")
    parser.add_argument("--result-file", required=True, help="Path to a JSONL prediction file.")
    parser.add_argument("--judge-model", required=True, help="Judge model name on an OpenAI-compatible endpoint.")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of samples to evaluate.")
    args = parser.parse_args()

    if "OPENAI_BASE_URL" not in os.environ or "OPENAI_API_KEY" not in os.environ:
        raise RuntimeError("Please set OPENAI_BASE_URL and OPENAI_API_KEY before running generative evaluation.")

    scores = evaluate_file(args.result_file, args.judge_model, args.limit)
    print(f"Generative Strict_F1: {scores['strict_f1'] * 100:.2f}")
    print(f"Generative Strict_Precision: {scores['strict_precision'] * 100:.2f}")
    print(f"Generative Recall: {scores['recall'] * 100:.2f}")


if __name__ == "__main__":
    main()
