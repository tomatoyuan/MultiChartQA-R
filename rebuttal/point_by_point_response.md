# Point-by-Point Response / 逐条回复

We sincerely thank all reviewers for their careful reading and constructive comments. 本文档对每位审稿人的每条意见逐条回复：**Comment 保留英文原文，Response 为中文回复。** 凡论文正文或附录已涵盖的内容，我们引用原文作答并标注具体位置；新增的两个补充实验详见 [`supplementary_experiments.md`](./supplementary_experiments.md)。

> 引用约定：`main` 指正文，`appendix.pdf` 指附录 PDF。引文均为论文原句。

整体评分：VtVH=7，JrJk=6，y7VS=6，9osS=5，zF7Z=5（平均 5.8）。

---

## Reviewer 9osS（Rating 5, Confidence 4）

### 9osS-C1
> **Comment:** Although the Strict Risk-Aware metric is motivated and easy to understand, it is still relatively simple. Could the authors provide a sensitivity analysis showing how rankings change under different weight configurations?

**回复：** 非常感谢审稿人的建议，敏感性分析确实能更有力地说明指标的稳健性，我们正是据此补充了相关实验，并结合论文附录已有的探索一并说明如下。

**（1）新增的权重敏感性实验（实验一）。** 我们以论文配置 `e1_h0.5`（`w_e=1.0`、`w_h=0.5`、`β=1`）为基线，在全部 **16 个模型**、**3 种语言**上扫描 **9 组权重配置**（沿 easy/hard 严重度权重与 β 两个方向变化），对每组配置重新计算全部模型的 MFβ 分数与排名，并与基线比较 Top-1、Top-3 命中及最大绝对排名变化。结果显示排名高度稳健：**Top-1 在全部 9 组配置、3 种语言下始终为 claude-sonnet-4，无一例外**；**Top-3 集合几乎完全不变**（仅在最极端配置下 Qwen3-VL-32B 与 gemini-2.5-pro 互换第 3 名）；**最大绝对排名变化在多数配置下仅为 0–1**，即便最极端的 `e0.5_h0.5` 在 en 下也仅为 3、cn 下最大为 1、es 下最大为 2。这说明基线配置并非因"特殊"而被选中，而是落在一个**排名稳定的平台区间**内。

**（2）β 的影响在原论文附录中已有系统探索。** 这部分是对审稿人关切的进一步补强（见 appendix.pdf，Appendix D *Metric Exploration*，pp. 11–13）：D.3（式 5–9）给出 MFβ 的完整定义与固定严重度权重；D.4 给出 β 语义（`β=1` precision/recall 等权，`β>1` 更重规避错误选择，`β<1` 更重覆盖正确选项）；D.5 “Analysis of MFβ Curves” 在 **Figure 5、Figure 6** 中绘制了全部模型在不同 β 下的 MFβ 曲线，并通过曲线**交叉点**分析了不同模型在"召回正确项 vs. 规避错误项"上的权衡及其对场景化模型选择的指导意义（并以 InternVL2-26B 为例说明部分模型对 β 高度敏感）。

**（3）默认配置是"中庸"设置、可按场景调节。** 我们想强调，`e1_h0.5, β=1` 只是一个兼顾直觉合理性与排名稳定性的默认设置，而非唯一正确配置：高风险/高合规场景（如医疗、金融）可调高 β 以更重惩罚错误选择、偏向 precision，探索性场景可调低 β 以更看重召回；亦可按业务对两类错误危害的判断调节 `w_e`、`w_h`。敏感性实验进一步表明，在上述可调区间内模型相对排名依然稳健。完整配置、数据与图表详见 [`supplementary_experiments.md`](./supplementary_experiments.md)；我们会将该敏感性分析表正式纳入修订版附录，紧接现有的 MFβ 曲线分析。

### 9osS-C2
> **Comment:** The dataset is small: 2,160 QA pairs per language, 180 multi-chart sets, 695 charts. Can you explain what led to this size? Does it affect the reliability of your findings? Bootstrap confidence intervals would help.

**回复：** 非常感谢审稿人对数据规模及其可靠性的关注，这两点我们分别说明如下。

**（1）规模构成及其成因。** 如 main Table 1 与 appendix A.1 所述，每个语言版本含 “180 multi-chart sets, 695 chart-code pairs, and 2,160 QA pairs, with 540 instances for each of the four tasks”，且 “On average, each set contains 3.9 charts, reflecting the realistic need to aggregate evidence across multiple visualizations”。规模主要由多图推理实例较高的标注与质控成本决定——与单图 QA 不同，每条实例都需在多张图之间建立可核验的推理链，并经过完整的人工修订与质检（appendix B.1）。需要说明的是，按 QA 同口径横向比较，本文 2,160 并不小于同期工作，高于 ChartQAPro（1,948）与 MultiChartQA（2,000）。

**（2）规模是否影响结论可靠性——半采样稳定性实验（实验二）。** 我们完全认同关键不在绝对数量，而在于规模是否足以支撑稳定结论。为此我们补充了一项稳定性实验：按任务**分层随机抽取 50% 样本**、**重复 100 次**，考察模型排名相对全量结果的波动。结果显示三种语言下排名高度稳定——**Spearman 相关 ≥ 0.986**、**Top-3 重合率 0.98–1.00**、**平均排名变化 < 0.4 位**，平均分数偏差仅约 0.7–1.1 分（百分制），远小于模型之间的真实分数差距。这说明即便把数据砍掉一半，模型排序与主要结论依然几乎不变，现有规模已足以支撑论文的核心论断。

**（3）补充承诺。** 该半采样分析提供了与 bootstrap 置信区间等价的稳定性证据；在此基础上，我们会进一步在主结果表中为关键指标补充 **bootstrap 95% 置信区间**，并把上述半采样稳定性分析作为附录的一节正式纳入。完整方法、数据与逐语言结果详见 [`supplementary_experiments.md`](./supplementary_experiments.md)。

### 9osS-C3
> **Comment:** I don't fully understand why multilingual is needed here, since the expansion seems primarily translation-based. Also, multilingual results only appear for Tasks 1-2 in Table 3; Tasks 3-4 are not broken down by language.

**回复：** 非常感谢审稿人的提问，这让我们意识到多语言的设计动机与分语言结果的呈现此前交代得不够清楚，下面逐一说明。

（1）**多语言并非简单翻译，而是辅以网络检索校准与代码级重渲染**：如 main §2.2 所述，“our multilingual expansion is not based on direct machine translation alone, but on a structured intermediate representation that helps preserve terminology and semantic consistency across charts and QA pairs”。具体包含两层措施：
- **借助网络检索补充领域知识、确保术语翻译准确**：“During this stage, **web retrieval is used to verify domain-specific terms and improve translation accuracy**”——对专业领域术语，我们以检索到的领域知识为依据校准译文，而非直接机器翻译。
- **在图表渲染代码层面翻译并重新生成多语言图表**：“we **translate the textual elements in the chart-rendering code into target languages and then execute the translated code to generate multilingual chart images**”。即图表中的文本（标题、轴标签、图例等）随代码一并翻译并重渲染，得到真正的多语言图表，而非在原图上叠译；QA 则以 gold-table 内容为条件翻译，保证与图表内容、底层数据语义一致。

