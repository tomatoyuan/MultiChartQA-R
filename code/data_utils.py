from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


MAIN_TASK_TYPE_TO_ID = {"2": 1, "3": 2, "4": 3, "5": 4}


def _sorted_json_files(data_dir: Path) -> List[Path]:
    return sorted(data_dir.glob("*.json"), key=lambda p: int(p.stem))


def _chart_paths(image_root: Path, chart_names: Sequence[str]) -> List[str]:
    return [str(image_root / f"{chart_name}.png") for chart_name in chart_names]


def load_main_benchmark(language: str = "en", benchmark_root: str | Path = "../benchmark") -> Dict[int, List[Dict]]:
    """Load the main benchmark and regroup QA pairs by released task id (1-4)."""
    benchmark_root = Path(benchmark_root)
    json_root = benchmark_root / "json" / language
    image_root = benchmark_root / "images" / language

    task_buckets: Dict[int, List[Dict]] = {1: [], 2: [], 3: [], 4: []}
    for json_path in _sorted_json_files(json_root):
        with json_path.open("r", encoding="utf-8") as f:
            content = json.load(f)

        for qa_pair in content["qa_pairs"]:
            released_task_id = MAIN_TASK_TYPE_TO_ID[str(qa_pair["type"])]
            item = dict(qa_pair)
            item["task_id"] = released_task_id
            item["file_name"] = json_path.name
            item["charts_involved"] = _chart_paths(image_root, item["charts_involved"])
            task_buckets[released_task_id].append(item)

    return task_buckets


def load_extended_benchmark(benchmark_root: str | Path = "../benchmark-extended") -> Dict[str, List[Dict]]:
    """Load the retrieval-oriented extended benchmark."""
    benchmark_root = Path(benchmark_root)
    buckets: Dict[str, List[Dict]] = {
        "parallel_pcpc": [],
        "parallel_pcmc": [],
        "union_pcpc": [],
        "union_pcmc": [],
    }
    order = list(buckets.keys())

    for paper_dir in sorted(p for p in benchmark_root.iterdir() if p.is_dir()):
        qa_pairs_path = paper_dir / "qa_pairs.json"
        with qa_pairs_path.open("r", encoding="utf-8") as f:
            qa_groups = json.load(f)

        for bucket_name, qa_group in zip(order, qa_groups):
            for qa_pair in qa_group["qa_pairs"]:
                item = dict(qa_pair)
                item["paper_dir"] = paper_dir.name
                item["charts_involved"] = _extended_chart_paths(paper_dir, item["involved_content_sources"])
                buckets[bucket_name].append(item)

    return buckets


def split_extended_by_chart_count(qa_pairs: Sequence[Dict]) -> Tuple[List[Dict], List[Dict], List[Dict]]:
    two_chart, three_chart, four_chart = [], [], []
    for item in qa_pairs:
        chart_count = str(item["chart_count"])
        if chart_count == "2":
            two_chart.append(item)
        elif chart_count == "3":
            three_chart.append(item)
        else:
            four_chart.append(item)
    return two_chart, three_chart, four_chart


def _extended_chart_paths(paper_dir: Path, content_sources: Sequence[str]) -> List[str]:
    chart_paths = set()
    for source in content_sources:
        chart_idx = source.split("-")[0].split("_")[-1]
        chart_paths.add(str(paper_dir / f"image_{chart_idx}.png"))
    return sorted(chart_paths)

