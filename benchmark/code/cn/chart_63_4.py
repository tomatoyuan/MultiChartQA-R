import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
# 拍摄频率分类
labels = [
    "平均每天5次以上", "平均每天2-5次", "平均每天1次",
    "平均每周4-6次", "平均每周2-3次", "平均每周1次",
    "平均每周不足1次"
]
# 百分比数据
percentages = [6.4, 27.1, 18.7, 20.9, 15.7, 5.9, 5.4]

# 分组标记（前三项为“平均每天至少拍摄1次”）
group_indices = [0, 1, 2]  # 前三项的索引

# 颜色配置（贴近原图绿色系）
bar_colors = ["#a5d6a7"] * len(labels)

# 注释文本（右上角蓝色框）
annotation_text = "平均每天至少拍摄1次\n用户占比 52.2%"
annotation_box = {
    "boxstyle": "round,pad=0.5",
    "facecolor": "lightblue",
    "edgecolor": "blue",
    "alpha": 0.8
}

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(labels))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_colors, 
    height=0.6
)

# -------------------- 添加数据标注 --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1, 
        bar.get_y() + bar.get_height() / 2,
        f"{width}%",
        va="center", 
        fontsize=9, 
        color="#424242",
        fontweight="bold"
    )

# -------------------- 绘制分组虚线框 --------------------
# 找到分组的最小和最大y坐标
min_y = min([y[i] for i in group_indices]) - 0.3
max_y = max([y[i] for i in group_indices]) + 0.3
max_width = max([percentages[i] for i in group_indices]) + 3  # 虚线框宽度

# 绘制虚线框
ax.plot([0, max_width], [min_y, min_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max_width], [max_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([max_width, max_width], [min_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [min_y, max_y], color="blue", linestyle="--", linewidth=1)

# -------------------- 添加右上角注释 --------------------
ax.text(
    max_width - 2,  # 水平位置
    max_y + 0.5,    # 垂直位置（在虚线框上方）
    annotation_text,
    fontsize=9,
    color="blue",
    fontweight="bold",
    bbox=annotation_box
)

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# 隐藏x轴刻度
ax.set_xticks([])

# 隐藏顶部、右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title(
    "2022年中国美颜拍摄类APP用户拍摄人像频率",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()