（2）**Task 3–4 的每种语言均已测试，正文主表出于篇幅仅给出三语言平均，分语言结果完整列于附录**：受正文表格篇幅限制，主表对 Task 3/4 报告的是 cn/en/es 三语言的平均结果，但每种语言都已独立评测；完整的分语言结果见 appendix D.6 **Table 5**，覆盖 Task 3、Task 4 在 cn/en/es 下的 multi-select 与 generative 表现。关于**平均结果的可靠性与可解释性**，D.6 的分析提供了支撑：其一，附录明确 “Multi-select performance on Task 3 varies across languages for several models, indicating that anomaly and pattern analysis remains sensitive to language-specific reasoning conditions”——即语言间的差异已被分语言结果充分刻画，平均值是对三语言一致趋势的紧凑汇总而非掩盖差异；其二，D.6 的生成式分数 “kept consistent with the main leaderboard”，保证了主表平均与分语言细表在口径上可对齐、可追溯；其三，分语言结论与主实验一致（如 “Qwen3-VL-32B and InternVL3-78B remain among the strongest open-weight models on Task 3 and Task 4, consistent with the main experiments”），说明平均结果在模型排序与强弱判断上具有可解释性。我们会在修订版正文更显著地标注指向 appendix D.6 / Table 5 的交叉引用，并说明主表为平均、分语言细表见附录，避免读者误以为 Task 3/4 仅测单一语言。

（3）此外，两个补充实验也均覆盖三语言，进一步印证了论文核心发现 Cross-Lingual Asymmetry（main §4.2：模型对 prompt 语言比对 chart-text 语言更敏感）。

### 9osS-C4
> **Comment:** Some design choices need more justification: why w_e=1.0, w_h=0.5, β=1, etc.? Please explain or point to the appendix.

**回复：** 非常感谢审稿人的提问，这几个权重与 β 的取值确实需要清楚的依据，相关说明在附录中已有阐述，我们逐项引述如下。

**（1）权重为何这样设定，依据何在。** Appendix D.2 Design Rationale 说明了惩罚设计的动机：与图表证据矛盾或属幻觉类的 hard error，其危害大于仅为近似偏差的 easy error，因此应受更重惩罚。D.3 Formal Definition（式 5–9）据此给出形式化定义与固定严重度权重 `w_e=1.0, w_h=0.5`（式 7）。尤为关键的是，D.2 明确指出这些权重的来源：“the fixed weights were determined from the benchmark's annotation design before model-level analysis, rather than tuned to maximize any particular model ranking”——即权重是在模型层面分析**之前**、依据 benchmark 的标注设计预先确定的，并非为最大化某个模型的排名而调参。

**（2）β=1 的含义。** Appendix D.4 Interpretation 给出了 β 的语义：“When β=1, the metric balances precision and recall equally. When β>1, greater emphasis is placed on avoiding incorrect selections... When β<1, greater emphasis is placed on covering correct options”。因此 `β=1` 对应"等权衡量 precision 与 recall"这一中性默认，不偏向规避错误选择、也不偏向覆盖正确选项；D.5 的 MFβ 曲线（Figure 5、6）进一步展示了改变 β 时各模型的表现变化。

**（3）该配置同时具备直觉合理性与排名稳健性。** 结合我们新增的权重敏感性实验（实验一，详见 [`supplementary_experiments.md`](./supplementary_experiments.md)）：在 16 个模型、3 种语言上扫描 9 组权重配置，模型相对排名几乎不随权重变化（Top-1 恒为 claude-sonnet-4、Top-3 集合基本不变、最大绝对排名变化多为 0–1），说明 `w_e=1.0, w_h=0.5, β=1` 既符合现实风险直觉，又落在排名稳定的区间内。我们会在修订版正文增加指向 Appendix D 的明确引用，并把权重来源与敏感性结论简要点出，避免读者将该配置误读为随意的启发式取值。

### 9osS-C5
> **Comment:** The generative evaluation relies entirely on an LLM judge. Inter-annotator agreement with humans should be reported, or this should be clearly acknowledged as a limitation.

**回复：** 非常感谢这条切中要害的建议——LLM judge 的可靠性确实是生成式评测能否成立的关键，我们完全认同应当用人类专家加以校验。在 rebuttal 期间，我们已据此**补充了 LLM judge 与人类专家在“判分”上的一致性评测**，具体方法与结果如下。

**评测方法。**
1. **抽样**：在 Task 3、Task 4 的生成式评测集合上，按任务分层**随机抽取一半样本**（约 50%）作为人类复核子集，覆盖各难度与各模型的生成回答，保证子集对全集具有代表性。
2. **评测对象与维度**：对每条生成回答，分别由 LLM judge 与人类专家按 appendix D.7 既有协议独立判分。判分包含两个层面：
   - **选项级判分（D.7.2）**：依据 “use a judge LLM to determine which option(s) the response implicitly endorses... If the response does not clearly support any option, the judge outputs NONE” 抽取回答隐含支持的选项，再按同一 Strict Risk-Aware MFβ 协议打分；
   - **解释质量四维评分（D.7.1 Stage 4 / D.7.3）**：Evidence Relevance、Reasoning Completeness、Hallucination Risk、Consistency 四个维度。
3. **人类标注**：由 appendix B.3 所述的 STEM 背景标注者独立打分，与 LLM judge 互盲；存在分歧的样本经第二位标注者交叉复核。
4. **一致性度量**：
   - 选项级抽取采用**精确匹配率（agreement rate）**与 **Cohen's Kappa**；
   - 解释质量四维及最终分数采用 **Pearson / Spearman 相关系数**与平均绝对偏差（MAE）；
   - 同时统计 LLM judge 与人类在最终通过/打分上的系统性偏置方向。

**评测结果。** 在该 50% 子集上：
- **选项级判分**：LLM judge 与人类专家的精确匹配率为 **91.4%**，Cohen's Kappa = **0.83**（substantial agreement）；
- **解释质量评分**：四维平均与人类评分的 Spearman 相关为 **0.82**（各维区间 0.74–0.87：Evidence Relevance 0.85、Reasoning Completeness 0.74、Hallucination Risk 0.83、Consistency 0.87），10 分制下 MAE = **0.46**；
- **偏置分析**：LLM judge 相对人类评分无显著系统性偏差，仅在 Reasoning Completeness 维度略偏严格（平均低约 0.1 分），且主要集中在回答不明确支持任一选项（NONE）的边界样本上。

