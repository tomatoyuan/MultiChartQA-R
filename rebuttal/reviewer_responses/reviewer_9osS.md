<div align="right">
  <span style="display: inline-block; padding: 8px 16px; background-color: #e1e4e8; color: #586069; border-radius: 6px; font-size: 14px; font-weight: 500;">
    🇨🇳 中文
  </span>
  <a href="./reviewer_9osS_en.md" style="display: inline-block; padding: 8px 16px; background-color: #0366d6; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 500; margin-left: 4px;">
    🇺🇸 English
  </a>
</div>

## Reviewer 9osS（Rating 5, Confidence 4）

### 9osS-C1
> **Comment:** Although the Strict Risk-Aware metric is motivated and easy to understand, it is still relatively simple. Could the authors provide a sensitivity analysis showing how rankings change under different weight configurations?

**回复：** 非常感谢审稿人的建议，敏感性分析确实能更有力地说明指标的稳健性，我们正是据此补充了相关实验，并结合论文附录已有的探索一并说明如下。

**（1）新增的权重敏感性实验（实验一）。** 我们以论文配置 `e1_h0.5`（`w_e=1.0`、`w_h=0.5`、`β=1`）为基线，在全部 **16 个模型**、**3 种语言**上扫描 **9 组权重配置**（沿 easy/hard 严重度权重与 β 两个方向变化），对每组配置重新计算全部模型的 MFβ 分数与排名，并与基线比较 Top-1、Top-3 命中及最大绝对排名变化。结果显示排名高度稳健：**Top-1 在全部 9 组配置、3 种语言下始终为 claude-sonnet-4，无一例外**；**Top-3 集合几乎完全不变**（仅在最极端配置下 Qwen3-VL-32B 与 gemini-2.5-pro 互换第 3 名）；**最大绝对排名变化在多数配置下仅为 0–1**，即便最极端的 `e0.5_h0.5` 在 en 下也仅为 3、cn 下最大为 1、es 下最大为 2。这说明基线配置并非因"特殊"而被选中，而是落在一个**排名稳定的平台区间**内。

**（2）β 的影响在原论文附录中已有系统探索。** 这部分是对审稿人关切的进一步补强（见 appendix.pdf，Appendix D *Metric Exploration*，pp. 11–13）：D.3（式 5–9）给出 MFβ 的完整定义与固定严重度权重；D.4 给出 β 语义（`β=1` precision/recall 等权，`β>1` 更重规避错误选择，`β<1` 更重覆盖正确选项）；D.5 "Analysis of MFβ Curves" 在 **Figure 5、Figure 6** 中绘制了全部模型在不同 β 下的 MFβ 曲线，并通过曲线**交叉点**分析了不同模型在"召回正确项 vs. 规避错误项"上的权衡及其对场景化模型选择的指导意义（并以 InternVL2-26B 为例说明部分模型对 β 高度敏感）。

**（3）默认配置是"中庸"设置、可按场景调节。** 我们想强调，`e1_h0.5, β=1` 只是一个兼顾直觉合理性与排名稳定性的默认设置，而非唯一正确配置：高风险/高合规场景（如医疗、金融）可调高 β 以更重惩罚错误选择、偏向 precision，探索性场景可调低 β 以更看重召回；亦可按业务对两类错误危害的判断调节 `w_e`、`w_h`。敏感性实验进一步表明，在上述可调区间内模型相对排名依然稳健。完整配置、数据与图表详见 [`supplementary_experiments.md`](./supplementary_experiments.md)；我们会将该敏感性分析表正式纳入修订版附录，紧接现有的 MFβ 曲线分析。

### 9osS-C2
> **Comment:** The dataset is small: 2,160 QA pairs per language, 180 multi-chart sets, 695 charts. Can you explain what led to this size? Does it affect the reliability of your findings? Bootstrap confidence intervals would help.

**回复：** 非常感谢审稿人对数据规模及其可靠性的关注，这两点我们分别说明如下。

**（1）规模构成及其成因。** 如 main Table 1 与 appendix A.1 所述，每个语言版本含 "180 multi-chart sets, 695 chart-code pairs, and 2,160 QA pairs, with 540 instances for each of the four tasks"，且 "On average, each set contains 3.9 charts, reflecting the realistic need to aggregate evidence across multiple visualizations"。规模主要由多图推理实例较高的标注与质控成本决定——与单图 QA 不同，每条实例都需在多张图之间建立可核验的推理链，并经过完整的人工修订与质检（appendix B.1）。需要说明的是，按 QA 同口径横向比较，本文 2,160 并不小于同期工作，高于 ChartQAPro（1,948）与 MultiChartQA（2,000）。

**（2）规模是否影响结论可靠性——半采样稳定性实验（实验二）。** 我们完全认同关键不在绝对数量，而在于规模是否足以支撑稳定结论。为此我们补充了一项稳定性实验：按任务**分层随机抽取 50% 样本**、**重复 100 次**，考察模型排名相对全量结果的波动。结果显示三种语言下排名高度稳定——**Spearman 相关 ≥ 0.986**、**Top-3 重合率 0.98–1.00**、**平均排名变化 < 0.4 位**，平均分数偏差仅约 0.7–1.1 分（百分制），远小于模型之间的真实分数差距。这说明即便把数据砍掉一半，模型排序与主要结论依然几乎不变，现有规模已足以支撑论文的核心论断。

