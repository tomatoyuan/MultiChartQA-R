<div align="right">
  <span style="display: inline-block; padding: 8px 16px; background-color: #e1e4e8; color: #586069; border-radius: 6px; font-size: 14px; font-weight: 500;">
    🇨🇳 中文
  </span>
  <a href="./reviewer_JrJk_en.md" style="display: inline-block; padding: 8px 16px; background-color: #0366d6; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 500; margin-left: 4px;">
    🇺🇸 English
  </a>
</div>

## Reviewer JrJk（Rating 6, Confidence 3）

### JrJk-C1
> **Comment:** The reliability of the gold tables needs more validation. The pipeline reverse-engineers rendering code from chart images using an LLM, then extracts the underlying data from that code. But the paper reports no fidelity metrics for this reconstruction step. ... This matters most for Task 2, which requires precise numerical computation.

**回复：** 感谢这一关切，我们想澄清一个可能此前未表达清楚的关键设计，它正好可以打消对 gold-table 可靠性的顾虑。**最终用于评测的图并不是报表中的原始图片，而是由 rendering code 渲染出的 chart；而 gold-table 直接取自这份 code 中的底层数据。** 也就是说，模型看到的图与作为标准答案的数据**同源于同一份代码**，二者在构造上必然一致——并不存在"先有图、再用 LLM 从图像反推数值"从而引入读数误差的环节。因此，"重建数据是否与图像中的数值相符"这一意义上的保真度问题在我们的流程中天然不存在，也无需用匹配率/拒绝率这类指标去事后校验图-数一致性。

需要区分的是另一层面的一致性——**渲染图相对原始报表图在视觉上的还原程度**（数据分布、数值大小、变化走势）。这一层由人工监督与反复调整保证，如 main §2.2 所述 "iterative human feedback to ensure that the generated charts faithfully preserve the original content and visual patterns"。它关乎 benchmark 的真实性，但不影响"图与 gold-table 是否一致"。此外针对审稿人特别关注的 Task 2，appendix G 还说明我们将 rationale 转为可执行 Python 代码计算最终标签（"use variables to replace the intermediate calculation results... as the code execution is more accurate and avoids cumulative errors"），进一步保证数值计算的准确性。若审稿人认为有益，我们也乐于在修订版中补充关于"渲染图与原始报表视觉一致性"的人工核验流程的更详细说明。

### JrJk-C2
> **Comment:** Tasks 3 and 4 rely heavily on automatic synthesis by a frontier reasoning model, followed by human correction. The paper ... does not report the proportion of items corrected, what types of corrections were made, or inter-annotator agreement.

**回复：** 非常感谢审稿人对 Task 3/4 数据构建严谨性的关注，这一点对 benchmark 的可信度确实很重要，我们借此机会把流程说明得更清楚一些。

**关于以纯文本推理模型进行合成的合理性。** 想先说明这一选择背后的依据。如 main §2.2 与 Figure 2（The Construction Pipeline of MultiChartQA-R，直观展示了 chart-code pair collection → question-answer pair construction → multilingual expansion 的完整流程）所示，Task 3/4 的合成并非让模型"凭空出题"，而是以**包含底层 gold-table 信息的 chart-rendering code 连同任务定义**作为输入，以 few-shot 方式提供给一个 frontier reasoning model 来生成问题、正确选项及"为何正确"的解释，再据此生成干扰项及其"为何错误"的解释（"we use chart-rendering code, which contains the underlying gold-table information, together with task definitions as input to a frontier reasoning model in a few-shot manner to generate questions, correct options, and explanations"）。也就是说，模型的生成是**以确定的结构化数据（gold-table）为事实依据**的——它的角色更接近"在给定真值数据上组织出符合任务定义的推理问题"，而非自由编造内容；同时我们还 "incorporate web-retrieved knowledge during generation" 以增强领域相关性。正因为合成全程锚定在 gold-table 这一可核验的事实来源上，使用纯文本推理模型来承担这部分高成本的跨图推理标注既高效、又能保证题目与真值数据严格对应；这也是我们对 Task 1（可一目了然）用人工标注、对 Task 3/4（标注成本高）采用"自动合成 + 人工修订"的原因。

**关于潜在的循环风险。** 这里还有一个我们此前可能没有交代清楚的设计细节：用于合成 Task 3/4 题目的是一个**纯文本推理模型**，它在生成时只接触结构化的文本信息（gold-table 内容、rationale 等），并不"看图"；而 benchmark 实际评测的对象是**多模态大模型（MLLM）**，需要从 chart 图像中感知并整合视觉信息才能作答。由于二者在模态（纯文本 vs. 多模态）与模型上都不相同，被测模型很难仅靠"贴合合成模型的文本逻辑"就拿到高分——它真正要面对的跨图视觉推理，恰恰是合成模型从未经历的环节。因此这与"同一个模型既合成又作答"的自偏好情形有所不同。我们也在实验中观察到与此一致的现象：现有强模型（含被用作 baseline 的多模态模型）在 Task 3/4 上并未表现出系统性领先（见 appendix Table 5），间接印证了这一点。我们会在修订版中把这一"合成用纯文本模型、评测用多模态模型"的区别写得更明确，以打消相关顾虑。

