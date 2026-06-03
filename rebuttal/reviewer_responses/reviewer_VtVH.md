<div align="right">
  <span style="display: inline-block; padding: 8px 16px; background-color: #e1e4e8; color: #586069; border-radius: 6px; font-size: 14px; font-weight: 500;">
    🇨🇳 中文
  </span>
  <a href="./reviewer_VtVH_en.md" style="display: inline-block; padding: 8px 16px; background-color: #0366d6; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 500; margin-left: 4px;">
    🇺🇸 English
  </a>
</div>

## Reviewer VtVH（Rating 7, Confidence 4）

### VtVH-C1
> **Comment:** Tasks 3 and 4 rely heavily on "frontier reasoning models" for synthesis. Since the same or similar models (GPT-4o, Claude) are used as baselines, there is a risk that the benchmark measures model alignment to GPT-generated logic rather than objective reasoning. ... What percentage of the GPT-synthesized questions for Tasks 3 and 4 were significantly modified by human annotators?

**回复：** 非常感谢审稿人对 Task 3/4 合成流程严谨性的关注，"benchmark 是否只是在测量对 GPT 生成逻辑的对齐、而非客观推理"是一个很关键的问题，我们借此把设计依据讲清楚。

**首先想说明以推理模型进行合成的合理性。** Task 3/4 的合成并不是让模型自由编题，而是有确定事实依据的。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，完整展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 三个阶段）所示，我们以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model，生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（"we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations"），并 "incorporate web-retrieved knowledge during generation" 以增强领域相关性。也就是说，合成全程**锚定在 gold-table 这一可核验的真值数据上**，模型承担的是"在给定真实数据上组织出符合任务定义的推理问题"，而非凭空编造内容——这正是我们对成本高昂的 Task 3/4 采用"自动合成 + 人工修订"、而对可一目了然的 Task 1 用人工标注的原因。

**其次，关于审稿人最关心的循环风险，这里有一个我们此前可能没有交代清楚的设计细节：合成与评测使用的是不同模态的模型。** 用于合成 Task 3/4 题目的是一个**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象（包括作为 baseline 的 GPT-4o、Claude 等）是**多模态大模型（MLLM）**，必须从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，被测模型很难仅凭"贴合合成模型的文本逻辑"就拿到高分——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。因此这与"同一个模型既合成又作答"的自偏好情形有本质区别。这一点也有实验证据间接印证：作为 baseline 的 GPT-4o、Claude 等并未在 Task 3/4 上表现出系统性领先（GPT-4o 多处于中后段，见 appendix Table 5），与"benchmark 偏向生成逻辑"的预期相反，说明其测量的并非对生成模型逻辑的对齐。在修订版中，我们会把"合成用纯文本模型、评测用多模态模型"这一关键区别直接补入 §2.2 的数据构建段落，并在 appendix 注明合成所用模型的具体配置，使读者无需推断即可确认二者的模态差异。

**关于"被显著修改题目的百分比"。** 我们完全理解审稿人希望了解人工介入到何种程度——这在评估数据质量时是很自然的关切。这里想和审稿人交流一点我们的考虑：人工修订的目标是确保**最终发布实例**的质量，最终进入 benchmark 的都是 "human-refined benchmark instances rather than raw model outputs"（main §2.2）。也就是说，无论某条题目是经过大幅改写还是仅作微调，都需通过统一的质量标准才会入库，benchmark 的可靠性主要取决于成品质量，而这一点已有较直接的证据支撑：appendix B.1 说明人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（"Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%"）。考虑到"显著修改占比"本身较难给出统一的判定口径、单看该比例也未必能反映成品质量，我们更倾向于在附录新增一小节，按上述四个修订方面各给出"修订前 → 修订后"的典型对照示例，直观呈现人工介入的方式与作用。若审稿人认为量化的修改比例仍有必要，我们也很乐意在其指定的判定口径下统计并一并补入该小节。

### VtVH-C2
> **Comment:** With 2,160 QA pairs per language, the dataset is respectable but relatively small ... some domains may have very sparse representation, limiting the statistical power of domain-specific insights. In Task 4, did you find cases where the LLM Judge ... disagreed with human experts on ... Reasoning Completeness? How did you define the boundary between Easy and Hard distractors during the synthesis phase to ensure consistency across the 36 domains?

