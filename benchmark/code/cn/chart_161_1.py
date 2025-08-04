import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据
categories = {
    '护肤': {
        'labels': ['面部护理', '护肤套装', '面膜', '洁面', '爽肤水', '眼部护理', '防晒', '护肤-其他', '唇部护理'],
        'values': [38, 23, 12, 9, 5, 5, 5, 1, 1],
        'color': 'Reds'
    },
    '彩妆': {
        'labels': ['面部彩妆', '唇部彩妆', '眼部彩妆', '彩妆工具', '彩妆套装', '美甲'],
        'values': [47, 24, 12, 10, 6, 1],
        'color': 'Blues'
    },
    '香水': {
        'labels': ['香水'],
        'values': [100],
        'color': 'Greens'
    }
}

# 初始化图形
fig, ax = plt.subplots(figsize=(10, 8))
y_base = 0
bar_height = 0.6
group_gap = 1.2
label_padding = 0.5

# 绘图主循环
for group_index, (group, content) in enumerate(categories.items()):
    labels = content['labels']
    values = content['values']
    cmap = plt.get_cmap(content['color'])
    num_items = len(values)

    # 色阶
    colors = [cmap(0.3 + 0.6 * i / max(len(values)-1, 1)) for i in range(len(values))]

    # 背景区块
    ax.add_patch(
        patches.Rectangle(
            (-10, y_base - bar_height/2 - 0.3),
            110, num_items * (bar_height + 0.2),
            color=cmap(0.05), zorder=0
        )
    )

    # 左侧组名标签
    ax.text(-12, y_base + (num_items - 1) * (bar_height + 0.2)/2,
            f'{group}', va='center', ha='center',
            fontsize=13, weight='bold', bbox=dict(facecolor=cmap(0.2), boxstyle='round,pad=0.4', edgecolor='none'))

    for i, (label, value) in enumerate(zip(labels, values)):
        y = y_base + i * (bar_height + 0.2)
        ax.barh(y, value, height=bar_height, color=colors[i], edgecolor='black')
        ax.text(value + 1, y, f'{value}%', va='center', ha='left', fontsize=10)
        ax.text(-0.5, y, label, va='center', ha='right', fontsize=10)

    y_base += num_items * (bar_height + 0.2) + group_gap

# 格式设置
ax.set_xlim(-10, 110)
ax.set_ylim(-1, y_base)
ax.set_xticks(range(0, 101, 20))
ax.set_xticklabels([f'{x}%' for x in range(0, 101, 20)])
ax.set_yticks([])
ax.set_xlabel('百分比（%）', labelpad=15)
ax.set_title('2024年Q1电商市场细分类目规模分布（二级）', fontsize=14, weight='bold')
ax.invert_yaxis()
plt.tight_layout()
plt.show()