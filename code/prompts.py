from __future__ import annotations

from typing import Dict


TASK_OUTPUT_PROMPTS: Dict[str, Dict[int, str]] = {
    "cn": {
        1: (
            "\n请按照下面的 JSON 格式输出：\n"
            '{\n  "rationale": "推理过程",\n  "answer": "最终答案"\n}\n'
            "请严格输出合法 JSON。\n"
        ),
        2: (
            "\n请按以下步骤回答，且不要省略关键细节：\n"
            "1. 提取相关信息，并说明各数据来自哪张图表。\n"
            "2. 解释为什么需要这些数据。\n"
            "3. 写出详细计算过程。\n"
            "4. 按题目要求给出最终答案。\n"
        ),
        3: (
            "\n请根据图表内容回答，并按照下面的 JSON 格式输出：\n"
            '{\n  "rationale": "基于图表证据的推理过程",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            "answer 字段只保留你判断为正确的选项字母，不要模仿固定选项模式。\n"
        ),
        4: (
            "\n请根据图表内容回答，并按照下面的 JSON 格式输出：\n"
            '{\n  "rationale": "基于图表证据的推理过程",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            "answer 字段只保留你判断为正确的选项字母，不要模仿固定选项模式。\n"
        ),
    },
    "en": {
        1: (
            "\nPlease answer in the following JSON format:\n"
            '{\n  "rationale": "Reasoning process",\n  "answer": "Final answer"\n}\n'
            "Please output valid JSON only.\n"
        ),
        2: (
            "\nPlease answer with the following steps and include all key details:\n"
            "1. Extract the relevant information and identify which chart each value comes from.\n"
            "2. Explain why these data are needed.\n"
            "3. Write out the calculation process.\n"
            "4. Provide the final answer in the format required by the question.\n"
        ),
        3: (
            "\nAnswer the question in the following JSON format:\n"
            '{\n  "rationale": "Reasoning process grounded in the chart evidence",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            'The "answer" field should contain only the option letters you judge to be correct. '
            "Do not imitate any fixed option pattern.\n"
        ),
        4: (
            "\nAnswer the question in the following JSON format:\n"
            '{\n  "rationale": "Reasoning process grounded in the chart evidence",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            'The "answer" field should contain only the option letters you judge to be correct. '
            "Do not imitate any fixed option pattern.\n"
        ),
    },
    "es": {
        1: (
            "\nResponde en el siguiente formato JSON:\n"
            '{\n  "rationale": "Proceso de razonamiento",\n  "answer": "Respuesta final"\n}\n'
            "Genera únicamente JSON válido.\n"
        ),
        2: (
            "\nResponde con los siguientes pasos e incluye todos los detalles clave:\n"
            "1. Extrae la información relevante e indica de qué gráfico proviene cada dato.\n"
            "2. Explica por qué se necesitan esos datos.\n"
            "3. Escribe el proceso de cálculo.\n"
            "4. Da la respuesta final en el formato requerido por la pregunta.\n"
        ),
        3: (
            "\nResponde la pregunta en el siguiente formato JSON:\n"
            '{\n  "rationale": "Proceso de razonamiento basado en la evidencia de los gráficos",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            'El campo "answer" debe contener solo las letras de las opciones correctas. '
            "No imites ningún patrón fijo de respuestas.\n"
        ),
        4: (
            "\nResponde la pregunta en el siguiente formato JSON:\n"
            '{\n  "rationale": "Proceso de razonamiento basado en la evidencia de los gráficos",\n  "answer": ["option_letter_1", "option_letter_2"]\n}\n'
            'El campo "answer" debe contener solo las letras de las opciones correctas. '
            "No imites ningún patrón fijo de respuestas.\n"
        ),
    },
}


TASK2_CODE_PROMPTS: Dict[str, str] = {
    "cn": (
        "上面是推理过程。请忽略其中的中间计算结果，把该过程改写为可执行的 Python 代码。\n"
        "要求：严格遵循推理步骤；使用变量重新计算中间值；最终只输出题目要求的答案；"
        "若涉及浮点运算，请优先使用 decimal 库。"
    ),
    "en": (
        "The text above is a reasoning process. Ignore the intermediate numeric results and rewrite it as executable "
        "Python code. Follow the reasoning steps faithfully, recompute intermediate values with variables, and print "
        "only the final answer in the format required by the question. Prefer the decimal library for floating-point calculations."
    ),
    "es": (
        "El texto anterior es un proceso de razonamiento. Ignora los resultados numéricos intermedios y reescríbelo "
        "como código Python ejecutable. Sigue fielmente los pasos del razonamiento, vuelve a calcular los valores "
        "intermedios con variables y muestra solo la respuesta final en el formato exigido por la pregunta. "
        "Si hay cálculos de punto flotante, utiliza preferentemente la biblioteca decimal."
    ),
}


HINTS: Dict[str, str] = {
    "cn": "（多选题）请基于图表证据选择正确选项。没有图表依据的选项应视为错误。",
    "en": "(Multiple-choice question) Select the correct options based on chart-grounded evidence. "
    "Options without chart support should be treated as incorrect.",
    "es": "(Pregunta de selección múltiple) Selecciona las opciones correctas con base en la evidencia de los gráficos. "
    "Las opciones sin respaldo en los gráficos deben tratarse como incorrectas.",
}


OPTIONS_PREFIX: Dict[str, str] = {
    "cn": "选项如下：\n",
    "en": "The options are:\n",
    "es": "Las opciones son:\n",
}


def get_task_prompt(language: str, task_id: int, question: str, answer_choices: Dict[str, str] | None = None) -> str:
    if language not in TASK_OUTPUT_PROMPTS:
        raise ValueError(f"Unknown language: {language}")
    if task_id not in TASK_OUTPUT_PROMPTS[language]:
        raise ValueError(f"Unknown task id: {task_id}")

    prompt = question + TASK_OUTPUT_PROMPTS[language][task_id]
    if task_id in (3, 4):
        if not answer_choices:
            raise ValueError("answer_choices are required for multi-select tasks.")
        options = "\n".join(f"{letter}: {text}" for letter, text in sorted(answer_choices.items()))
        prompt = HINTS[language] + "\n" + question + "\n" + OPTIONS_PREFIX[language] + options + TASK_OUTPUT_PROMPTS[language][task_id]
    return prompt


def get_task2_code_prompt(language: str) -> str:
    if language not in TASK2_CODE_PROMPTS:
        raise ValueError(f"Unknown language: {language}")
    return TASK2_CODE_PROMPTS[language]

