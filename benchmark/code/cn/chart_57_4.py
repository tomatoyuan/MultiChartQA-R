import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# -------------------- 数据定义 --------------------
years = ["2025e", "2026e", "2027e"]
market_size = [8.1, 9.4, 10.9]  # 市场规模（亿元）
growth_rate = [13.9, 16.6, 15.9]  # 增速（%）

# 颜色配置（贴近原图）
bar_color = "#a5d6a7"
line_color = "#4dd0e1"
cagr_color = "#a5d6a7"  # CAGR 趋势线颜色

# -------------------- 加载插图（简化模拟，实际可替换为精准图片） --------------------
# 这里用简单形状模拟，如需精准插图，可替换为实际图片路径
# img = mpimg.imread('phone_illustration.png')  # 实际插图路径
# 临时用颜色块模拟插图位置
illustration = plt.Circle((0, 0), 1, color='lightblue')

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
    label="中国海外红人营销SaaS市场规模（亿元）"
)

# -------------------- 绘制折线图（增速） --------------------
ax2.plot(
    x, 
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="增速（%）"
)

# -------------------- 绘制 CAGR 趋势线及标注 --------------------
# 计算 CAGR（简化为示意，实际需按公式计算）
cagr = 15.0
ax1.annotate(
    f"CAGR≈{cagr}%",
    xy=(2, 10.9),  # 箭头起点（2027e 柱子顶部）
    xytext=(2.2, 10.9), 
    arrowprops=dict(
        facecolor=cagr_color, 
        edgecolor=cagr_color, 
        arrowstyle="->", 
        linewidth=2
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.5)
)

# -------------------- 添加数据标注 --------------------
# 标注市场规模
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 0.2, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# 标注增速
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 0.5, 
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

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# 添加标题
ax1.set_title(
    "2025-2027年中国海外红人营销SaaS市场规模及增速预测",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()