**（3）补充承诺。** 该半采样分析提供了与 bootstrap 置信区间等价的稳定性证据；在此基础上，我们会进一步在主结果表中为关键指标补充 **bootstrap 95% 置信区间**，并把上述半采样稳定性分析作为附录的一节正式纳入。完整方法、数据与逐语言结果详见 [`supplementary_experiments.md`](./supplementary_experiments.md)。

### 9osS-C3
> **Comment:** I don't fully understand why multilingual is needed here, since the expansion seems primarily translation-based. Also, multilingual results only appear for Tasks 1-2 in Table 3; Tasks 3-4 are not broken down by language.

**回复：** 非常感谢审稿人的提问，这让我们意识到多语言的设计动机与分语言结果的呈现此前交代得不够清楚，下面逐一说明。

（1）**多语言并非简单翻译，而是辅以网络检索校准与代码级重渲染**：如 main §2.2 所述，"our multilingual expansion is not based on direct machine translation alone, but on a structured intermediate representation that helps preserve terminology and semantic consistency across charts and QA pairs"。具体包含两层措施：
- **借助网络检索补充领域知识、确保术语翻译准确**："During this stage, **web retrieval is used to verify domain-specific terms and improve translation accuracy**"——对专业领域术语，我们以检索到的领域知识为依据校准译文，而非直接机器翻译。
- **在图表渲染代码层面翻译并重新生成多语言图表**："we **translate the textual elements in the chart-rendering code into target languages and then execute the translated code to generate multilingual chart images**"。即图表中的文本（标题、轴标签、图例等）随代码一并翻译并重渲染，得到真正的多语言图表，而非在原图上叠译；QA 则以 gold-table 内容为条件翻译，保证与图表内容、底层数据语义一致。

（2）**Task 3–4 的每种语言均已测试，正文主表出于篇幅仅给出三语言平均，分语言结果完整列于附录**：受正文表格篇幅限制，主表对 Task 3/4 报告的是 cn/en/es 三语言的平均结果，但每种语言都已独立评测；完整的分语言结果见 appendix D.6 **Table 5**，覆盖 Task 3、Task 4 在 cn/en/es 下的 multi-select 与 generative 表现。关于**平均结果的可靠性与可解释性**，D.6 的分析提供了支撑：其一，附录明确 "Multi-select performance on Task 3 varies across languages for several models, indicating that anomaly and pattern analysis remains sensitive to language-specific reasoning conditions"——即语言间的差异已被分语言结果充分刻画，平均值是对三语言一致趋势的紧凑汇总而非掩盖差异；其二，D.6 的生成式分数 "kept consistent with the main leaderboard"，保证了主表平均与分语言细表在口径上可对齐、可追溯；其三，分语言结论与主实验一致（如 "Qwen3-VL-32B and InternVL3-78B remain among the strongest open-weight models on Task 3 and Task 4, consistent with the main experiments"），说明平均结果在模型排序与强弱判断上具有可解释性。我们会在修订版正文更显著地标注指向 appendix D.6 / Table 5 的交叉引用，并说明主表为平均、分语言细表见附录，避免读者误以为 Task 3/4 仅测单一语言。

（3）此外，两个补充实验也均覆盖三语言，进一步印证了论文核心发现 Cross-Lingual Asymmetry（main §4.2：模型对 prompt 语言比对 chart-text 语言更敏感）。

### 9osS-C4
> **Comment:** Some design choices need more justification: why w_e=1.0, w_h=0.5, β=1, etc.? Please explain or point to the appendix.

**回复：** 非常感谢审稿人的提问，这几个权重与 β 的取值确实需要清楚的依据，相关说明在附录中已有阐述，我们逐项引述如下。

**（1）权重为何这样设定，依据何在。** Appendix D.2 Design Rationale 说明了惩罚设计的动机：与图表证据矛盾或属幻觉类的 hard error，其危害大于仅为近似偏差的 easy error，因此应受更重惩罚。D.3 Formal Definition（式 5–9）据此给出形式化定义与固定严重度权重 `w_e=1.0, w_h=0.5`（式 7）。尤为关键的是，D.2 明确指出这些权重的来源："the fixed weights were determined from the benchmark's annotation design before model-level analysis, rather than tuned to maximize any particular model ranking"——即权重是在模型层面分析**之前**、依据 benchmark 的标注设计预先确定的，并非为最大化某个模型的排名而调参。

**（2）β=1 的含义。** Appendix D.4 Interpretation 给出了 β 的语义："When β=1, the metric balances precision and recall equally. When β>1, greater emphasis is placed on avoiding incorrect selections... When β<1, greater emphasis is placed on covering correct options"。因此 `β=1` 对应"等权衡量 precision 与 recall"这一中性默认，不偏向规避错误选择、也不偏向覆盖正确选项；D.5 的 MFβ 曲线（Figure 5、6）进一步展示了改变 β 时各模型的表现变化。

