from __future__ import annotations

import json
import re
from typing import Any, Dict, Iterable, List


def clean_json_string(raw_text: str) -> str:
    if not isinstance(raw_text, str):
        return ""

    fenced = re.search(r"```json\s*([\s\S]*?)\s*```", raw_text)
    if fenced:
        raw_text = fenced.group(1)
    else:
        brace_start = raw_text.find("{")
        brace_end = raw_text.rfind("}")
        if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
            raw_text = raw_text[brace_start : brace_end + 1]
        else:
            return ""

    raw_text = re.sub(r"//.*$", "", raw_text, flags=re.M)
    raw_text = re.sub(r"/\*.*?\*/", "", raw_text, flags=re.S)
    return raw_text.strip()


def parse_prediction_json(raw_text: str) -> Dict[str, Any] | None:
    cleaned = clean_json_string(raw_text)
    if not cleaned:
        return None
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return _parse_prediction_json_fallback(cleaned)


def _parse_prediction_json_fallback(cleaned: str) -> Dict[str, Any] | None:
    result: Dict[str, Any] = {}

    rationale_match = re.search(r'"rationale"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned, flags=re.S)
    if rationale_match:
        result["rationale"] = re.sub(r"\\(.)", r"\1", rationale_match.group(1))

    list_match = re.search(r'"answer"\s*:\s*\[(.*?)\]', cleaned, flags=re.S)
    if list_match:
        result["answer"] = re.findall(r'"([^"]*)"', list_match.group(1))
    else:
        scalar_match = re.search(r'"answer"\s*:\s*"((?:[^"\\]|\\.)*)"', cleaned, flags=re.S)
        if scalar_match:
            result["answer"] = re.sub(r"\\(.)", r"\1", scalar_match.group(1))

    return result or None


def normalize_option_answer(raw_answer: Any) -> List[str]:
    if isinstance(raw_answer, list):
        return [str(item).strip() for item in raw_answer if str(item).strip()]
    if isinstance(raw_answer, str):
        text = raw_answer.strip()
        if not text:
            return []
        letters = re.findall(r"[A-Z]", text.upper())
        return letters or [part.strip() for part in re.split(r"[,\s]+", text) if part.strip()]
    return []

