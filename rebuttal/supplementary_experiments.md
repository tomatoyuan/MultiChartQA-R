# Supplementary Experiments / 补充实验与说明

本文档汇总针对审稿意见补充的两个新实验。

- 权重敏感性实验
- 半采样稳定性实验

两个实验分别直接回应评审中最集中的两点质疑：

1. **Strict Risk-Aware MFβ 指标的权重是否武断、排名是否随权重变化**（Reviewer 9osS / JrJk / VtVH）
2. **Benchmark 规模是否足以支撑稳定结论**（Reviewer 9osS / VtVH / zF7Z）

---

## 实验一：Strict Risk-Aware MFβ 权重敏感性（Relevant Risk-Weight Sensitivity）

### 动机

审稿人指出 MFβ 的权重设置（`w_e=1.0`、`w_h=0.5`、`β=1`）看起来比较启发式，担心不同权重会改变模型排名。本实验系统检验排名对权重的敏感性。

### 设计

以论文配置 `e1_h0.5`（easy-error 权重 = 1.0、hard-error 权重 = 0.5）为基线，在全部 **16 个模型**、**3 种语言**上扫描 **9 组权重配置**，分两个方向：

- 固定 hard 权重 = 0.5，变动 easy 权重：0.5 / 0.75 / 1.0 / 1.25 / 1.5
- 固定 easy 权重 = 1.0，变动 hard 权重：0.0 / 0.25 / 0.5 / 0.75 / 1.0

对每组配置重新计算全部模型的 MFβ 分数与排名，并与基线比较 Top-1、Top-3 命中以及最大绝对排名变化（max abs. rank shift）。

### 结果（English / en）

| 配置 | Top-1 | Top-3 | 最大绝对排名变化 |
|---|---|---|---:|
| e0.5_h0.5 | claude-sonnet-4 | claude, Qwen3-VL-32B, Seed1.5-VL | 3 |
| e0.75_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 1 |
| **e1_h0.5（基线）** | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1.25_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1.5_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1_h0 | claude-sonnet-4 | claude, Seed1.5-VL, gemini-2.5-pro | 2 |
| e1_h0.25 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 2 |
| e1_h0.75 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 1 |
| e1_h1 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 2 |

### 结论

- **Top-1 在全部 9 组配置、3 种语言下始终是 claude-sonnet-4，无一例外。**
- **Top-3 集合几乎完全不变**（仅在最极端配置下 Qwen3-VL-32B 与 gemini-2.5-pro 互换第 3 名）。
- 最大绝对排名变化在多数配置下为 0–1；最极端的 `e0.5_h0.5` 也仅为 3（en），cn 下最大仅 1，es 下最大仅 2。
- 权重变动主要影响绝对分数的整体平移（如把 hard 惩罚从 0 提到 1 时，gpt-4o 这类“高召回但高误报”模型分数下降更明显），但**不改变模型之间的相对优劣判断**。

因此选择 `e1_h0.5` 并非因为它“特殊”，而是因为它处在一个**排名稳定的平台区间**内，且符合“hard error（与图表证据矛盾、幻觉类）比 easy error（近似错误）危害更大、应受更重惩罚”的直觉。

### 与论文附录的衔接：β 已在附录中系统探索

需要说明的是，**关于 β 的探索在原论文附录中已经给出，本次敏感性实验是对其的进一步补强**。具体位置如下（见 `appendix.pdf`，Appendix D *Metric Exploration and Phenomenon Analysis*，pp. 11–13）：

- **D.3 Formal Definition（式 5–9）**：给出 Strict Risk-Aware MFβ 的完整定义，固定严重度权重 `w_e=1.0, w_h=0.5`（式 7）。
- **D.2 Design Rationale**：明确说明该权重是**依据 benchmark 标注设计在模型分析之前预先确定的**，并非为最大化某一模型排名而调参——目的是反映 benchmark 既定的风险结构（更明显违背图表证据的选项应受更大惩罚）。
- **D.4 Interpretation**：给出 β 的语义——`β=1` 时 precision 与 recall 等权；`β>1` 更强调避免错误选择（高 precision）；`β<1` 更强调覆盖正确选项（高 recall）。
- **D.5 Why Not Standard F1? → “Analysis of MFβ Curves”**：在 **Figure 5 与 Figure 6** 中绘制了**全部模型在不同 β 取值下的 MFβ 曲线**。曲线整体单调递增，说明当前任务下“选全正确项”比“避开错误项”更难；曲线之间的**交叉点（intersection points）**揭示了不同模型在“召回正确项 vs. 规避错误项”上的权衡，可据此为不同场景做模型选择（recall 导向任务优先选交叉点之前更优的模型，precision 导向任务优先选交叉点之后更优的模型）；并以 InternVL2-26B 为例说明部分模型对 β 变化高度敏感，反映其 recall/precision 平衡能力不稳定。

