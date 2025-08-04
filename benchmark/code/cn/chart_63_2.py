import matplotlib.pyplot as plt
import numpy as np

# 数据（名称、百分比）
labels = [
    "平均每天多次", "平均每天一次", "平均2-3天发布一次",
    "平均4-6天一次", "平均每周一次", "平均每月2-3次",
    "平均每月1次", "几乎从不"
]
percentages = [8.4, 13.5, 28.2, 12.2, 12.9, 10.9, 7.2, 6.7]

# 颜色配置（贴近原图绿色系，最后一个“几乎从不”用灰色）
colors = ["#a5d6a7"] * 7 + ["#d3d3d3"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向条形图
y = np.arange(len(labels))
bars = ax.barh(y, percentages, color=colors, height=0.6)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
            f"{width}%", va="center", fontsize=9, color="#333")

# 绘制蓝色虚线框（选中前三项）
ax.plot([0, max(percentages) + 5], [y[0] - 0.3, y[0] - 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max(percentages) + 5], [y[2] + 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([max(percentages) + 5, max(percentages) + 5], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)

# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# 隐藏x轴刻度
ax.set_xticks([])

# 隐藏顶部、右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title("2022年中国美颜拍摄类APP用户原创内容发布频率", fontsize=14, fontweight="bold", pad=20)

# 调整布局
plt.tight_layout()
plt.show()