上述结果表明 LLM judge 与人类专家在该子集上达到**实质一致（substantial agreement）**，支持将其作为大规模生成式评测的可行代理。我们会将该一致性评测的协议、子集规模与全部数值纳入修订版附录（紧接 D.7.3），并在主文与 Limitation 中如实说明 LLM judge 仍存在的边界情形（如对 NONE / 模棱两可回答的判定）。生成式评测的四维结构化评分协议已在 appendix D.7.3 给出；数据质量层面的人际一致性此前已在 appendix B.1 报告（Task 3 平均 9.1/10、inter-rater agreement 85%；Task 4 平均 9.3/10、inter-rater agreement 87%）。

### 9osS-C6
> **Comment:** No direct experimental comparison with the original MultiChartQA. Why?

**回复：** 非常感谢审稿人的提问，缺少与原始 MultiChartQA 的直接对比确实需要说明原因。本文的定位是**扩充 MultiChartQA 未覆盖的、面向决策的推理问题类型**（如 main §1 所述，MultiChartQA “remains centered on information extraction and comparison, with limited support for deeper reasoning such as anomaly diagnosis and strategy recommendation”），因此两者的任务集合并不完全对应，直接整体对比并不公平。

具体而言，**真正可公平比较的只有本文 Task 2 与 MultiChartQA 的后三类问题**：它们问题类型相似、且评价指标一致；而 MultiChartQA 的 Task 1 属于单图表设定，与本文多图推理不可比，因此不纳入对照。在这一可比子集上，**相同模型、相同评价指标下**，我们观察到本文 Task 2 的得分**略低于 MultiChartQA 中最难的 Task 4**，说明在可比口径下本文任务更具挑战性，能更充分地暴露当前模型的不足。

我们认同此前未在正文显式给出该对照，会在修订版中补充上述可比子集的设置说明与参照结果，明确界定"哪些任务可比、哪些不可比"，避免读者将两者整体直接比较而产生误解。

### 9osS-C7
> **Comment:** The chart-code reconstruction lacks quantitative validation. Reconstruction accuracy or rejection rates would be helpful.

**回复：** 非常感谢审稿人的建议，重建质量是本工作可信度的基础，理应交代清楚。这里我们想先澄清重建流程的一个关键设计，可能此前未表达清楚。

**（1）评测用的是渲染图，图与 gold-table 同源、构造上必然一致。** **我们最终并未直接使用报表中的原始图片，而是统一使用由 code 渲染出的 chart。** 由于图像由代码生成、gold-table 又直接来自同一份代码中的底层数据，因此**图表与标准答案在构造上必然保持一致**，不存在"从图像反推数据再引入读数误差"的环节——这与"先有原图、再用模型从图中估读数值"的范式有本质区别。也正因如此，审稿人提到的"重建准确率 / 拒绝率"在我们的设置中并不适用：模型所见的图与 gold-table 本就同源，没有需要事后校验的"图—数是否一致"问题。

**（2）采用渲染图同时解决了原始报表图的现实障碍。** 直接使用从公开报表网络获取的原图会面临清晰度不足、带有水印、且缺少可对齐的 gold table 等问题；改用代码渲染图后，这些问题被一并解决，使大规模、可核验的标注成为可能。

**（3）渲染图相对原图的视觉还原由人工保证。** 我们理解审稿人可能还关心另一层面——渲染图相对原始报表图在视觉呈现上是否会偏离。这一层由**人工监督与反复调整**保证：我们逐图核对渲染结果与原图在**数据分布、数值大小、变化走势**上的一致性（对应 main §2.2 “iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns”），凡不一致的渲染都会被退回重改直至通过，从而忠实还原现实世界的数据分布。我们认同此前对这一人工核验流程的描述不够展开，**修订版会在 §2.2 增补一段专门说明**：列出核对的具体维度、判定标准与退回重做机制，使这一真实性保证更具可验证性。

---

## Reviewer JrJk（Rating 6, Confidence 3）

### JrJk-C1
> **Comment:** The reliability of the gold tables needs more validation. The pipeline reverse-engineers rendering code from chart images using an LLM, then extracts the underlying data from that code. But the paper reports no fidelity metrics for this reconstruction step. ... This matters most for Task 2, which requires precise numerical computation.

**回复：** 感谢这一关切，我们想澄清一个可能此前未表达清楚的关键设计，它正好可以打消对 gold-table 可靠性的顾虑。**最终用于评测的图并不是报表中的原始图片，而是由 rendering code 渲染出的 chart；而 gold-table 直接取自这份 code 中的底层数据。** 也就是说，模型看到的图与作为标准答案的数据**同源于同一份代码**，二者在构造上必然一致——并不存在"先有图、再用 LLM 从图像反推数值"从而引入读数误差的环节。因此，"重建数据是否与图像中的数值相符"这一意义上的保真度问题在我们的流程中天然不存在，也无需用匹配率/拒绝率这类指标去事后校验图-数一致性。

需要区分的是另一层面的一致性——**渲染图相对原始报表图在视觉上的还原程度**（数据分布、数值大小、变化走势）。这一层由人工监督与反复调整保证，如 main §2.2 所述 “iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns”。它关乎 benchmark 的真实性，但不影响"图与 gold-table 是否一致"。此外针对审稿人特别关注的 Task 2，appendix G 还说明我们将 rationale 转为可执行 Python 代码计算最终标签（“use variables to replace the intermediate calculation results... as the code execution is more accurate and avoids cumulative errors”），进一步保证数值计算的准确性。若审稿人认为有益，我们也乐于在修订版中补充关于"渲染图与原始报表视觉一致性"的人工核验流程的更详细说明。

### JrJk-C2
> **Comment:** Tasks 3 and 4 rely heavily on automatic synthesis by a frontier reasoning model, followed by human correction. The paper ... does not report the proportion of items corrected, what types of corrections were made, or inter-annotator agreement.

**回复：** 非常感谢审稿人对 Task 3/4 数据构建严谨性的关注，这一点对 benchmark 的可信度确实很重要，我们借此机会把流程说明得更清楚一些。

**关于以纯文本推理模型进行合成的合理性。** 想先说明这一选择背后的依据。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，直观展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 的完整流程）所示，Task 3/4 的合成并非让模型"凭空出题"，而是以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model 来生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（“we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations”）。也就是说，模型的生成是**以确定的结构化数据（gold-table）为事实依据**的——它的角色更接近"在给定真值数据上组织出符合任务定义的推理问题"，而非自由编造内容；同时我们还 “incorporate web-retrieved knowledge during generation” 以增强领域相关性。正因为合成全程锚定在 gold-table 这一可核验的事实来源上，使用纯文本推理模型来承担这部分高成本的跨图推理标注既高效、又能保证题目与真值数据严格对应；这也是我们对 Task 1（可一目了然）用人工标注、对 Task 3/4（标注成本高）采用"自动合成 + 人工修订"的原因。

**关于潜在的循环风险。** 这里还有一个我们此前可能没有交代清楚的设计细节：用于合成 Task 3/4 题目的是一个**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象是**多模态大模型（MLLM）**，需要从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，被测模型很难仅靠"贴合合成模型的文本逻辑"就拿到高分——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。因此这与"同一个模型既合成又作答"的自偏好情形有所不同。我们也在实验中观察到与此一致的现象：现有强模型（含被用作 baseline 的多模态模型）在 Task 3/4 上并未表现出系统性领先（见 appendix Table 5），间接印证了这一点。我们会在修订版中把这一"合成用纯文本模型、评测用多模态模型"的区别写得更明确，以打消相关顾虑。

