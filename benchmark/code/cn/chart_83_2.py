import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# -------------------- 数据定义 --------------------
years = ["2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e"]
market_size = [667, 817, 1011, 1266, 1618, 2079, 2686]
x = np.arange(len(years))
bar_width = 0.3

# -------------------- 配色方案（渐变+可爱风） --------------------
colors = ['#A5D6A7', '#81C784', '#4DD0E1', '#4FC3F7', '#9575CD', '#BA68C8', '#F48FB1']

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# 设置合适的y轴范围，避免柱子太高撑爆图像
max_height = max(market_size)
ax.set_ylim(0, max_height * 1.15)  # 最高值的 115%

# -------------------- 绘制圆角柱状图 --------------------
for i in range(len(x)):
    bar_height = market_size[i]
    bar_color = colors[i % len(colors)]
    # 使用 FancyBboxPatch 画圆角矩形（bar）
    rect = FancyBboxPatch(
        (x[i] - bar_width / 2, 0),     # 左下角
        bar_width, bar_height,         # 宽、高
        boxstyle="round,pad=0.02,rounding_size=6",  # 圆角配置
        linewidth=0,
        facecolor=bar_color,
        edgecolor=None
    )
    ax.add_patch(rect)
    
    # 添加数据标注
    ax.text(
        x[i], bar_height + 50,
        f"{bar_height}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=bar_color
    )

# -------------------- 坐标轴与装饰 --------------------
# 设置x轴
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
# 设置y轴标签
ax.set_ylabel("中国康复医疗服务市场规模及空间（亿元）", fontsize=11)

# 添加CAGR标注（左上角）
ax.text(
    0.05, 0.93,
    "CAGR = 38.5%",
    transform=ax.transAxes,
    fontsize=12,
    fontweight="bold",
    color="#F06292",
    bbox=dict(facecolor="#ffe0f0", alpha=0.6, boxstyle="round,pad=0.3", edgecolor='none')
)

# 添加标题
ax.set_title("2019-2025年中国康复医疗服务市场规模及空间", fontsize=14, fontweight="bold", pad=20)

# 隐藏顶部和右边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 自动布局
plt.tight_layout()
plt.show()