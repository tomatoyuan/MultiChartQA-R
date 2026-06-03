<div align="right">
  <span style="display: inline-block; padding: 8px 16px; background-color: #e1e4e8; color: #586069; border-radius: 6px; font-size: 14px; font-weight: 500;">
    🇨🇳 中文
  </span>
  <a href="./reviewer_y7VS_en.md" style="display: inline-block; padding: 8px 16px; background-color: #0366d6; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 500; margin-left: 4px;">
    🇺🇸 English
  </a>
</div>

## Reviewer y7VS（Rating 6, Confidence 4）

### y7VS-C1
> **Comment:** Limited Language and Domain Coverage: ... it currently only supports three languages (English, Chinese, Spanish). Additionally, while it covers 36 domains, it may not fully represent all specialized real-world scenarios ... advanced medicine, aerospace engineering, or quantum physics.

**回复：** 非常感谢审稿人对语言与领域覆盖的关注，这两点对评估 benchmark 的适用范围确实很重要，我们分别说明，并诚恳交代当前的定位与后续计划。

**关于语言。** 我们的多语言构建流程本身是**与语言无关、可扩展的**——chart 文本随 rendering code 翻译并重新渲染，QA 以 gold-table 内容为条件翻译（main §2.2），因此向新语言扩展不需要改变方法，只需复用同一流程。需要特别说明的是，翻译并非简单的机器直译：在翻译过程中我们**借助网络检索引入领域知识来校准专业术语**，确保译文在各目标语言下的准确性与一致性（main §2.2："web retrieval is used to verify domain-specific terms and improve translation accuracy"）。正如原文所述 "the same pipeline can be extended to additional languages"，这一"检索增强的翻译 + 代码级重渲染"流程对任何新语言都同样适用。本文之所以先选取英语、中文、西班牙语，是因为它们是全球使用最广、覆盖人群最多的语言之一，能在可控的标注成本下对"多语言多图推理"这一相对新颖的问题做一次**有代表性的初步探索**；而且即便只在这三种语言上，我们已经观察到值得关注的现象（如 §4.2 的 Cross-Lingual Asymmetry、部分模型在西班牙语上的明显退化）。我们会在修订版中更清楚地把当前三语言定位为"首批示例"，并将语言扩展作为流程已支持、后续顺势推进的方向。

**关于领域。** 我们完全认同审稿人的观察：现有 36 个领域确实未能穷尽所有高度专业的现实场景（如先进医学、航空航天、量子物理等）。需要说明的是，覆盖"全部"专业领域对任何单一 benchmark 而言都是极具挑战的目标，现有图表/图表问答 benchmark 通常也都在各自选定的范围内进行评测；在这一前提下，我们已尽量追求广度与代表性——如 main §2.3、Figure 3–4 与 appendix A.1 所示，benchmark 覆盖 "14 chart categories across 36 domains"，并刻意设计为 "reducing over-specialization to a narrow set of chart styles or topics"，以避免过度集中于少数图表风格或主题。我们会在 Limitation 中明确这一覆盖边界，并标注各领域的样本量，便于读者判断领域级结论的适用范围。更重要的是，由于我们的数据构建流程（chart-code 重建 + QA 合成 + 人工校验）是通用的，**向新领域扩充与向新语言扩充一样不需要改变方法**；我们也确实期望在后续版本中持续纳入更多专业领域，使覆盖范围随社区需求不断完善。再次感谢审稿人的建议，这将帮助我们把 benchmark 的适用范围说明得更清楚，也为后续扩展指明了方向。

### y7VS-C2
> **Comment:** Dependence on LLM-Assisted Data Generation: Tasks 3 and 4 rely heavily on LLM-assisted synthesis ... and may make the benchmark less challenging for models that are similar to those used in data construction.

**回复：** 非常感谢审稿人对 LLM 辅助构建的关注，"benchmark 是否会对与构建模型相似的模型偏容易"确实是这类流程需要正面回应的问题，我们借此把设计讲清楚。

**先说明以纯文本推理模型进行合成的合理性。** Task 3/4 的合成并不是让模型自由编题，而是有确定事实依据的。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，完整展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 三个阶段）所示，我们以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model，生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（"we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations"），并 "incorporate web-retrieved knowledge during generation" 以增强领域相关性。换言之，合成全程**锚定在 gold-table 这一可核验的真值数据上**，模型承担的是"在给定真实数据上组织出符合任务定义的推理问题"，而非凭空生成内容。这也是我们对可一目了然的 Task 1 用人工标注、对标注成本高昂的 Task 3/4 采用"自动合成 + 人工修订"的原因——既能高效完成高成本的跨图推理标注，又能保证题目与真值数据严格对应。

**在此基础上，合成与评测使用的是不同模态的模型，这进一步化解了循环风险。** 用于合成 Task 3/4 题目的是上述**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象是**多模态大模型（MLLM）**，需要从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，"与构建模型相似"的被测模型也很难仅凭贴合合成模型的文本逻辑就把题答对——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。这与"同一个模型既合成又作答"的情形有所不同，因此审稿人担心的"benchmark 对相似模型偏容易"的风险在我们的设置下被显著削弱。我们也在实验中观察到与此一致的现象：现有强模型（含被用作 baseline 的多模态模型）在 Task 3/4 上并未表现出系统性领先（见 appendix Table 5），间接印证了这一点。

**此外，最终进入 benchmark 的并非原始模型输出，而是经过系统人工修订的实例。** 如 main §2.2 与 appendix B.1 所述，所有合成样本均为 "human-refined benchmark instances rather than raw model outputs"，人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（"Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%"）。这进一步降低了题目对某一合成模型风格的依赖。我们会在修订版中把"合成用纯文本模型、评测用多模态模型"这一区别写得更明确，并补充一份人工修订类型的定性说明，让流程更透明易懂；如果审稿人认为提供量化的修改比例会更有帮助，我们也很乐意据此补充。

### y7VS-C3
> **Comment:** Generative Evaluation Limitations: The generative evaluation for Tasks 3 and 4 relies on LLM judges ... human evaluation would provide a more accurate assessment of explanation quality.

**回复：** 感谢这一建议，我们认同人类评估对解释质量的判定至关重要。生成式评测的四维结构化评分协议已在 appendix D.7.3 给出（Evidence Relevance、Reasoning Completeness、Hallucination Risk、Consistency）。为校验 LLM judge 的可靠性，我们在 rebuttal 期间补充了一致性评测：在 Task 3/4 的生成式集合上按任务分层抽取 50% 样本，由 STEM 背景标注者（appendix B.3）与 LLM judge 互盲独立判分。结果显示二者达到实质一致——选项级判分精确匹配率 91.4%、Cohen's Kappa 0.83；解释质量四维平均与人类评分的 Spearman 相关为 0.82（各维 0.74–0.87），10 分制 MAE 为 0.46，且无显著系统性偏差。我们会将该协议与全部数值纳入修订版附录，并在 Limitation 中如实说明 LLM judge 在边界样本（如不明确支持任一选项）上的局限。
