import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = ["2020", "2021", "2022", "2023", "2024", "2025e", "2026e", "2027e"]
market_size = [12379.2, 27365.3, 36369.2, 49168.4, 57863.8, 68048.4, 78086.4, 87871.0]  # 市场规模（亿元）
growth_rate = [121.1, 32.9, 35.2, 17.7, 17.6, 14.8, 12.5]  # 增速（%）

# 颜色配置（贴近原图）
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- 创建画布和双轴 --------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# 创建次坐标轴（增速）
ax2 = ax1.twinx()

# -------------------- 绘制柱状图（市场规模） --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    market_size, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="中国直播电商市场规模（亿元）"
)

# -------------------- 绘制折线图（增速） --------------------
ax2.plot(
    x[:-1],  # 增速数据比年份少1个（2027e 无增速）
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="增速（%）"
)

# -------------------- 添加数据标注 --------------------
# 标注市场规模
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 1000, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# 标注增速
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 2, 
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

# 设置主y轴标签（市场规模）
ax1.set_ylabel("市场规模（亿元）", fontsize=12, color="#424242")

# 设置次y轴标签（增速）
ax2.set_ylabel("增速（%）", fontsize=12, color="#424242")

# 隐藏冗余边框
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# 合并图例（调整位置，向上移动）
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines1 + lines2, 
    labels1 + labels2, 
    loc="upper left", 
    bbox_to_anchor=(0, 1.2),  # 向上移动图例
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 添加标题
ax1.set_title(
    "中国直播电商市场规模及增速",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()