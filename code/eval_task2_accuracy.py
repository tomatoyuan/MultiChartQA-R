from __future__ import annotations

import argparse
import json
from typing import Any

from parse_predictions import parse_prediction_json


def validate_value(expected: Any, actual: Any, tolerance: float = 0.05) -> bool:
    try:
        expected_num = float(str(expected).replace(" ", "").replace("　", "").strip("%"))
        actual_num = float(str(actual).replace(" ", "").replace("　", "").strip("%"))
        if expected_num == 0:
            return actual_num == 0
        return abs(expected_num - actual_num) / abs(expected_num) <= tolerance
    except (TypeError, ValueError):
        expected_text = str(expected).replace(" ", "").replace("　", "").lower()
        actual_text = str(actual).replace(" ", "").replace("　", "").lower()
        return expected_text == actual_text


def evaluate_file(result_file: str, limit: int | None = None) -> float:
    total = 0
    correct = 0
    with open(result_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if limit is not None and idx > limit:
                break
            item = json.loads(line)
            parsed = parse_prediction_json(item.get("predict_answer", ""))
            pred = parsed.get("answer") if parsed else None
            total += 1
            if validate_value(item["answer"], pred):
                correct += 1
    return 0.0 if total == 0 else correct / total


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Task 2 (data integration) accuracy.")
    parser.add_argument("--result-file", required=True, help="Path to a JSONL prediction file.")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of samples to evaluate.")
    args = parser.parse_args()

    accuracy = evaluate_file(args.result_file, args.limit)
    print(f"Task 2 accuracy: {accuracy * 100:.2f}")


if __name__ == "__main__":
    main()