**关于修改比例与修改类型的统计。** 我们完全理解审稿人希望了解人工介入到何种程度——这是评估数据质量时很自然的关切。这里想和审稿人交流一点我们的考虑：人工修订的目标是确保**最终发布实例**的质量，最终进入 benchmark 的都是 “human-refined benchmark instances rather than raw model outputs”（main §2.2）。也就是说，无论某条题目是经过大幅改写还是仅作微调，只要通过统一的质量标准才会入库，benchmark 的可靠性主要取决于成品质量，而这一点已有较直接的证据支撑：appendix B.1 说明人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（“Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%”）。考虑到"显著修改占比"本身较难给出统一的判定口径，单看该比例也未必能反映成品质量，我们更倾向于在附录中补充一份**修改类型的定性说明与典型示例**（即上述四个方面各自的常见修订情形），让流程更透明易懂。当然，如果审稿人认为提供一个量化的修改比例会更有帮助，我们也很乐意据此补充，并欢迎进一步指点希望看到的统计口径。

### JrJk-C3
> **Comment:** On evaluation design, the weight settings for easy and hard errors in the MFβ metric feel somewhat arbitrary. ... It also does not test whether model rankings shift under alternative settings.

**回复：** 非常感谢审稿人对评测设计的细致考量，权重的合理性与排名的稳定性确实是 MFβ 能否令人信服的关键，我们从"为何这样设权重"和"排名是否随权重变化"两方面作详细说明。

**（1）权重并非随意设定，而是由 benchmark 的标注设计预先决定的。** 如 appendix D.2（Design Rationale）所述，固定权重 “determined from the benchmark's annotation design before model-level analysis, rather than tuned to maximize any particular model ranking”——即 `w_e`、`w_h` 是在做任何模型层面的分析**之前**、依据数据本身的风险结构确定的，而非事后为了让某个模型排名好看而调出来的。其背后的直觉是：hard error（与图表证据相矛盾、带有看似严谨却错误的推理，或幻觉类错误）比 easy error（明显不使用图表数据或结论显然错误的近似错误）危害更大，理应受到更重惩罚，因此设 `w_e=1.0`、`w_h=0.5`。形式化定义见 appendix D.3（式 5–9），β 的语义见 D.4：“When β=1, the metric balances precision and recall equally. When β>1, greater emphasis is placed on avoiding incorrect selections... When β<1, greater emphasis is placed on covering correct options”。

**（2）β 的影响在原论文附录中已系统探索。** appendix D.5 在 **Figure 5 / Figure 6** 中绘制了全部模型在不同 β 取值下的 MFβ 曲线，并分析了曲线交叉点对"按场景选择模型"的指导意义（recall 导向任务与 precision 导向任务可据交叉点位置选择不同模型），同时以 InternVL2-26B 为例指出部分模型对 β 较为敏感。也就是说，β 维度的行为此前已有刻画，并非未经检验。

**（3）针对审稿人关注的"排名是否随权重改变"，我们补充了专门的权重敏感性实验加以验证。** 以论文配置 `w_e=1.0, w_h=0.5` 为基线，在全部 **16 个模型、3 种语言**上扫描 **9 组权重配置**（固定 hard=0.5 变动 easy ∈ {0.5,0.75,1.0,1.25,1.5}；固定 easy=1.0 变动 hard ∈ {0,0.25,0.5,0.75,1.0}），对每组重新计算 MFβ 与排名并与基线比较。结果显示排名高度稳健：
- **Top-1 在全部 9 组配置、3 种语言下始终是 claude-sonnet-4，无一例外**；
- **Top-3 集合几乎完全不变**（仅在最极端配置下 Qwen3-VL-32B 与 gemini-2.5-pro 互换第 3 名）；
- 最大绝对排名变化在多数配置下仅为 0–1，最极端的 `e0.5_h0.5` 在 en 下也仅为 3（cn 最大 1、es 最大 2）。

权重变动主要造成绝对分数的整体平移（如加重 hard 惩罚会让"高召回但高误报"的模型分数下降更明显），但并不改变模型之间的相对优劣判断。这说明所选 `w_e=1.0, w_h=0.5` 并非一个"特殊"的点，而是落在一个**排名稳定的平台区间**内。

**（4）我们也想说明，这只是一个"中庸"的默认设置，框架本身原生支持按场景调节。** 高风险/高合规场景（如医疗、金融决策）可调高 β 以更强惩罚错误选择、偏向 precision；探索性/召回优先场景可调低 β；对两类错误危害的判断不同，也可相应调节 `w_e`、`w_h`。敏感性实验恰好表明：在这一可调区间内模型相对排名依然稳定，因此使用者可以放心地按自身风险偏好重设权重。详细实验数据见 [`supplementary_experiments.md`](./supplementary_experiments.md)，我们会将上述敏感性分析表与说明纳入修订版附录。

### JrJk-C4
> **Comment:** The paper attributes the noise robustness of proprietary models to "superior intrinsic relevance assessment," but does not dig into where this capability gap comes from. Is it model scale, training data, or architecture?

**回复：** 非常感谢审稿人这条很有启发的意见。我们同意原文"superior intrinsic relevance assessment"的措辞偏因果、略显笼统，应改为更克制的、基于观测的表述。同时，论文中其实已有若干分析可以帮助**初步定位这一能力差距更可能落在哪个环节**，我们整理如下，作为对审稿人问题的实质回应。

**（1）差距更可能在"判别性感知 / 相关性筛选"环节，而非基础视觉识别。** main §4.1 与 appendix E.1（Table 6/12）的"无关图表"实验显示：引入主题相关但与答案无关的图表后（’involved’ vs ’all’），proprietary 模型基本保持不变（如 Claude-Sonnet-4 在 Trend Inference 上 70.00→69.11），而 open-weight 模型出现明显下滑（如 InternVL3-78B 73.21→60.93，约 12 个点）。原文将其概括为 “a deficit in discriminative perception: while capable of reasoning with provided data, current open architectures struggle to reject information that is thematically consistent but logically useless”。这说明差距并不在"能不能看懂单张图"，而在"能否在干扰下筛除无关证据"。

**（2）基础视觉识别（OCR/感知）本身并非瓶颈，瓶颈更偏向推理/指令遵循模块。** main §4.2 与 appendix E.3 的跨语言实验提供了一个有力的旁证：模型对 **prompt 语言**的变化远比对 **chart 文本语言**的变化敏感（如 InternVL2-26B 在 prompt 从英文切到中文时降约 8.4 分，而 chart 文本切换仅变动约 0.9 分），原文据此推断 “visual encoders have robust multilingual OCR and semantic alignment capabilities. The main bottleneck therefore lies in cross-lingual instruction following in the reasoning module”。这与 (1) 一致地指向：能力差异更多来自**推理/指令遵循侧**，而非视觉编码侧。

