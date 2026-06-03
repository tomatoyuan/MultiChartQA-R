<div align="right">
  <span style="display: inline-block; padding: 8px 16px; background-color: #e1e4e8; color: #586069; border-radius: 6px; font-size: 14px; font-weight: 500;">
    🇨🇳 中文
  </span>
  <a href="./reviewer_zF7Z_en.md" style="display: inline-block; padding: 8px 16px; background-color: #0366d6; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 500; margin-left: 4px;">
    🇺🇸 English
  </a>
</div>

## Reviewer zF7Z（Rating 5, Confidence 3）

### zF7Z-C1
> **Comment:** The paper emphasizes realism, yet ... charts are reconstructed from public reports, and questions are synthesized mostly via LLMs with human correction. The authors should discuss whether reconstructed charts might systematically differ from original reports in ways that affect task difficulty.

**回复：** 非常感谢审稿人对真实性这一核心卖点的认真审视——这正是我们最希望讲清楚的地方。这里想先澄清一个可能此前未表达清楚的关键设计：**最终用于评测的并非报表中的原始图片，而是由 rendering code 渲染出的 chart**，且 gold-table 直接来自同一份代码中的底层数据。因此图表与标准答案同源于一份代码，二者在构造上必然一致，不存在"图—数不符"的保真度隐患。采用渲染图而非直接使用原图，还一并解决了从公开报表网络获取的原图清晰度不足、带有水印、且缺少可对齐 gold table 等现实障碍，使大规模、可核验的标注成为可能。

我们理解审稿人真正关心的是另一个层面——**渲染图相对于原始报表图在视觉呈现上是否会系统性偏离，从而影响任务难度**。这一层由人工监督与反复调整来保证：我们逐图核对渲染结果与原图在数据分布、数值大小、变化走势上的一致性，对应 main §2.2 "iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns"，凡不一致的渲染都会被退回重改直至通过，力求忠实还原现实世界的数据分布与图表形态。我们认同此前对这一人工核验流程的描述不够展开，**修订版会在 §2.2 增补一段专门说明**：列出核对的具体维度（数据点数值、趋势方向、图表类型与坐标范围等）、判定标准与退回重做机制，并就"渲染—原图差异是否影响任务难度"作一段定性讨论，使这一真实性保证更具可验证性。

### zF7Z-C2
> **Comment:** Scale is small for a benchmark: With 2,160 QA pairs per language, the per-task sample size is approximately 540.

**回复：** 非常感谢审稿人对数据规模的关注。我们理解每语言 2,160 QA、每任务约 540 在绝对数量上看起来并不算大；这一规模主要由多图推理实例较高的标注与质控成本决定——与单图 QA 不同，每条实例都需要在多张图之间建立可核验的推理链，并经过完整的人工修订与质检。需要说明的是，按 QA 同口径横向比较，本文规模与同期 benchmark 相当甚至更大（高于 ChartQAPro 的 1,948、MultiChartQA 的 2,000）。

不过我们也认同，规模的关键不在于绝对数量，而在于**是否足以支撑稳定可靠的结论**。为此我们专门补充了一项**半采样稳定性实验**：按任务分层随机抽取 50% 样本（即每任务约 270）、重复 100 次，三种语言下模型排名的 Spearman 相关 ≥ 0.986、Top-3 重合率 0.98–1.00、平均排名变化 < 0.4 位。这说明即便把数据砍掉一半，模型排序与主要结论依然高度稳定，现有规模已足以支撑论文的核心论断。在此基础上，**修订版会在主结果表中为关键指标补充 bootstrap 95% 置信区间**，并把上述半采样稳定性分析作为附录的一节正式纳入，让规模的充分性有可量化的证据支撑。

### zF7Z-C3
> **Comment:** Human performance baselines lack detail, such as the annotation protocol, number of annotators, inter-annotator agreement, and annotator qualifications.

**回复：** 非常感谢审稿人指出这一点。审稿人关心的几项细节——标注协议、标注人数、标注者一致性与资质——论文附录 B 中其实已有较完整的交代，此前可能未在正文充分指引，我们在此逐项引述，并说明将如何补强：

