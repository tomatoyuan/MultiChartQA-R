import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = ["互联网使用", "学习培训", "文化休闲娱乐", "运动健身"]
years = ["2008年", "2018年", "2024年"]

# 数据：[2008, 2018, 2024]（分钟）
data = [
    [14, 162, 363],    # 互联网使用：14→162→363（分钟）
    [27, 107, 287],    # 学习培训：27→107→287（分钟）
    [40, 105, 153],    # 文化休闲娱乐：40→105→153（分钟）
    [23, 31, 35]       # 运动健身：23→31→35（分钟）
]

# 颜色配置（贴近原图）
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]  # 2008、2018、2024 对应颜色

# 注释配置（增长率）
annotations = [
    {"year": "2018→2024", "growth": 125.9, "pos": (2, 363 + 10)},
    {"year": "2008→2018", "growth": 260.0, "pos": (1, 107 + 10)},
]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- 绘制分组柱状图 --------------------
x = np.arange(len(categories))
bar_width = 0.25

for i in range(len(years)):
    ax.bar(
        x + i * bar_width, 
        [d[i] for d in data], 
        width=bar_width, 
        color=colors[i], 
        label=years[i],
        edgecolor="white",
        linewidth=1
    )

# -------------------- 添加数据标注（分钟） --------------------
for i in range(len(categories)):
    for j in range(len(years)):
        val = data[i][j]
        ax.text(
            x[i] + j * bar_width, 
            val + 5, 
            f"{val}分钟",
            ha="center", 
            va="bottom",
            fontsize=9,
            color="#424242",
            fontweight="bold"
        )

# -------------------- 美化图表 --------------------
# 设置x轴标签（活动类型）
ax.set_xticks(x + bar_width)
ax.set_xticklabels(categories, fontsize=11, color="#424242")

# 设置y轴范围（0-400分钟，根据数据调整）
ax.set_ylim(0, 400)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加图例
ax.legend(
    loc="upper left", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "全国居民每日活动平均时长",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()