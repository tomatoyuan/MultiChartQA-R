import matplotlib.pyplot as plt
import numpy as np

# --------------------- 左侧饼图数据 ---------------------
labels_pie = ["501-1000元", "1001-3000元", "500元及以下", "3001元及以上"]
sizes_pie = [49.5, 41.4, 6.5, 2.6]
colors_pie = ["#D2691E", "#F4A460", "#CD853F", "#FFDEAD"]

# --------------------- 右侧分组柱状图数据 ---------------------
labels_bar = ["一周3次及以上", "每周1-2次", "每月1-2次", "数月1次", "几乎不在大学城内消费"]
sizes_bar = [
    [13.5, 86.5],  # 第一组：下方橙色、上方浅色
    [51.8, 48.2], 
    [29.5, 70.5], 
    [3.6, 96.4], 
    [1.6, 98.4]
]
colors_bar = ["#D2691E", "#FAF0E6"]  # 橙色、浅米色

# 创建画布，一行两列布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- 绘制左侧饼图 ---------------------
wedges, texts, autotexts = ax1.pie(sizes_pie, colors=colors_pie, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023年以来中国大学城主要消费群体月均消费')
# 调整图例
ax1.legend(wedges, labels_pie, title="消费区间", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制右侧分组柱状图 ---------------------
# 分组柱状图绘制（堆叠形式）
x = np.arange(len(labels_bar))
bottom = np.zeros(len(labels_bar))
for i in range(2):
    ax2.bar(x, [size[i] for size in sizes_bar], bottom=bottom, color=colors_bar[i], label=labels_pie[i] if i==0 else '')
    bottom += [size[i] for size in sizes_bar]

ax2.set_title('2023年中国大学城主要消费群体的消费频率')
ax2.set_ylabel('占比（%）')
ax2.set_xticks(x)
ax2.set_xticklabels(labels_bar)
ax2.legend(title="消费区间", loc="upper left")

# 添加分组柱状图数值标注
for i, (size1, size2) in enumerate(sizes_bar):
    ax2.text(i, size1/2, f'{size1}%', ha='center', va='center', color='white')
    ax2.text(i, size1 + size2/2, f'{size2}%', ha='center', va='center', color='black')

# 模拟黄色虚线框（第二组）
ax2.plot([x[1]-0.3, x[1]+0.3, x[1]+0.3, x[1]-0.3, x[1]-0.3], 
         [0, 0, 100, 100, 0], 
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('中国大学城主要消费群体的行为分析：消费区间与频率', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()