**回复：** 非常感谢审稿人如此细致地从规模、领域稀疏性、评测一致性到 Easy/Hard 边界提出了一系列建设性问题——这些都直指 benchmark 的可信度，我们逐一认真回应。

**（1）规模与统计稳健性。** 我们理解每语言 2,160 QA（每任务约 540）在绝对数量上看起来并不算大；这一规模主要源于多图推理实例的标注与质控成本远高于单图 QA——每条实例都需要在多张图之间建立可核验的推理链并经人工修订。按 QA 同口径来看，本文规模实际与同期 benchmark 相当甚至更高（高于 ChartQAPro 的 1,948、MultiChartQA 的 2,000）。更关键的是规模是否足以支撑稳定的结论，为此我们补充了一项**半采样稳定性实验**：按任务分层随机抽取 50% 样本、重复 100 次，三种语言下 Spearman ≥ 0.986、Top-3 重合 0.98–1.00、平均排名变化 < 0.4 位。这表明即便只用一半数据，模型排序与主要结论依然高度稳定，现有规模已足以支撑论文的核心论断。对于个别样本稀疏的领域，我们完全认同其统计功效有限，会在修订版的结果表中为每个领域标注样本量 n，并把样本量偏少的领域结论统一标注为"探索性观察（指示性、非确证）"，让读者一眼即可分辨哪些领域级结论可以放心解读。

**（2）Easy/Hard 边界的跨领域一致性。** 这是一个很好的问题。需要先说明的是，Easy/Hard 的划分并非逐领域分别设定，而是在 **Figure 2（The Construction Pipeline of MultiChartQA-R）** 的 question-answer pair construction 阶段就已统一固化进 pipeline——该图直接图示了正确选项与两类干扰项是如何生成的、以及每题的选项数量设置。对应的语义判据在 main §2.2 中有明确文字表述：干扰项被设计为两个难度等级，Easy distractors "either do not use chart data or contain clearly incorrect conclusions"；Hard distractors "involve either correct data interpretation with rigorous reasoning but an incorrect conclusion, or misinterpreted chart data combined with seemingly rigorous reasoning"。可见这一判据针对的是"干扰项与图表证据/推理之间的关系"，是**与具体领域内容无关的**，因而天然适用于跨领域的一致划分。在按 pipeline 生成之后，所有干扰项还会经人工按同一标准统一复核（main §2.2："Human annotators finally review and revise the synthesized data to ensure validity and quality"），进一步保证不同领域间难度口径的一致。

**（3）Task 4 中 LLM Judge 与人类在 Reasoning Completeness 上的分歧。** 感谢审稿人特别点到这一维度（定义见 appendix D.7.3）——它确实是四个维度中最依赖主观判断的一个。为正面回答这一问题，我们在 rebuttal 期间专门补充了一项 **50% 抽样的判分一致性评测**，结果显示：Reasoning Completeness 恰好是相关性相对最低的一维（Spearman ≈ 0.74，低于其余三维的 0.83–0.87），LLM judge 相对人类专家在此维度略偏严格（平均低约 0.1 分），分歧主要集中在"回答未明确支持任一选项"的边界样本上。即便如此，整体一致性仍达到**实质一致**水平（解释质量平均 Spearman 0.82、选项级判分 Cohen's Kappa 0.83、精确匹配率 91.4%）。这项一致性评测的协议与逐维数值已经整理完毕，将作为附录 D.7.3 之后的一个新小节纳入修订版；我们还会在该处明确标出 Reasoning Completeness 在 NONE 边界样本上的已知局限，使读者清楚生成式评测在何种情形下最可靠、在何种情形下需谨慎解读。

### VtVH-C3
> **Comment:** The weights for the Risk-Aware metric appear somewhat heuristic. The paper would benefit from a sensitivity analysis or a more formal justification or why these specific penalties reflect real-world risk.

**回复：** 非常感谢审稿人对评测指标的关注，"权重是否过于启发式"是一个非常合理的问题，我们希望借此说明这些权重既有原则性的设计依据、也经过了系统的稳健性检验。