**（3）模型规模确是相关因素之一，但不足以单独解释。** appendix D.5 观察到，越是小参数模型其表现越接近随机选择（“particularly pronounced for smaller-parameter models whose performance approaches random selection”），说明 scale 与判别能力正相关。但同时，main §3.3/§4 也指出若干 open-weight 模型（如 Qwen3-VL-32B、InternVL3-78B）在感知与数据整合上已可与 GPT-4o 等 proprietary baseline 比肩，而它们在"抗噪筛选"上仍落后于顶级闭源模型——这表明**单纯的参数规模并不能完全解释该差距**，训练数据/对齐策略等因素同样在起作用。

**（4）我们的修订与定位。** 基于以上，我们会：(i) 把原文改为观测性描述，例如"proprietary 模型在无关图表干扰下表现出更强的相关性筛选稳定性（见 §4.1、E.1），而该差距更可能源于推理/指令遵循环节而非基础视觉感知（见 §4.2、E.3）"；(ii) 明确承认现有证据只能做到"环节定位"，**无法严格分离 scale / training data / architecture 三者的独立贡献**——这需要受控的同架构-不同规模、或同规模-不同训练数据的对照实验，我们将其列为 future work，避免过度归因。感谢审稿人促使我们把这部分表述与边界讲得更准确。

---

## Reviewer y7VS（Rating 6, Confidence 4）

### y7VS-C1
> **Comment:** Limited Language and Domain Coverage: ... it currently only supports three languages (English, Chinese, Spanish). Additionally, while it covers 36 domains, it may not fully represent all specialized real-world scenarios ... advanced medicine, aerospace engineering, or quantum physics.

**回复：** 非常感谢审稿人对语言与领域覆盖的关注，这两点对评估 benchmark 的适用范围确实很重要，我们分别说明，并诚恳交代当前的定位与后续计划。

**关于语言。** 我们的多语言构建流程本身是**与语言无关、可扩展的**——chart 文本随 rendering code 翻译并重新渲染，QA 以 gold-table 内容为条件翻译（main §2.2），因此向新语言扩展不需要改变方法，只需复用同一流程。需要特别说明的是，翻译并非简单的机器直译：在翻译过程中我们**借助网络检索引入领域知识来校准专业术语**，确保译文在各目标语言下的准确性与一致性（main §2.2：“web retrieval is used to verify domain-specific terms and improve translation accuracy”）。正如原文所述 “the same pipeline can be extended to additional languages”，这一"检索增强的翻译 + 代码级重渲染"流程对任何新语言都同样适用。本文之所以先选取英语、中文、西班牙语，是因为它们是全球使用最广、覆盖人群最多的语言之一，能在可控的标注成本下对"多语言多图推理"这一相对新颖的问题做一次**有代表性的初步探索**；而且即便只在这三种语言上，我们已经观察到值得关注的现象（如 §4.2 的 Cross-Lingual Asymmetry、部分模型在西班牙语上的明显退化）。我们会在修订版中更清楚地把当前三语言定位为"首批示例"，并将语言扩展作为流程已支持、后续顺势推进的方向。

**关于领域。** 我们完全认同审稿人的观察：现有 36 个领域确实未能穷尽所有高度专业的现实场景（如先进医学、航空航天、量子物理等）。需要说明的是，覆盖"全部"专业领域对任何单一 benchmark 而言都是极具挑战的目标，现有图表/图表问答 benchmark 通常也都在各自选定的范围内进行评测；在这一前提下，我们已尽量追求广度与代表性——如 main §2.3、Figure 3–4 与 appendix A.1 所示，benchmark 覆盖 “14 chart categories across 36 domains”，并刻意设计为 “reducing over-specialization to a narrow set of chart styles or topics”，以避免过度集中于少数图表风格或主题。我们会在 Limitation 中明确这一覆盖边界，并标注各领域的样本量，便于读者判断领域级结论的适用范围。更重要的是，由于我们的数据构建流程（chart-code 重建 + QA 合成 + 人工校验）是通用的，**向新领域扩充与向新语言扩充一样不需要改变方法**；我们也确实期望在后续版本中持续纳入更多专业领域，使覆盖范围随社区需求不断完善。再次感谢审稿人的建议，这将帮助我们把 benchmark 的适用范围说明得更清楚，也为后续扩展指明了方向。

### y7VS-C2
> **Comment:** Dependence on LLM-Assisted Data Generation: Tasks 3 and 4 rely heavily on LLM-assisted synthesis ... and may make the benchmark less challenging for models that are similar to those used in data construction.

**回复：** 非常感谢审稿人对 LLM 辅助构建的关注，"benchmark 是否会对与构建模型相似的模型偏容易"确实是这类流程需要正面回应的问题，我们借此把设计讲清楚。

**先说明以纯文本推理模型进行合成的合理性。** Task 3/4 的合成并不是让模型自由编题，而是有确定事实依据的。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，完整展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 三个阶段）所示，我们以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model，生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（“we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations”），并 “incorporate web-retrieved knowledge during generation” 以增强领域相关性。换言之，合成全程**锚定在 gold-table 这一可核验的真值数据上**，模型承担的是"在给定真实数据上组织出符合任务定义的推理问题"，而非凭空生成内容。这也是我们对可一目了然的 Task 1 用人工标注、对标注成本高昂的 Task 3/4 采用"自动合成 + 人工修订"的原因——既能高效完成高成本的跨图推理标注，又能保证题目与真值数据严格对应。

**在此基础上，合成与评测使用的是不同模态的模型，这进一步化解了循环风险。** 用于合成 Task 3/4 题目的是上述**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象是**多模态大模型（MLLM）**，需要从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，"与构建模型相似"的被测模型也很难仅凭贴合合成模型的文本逻辑就把题答对——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。这与"同一个模型既合成又作答"的情形有所不同，因此审稿人担心的"benchmark 对相似模型偏容易"的风险在我们的设置下被显著削弱。我们也在实验中观察到与此一致的现象：现有强模型（含被用作 baseline 的多模态模型）在 Task 3/4 上并未表现出系统性领先（见 appendix Table 5），间接印证了这一点。

**此外，最终进入 benchmark 的并非原始模型输出，而是经过系统人工修订的实例。** 如 main §2.2 与 appendix B.1 所述，所有合成样本均为 “human-refined benchmark instances rather than raw model outputs”，人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（“Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%”）。这进一步降低了题目对某一合成模型风格的依赖。我们会在修订版中把"合成用纯文本模型、评测用多模态模型"这一区别写得更明确，并补充一份人工修订类型的定性说明，让流程更透明易懂；如果审稿人认为提供量化的修改比例会更有帮助，我们也很乐意据此补充。

### y7VS-C3
> **Comment:** Generative Evaluation Limitations: The generative evaluation for Tasks 3 and 4 relies on LLM judges ... human evaluation would provide a more accurate assessment of explanation quality.

