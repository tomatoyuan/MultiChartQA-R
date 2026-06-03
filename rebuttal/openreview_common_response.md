# OpenReview Rebuttal — Common Response (≤5000 chars)

> 用途：直接粘贴到 OpenReview 的统一回复（Common Response）。正文为英文，已控制在 5000 字符以内。逐条回复与补充实验细节见文末 GitHub 链接。

---

We thank all reviewers for their careful and constructive feedback. We are encouraged that reviewers found the task design "pushes the boundary toward what analysts actually do" (JrJk, VtVH), the Strict Risk-Aware MFβ metric "a significant contribution" (VtVH, JrJk), and the Cross-Lingual Asymmetry finding "interesting and non-obvious" (zF7Z, 9osS, VtVH). Below we address the two most shared concerns with **two new experiments**, then summarize our revision plan. Per-reviewer replies and full results are linked at the end; all artifacts are reproducible in our repo.

**[1] Are the MFβ weights arbitrary? Do rankings change under different weights? (9osS, JrJk, VtVH)**

We ran a **Risk-Weight Sensitivity** experiment over **9 weight configurations × 16 models × 3 languages**, varying easy-error weight (0.5–1.5) and hard-error weight (0.0–1.0) around our config `e1_h0.5`. Findings:
- **Top-1 is claude-sonnet-4 in every configuration and every language, without exception.**
- The **Top-3 set is almost invariant** (only the most extreme config swaps rank-3 between Qwen3-VL-32B and gemini-2.5-pro).
- The **max absolute rank shift is mostly 0–1** (max 3 in en, 1 in cn, 2 in es).

Weight changes mainly shift absolute scores (e.g., raising the hard penalty lowers high-recall/high-false-positive models like gpt-4o) but **do not change relative ordering**. Thus `e1_h0.5` is not "special"; it sits on a stable ranking plateau and reflects the intuition that hard errors (contradicting visual evidence / hallucinations) are more harmful than easy (approximate) errors. We will add this analysis and reframe tunable-yet-robust weighting as a feature.

**[2] Is the dataset too small to support stable conclusions? (9osS, VtVH, zF7Z)**

First, on scale: our construction unit is the **multi-chart set**, with 4 task instances per set per language (180×4×3 → 2,160 QA/language). Multi-chart reasoning items are far costlier to annotate and verify than single-chart QA. By QA count, our per-language size is on par with or larger than recent chart benchmarks: **MultiChartQA-R 2,160 > MultiChartQA 2,000 > ChartQAPro 1,948** (CharXiv has more questions but is single-chart and more template-based).

Second, we ran a **Half-Sampling Stability** experiment: on the common scorable intersection of all 16 models, we draw stratified 50% samples, repeat 100×, and recompute the leaderboard. Across all three languages:
- **Spearman ≥ 0.986** between half-sample and full rankings;
- **Top-3 overlap 0.98–1.00**;
- mean score deviation ~0.7–1.1 (×100), mean rank shift < 0.4.

Random fluctuation from the current scale is **far smaller than true between-model gaps**, giving bootstrap-equivalent evidence that conclusions are insensitive to sample subsets. We will also add bootstrap CIs to key table entries.

**Note on circularity (VtVH, JrJk, y7VS):** the synthesis models (GPT-4o/Claude) used for Tasks 3–4 do **not** systematically top those tasks (e.g., gpt-4o ranks mid/low), which is contrary to what a circularity bias would predict.

**Revision plan for remaining points:**
- **Reconstruction fidelity (9osS, JrJk, zF7Z):** add quantitative validation (key-value match rate / rejection rate), focusing on Task 2.
- **Tasks 3–4 transparency (JrJk, VtVH, y7VS):** report % significantly edited vs. filtered, correction types, and IAA of human refinement.
- **LLM-judge validity (9osS, y7VS, VtVH):** report LLM-judge vs. human-expert agreement (correlation/Kappa) on a sampled subset; state as a limitation if low.
- **Multilingual (9osS):** both new experiments cover en/cn/es and show consistent-but-divergent behavior (es most volatile), supporting the multilingual design; we will break down Tasks 3–4 by language in the main table.
- **Modular baseline (VtVH):** add a (SOTA Chart-to-Table)+(GPT-4o) pipeline to disentangle perception vs. reasoning failures.
- **Human baseline & error analysis (zF7Z):** add annotation protocol/qualifications/IAA, and qualitative analysis of substantive reasoning failures (cross-chart integration, causal errors).
- **Comparison to original MultiChartQA (9osS):** clarify task/metric differences and provide a comparable-subset reference.

We believe the two new experiments directly and quantitatively resolve the core concerns on **metric robustness** and **scale reliability**, and we have a concrete plan for the rest. We would be glad to discuss further.

---

## Supporting materials (GitHub)

- Supplementary experiments (weight sensitivity + half-sampling stability), full tables & reproducible artifacts:
  https://github.com/tomatoyuan/MultiChartQA-R/blob/main/rebuttal/supplementary_experiments.md
- Point-by-point response to every reviewer comment:
  https://github.com/tomatoyuan/MultiChartQA-R/blob/main/rebuttal/point_by_point_response.md