**首先，权重并非随意设定，而是依据 benchmark 的标注设计预先确定的。** 如 appendix D.2 所述，权重是 "determined from the benchmark's annotation design before model-level analysis"——即在任何模型层面的分析之前就已固定，而非为最大化某个模型的排名而事后调参。其设计直觉是：在面向决策的现实场景中，"看似严谨却得出错误结论"的 hard error，其潜在危害远大于"明显离谱"的 easy error，因此理应受到更重的惩罚。这一现实风险对应关系在 appendix D.4 中有明确表述："severe errors actively deduct from the model's score... This mirrors high-stakes decision-making, where a single fatal flaw can render a strategy unusable"。指标的形式化定义与各权重的语义见 appendix D.3（式 5–9）。

**其次，针对审稿人建议的敏感性分析，我们已在论文附录中做过探索，并在 rebuttal 中进一步系统化。** appendix D（Figures 5–6）已绘制了所有模型的 MFβ 曲线，展示了不同 β 取值下分数的变化与模型间的交叉关系（例如 InternVL2-26B 对 β 较为敏感的案例）。在此基础上，我们补充了一项更全面的**权重敏感性实验**：在 16 个模型 × 3 种语言上扫描 9 组不同的权重配置。结果显示模型排名高度稳健——Top-1 始终为 claude-sonnet-4，Top-3 几乎不变，最大排名变化仅 0–3 位，论文采用的默认设置恰好落在"排名稳定的平台区间"内。这说明结论并不依赖于某一组特定权重。

**最后想补充说明的是，论文给出的只是一个"中庸的"默认设置，使用者完全可以按实际场景调节。** 对风险更敏感的场景可调高 β 或 hard-error 权重，对惩罚要求较宽松的场景则反之；而上述敏感性实验恰恰表明，在合理的调节区间内模型排名依然稳定。基于此，修订版会在指标小节明确补上两点：一是说明默认权重的来源（依标注设计预先确定），二是附上敏感性实验的排名稳定性结果（含权重—排名对照表），并把 β/w 定位为"可按风险偏好调节的参数"而非固定常数。我们认为这恰好把审稿人指出的"启发式"顾虑，转化为该指标的一项可解释、可配置的优点。

### VtVH-C4
> **Comment:** While the paper includes modern models like Qwen3 and Gemini 2.5, it lacks a Modular Baseline. ... How does a pipeline of (State-of-the-art Chart-to-Table) + (GPT-4o) perform on this benchmark compared to the end-to-end MLLM approach?

**回复：** 非常感谢审稿人提出这一很有价值的建议。我们完全认同，模块化基线 (SOTA Chart-to-Table) + (GPT-4o) 与端到端 MLLM 的对照很有意义，并想借此分享我们对这两条技术路线关系的一点理解。

**我们认为，图表理解的总体发展方向是从"多阶段模块化"逐步向"端到端"演进。** 端到端 MLLM 的理想形态是直接从图像完成感知与推理的联合建模，这也是社区长期追求的目标；但就现状而言，端到端模型在跨图、需要精确读数与复杂推理的场景下仍不够成熟（这正是本 benchmark 想要揭示的难点）。也正因如此——**当端到端方案尚不足以稳定产出高质量标注时，我们在构造数据的 pipeline 中反而刻意采用了多阶段的方案**：先通过 chart-code 重建拿到可核验的 gold-table，再以纯文本推理模型在确定的真值数据上合成 QA，并辅以人工修订。这样做的目的，恰恰是借助多阶段的可控性来获得比端到端直接生成更高质量、更可靠的数据。换言之，多阶段方案在我们这里承担的是"高质量数据生产工具"的角色，而 benchmark 真正要评测和推动的，是端到端 MLLM 在这些高质量数据上的能力上限。

**这一视角也有助于理解为何评测以端到端 MLLM 为主体。** 既然领域目标是让端到端模型最终具备完整的"感知—推理"能力，benchmark 自然应以端到端表现作为衡量进展的标尺；而审稿人提到的模块化基线，则是一个很好的**参照系**，用以量化"当前端到端模型相比'先转表再推理'还差多少、差在哪个环节"。

在此基础上，我们非常愿意按审稿人的建议补充一组 (SOTA Chart-to-Table) + (GPT-4o) 的模块化基线，与端到端 MLLM 在四个任务上逐项对照，并按"转表环节误差 / 下游推理误差"对失败案例做归因拆分，作为衡量端到端路线进展的参照。这组对照将与端到端结果并列进入主结果表，相关讨论补入实验分析一节。这样既直接回应了审稿人的问题，也让"多阶段构建数据、端到端评测能力"这一设计取向在论文中更加清晰自洽。
