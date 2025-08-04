import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
enterprise_counts = [681, 736, 1362, 1380, 1698, 1780, 2218, 2810]  # 企业数量（个）
growth_rates = [8.1, 85.1, 1.3, 23.0, 4.8, 24.6, 26.7]              # 增长率（%）

# 颜色配置（贴近原图）
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- 创建画布和双轴 --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# 创建次坐标轴（增长率）
ax2 = ax1.twinx()

# -------------------- 绘制柱状图（企业数量） --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    enterprise_counts, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="中国IC设计企业数量（个）"
)

# -------------------- 绘制折线图（增长率） --------------------
# 增长率数据比企业数量少一个（2014年无增长率），需对齐年份
ax2.plot(
    x[1:],  # 从2015年开始
    growth_rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="中国IC设计企业数量增长率（%）"
)

# -------------------- 添加数据标注 --------------------
# 标注企业数量
for i, val in enumerate(enterprise_counts):
    ax1.text(
        i, val + 50, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# 标注增长率
for i, val in enumerate(growth_rates):
    # 增长率对应年份是2015-2021（x[1]到x[7]）
    ax2.text(
        x[i+1], val + 2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- 美化图表 --------------------
# 设置x轴标签（年份）
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10, color="#424242")

# 设置主y轴标签（企业数量）
ax1.set_ylabel("中国IC设计企业数量（个）", fontsize=12, color="#424242")

# 设置次y轴标签（增长率）
ax2.set_ylabel("中国IC设计企业数量增长率（%）", fontsize=12, color="#424242")

# 隐藏冗余边框
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# 添加标题
ax1.set_title(
    "2014-2021年中国IC设计业企业数量",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()