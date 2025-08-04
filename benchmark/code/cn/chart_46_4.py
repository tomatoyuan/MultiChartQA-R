import matplotlib.pyplot as plt
import numpy as np

# 数据整理
categories = ['基础功能', '进阶功能', '多维体验']
sub_categories = {
    '基础功能': ['坐感舒适性', '品质安全性', '产品耐用性', '功能支撑性'],
    '进阶功能': ['操作易用性', '可调节性', '绿色环保性'],
    '多维体验': ['智能交互性', '情绪价值及疗愈功能', '设计美观性', '个性化']
}
values = {
    '基础功能': [62, 56, 47, 43],
    '进阶功能': [38, 33, 28],
    '多维体验': [25, 23, 22, 17]
}

# 用于设置每组条形的位置
x_positions = {}
bar_width = 0.25
spacing = 0.5  # 不同主类别之间的间距

# 动态计算每个主类别的x位置
current_x = 0
for cat in categories:
    n_sub = len(sub_categories[cat])
    x_positions[cat] = np.arange(current_x, current_x + n_sub)
    current_x += n_sub + spacing

# 创建图形
fig, ax = plt.subplots(figsize=(14, 8))  # 增加图形高度以容纳标签

# 绘制每组条形并添加百分比标签
for i, cat in enumerate(categories):
    bars = ax.bar(x_positions[cat], values[cat], width=bar_width, label=cat)
    
    # 为每个条形添加百分比标签
    for bar, value in zip(bars, values[cat]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8, 
                f'{value}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # 为每个主类别添加子类别标签（微调位置）
    for j, pos in enumerate(x_positions[cat]):
        ax.text(pos, -3.5, sub_categories[cat][j], ha='center', rotation=45, fontsize=9)

# 设置x轴刻度（这里我们只需要标记每个主类别的起始位置）
ax.set_xticks([x_positions[cat][0] for cat in categories])
ax.set_xticklabels(categories)

# 添加标题、图例和标签
ax.set_title('消费者对座椅消费的需求', fontsize=14)
ax.set_xlabel('需求类型', fontsize=12)
ax.set_ylabel('占比（%）', fontsize=12)
ax.legend()

# 设置y轴范围，使负值标签和数值标签可见
ax.set_ylim(bottom=-5, top=75)  # 调整y轴上限以确保标签不超出

# 添加网格线，便于读取数值
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()