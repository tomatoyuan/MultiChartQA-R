import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# 数据
labels = [
    "受到激励，近一年尝试选择更令自己舒适的生活方式",
    "通过外界了解到更多女性相关的议题，但未公开表达",
    "近一年我有参与公众关于女性话题的讨论",
    "一直不太关注，觉得与自己的生活太远，过好自己的生活就…",
    "girls help girls，近一年尝试通过向外表达影响身边的女性",
    "觉得话题过度饱和，近一年刻意减少关注"
]
percentages = [41.9, 18.3, 17.4, 10.1, 8.0, 4.3]

# 创建自定义渐变色
colors = ["#4a6fe3", "#6a89f0", "#8aa5f7", "#a9bffb", "#c7d8fd", "#e5f0ff"]

# 创建图表
fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(labels))

# 绘制横向渐变色条形图
for i, (value, label) in enumerate(zip(percentages, labels)):
    bar = ax.barh(i, value, align='center', color=colors[i], alpha=0.9, edgecolor='none')
    ax.text(value + 0.5, i, f'{value}%', va='center', fontsize=11, color='#333333')

# 设置Y轴标签
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12)
ax.invert_yaxis()  # 标签从上到下排列

# 设置X轴范围
ax.set_xlim(0, max(percentages) * 1.15)  # 留出一些空间显示标签

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.7)

# 设置标题和标签
ax.set_title('女性话题对女性个体影响调研', fontsize=16, pad=20)
ax.set_xlabel('百分比（%）', fontsize=12, labelpad=10)

# 调整边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()