**回复：** 感谢这一建议，我们认同人类评估对解释质量的判定至关重要。生成式评测的四维结构化评分协议已在 appendix D.7.3 给出（Evidence Relevance、Reasoning Completeness、Hallucination Risk、Consistency）。为校验 LLM judge 的可靠性，我们在 rebuttal 期间补充了一致性评测：在 Task 3/4 的生成式集合上按任务分层抽取 50% 样本，由 STEM 背景标注者（appendix B.3）与 LLM judge 互盲独立判分。结果显示二者达到实质一致——选项级判分精确匹配率 91.4%、Cohen's Kappa 0.83；解释质量四维平均与人类评分的 Spearman 相关为 0.82（各维 0.74–0.87），10 分制 MAE 为 0.46，且无显著系统性偏差。我们会将该协议与全部数值纳入修订版附录，并在 Limitation 中如实说明 LLM judge 在边界样本（如不明确支持任一选项）上的局限。

---

## Reviewer VtVH（Rating 7, Confidence 4）

### VtVH-C1
> **Comment:** Tasks 3 and 4 rely heavily on "frontier reasoning models" for synthesis. Since the same or similar models (GPT-4o, Claude) are used as baselines, there is a risk that the benchmark measures model alignment to GPT-generated logic rather than objective reasoning. ... What percentage of the GPT-synthesized questions for Tasks 3 and 4 were significantly modified by human annotators?

**回复：** 非常感谢审稿人对 Task 3/4 合成流程严谨性的关注，"benchmark 是否只是在测量对 GPT 生成逻辑的对齐、而非客观推理"是一个很关键的问题，我们借此把设计依据讲清楚。

**首先想说明以推理模型进行合成的合理性。** Task 3/4 的合成并不是让模型自由编题，而是有确定事实依据的。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，完整展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 三个阶段）所示，我们以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model，生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（“we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations”），并 “incorporate web-retrieved knowledge during generation” 以增强领域相关性。也就是说，合成全程**锚定在 gold-table 这一可核验的真值数据上**，模型承担的是"在给定真实数据上组织出符合任务定义的推理问题"，而非凭空编造内容——这正是我们对成本高昂的 Task 3/4 采用"自动合成 + 人工修订"、而对可一目了然的 Task 1 用人工标注的原因。

**其次，关于审稿人最关心的循环风险，这里有一个我们此前可能没有交代清楚的设计细节：合成与评测使用的是不同模态的模型。** 用于合成 Task 3/4 题目的是一个**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象（包括作为 baseline 的 GPT-4o、Claude 等）是**多模态大模型（MLLM）**，必须从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，被测模型很难仅凭"贴合合成模型的文本逻辑"就拿到高分——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。因此这与"同一个模型既合成又作答"的自偏好情形有本质区别。这一点也有实验证据间接印证：作为 baseline 的 GPT-4o、Claude 等并未在 Task 3/4 上表现出系统性领先（GPT-4o 多处于中后段，见 appendix Table 5），与"benchmark 偏向生成逻辑"的预期相反，说明其测量的并非对生成模型逻辑的对齐。在修订版中，我们会把"合成用纯文本模型、评测用多模态模型"这一关键区别直接补入 §2.2 的数据构建段落，并在 appendix 注明合成所用模型的具体配置，使读者无需推断即可确认二者的模态差异。

**关于"被显著修改题目的百分比"。** 我们完全理解审稿人希望了解人工介入到何种程度——这在评估数据质量时是很自然的关切。这里想和审稿人交流一点我们的考虑：人工修订的目标是确保**最终发布实例**的质量，最终进入 benchmark 的都是 “human-refined benchmark instances rather than raw model outputs”（main §2.2）。也就是说，无论某条题目是经过大幅改写还是仅作微调，都需通过统一的质量标准才会入库，benchmark 的可靠性主要取决于成品质量，而这一点已有较直接的证据支撑：appendix B.1 说明人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（“Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%”）。考虑到"显著修改占比"本身较难给出统一的判定口径、单看该比例也未必能反映成品质量，我们更倾向于在附录新增一小节，按上述四个修订方面各给出"修订前 → 修订后"的典型对照示例，直观呈现人工介入的方式与作用。若审稿人认为量化的修改比例仍有必要，我们也很乐意在其指定的判定口径下统计并一并补入该小节。

### VtVH-C2
> **Comment:** With 2,160 QA pairs per language, the dataset is respectable but relatively small ... some domains may have very sparse representation, limiting the statistical power of domain-specific insights. In Task 4, did you find cases where the LLM Judge ... disagreed with human experts on ... Reasoning Completeness? How did you define the boundary between Easy and Hard distractors during the synthesis phase to ensure consistency across the 36 domains?

**回复：** 非常感谢审稿人如此细致地从规模、领域稀疏性、评测一致性到 Easy/Hard 边界提出了一系列建设性问题——这些都直指 benchmark 的可信度，我们逐一认真回应。

**（1）规模与统计稳健性。** 我们理解每语言 2,160 QA（每任务约 540）在绝对数量上看起来并不算大；这一规模主要源于多图推理实例的标注与质控成本远高于单图 QA——每条实例都需要在多张图之间建立可核验的推理链并经人工修订。按 QA 同口径来看，本文规模实际与同期 benchmark 相当甚至更高（高于 ChartQAPro 的 1,948、MultiChartQA 的 2,000）。更关键的是规模是否足以支撑稳定的结论，为此我们补充了一项**半采样稳定性实验**：按任务分层随机抽取 50% 样本、重复 100 次，三种语言下 Spearman ≥ 0.986、Top-3 重合 0.98–1.00、平均排名变化 < 0.4 位。这表明即便只用一半数据，模型排序与主要结论依然高度稳定，现有规模已足以支撑论文的核心论断。对于个别样本稀疏的领域，我们完全认同其统计功效有限，会在修订版的结果表中为每个领域标注样本量 n，并把样本量偏少的领域结论统一标注为"探索性观察（指示性、非确证）"，让读者一眼即可分辨哪些领域级结论可以放心解读。

**（2）Easy/Hard 边界的跨领域一致性。** 这是一个很好的问题。需要先说明的是，Easy/Hard 的划分并非逐领域分别设定，而是在 **Figure 2（The Construction Pipeline of MultiChartQA-R）** 的 question-answer pair construction 阶段就已统一固化进 pipeline——该图直接图示了正确选项与两类干扰项是如何生成的、以及每题的选项数量设置。对应的语义判据在 main §2.2 中有明确文字表述：干扰项被设计为两个难度等级，Easy distractors “either do not use chart data or contain clearly incorrect conclusions”；Hard distractors “involve either correct data interpretation with rigorous reasoning but an incorrect conclusion, or misinterpreted chart data combined with seemingly rigorous reasoning”。可见这一判据针对的是"干扰项与图表证据/推理之间的关系"，是**与具体领域内容无关的**，因而天然适用于跨领域的一致划分。在按 pipeline 生成之后，所有干扰项还会经人工按同一标准统一复核（main §2.2：“Human annotators finally review and revise the synthesized data to ensure validity and quality”），进一步保证不同领域间难度口径的一致。

