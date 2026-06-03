Thank you for your thoughtful reviews. We have prepared **point-by-point responses to each reviewer**, including two new experiments addressing top concerns.

**Full rebuttal (bilingual, default English):**
**https://github.com/tomatoyuan/MultiChartQA-R/blob/main/rebuttal/readme.md**

Below we summarize responses to common concerns.

### 1. Are MFβ metric weights arbitrary? Do rankings change? (9osS, JrJk, VtVH)

We ran a **Risk-Weight Sensitivity** experiment across **9 configs × 16 models × 3 languages**, varying easy-error (0.5–1.5) and hard-error weights (0.0–1.0) around our default `e1_h0.5` (shorthand: `w_e=1.0`, `w_h=0.5`). Findings:
- **Top-1 is claude-sonnet-4 in every config and language, without exception.**
- **Top-3 set is nearly invariant** — only the most extreme config swaps rank-3 between Qwen3-VL-32B and gemini-2.5-pro.
- **Max rank shift is mostly 0–1**; even the most extreme case reaches only 3 in en, 1 in cn, 2 in es.

**Parameters:**
- `w_e`: penalizes approximate mistakes/clearly wrong conclusions — **easy errors are more harmful** (fundamental comprehension failures)
- `w_h`: penalizes evidence-contradicting errors/hallucinations
- `β`: balances precision vs. recall (`β=1` equal, `β>1` favors precision, `β<1` favors recall)

**By scenario:**
- **High-stakes** (medical/financial): ↑`β` (→2) and ↑`w_e` (→1.5) to heavily penalize missed answers/obvious mistakes
- **General analytics**: default `e1_h0.5, β=1` for balanced precision/recall
- **Exploratory analysis**: ↓`β` (→0.5) to prioritize recalling all correct options

Weight changes shift absolute scores but **do not alter relative ordering**. The default sits squarely within a **stable ranking plateau**. Critically, weights were set from annotation design **before any model analysis** (Appendix D.2). The influence of β was systematically explored in the original paper (Appendix D.4–D.5, Figures 5–6). We will add this sensitivity analysis to the revised appendix.

### 2. Is the dataset too small for stable conclusions? (9osS, VtVH, zF7Z)

Our unit is the **multi-chart set** (180 sets/language, 540 instances/task × 4 tasks → 2,160 QA pairs/language; main §2.2, Appendix A.1, Table 1). Multi-chart items are far costlier to annotate than single-chart QA. By QA count, our per-language scale is comparable to or larger than recent benchmarks: **MultiChartQA-R 2,160 > MultiChartQA 2,000 > ChartQAPro 1,948**.

We ran a **Half-Sampling Stability** experiment: stratified 50% sampling by task, repeated 100× across all 16 models. Across all three languages:
- **Spearman ≥ 0.986** between half-sample and full rankings;
- **Top-3 overlap 0.98–1.00**;
- Mean score deviation ~0.7–1.1 (×100), mean rank shift < 0.4.

Random fluctuation is **far smaller than true between-model gaps**, providing bootstrap-equivalent evidence of stability. We will add bootstrap 95% CIs to key table entries.

### 3. Other Commonly Raised Concerns

**LLM-Assisted Data Generation (VtVH, JrJk, y7VS):**
**Critical design detail: synthesis and evaluation use models of different modalities.** The Tasks 3–4 synthesis model is a **text-only reasoning model** that takes chart-rendering code (with gold-table data) and task definitions as input — it never sees chart *images* (main §2.2, Figure 2). Evaluation targets are **multimodal LLMs** that must perceive visual information from chart images. This fundamentally eliminates circular risk. Notably, even strong multimodal baselines do **not** systematically top Tasks 3–4 (e.g., several commercial models rank mid/lower; Appendix D.6, Table 5). All instances are human-refined with 85–87% inter-rater agreement (Appendix B.1).

**LLM Judge Reliability (9osS, y7VS, VtVH):**
We supplemented a **50% human-LLM consistency evaluation** (STEM annotators, blind scoring; Appendix D.7, Generative Evaluation):
- Option-level: 91.4% exact match, Cohen's Kappa = 0.83;
- Explanation quality: average Spearman 0.82, MAE = 0.46 (Appendix D.7.3);
- No significant systematic bias, only slight strictness on boundary samples.

**Chart Reconstruction (JrJk, 9osS, zF7Z):**
Evaluation charts are **code-rendered**, with gold-tables extracted from the *same code's underlying data* (main §2.2). Charts and ground truth are **homologous by construction** — no "reconstruct data from images" step exists to introduce errors. Visual fidelity is ensured through iterative human verification (main §2.2).

**Concrete revision plans for the final paper:** We will add: (1) the full weight sensitivity analysis to Appendix D; (2) bootstrap 95% CIs to all key metrics in main results Table 2; (3) qualitative error analysis of substantive reasoning failures to Appendix E; (4) a modular baseline comparison (SOTA Chart-to-Table + LLM) to §4; (5) explicit cross-references to Appendix B for human baseline details; (6) a comparable-subset reference to the original MultiChartQA in §4.

Full point-by-point responses, experimental data, and reproducible artifacts are available in our repository. We sincerely thank reviewers for their thoughtful feedback, which has significantly strengthened this work. We welcome further discussion.

**Paper and Appendix:**
- Full paper: https://tomatoyuan.github.io/MultiChartQA-R/paper.html
- Appendix: https://tomatoyuan.github.io/MultiChartQA-R/appendix.html