**补充说明：我们提供的只是一个“中庸”的默认设置，并非唯一正确配置。** MFβ 的设计初衷正是**可按实际场景灵活调节**：

- **不同风险承受度**：高风险/高合规场景（如医疗、金融决策）可调高 β（>1）以更强惩罚错误选择、偏向 precision；探索性/召回优先场景可调低 β（<1）以更看重覆盖正确选项。
- **不同 easy/hard 错误惩罚力度**：可按业务对两类错误危害的判断调节 `w_e`、`w_h`，例如某些场景中“似是而非的 hard error”反而更具误导性、可相应提高 `w_h`。

本次新增的权重敏感性实验进一步证明：在上述可调区间内，**模型相对排名高度稳健**。因此默认配置 `e1_h0.5, β=1` 兼顾了直觉合理性与排名稳定性，而使用者完全可以根据自身风险偏好重新设定权重与 β，指标框架本身对此原生支持。

---

## 实验二：半采样稳定性（Half-Sampling Stability）

### 动机

审稿人认为每语言 2,160 个 QA、每任务约 540 偏小，担心结论是样本量不足导致的偶然结果，并建议提供 bootstrap 置信区间。本实验直接检验“规模是否足以支撑稳定结论”。

### 设计

在 Table 3 的 **16 个模型的共同可评分样本交集**上（保证所有模型在同一批样本上公平比较），按 task 分层做 **50% 随机抽样**，**重复 100 次**，每次重新计算各模型分数与排行榜，再与全量结果比较：

- `spearman`：half-sample 排名与全量排名的秩相关系数（越接近 1 越稳定）；
- `top3_overlap` / `top5_overlap`：头部模型集合重合比例；
- `mean/max_abs_score_diff`：分数绝对偏差（已 ×100）；
- `mean/max_abs_rank_shift`：排名变化幅度。

主指标定义：Task1/Task2 为 `accuracy`，Task3/Task4 为 `mf_beta`，`overall_macro` 为四个任务主指标的等权宏平均。

### 结果（100 次重复均值）

| 语言 | Spearman | Top-3 overlap | Top-5 overlap | 平均分数偏差 | 平均排名变化 | 最大排名变化 |
|---|---:|---:|---:|---:|---:|---:|
| en | 0.996 | 0.997 | 0.992 | 0.74 | 0.145 | 0.74 |
| cn | 0.987 | 1.000 | 0.850 | 0.78 | 0.38 | 1.78 |
| es | 0.986 | 0.983 | 0.844 | 1.07 | 0.36 | 1.96 |

### 结论

- 即使**只用一半样本**，排名与全量结果的 **Spearman ≥ 0.986**，三语言下排名几乎完全一致。
- **Top-3 重合度 0.98–1.00**，头部结论极其稳定。
- 平均分数偏差仅约 0.7–1.1 分（百分制），平均排名变化不足 0.4 位，远小于模型之间的真实分数差距。
- 当前规模带来的随机波动**显著小于模型间真实差异**，论文排序与结论并非样本量不足导致的偶然现象。

该实验提供了与 bootstrap 置信区间等价的稳定性证据：**结论对样本子集高度不敏感**。

---

## 规模的同口径对比

按 QA 数同口径，MultiChartQA-R 每语言规模与近期 chart QA / 多图 chart benchmark 相当或更大：

| Benchmark | QA 数 |
|---|---:|
| CharXiv (Wang et al., 2024) | ~5,000（验证集，单图） |
| **MultiChartQA-R（本文，每语言）** | **2,160** |
| MultiChartQA (Zhu et al., 2024) | 2,000 |
| ChartQAPro (Masry et al., 2025) | 1,948 |

本文每语言 2,160 个 QA 已高于 ChartQAPro（1,948）与 MultiChartQA（2,000）；CharXiv 题量更大，但其为单图、模板化程度更高的任务，与本文聚焦的跨图决策推理在难度构成上不同。
