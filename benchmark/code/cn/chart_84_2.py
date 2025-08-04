import matplotlib.pyplot as plt
import numpy as np

# 主要因素
factors = [
    "服用方便",
    "效果好",
    "便携",
    "没有“吃药”体感",
    "新颖",
    "包装好看"
]
# 对应占比（%），数据与图表一致
percentages = [65.0, 56.0, 45.0, 38.0, 30.0, 23.0]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制条形图（水平条形图，调整为与原图方向一致）
y = np.arange(len(factors))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#A4C639")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签（调整顺序，让第一个因素在最上方）
ax.set_yticks(y)
ax.set_yticklabels(factors)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2021年消费者选择“功能性零食”的主要因素", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()