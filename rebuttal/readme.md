# Rebuttal for MultiChartQA-R

## To Reviewers

We sincerely thank all reviewers for taking the time to review our paper and for providing valuable, detailed, and constructive comments. We have carefully read each comment from every reviewer and will respond thoroughly to each one.

Below are links to the responses for each reviewer, ordered according to the OpenReview sequence:

### Point-by-Point Responses (in OpenReview Order)

- [Reviewer 9osS（Rating 5, Confidence 4）](./reviewer_responses/reviewer_9osS_en.md)
- [Reviewer JrJk（Rating 6, Confidence 3）](./reviewer_responses/reviewer_JrJk_en.md)
- [Reviewer y7VS（Rating 6, Confidence 4）](./reviewer_responses/reviewer_y7VS_en.md)
- [Reviewer VtVH（Rating 7, Confidence 4）](./reviewer_responses/reviewer_VtVH_en.md)
- [Reviewer zF7Z（Rating 5, Confidence 3）](./reviewer_responses/reviewer_zF7Z_en.md)

### Paper and Appendix

- [Full Paper (with Appendix)](https://tomatoyuan.github.io/MultiChartQA-R/paper.html)
- [Appendix](https://tomatoyuan.github.io/MultiChartQA-R/appendix.html)

---

## Supplementary Experiments

For the convenience of reviewers, below is the complete content of the two new experiments we have supplemented in response to the review comments.

# Supplementary Experiments

This document summarizes the two new experiments we conducted in response to the reviews.

- Risk-Weight Sensitivity experiment
- Half-Sampling Stability experiment

The two experiments directly address the two most frequently raised concerns:

1. **Whether the weights of the Strict Risk-Aware MFβ metric are arbitrary, and whether the model ranking shifts as the weights change** (Reviewers 9osS / JrJk / VtVH)
2. **Whether the benchmark is large enough to support stable conclusions** (Reviewers 9osS / VtVH / zF7Z)

---

## Experiment 1: Strict Risk-Aware MFβ Risk-Weight Sensitivity

### Motivation

Reviewers noted that the weight settings of the MFβ metric (`w_e=1.0`, `w_h=0.5`, `β=1`) appear somewhat heuristic, and were concerned that different weights might change the model ranking. This experiment systematically examines how sensitive the ranking is to the choice of weights.

### Design

Using the paper's configuration `e1_h0.5` (easy-error weight = 1.0, hard-error weight = 0.5) as the baseline, we swept **9 weight configurations** across all **16 models** and **3 languages**, along two axes:

- Fix the hard-error weight at 0.5 and vary the easy-error weight: 0.5 / 0.75 / 1.0 / 1.25 / 1.5
- Fix the easy-error weight at 1.0 and vary the hard-error weight: 0.0 / 0.25 / 0.5 / 0.75 / 1.0

For each configuration, we recomputed the MFβ scores and rankings for all models, and compared them against the baseline in terms of Top-1, Top-3 membership, and maximum absolute rank shift.

### Results (English / en)

| Configuration | Top-1 | Top-3 | Max abs. rank shift |
|---|---|---|---:|
| e0.5_h0.5 | claude-sonnet-4 | claude, Qwen3-VL-32B, Seed1.5-VL | 3 |
| e0.75_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 1 |
| **e1_h0.5 (baseline)** | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1.25_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1.5_h0.5 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 0 |
| e1_h0 | claude-sonnet-4 | claude, Seed1.5-VL, gemini-2.5-pro | 2 |
| e1_h0.25 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 2 |
| e1_h0.75 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 1 |
| e1_h1 | claude-sonnet-4 | claude, Seed1.5-VL, Qwen3-VL-32B | 2 |

### Findings

- **Top-1 is claude-sonnet-4 under all 9 configurations and all 3 languages, without exception.**
- **The Top-3 set is almost entirely unchanged** (only under the most extreme configuration do Qwen3-VL-32B and gemini-2.5-pro swap the third position).
- The maximum absolute rank shift is 0–1 under most configurations; even the most extreme case, `e0.5_h0.5`, reaches only 3 (en), while the maximum is 1 for cn and 2 for es.
- Varying the weights mainly produces a global shift in the absolute scores (for example, raising the hard-error penalty from 0 to 1 causes a more pronounced drop for "high-recall but high-false-positive" models such as gpt-4o), but **it does not change the relative ordering among models**.

Therefore, `e1_h0.5` was not chosen because it is "special," but because it lies within a **stable ranking plateau** and is consistent with the intuition that "hard errors (those contradicting chart evidence, or hallucination-type errors) are more harmful than easy errors (approximate mistakes) and should be penalized more heavily."

### Connection to the Appendix: β Has Already Been Systematically Explored

We emphasize that **the exploration of β is already presented in the appendix of the original paper, and this sensitivity experiment serves to further reinforce it.** The relevant locations are as follows (see `appendix.pdf`, Appendix D *Metric Exploration and Phenomenon Analysis*, pp. 11–13):

- **D.3 Formal Definition (Eqs. 5–9):** provides the full definition of the Strict Risk-Aware MFβ score, with fixed severity weights `w_e=1.0, w_h=0.5` (Eq. 7).
- **D.2 Design Rationale:** explicitly states that these weights were **determined from the benchmark's annotation design prior to any model-level analysis**, rather than tuned to maximize the ranking of any particular model—their purpose is to reflect the benchmark's intended risk structure (options that more clearly violate chart evidence should incur larger penalties).
- **D.4 Interpretation:** gives the semantics of β—at `β=1`, precision and recall are weighted equally; at `β>1`, more emphasis is placed on avoiding incorrect selections (higher precision); at `β<1`, more emphasis is placed on covering the correct options (higher recall).
- **D.5 Why Not Standard F1? → "Analysis of MFβ Curves":** **Figures 5 and 6** plot the **MFβ curves of all models across varying values of β**. The curves are overall monotonically increasing, indicating that under the current task setting "selecting all correct options" is harder than "avoiding incorrect options." The **intersection points** between curves reveal the trade-off each model makes between "recalling correct options" and "avoiding incorrect ones," and can guide model selection for different scenarios (for recall-oriented tasks, prefer models that lead before the intersection point; for precision-oriented tasks, prefer those that lead after it). Taking InternVL2-26B as an example, its curve is highly sensitive to changes in β, reflecting an unstable ability to balance recall and precision.

**A note: the configuration we provide is merely a balanced default, not the only correct one.** By design, MFβ is intended to be **flexibly adjustable according to the actual deployment scenario:**

- **Different risk tolerances:** in high-stakes / high-compliance scenarios (e.g., medical or financial decision-making), one can raise β (>1) to penalize incorrect selections more strongly and favor precision; in exploratory / recall-first scenarios, one can lower β (<1) to place greater weight on covering the correct options.
- **Different penalty strengths for easy vs. hard errors:** `w_e` and `w_h` can be adjusted according to how harmful each error type is in a given application—for instance, in some scenarios "plausible-looking hard errors" may be more misleading, in which case `w_h` can be raised accordingly.

The newly added weight-sensitivity experiment further demonstrates that, within this adjustable range, **the relative model ranking remains highly robust.** Thus the default configuration `e1_h0.5, β=1` balances intuitive justification with ranking stability, while users are free to re-specify the weights and β according to their own risk preferences—something the metric framework natively supports.

---

## Experiment 2: Half-Sampling Stability

### Motivation

Reviewers considered the 2,160 QA pairs per language (about 540 per task) to be relatively small, and were concerned that the conclusions might be artifacts of an insufficient sample size; they suggested providing bootstrap confidence intervals. This experiment directly tests "whether the scale is sufficient to support stable conclusions."

### Design

On the **intersection of commonly scorable samples across the 16 models** in Table 3 (ensuring all models are compared on the same set of samples), we perform **stratified 50% random sampling** by task, **repeated 100 times**. For each draw we recompute every model's score and the resulting leaderboard, and compare against the full-set results:

- `spearman`: the rank correlation between the half-sample ranking and the full-set ranking (closer to 1 means more stable);
- `top3_overlap` / `top5_overlap`: the overlap ratio of the top-model sets;
- `mean/max_abs_score_diff`: the absolute score deviation (already ×100);
- `mean/max_abs_rank_shift`: the magnitude of rank changes.

Primary-metric definitions: `accuracy` for Task1/Task2, `mf_beta` for Task3/Task4, and `overall_macro` is the equally weighted macro-average of the four tasks' primary metrics.

### Results (mean over 100 repetitions)

| Language | Spearman | Top-3 overlap | Top-5 overlap | Mean score dev. | Mean rank shift | Max rank shift |
|---|---:|---:|---:|---:|---:|---:|
| en | 0.996 | 0.997 | 0.992 | 0.74 | 0.145 | 0.74 |
| cn | 0.987 | 1.000 | 0.850 | 0.78 | 0.38 | 1.78 |
| es | 0.986 | 0.983 | 0.844 | 1.07 | 0.36 | 1.96 |

### Findings

- Even when **using only half of the samples**, the Spearman correlation between the resulting ranking and the full-set ranking is **≥ 0.986**, and the rankings are nearly identical across all three languages.
- The **Top-3 overlap is 0.98–1.00**, so the top-tier conclusions are extremely stable.
- The mean score deviation is only about 0.7–1.1 points (on a 0–100 scale), and the mean rank shift is under 0.4 positions—far smaller than the true score gaps between models.
- The random fluctuation induced by the current scale is **substantially smaller than the true differences between models**, so the ordering and conclusions in the paper are not coincidental artifacts of insufficient sample size.

This experiment provides stability evidence equivalent to bootstrap confidence intervals: **the conclusions are highly insensitive to the choice of sample subset.**

---

## Like-for-Like Comparison of Scale

On a like-for-like basis by number of QA pairs, the per-language scale of MultiChartQA-R is comparable to or larger than that of recent chart QA / multi-chart benchmarks:

| Benchmark | # QA |
|---|---:|
| CharXiv (Wang et al., 2024) | ~5,000 (validation set, single-chart) |
| **MultiChartQA-R (ours, per language)** | **2,160** |
| MultiChartQA (Zhu et al., 2024) | 2,000 |
| ChartQAPro (Masry et al., 2025) | 1,948 |

Our 2,160 QA pairs per language already exceed ChartQAPro (1,948) and MultiChartQA (2,000); CharXiv has more questions, but its tasks are single-chart and more template-based, differing in difficulty composition from our focus on cross-chart, decision-oriented reasoning.