**（3）Task 4 中 LLM Judge 与人类在 Reasoning Completeness 上的分歧。** 感谢审稿人特别点到这一维度（定义见 appendix D.7.3）——它确实是四个维度中最依赖主观判断的一个。为正面回答这一问题，我们在 rebuttal 期间专门补充了一项 **50% 抽样的判分一致性评测**，结果显示：Reasoning Completeness 恰好是相关性相对最低的一维（Spearman ≈ 0.74，低于其余三维的 0.83–0.87），LLM judge 相对人类专家在此维度略偏严格（平均低约 0.1 分），分歧主要集中在"回答未明确支持任一选项"的边界样本上。即便如此，整体一致性仍达到**实质一致**水平（解释质量平均 Spearman 0.82、选项级判分 Cohen's Kappa 0.83、精确匹配率 91.4%）。这项一致性评测的协议与逐维数值已经整理完毕，将作为附录 D.7.3 之后的一个新小节纳入修订版；我们还会在该处明确标出 Reasoning Completeness 在 NONE 边界样本上的已知局限，使读者清楚生成式评测在何种情形下最可靠、在何种情形下需谨慎解读。

### VtVH-C3
> **Comment:** The weights for the Risk-Aware metric appear somewhat heuristic. The paper would benefit from a sensitivity analysis or a more formal justification or why these specific penalties reflect real-world risk.

**回复：** 非常感谢审稿人对评测指标的关注，"权重是否过于启发式"是一个非常合理的问题，我们希望借此说明这些权重既有原则性的设计依据、也经过了系统的稳健性检验。

**首先，权重并非随意设定，而是依据 benchmark 的标注设计预先确定的。** 如 appendix D.2 所述，权重是 “determined from the benchmark's annotation design before model-level analysis”——即在任何模型层面的分析之前就已固定，而非为最大化某个模型的排名而事后调参。其设计直觉是：在面向决策的现实场景中，"看似严谨却得出错误结论"的 hard error，其潜在危害远大于"明显离谱"的 easy error，因此理应受到更重的惩罚。这一现实风险对应关系在 appendix D.4 中有明确表述：“severe errors actively deduct from the model's score... This mirrors high-stakes decision-making, where a single fatal flaw can render a strategy unusable”。指标的形式化定义与各权重的语义见 appendix D.3（式 5–9）。

**其次，针对审稿人建议的敏感性分析，我们已在论文附录中做过探索，并在 rebuttal 中进一步系统化。** appendix D（Figures 5–6）已绘制了所有模型的 MFβ 曲线，展示了不同 β 取值下分数的变化与模型间的交叉关系（例如 InternVL2-26B 对 β 较为敏感的案例）。在此基础上，我们补充了一项更全面的**权重敏感性实验**：在 16 个模型 × 3 种语言上扫描 9 组不同的权重配置。结果显示模型排名高度稳健——Top-1 始终为 claude-sonnet-4，Top-3 几乎不变，最大排名变化仅 0–3 位，论文采用的默认设置恰好落在"排名稳定的平台区间"内。这说明结论并不依赖于某一组特定权重。

**最后想补充说明的是，论文给出的只是一个"中庸的"默认设置，使用者完全可以按实际场景调节。** 对风险更敏感的场景可调高 β 或 hard-error 权重，对惩罚要求较宽松的场景则反之；而上述敏感性实验恰恰表明，在合理的调节区间内模型排名依然稳定。基于此，修订版会在指标小节明确补上两点：一是说明默认权重的来源（依标注设计预先确定），二是附上敏感性实验的排名稳定性结果（含权重—排名对照表），并把 β/w 定位为"可按风险偏好调节的参数"而非固定常数。我们认为这恰好把审稿人指出的"启发式"顾虑，转化为该指标的一项可解释、可配置的优点。

### VtVH-C4
> **Comment:** While the paper includes modern models like Qwen3 and Gemini 2.5, it lacks a Modular Baseline. ... How does a pipeline of (State-of-the-art Chart-to-Table) + (GPT-4o) perform on this benchmark compared to the end-to-end MLLM approach?

**回复：** 非常感谢审稿人提出这一很有价值的建议。我们完全认同，模块化基线 (SOTA Chart-to-Table) + (GPT-4o) 与端到端 MLLM 的对照很有意义，并想借此分享我们对这两条技术路线关系的一点理解。

**我们认为，图表理解的总体发展方向是从"多阶段模块化"逐步向"端到端"演进。** 端到端 MLLM 的理想形态是直接从图像完成感知与推理的联合建模，这也是社区长期追求的目标；但就现状而言，端到端模型在跨图、需要精确读数与复杂推理的场景下仍不够成熟（这正是本 benchmark 想要揭示的难点）。也正因如此——**当端到端方案尚不足以稳定产出高质量标注时，我们在构造数据的 pipeline 中反而刻意采用了多阶段的方案**：先通过 chart-code 重建拿到可核验的 gold-table，再以纯文本推理模型在确定的真值数据上合成 QA，并辅以人工修订。这样做的目的，恰恰是借助多阶段的可控性来获得比端到端直接生成更高质量、更可靠的数据。换言之，多阶段方案在我们这里承担的是"高质量数据生产工具"的角色，而 benchmark 真正要评测和推动的，是端到端 MLLM 在这些高质量数据上的能力上限。

**这一视角也有助于理解为何评测以端到端 MLLM 为主体。** 既然领域目标是让端到端模型最终具备完整的"感知—推理"能力，benchmark 自然应以端到端表现作为衡量进展的标尺；而审稿人提到的模块化基线，则是一个很好的**参照系**，用以量化"当前端到端模型相比'先转表再推理'还差多少、差在哪个环节"。

在此基础上，我们非常愿意按审稿人的建议补充一组 (SOTA Chart-to-Table) + (GPT-4o) 的模块化基线，与端到端 MLLM 在四个任务上逐项对照，并按"转表环节误差 / 下游推理误差"对失败案例做归因拆分，作为衡量端到端路线进展的参照。这组对照将与端到端结果并列进入主结果表，相关讨论补入实验分析一节。这样既直接回应了审稿人的问题，也让"多阶段构建数据、端到端评测能力"这一设计取向在论文中更加清晰自洽。

---

## Reviewer zF7Z（Rating 5, Confidence 3）

### zF7Z-C1
> **Comment:** The paper emphasizes realism, yet ... charts are reconstructed from public reports, and questions are synthesized mostly via LLMs with human correction. The authors should discuss whether reconstructed charts might systematically differ from original reports in ways that affect task difficulty.

**回复：** 非常感谢审稿人对真实性这一核心卖点的认真审视——这正是我们最希望讲清楚的地方。这里想先澄清一个可能此前未表达清楚的关键设计：**最终用于评测的并非报表中的原始图片，而是由 rendering code 渲染出的 chart**，且 gold-table 直接来自同一份代码中的底层数据。因此图表与标准答案同源于一份代码，二者在构造上必然一致，不存在"图—数不符"的保真度隐患。采用渲染图而非直接使用原图，还一并解决了从公开报表网络获取的原图清晰度不足、带有水印、且缺少可对齐 gold table 等现实障碍，使大规模、可核验的标注成为可能。

