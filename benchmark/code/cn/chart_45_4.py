import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['基础性防晒', '功能时尚防晒服饰', '奢品防晒/防晒套装服饰']
price_ranges = [
    ['100元以内', '100 - 150元'],
    ['150 - 200元', '200 - 250元'],
    ['250 - 300元', '300 - 500元', '500元以上']
]
percentages = [
    [3, 15],
    [29, 24],
    [16, 10, 3]
]

# 确保所有价格区间都有图例
all_price_ranges = ['100元以内', '100 - 150元', '150 - 200元', '200 - 250元', '250 - 300元', '300 - 500元', '500元以上']

# 设置图形参数
bar_width = 0.6
y_positions = np.arange(len(categories))

# 创建图形和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 定义颜色列表，确保每个价格区间颜色一致
colors = plt.cm.tab20.colors

# 绘制柱状图
bottoms = [0] * len(categories)
for i, (ranges, percs) in enumerate(zip(price_ranges, percentages)):
    for j, (price_range, percent) in enumerate(zip(ranges, percs)):
        color_idx = all_price_ranges.index(price_range)
        label = price_range  # 为每个价格区间设置标签
        ax.barh(y_positions[i], percent, bar_width, left=bottoms[i], 
                label=label, alpha=0.8, color=colors[color_idx])
        bottoms[i] += percent

# 添加数据标签
for i, (ranges, percs) in enumerate(zip(price_ranges, percentages)):
    current_bottom = 0
    for j, (price_range, percent) in enumerate(zip(ranges, percs)):
        if percent > 0:  # 只在百分比大于0时添加标签
            ax.text(current_bottom + percent/2, i, f"{percent}%", 
                    ha='center', va='center', color='black', fontweight='bold')
        current_bottom += percent

# 设置图表属性
ax.set_yticks(y_positions)
ax.set_yticklabels(categories)
ax.set_xlabel('百分比 (%)')
ax.set_title('消费者购买防晒服饰及用品倾向价格区间')

# 调整图例
handles, labels = ax.get_legend_handles_labels()
# 创建唯一的图例项
unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
ax.legend(*zip(*unique), loc='lower right')

# 显示网格线
ax.grid(axis='x', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()