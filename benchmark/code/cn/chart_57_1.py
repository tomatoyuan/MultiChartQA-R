import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
ratios = [10.5, 11.0, 6.4, 9.5, 9.1, 7.7, 7.7]  # 营销预算占比（%）

# 颜色配置（贴近原图绿色）
line_color = "#a5d6a7"
trend_color = "#dcdcdc"  # 趋势线颜色

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制折线图 --------------------
ax.plot(
    years, 
    ratios, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="平均营销预算占营业收入的比例"
)

# -------------------- 绘制趋势线（虚线） --------------------
# 计算线性拟合趋势
z = np.polyfit(years, ratios, 1)
p = np.poly1d(z)
ax.plot(years, p(years), color=trend_color, linestyle="--", linewidth=1)

# -------------------- 添加数据标注 --------------------
for i, val in enumerate(ratios):
    ax.text(
        years[i], val + 0.2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- 添加底部注释 --------------------
ax. annotate(
    "宏观经济不确定增强，企业营销预算占比下滑",
    xy=(0.5, -0.25),  # 注释位置（底部居中）
    xycoords="axes fraction",
    ha="center",
    va="top",
    fontsize=12,
    color="#424242",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# -------------------- 美化图表 --------------------
# 设置x轴标签（年份）
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, color="#424242")

# 设置y轴范围（0-12%）
ax.set_ylim(0, 12)

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
    "2019-2025年全球企业平均营销预算占营业收入的比例",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()