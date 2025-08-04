import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2014, 2015, 2016, 2017, 2021, 2019, 2020, 2021]
sales_scales = [1047, 1325, 1644, 2074, 2519, 3064, 3778, 4519]  # 销售规模（亿元）
growth_rates = [26.5, 24.1, 26.1, 21.5, 21.6, 23.3, 19.6]        # 增长率（%）

# 颜色配置（贴近原图）
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- 创建画布和双轴 --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# 创建次坐标轴（增长率）
ax2 = ax1.twinx()

# -------------------- 绘制柱状图（销售规模） --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    sales_scales, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="中国IC设计业销售规模（亿元）"
)

# -------------------- 绘制折线图（增长率） --------------------
# 增长率数据比销售规模少一个（2014年无增长率），需对齐年份
ax2.plot(
    x[1:],  # 从2015年开始
    growth_rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="中国IC设计业销售规模增长率（%）"
)

# -------------------- 添加数据标注 --------------------
# 标注销售规模
for i, val in enumerate(sales_scales):
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
        x[i+1], val + 0.5, 
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

# 设置主y轴标签（销售规模）
ax1.set_ylabel("中国IC设计业销售规模（亿元）", fontsize=12, color="#424242")

# 设置次y轴标签（增长率）
ax2.set_ylabel("中国IC设计业销售规模增长率（%）", fontsize=12, color="#424242")

# 隐藏冗余边框
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# 添加标题
ax1.set_title(
    "2014-2021年中国IC设计业销售规模",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()