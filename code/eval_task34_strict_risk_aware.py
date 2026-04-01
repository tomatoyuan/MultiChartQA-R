from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from parse_predictions import normalize_option_answer, parse_prediction_json


def evaluate_question_strict_risk_aware(
    pred_answer: Iterable[str],
    label: Iterable[str],
    easy_error: Iterable[str],
    hard_error: Iterable[str],
    beta: float = 1.0,
    easy_weight: float = 1.0,
    hard_weight: float = 0.5,
) -> Dict[str, Any]:
    pred_set = set(pred_answer) if pred_answer else set()
    label_set = set(label) if label else set()
    easy_set = set(easy_error) if easy_error else set()
    hard_set = set(hard_error) if hard_error else set()

    tp = len(pred_set & label_set)
    selected_easy = len(pred_set & easy_set)
    selected_hard = len(pred_set & hard_set)
    net_tp = max(0.0, float(tp) - easy_weight * selected_easy - hard_weight * selected_hard)

    strict_precision = 0.0 if not pred_set else net_tp / len(pred_set)
    recall = 0.0 if not label_set else tp / len(label_set)
    denom = (beta**2) * strict_precision + recall
    f_beta = 0.0 if denom == 0 else (1 + beta**2) * strict_precision * recall / denom

    return {
        "f_beta": f_beta,
        "strict_precision": strict_precision,
        "recall": recall,
        "net_tp": net_tp,
        "tp": tp,
        "selected_easy": selected_easy,
        "selected_hard": selected_hard,
    }


def evaluate_file(
    result_file: str,
    limit: int | None = None,
    beta: float = 1.0,
    easy_weight: float = 1.0,
    hard_weight: float = 0.5,
) -> Dict[str, float]:
    f_scores: List[float] = []
    precisions: List[float] = []
    recalls: List[float] = []

    with open(result_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if limit is not None and idx > limit:
                break
            item = json.loads(line)
            parsed = parse_prediction_json(item.get("predict_answer", ""))
            pred = normalize_option_answer(parsed.get("answer") if parsed else [])

            scores = evaluate_question_strict_risk_aware(
                pred_answer=pred,
                label=item.get("label", []),
                easy_error=item.get("easy_error", []),
                hard_error=item.get("hard_error", []),
                beta=beta,
                easy_weight=easy_weight,
                hard_weight=hard_weight,
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
    parser = argparse.ArgumentParser(description="Evaluate Task 3/4 with Strict Risk-Aware MF_beta.")
    parser.add_argument("--result-file", required=True, help="Path to a JSONL prediction file.")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of samples to evaluate.")
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--easy-weight", type=float, default=1.0)
    parser.add_argument("--hard-weight", type=float, default=0.5)
    args = parser.parse_args()

    scores = evaluate_file(
        result_file=args.result_file,
        limit=args.limit,
        beta=args.beta,
        easy_weight=args.easy_weight,
        hard_weight=args.hard_weight,
    )
    print(f"Strict_F1: {scores['strict_f1'] * 100:.2f}")
    print(f"Strict_Precision: {scores['strict_precision'] * 100:.2f}")
    print(f"Recall: {scores['recall'] * 100:.2f}")


if __name__ == "__main__":
    main()