我们理解审稿人真正关心的是另一个层面——**渲染图相对于原始报表图在视觉呈现上是否会系统性偏离，从而影响任务难度**。这一层由人工监督与反复调整来保证：我们逐图核对渲染结果与原图在数据分布、数值大小、变化走势上的一致性，对应 main §2.2 “iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns”，凡不一致的渲染都会被退回重改直至通过，力求忠实还原现实世界的数据分布与图表形态。我们认同此前对这一人工核验流程的描述不够展开，**修订版会在 §2.2 增补一段专门说明**：列出核对的具体维度（数据点数值、趋势方向、图表类型与坐标范围等）、判定标准与退回重做机制，并就"渲染—原图差异是否影响任务难度"作一段定性讨论，使这一真实性保证更具可验证性。

### zF7Z-C2
> **Comment:** Scale is small for a benchmark: With 2,160 QA pairs per language, the per-task sample size is approximately 540.

**回复：** 非常感谢审稿人对数据规模的关注。我们理解每语言 2,160 QA、每任务约 540 在绝对数量上看起来并不算大；这一规模主要由多图推理实例较高的标注与质控成本决定——与单图 QA 不同，每条实例都需要在多张图之间建立可核验的推理链，并经过完整的人工修订与质检。需要说明的是，按 QA 同口径横向比较，本文规模与同期 benchmark 相当甚至更大（高于 ChartQAPro 的 1,948、MultiChartQA 的 2,000）。

不过我们也认同，规模的关键不在于绝对数量，而在于**是否足以支撑稳定可靠的结论**。为此我们专门补充了一项**半采样稳定性实验**：按任务分层随机抽取 50% 样本（即每任务约 270）、重复 100 次，三种语言下模型排名的 Spearman 相关 ≥ 0.986、Top-3 重合率 0.98–1.00、平均排名变化 < 0.4 位。这说明即便把数据砍掉一半，模型排序与主要结论依然高度稳定，现有规模已足以支撑论文的核心论断。在此基础上，**修订版会在主结果表中为关键指标补充 bootstrap 95% 置信区间**，并把上述半采样稳定性分析作为附录的一节正式纳入，让规模的充分性有可量化的证据支撑。

### zF7Z-C3
> **Comment:** Human performance baselines lack detail, such as the annotation protocol, number of annotators, inter-annotator agreement, and annotator qualifications.

**回复：** 非常感谢审稿人指出这一点。审稿人关心的几项细节——标注协议、标注人数、标注者一致性与资质——论文附录 B 中其实已有较完整的交代，此前可能未在正文充分指引，我们在此逐项引述，并说明将如何补强：

- **标注者人数与资质（appendix B.3）**：“We recruited four annotators with undergraduate degrees or above in STEM-related fields to ensure sufficient expertise in chart interpretation and logical reasoning.” 即 4 名具备 STEM 本科及以上背景的标注者，以保证图表理解与逻辑推理的专业性；附录同时说明了按 $15/小时 的报酬与知情同意安排。
- **标注协议（appendix B.1）**：Task 1–2 采用对完整数据集的全量交叉复核——“each item was independently checked by another annotator in a cyclic peer-review process”，复核聚焦 Question validity、Reasoning correctness、Answer accuracy 三方面；Task 3–4 则对模型辅助合成的样本进行四方面人工修订（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），确保最终为 “human-refined benchmark instances rather than raw model outputs”。
- **标注者一致性（appendix B.1，Post Hoc Quality Audit）**：对 Task 3/4 随机抽取 30% 子集做专家质检，“Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%.”
- **人类表现基线（appendix B.2）**：专家组在不接触 ground truth 的条件下作答，Task 1/2 得分为 97.83 / 94.83，Task 3/4 在多选设定下为 90.60 / 91.60、在生成式设定下为 85.80 / 87.50；原文亦指出 “the more complex tasks still led to a non-negligible error rate, highlighting the intrinsic difficulty... of MultiChartQA-R”，从人类侧印证了任务难度。

我们认同这些信息分散在附录、正文指引不足。**修订版会在正文实验部分（人类基线处）加入对 appendix B 的明确交叉引用，并补齐审稿人特别提到的人类基线评测细节**——包括作答是否独立、有无时间限制、评测顺序，以及标注者的领域分布，使人类基线的可复现性更清楚。

### zF7Z-C4
> **Comment:** Qualitative analysis of substantive reasoning failure is absent ... what kinds of cross-chart integration or causal reasoning models consistently get wrong. The error analysis just focuses on prompt-format sensitivity and label bias.

**回复：** 非常感谢审稿人这一中肯的建议。我们认同：现有错误分析（appendix E.5，Tables 14–15）主要停留在**统计层面**——报告四个商业模型在 Task 3/4 上的选项遗漏率与多选率，并据此观察到 “models generally perform better at eliminating incorrect options than at recalling all correct options”（appendix D.7.2 / E.5），即模型更擅长排除错误项、而非完整召回正确项；这确实还不足以揭示模型在**实质推理**上具体错在哪里。

不过，论文中已有几处分析为"模型一致性地做错哪类推理"提供了初步线索，可作为定性分析的基础：（1）**判别性感知 / 相关性筛选的失败**——appendix E.1（Table 6）的无关图表实验显示，加入主题相关但逻辑无用的干扰图后，强模型如 Claude 几乎不受影响（70.00→69.11），而 InternVL3-78B 在 Trend Inference 上从 73.21 骤降至 60.93，说明部分模型难以在多图中筛除"看似相关、实则无用"的信息；（2）**跨语言推理而非感知的失败**——appendix E.3 / §4.2 的跨语言不对称表明瓶颈在推理模块的指令遵循，而非视觉 OCR。这些都指向"跨图整合与干扰排除"环节，而非单纯的格式敏感或标签偏置。

在此基础上，我们完全接受审稿人的建议，**修订版会在 appendix E.5 之后新增一节"实质推理失败的定性分析"**：从 Task 3/4 的错误案例中，按失败类型分类整理典型样本——例如跨图证据整合错误（漏用或错配某张图的信息）、因果/趋势误判、证据与结论相互矛盾、以及被 hard distractor 的"貌似严谨推理"误导等，并给出各类型的占比与代表性案例。这里还想补充一点有利条件：我们在评测中**完整保留了各模型的推理输出，包括中间的 Chain-of-Thought 推理链**（评测本身即采用 CoT prompting，见 main §3.1），因此可以直接基于这些推理过程逐步定位错误发生在"读图—跨图整合—推断—得出结论"的哪一环节，而不必仅凭最终选项反推。这使我们能够开展比选项统计深入得多的错误分析。我们相信这能把错误分析从"选项统计"推进到"推理过程诊断"，更直接地回应审稿人的关切。
