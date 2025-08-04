import matplotlib.pyplot as plt
import numpy as np

# 数据定义
categories = ["更换周期"]
labels = ["1年以内", "1-2年", "2-3年", "3-5年", "5年以上"]
sizes = [5.7, 41.4, 39.3, 11.1, 2.6]  # 占比（%）
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # 颜色配置

# 创建画布：增大高度，减小宽度，让图表更“瘦高”
fig, ax = plt.subplots(figsize=(6, 5))  # 调整为宽6，高5

# 绘制分段条形图（移除错误的 height 参数）
start = 0
for i in range(len(sizes)):
    ax.bar(
        categories, 
        sizes[i], 
        bottom=start, 
        color=colors[i], 
        edgecolor="white",
        linewidth=1,
        label=labels[i]
    )
    # 添加数据标注
    ax.text(
        categories[0], 
        start + sizes[i]/2, 
        f"{sizes[i]}%",
        ha="center", 
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )
    start += sizes[i]

# 隐藏y轴（仅保留x轴分类）
ax.set_yticks([])

# 隐藏顶部、右侧、左侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# 设置x轴标签
ax.set_xticklabels(categories, fontsize=10, color="#424242")

# 添加图例（调整位置到底部，横向排列）
ax.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.25),  # 图例位置微调
    ncol=len(labels),            # 横向排列
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "更换框架眼镜的周期",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局（给图例留出空间）
plt.subplots_adjust(bottom=0.25)

plt.show()