**关于修改比例与修改类型的统计。** 我们完全理解审稿人希望了解人工介入到何种程度——这是评估数据质量时很自然的关切。这里想和审稿人交流一点我们的考虑：人工修订的目标是确保**最终发布实例**的质量，最终进入 benchmark 的都是 "human-refined benchmark instances rather than raw model outputs"（main §2.2）。也就是说，无论某条题目是经过大幅改写还是仅作微调，只要通过统一的质量标准才会入库，benchmark 的可靠性主要取决于成品质量，而这一点已有较直接的证据支撑：appendix B.1 说明人工修订覆盖四个方面（Question-type alignment、Validity of correct options、Effectiveness of distractors、Explanation consistency），并经 30% 抽样的 Post Hoc Quality Audit（"Task 3 achieved an average score of 9.1/10 with an inter-rater agreement of 85%, while Task 4 achieved an average score of 9.3/10 with an inter-rater agreement of 87%"）。考虑到"显著修改占比"本身较难给出统一的判定口径，单看该比例也未必能反映成品质量，我们更倾向于在附录中补充一份**修改类型的定性说明与典型示例**（即上述四个方面各自的常见修订情形），让流程更透明易懂。当然，如果审稿人认为提供一个量化的修改比例会更有帮助，我们也很乐意据此补充，并欢迎进一步指点希望看到的统计口径。

### JrJk-C3
> **Comment:** On evaluation design, the weight settings for easy and hard errors in the MFβ metric feel somewhat arbitrary. ... It also does not test whether model rankings shift under alternative settings.

**回复：** 非常感谢审稿人对评测设计的细致考量，权重的合理性与排名的稳定性确实是 MFβ 能否令人信服的关键，我们从"为何这样设权重"和"排名是否随权重变化"两方面作详细说明。

**（1）权重并非随意设定，而是由 benchmark 的标注设计预先决定的。** 如 appendix D.2（Design Rationale）所述，固定权重 "determined from the benchmark's annotation design before model-level analysis, rather than tuned to maximize any particular model ranking"——即 `w_e`、`w_h` 是在做任何模型层面的分析**之前**、依据数据本身的风险结构确定的，而非事后为了让某个模型排名好看而调出来的。其背后的直觉是：hard error（与图表证据相矛盾、带有看似严谨却错误的推理，或幻觉类错误）比 easy error（明显不使用图表数据或结论显然错误的近似错误）危害更大，理应受到更重惩罚，因此设 `w_e=1.0`、`w_h=0.5`。形式化定义见 appendix D.3（式 5–9），β 的语义见 D.4："When β=1, the metric balances precision and recall equally. When β>1, greater emphasis is placed on avoiding incorrect selections... When β<1, greater emphasis is placed on covering correct options"。

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

**（1）差距更可能在"判别性感知 / 相关性筛选"环节，而非基础视觉识别。** main §4.1 与 appendix E.1（Table 6/12）的"无关图表"实验显示：引入主题相关但与答案无关的图表后（'involved' vs 'all'），proprietary 模型基本保持不变（如 Claude-Sonnet-4 在 Trend Inference 上 70.00→69.11），而 open-weight 模型出现明显下滑（如 InternVL3-78B 73.21→60.93，约 12 个点）。原文将其概括为 "a deficit in discriminative perception: while capable of reasoning with provided data, current open architectures struggle to reject information that is thematically consistent but logically useless"。这说明差距并不在"能不能看懂单张图"，而在"能否在干扰下筛除无关证据"。

**（2）基础视觉识别（OCR/感知）本身并非瓶颈，瓶颈更偏向推理/指令遵循模块。** main §4.2 与 appendix E.3 的跨语言实验提供了一个有力的旁证：模型对 **prompt 语言**的变化远比对 **chart 文本语言**的变化敏感（如 InternVL2-26B 在 prompt 从英文切到中文时降约 8.4 分，而 chart 文本切换仅变动约 0.9 分），原文据此推断 "visual encoders have robust multilingual OCR and semantic alignment capabilities. The main bottleneck therefore lies in cross-lingual instruction following in the reasoning module"。这与 (1) 一致地指向：能力差异更多来自**推理/指令遵循侧**，而非视觉编码侧。

**（3）模型规模确是相关因素之一，但不足以单独解释。** appendix D.5 观察到，越是小参数模型其表现越接近随机选择（"particularly pronounced for smaller-parameter models whose performance approaches random selection"），说明 scale 与判别能力正相关。但同时，main §3.3/§4 也指出若干 open-weight 模型（如 Qwen3-VL-32B、InternVL3-78B）在感知与数据整合上已可与 GPT-4o 等 proprietary baseline 比肩，而它们在"抗噪筛选"上仍落后于顶级闭源模型——这表明**单纯的参数规模并不能完全解释该差距**，训练数据/对齐策略等因素同样在起作用。

**（4）我们的修订与定位。** 基于以上，我们会：(i) 把原文改为观测性描述，例如"proprietary 模型在无关图表干扰下表现出更强的相关性筛选稳定性（见 §4.1、E.1），而该差距更可能源于推理/指令遵循环节而非基础视觉感知（见 §4.2、E.3）"；(ii) 明确承认现有证据只能做到"环节定位"，**无法严格分离 scale / training data / architecture 三者的独立贡献**——这需要受控的同架构-不同规模、或同规模-不同训练数据的对照实验，我们将其列为 future work，避免过度归因。感谢审稿人促使我们把这部分表述与边界讲得更准确。
