from __future__ import annotations

import argparse
import json
from typing import Any

from parse_predictions import parse_prediction_json


def normalize_binary_answer(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"yes", "是", "sí", "si"}:
        return "yes"
    if text in {"no", "否"}:
        return "no"
    return text or None


def evaluate_file(result_file: str, limit: int | None = None) -> float:
    total = 0
    correct = 0
    with open(result_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if limit is not None and idx > limit:
                break
            item = json.loads(line)
            gold = normalize_binary_answer(item["answer"])
            parsed = parse_prediction_json(item.get("predict_answer", ""))
            pred = normalize_binary_answer(parsed.get("answer") if parsed else None)
            total += 1
            if gold is not None and pred == gold:
                correct += 1
    return 0.0 if total == 0 else correct / total


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Task 1 (trend inference) accuracy.")
    parser.add_argument("--result-file", required=True, help="Path to a JSONL prediction file.")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of samples to evaluate.")
    args = parser.parse_args()

    accuracy = evaluate_file(args.result_file, args.limit)
    print(f"Task 1 accuracy: {accuracy * 100:.2f}")


if __name__ == "__main__":
    main()
