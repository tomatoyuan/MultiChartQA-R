import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- 数据定义 --------------------
categories = [
    "促进大脑发育",
    "免疫力问题",
    "促进肠胃消化",
    "强健骨骼/促进骨骼发育",
    "生长发育问题",
    "促进视力发育"
]
percentages = [73.5, 72.3, 68.1, 64.5, 63.9, 53.6]

# -------------------- 颜色映射：渐变配色 --------------------
# 使用 colormap（plasma/magma/turbo等）
cmap = cm.get_cmap("plasma")
norm = mcolors.Normalize(vmin=min(percentages), vmax=max(percentages))
colors = [cmap(norm(p)) for p in percentages]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- 绘制“进度条式”横向条形图 --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
    height=0.5,
    edgecolor="gray",
    linewidth=1.2
)

# 添加百分比文本
for i, (bar, value) in enumerate(zip(bars, percentages)):
    ax.text(
        value + 1, bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}%",
        va="center", ha="left",
        fontsize=10, fontweight="bold", color="#333333"
    )

# -------------------- 美化图表 --------------------
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color="#333333")

# 隐藏x轴刻度
ax.set_xticks([])
# 去除多余边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)

# 添加标题
ax.set_title("0-3岁婴幼儿阶段的健康关注（%）", fontsize=14, fontweight="bold", pad=20)

# 留白空间
plt.tight_layout()
plt.show()