**（3）该配置同时具备直觉合理性与排名稳健性。** 结合我们新增的权重敏感性实验（实验一，详见 [`supplementary_experiments.md`](./supplementary_experiments.md)）：在 16 个模型、3 种语言上扫描 9 组权重配置，模型相对排名几乎不随权重变化（Top-1 恒为 claude-sonnet-4、Top-3 集合基本不变、最大绝对排名变化多为 0–1），说明 `w_e=1.0, w_h=0.5, β=1` 既符合现实风险直觉，又落在排名稳定的区间内。我们会在修订版正文增加指向 Appendix D 的明确引用，并把权重来源与敏感性结论简要点出，避免读者将该配置误读为随意的启发式取值。

### 9osS-C5
> **Comment:** The generative evaluation relies entirely on an LLM judge. Inter-annotator agreement with humans should be reported, or this should be clearly acknowledged as a limitation.

**回复：** 非常感谢这条切中要害的建议——LLM judge 的可靠性确实是生成式评测能否成立的关键，我们完全认同应当用人类专家加以校验。在 rebuttal 期间，我们已据此**补充了 LLM judge 与人类专家在"判分"上的一致性评测**，具体方法与结果如下。

**评测方法。**
1. **抽样**：在 Task 3、Task 4 的生成式评测集合上，按任务分层**随机抽取一半样本**（约 50%）作为人类复核子集，覆盖各难度与各模型的生成回答，保证子集对全集具有代表性。
2. **评测对象与维度**：对每条生成回答，分别由 LLM judge 与人类专家按 appendix D.7 既有协议独立判分。判分包含两个层面：
   - **选项级判分（D.7.2）**：依据 "use a judge LLM to determine which option(s) the response implicitly endorses... If the response does not clearly support any option, the judge outputs NONE" 抽取回答隐含支持的选项，再按同一 Strict Risk-Aware MFβ 协议打分；
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

**回复：** 非常感谢审稿人的提问，缺少与原始 MultiChartQA 的直接对比确实需要说明原因。本文的定位是**扩充 MultiChartQA 未覆盖的、面向决策的推理问题类型**（如 main §1 所述，MultiChartQA "remains centered on information extraction and comparison, with limited support for deeper reasoning such as anomaly diagnosis and strategy recommendation"），因此两者的任务集合并不完全对应，直接整体对比并不公平。

具体而言，**真正可公平比较的只有本文 Task 2 与 MultiChartQA 的后三类问题**：它们问题类型相似、且评价指标一致；而 MultiChartQA 的 Task 1 属于单图表设定，与本文多图推理不可比，因此不纳入对照。在这一可比子集上，**相同模型、相同评价指标下**，我们观察到本文 Task 2 的得分**略低于 MultiChartQA 中最难的 Task 4**，说明在可比口径下本文任务更具挑战性，能更充分地暴露当前模型的不足。

我们认同此前未在正文显式给出该对照，会在修订版中补充上述可比子集的设置说明与参照结果，明确界定"哪些任务可比、哪些不可比"，避免读者将两者整体直接比较而产生误解。

### 9osS-C7
> **Comment:** The chart-code reconstruction lacks quantitative validation. Reconstruction accuracy or rejection rates would be helpful.

**回复：** 非常感谢审稿人的建议，重建质量是本工作可信度的基础，理应交代清楚。这里我们想先澄清重建流程的一个关键设计，可能此前未表达清楚。

**（1）评测用的是渲染图，图与 gold-table 同源、构造上必然一致。** **我们最终并未直接使用报表中的原始图片，而是统一使用由 code 渲染出的 chart。** 由于图像由代码生成、gold-table 又直接来自同一份代码中的底层数据，因此**图表与标准答案在构造上必然保持一致**，不存在"从图像反推数据再引入读数误差"的环节——这与"先有原图、再用模型从图中估读数值"的范式有本质区别。也正因如此，审稿人提到的"重建准确率 / 拒绝率"在我们的设置中并不适用：模型所见的图与 gold-table 本就同源，没有需要事后校验的"图—数是否一致"问题。

**（2）采用渲染图同时解决了原始报表图的现实障碍。** 直接使用从公开报表网络获取的原图会面临清晰度不足、带有水印、且缺少可对齐的 gold table 等问题；改用代码渲染图后，这些问题被一并解决，使大规模、可核验的标注成为可能。

**（3）渲染图相对原图的视觉还原由人工保证。** 我们理解审稿人可能还关心另一层面——渲染图相对原始报表图在视觉呈现上是否会偏离。这一层由**人工监督与反复调整**保证：我们逐图核对渲染结果与原图在**数据分布、数值大小、变化走势**上的一致性（对应 main §2.2 "iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns"），凡不一致的渲染都会被退回重改直至通过，从而忠实还原现实世界的数据分布。我们认同此前对这一人工核验流程的描述不够展开，**修订版会在 §2.2 增补一段专门说明**：列出核对的具体维度、判定标准与退回重做机制，使这一真实性保证更具可验证性。
