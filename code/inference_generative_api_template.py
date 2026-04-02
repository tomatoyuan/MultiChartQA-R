from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Dict, List

import requests


GENERATIVE_PROMPTS = {
    "cn": {
        3: "请直接基于图表进行分析并给出结论，不要看到候选选项。输出 JSON：{\"rationale\": \"推理过程\", \"answer\": \"最终分析结论\"}。",
        4: "请直接基于图表给出策略分析与结论，不要看到候选选项。输出 JSON：{\"rationale\": \"推理过程\", \"answer\": \"最终分析结论\"}。",
    },
    "en": {
        3: 'Analyze the charts directly without seeing the candidate options. Output JSON: {"rationale": "Reasoning process", "answer": "Final analysis"}.',
        4: 'Produce a strategy-oriented analysis directly from the charts without seeing the candidate options. Output JSON: {"rationale": "Reasoning process", "answer": "Final analysis"}.',
    },
    "es": {
        3: 'Analiza los gráficos directamente sin ver las opciones candidatas. Devuelve JSON: {"rationale": "Proceso de razonamiento", "answer": "Análisis final"}.',
        4: 'Produce un análisis orientado a la estrategia directamente a partir de los gráficos, sin ver las opciones candidatas. Devuelve JSON: {"rationale": "Proceso de razonamiento", "answer": "Análisis final"}.',
    },
}


def encode_image(image_path: str) -> Dict:
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    return {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}


def load_task_samples(language: str, task_id: int, benchmark_root: str | Path = "../benchmark") -> List[Dict]:
    benchmark_root = Path(benchmark_root)
    json_root = benchmark_root / "json" / language
    image_root = benchmark_root / "images" / language
    type_map = {3: "4", 4: "5"}
    raw_type = type_map[task_id]

    samples: List[Dict] = []
    for json_path in sorted(json_root.glob("*.json"), key=lambda p: int(p.stem)):
        with json_path.open("r", encoding="utf-8") as f:
            content = json.load(f)
        for qa_pair in content["qa_pairs"]:
            if str(qa_pair["type"]) != raw_type:
                continue
            item = dict(qa_pair)
            item["task_id"] = task_id
            item["file_name"] = json_path.name
            item["charts_involved"] = [str(image_root / f"{chart_name}.png") for chart_name in item["charts_involved"]]
            samples.append(item)
    return samples


def build_messages(sample: Dict, language: str) -> List[Dict]:
    prompt = sample["question"] + "\n" + GENERATIVE_PROMPTS[language][sample["task_id"]]
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
    parser = argparse.ArgumentParser(description="Minimal generative inference template for Task 3/4.")
    parser.add_argument("--model", required=True, help="Model name for an OpenAI-compatible endpoint.")
    parser.add_argument("--task", type=int, choices=[3, 4], required=True)
    parser.add_argument("--language", choices=["cn", "en", "es"], default="en")
    parser.add_argument("--sample-index", type=int, default=0, help="Zero-based sample index inside the task split.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    samples = load_task_samples(language=args.language, task_id=args.task, benchmark_root=repo_root / "benchmark")
    sample = samples[args.sample_index]
    messages = build_messages(sample, args.language)
    result = call_openai_compatible_api(args.model, messages)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
