from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Dict, List

import requests

from data_utils import load_main_benchmark
from prompts import get_task_prompt


def encode_image(image_path: str) -> Dict:
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    return {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}


def build_messages(sample: Dict, language: str) -> List[Dict]:
    question = sample["question"]
    task_id = sample["task_id"]
    answer_choices = sample["answer"] if task_id in (3, 4) and isinstance(sample["answer"], dict) else None
    prompt = get_task_prompt(language=language, task_id=task_id, question=question, answer_choices=answer_choices)

    content = [{"type": "text", "text": prompt}]
    for image_path in sample["charts_involved"]:
        content.append(encode_image(image_path))
    return [{"role": "user", "content": content}]


def call_openai_compatible_api(model_name: str, messages: List[Dict]) -> Dict:
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
            "messages": messages,
            "temperature": 0,
            "max_tokens": 4096,
        },
        timeout=180,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Minimal API inference template for MultiChartQA-R.")
    parser.add_argument("--model", required=True, help="Model name for an OpenAI-compatible endpoint.")
    parser.add_argument("--task", type=int, choices=[1, 2, 3, 4], required=True)
    parser.add_argument("--language", choices=["cn", "en", "es"], default="en")
    parser.add_argument("--sample-index", type=int, default=0, help="Zero-based sample index inside the task split.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    benchmark = load_main_benchmark(language=args.language, benchmark_root=repo_root / "benchmark")
    sample = benchmark[args.task][args.sample_index]
    messages = build_messages(sample, args.language)
    result = call_openai_compatible_api(args.model, messages)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
