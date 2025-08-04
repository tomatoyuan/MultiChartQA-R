import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# 数据准备
age_groups = ['18岁以下', '18-24岁', '25-34岁', '35-44岁', '45-54岁', '55-64岁', '65岁以上']
data = [20, 30, 15, 12, 10, 8, 8]

# 创建渐变色
colors = plt.cm.Blues(np.linspace(0.8, 0.4, len(age_groups)))
highlight_index = 1  # 高亮显示第二个年龄段
colors[highlight_index] = plt.cm.Oranges(0.6)  # 使用橙色高亮

# 创建画布和子图
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# 设置背景样式
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 绘制柱状图
bars = ax.bar(age_groups, data, color=colors, edgecolor='black', linewidth=0.5, alpha=0.9)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height}', ha='center', va='bottom', fontsize=10)

# 设置标题和标签
ax.set_title('冠心病搜索人群年龄层次分析', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('年龄分组', fontsize=12, labelpad=10)
ax.set_ylabel('搜索人数', fontsize=12, labelpad=10)

# 设置y轴范围和刻度
ax.set_ylim(0, max(data) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例
legend_labels = ['其他年龄段' if i != highlight_index else '18-24岁(最高)' for i in range(len(age_groups))]
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(age_groups))]
ax.legend(handles[0:2], legend_labels[0:2], loc='upper right')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()