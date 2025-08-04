import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2018, 2019, 2020, 2021, 2022]
rates = [53.60, 50.20, 52.70, 52.60, 51.90]  # 近视率（%）

# 颜色配置（贴近原图绿色）
line_color = "#a5d6a7"

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制折线图 --------------------
ax.plot(
    years, 
    rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="比率"
)

# -------------------- 添加数据标注 --------------------
for i, val in enumerate(rates):
    ax.text(
        years[i], val + 0.2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- 美化图表 --------------------
# 设置x轴标签（年份）
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, color="#424242")

# 设置y轴范围（49-55%，根据数据调整）
ax.set_ylim(49, 55)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加图例
ax.legend(
    loc="upper right", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "2018-2022年全国儿童青少年总体近视率",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()