- **标注者人数与资质（appendix B.3）**："We recruited four annotators with undergraduate degrees or above in STEM-related fields to ensure sufficient expertise in chart interpretation and logical reasoning." 即 4 名具备 STEM 本科及以上背景的标注者，以保证图表理解与逻辑推理的专业性；附录同时说明了按 $15/小时 的报酬与知情同意安排。
- **标注协议（appendix B.1）**：Task 1–2 采用对完整数据集的全量交叉复核——"each item was independently checked by another annotator in a cyclic peer-review process"，复核聚焦 Question validity、Reasoning correctness、Answer accuracy 三方面；Task 3–4 则对模型辅助合成的样本进行四方面人工修订（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），确保最终为 "human-refined benchmark instances rather than raw model outputs"。
- **标注者一致性（appendix B.1，Post Hoc Quality Audit）**：对 Task 3/4 随机抽取 30% 子集做专家质检，"Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%."
- **人类表现基线（appendix B.2）**：专家组在不接触 ground truth 的条件下作答，Task 1/2 得分为 97.83 / 94.83，Task 3/4 在多选设定下为 90.60 / 91.60、在生成式设定下为 85.80 / 87.50；原文亦指出 "the more complex tasks still led to a non-negligible error rate, highlighting the intrinsic difficulty... of MultiChartQA-R"，从人类侧印证了任务难度。

我们认同这些信息分散在附录、正文指引不足。**修订版会在正文实验部分（人类基线处）加入对 appendix B 的明确交叉引用，并补齐审稿人特别提到的人类基线评测细节**——包括作答是否独立、有无时间限制、评测顺序，以及标注者的领域分布，使人类基线的可复现性更清楚。

### zF7Z-C4
> **Comment:** Qualitative analysis of substantive reasoning failure is absent ... what kinds of cross-chart integration or causal reasoning models consistently get wrong. The error analysis just focuses on prompt-format sensitivity and label bias.

**回复：** 非常感谢审稿人这一中肯的建议。我们认同：现有错误分析（appendix E.5，Tables 14–15）主要停留在**统计层面**——报告四个商业模型在 Task 3/4 上的选项遗漏率与多选率，并据此观察到 "models generally perform better at eliminating incorrect options than at recalling all correct options"（appendix D.7.2 / E.5），即模型更擅长排除错误项、而非完整召回正确项；这确实还不足以揭示模型在**实质推理**上具体错在哪里。

不过，论文中已有几处分析为"模型一致性地做错哪类推理"提供了初步线索，可作为定性分析的基础：（1）**判别性感知 / 相关性筛选的失败**——appendix E.1（Table 6）的无关图表实验显示，加入主题相关但逻辑无用的干扰图后，强模型如 Claude 几乎不受影响（70.00→69.11），而 InternVL3-78B 在 Trend Inference 上从 73.21 骤降至 60.93，说明部分模型难以在多图中筛除"看似相关、实则无用"的信息；（2）**跨语言推理而非感知的失败**——appendix E.3 / §4.2 的跨语言不对称表明瓶颈在推理模块的指令遵循，而非视觉 OCR。这些都指向"跨图整合与干扰排除"环节，而非单纯的格式敏感或标签偏置。

在此基础上，我们完全接受审稿人的建议，**修订版会在 appendix E.5 之后新增一节"实质推理失败的定性分析"**：从 Task 3/4 的错误案例中，按失败类型分类整理典型样本——例如跨图证据整合错误（漏用或错配某张图的信息）、因果/趋势误判、证据与结论相互矛盾、以及被 hard distractor 的"貌似严谨推理"误导等，并给出各类型的占比与代表性案例。这里还想补充一点有利条件：我们在评测中**完整保留了各模型的推理输出，包括中间的 Chain-of-Thought 推理链**（评测本身即采用 CoT prompting，见 main §3.1），因此可以直接基于这些推理过程逐步定位错误发生在"读图—跨图整合—推断—得出结论"的哪一环节，而不必仅凭最终选项反推。这使我们能够开展比选项统计深入得多的错误分析。我们相信这能把错误分析从"选项统计"推进到"推理过程诊断"，更直接地回应审稿人的关切。
