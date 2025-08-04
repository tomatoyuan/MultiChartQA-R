import matplotlib.pyplot as plt
import numpy as np

labels = ['2022.7-2023.6', '2023.7-2024.6']
order_growth = [13.21, 20.16]
food_growth = [15.16, 18.28]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 4.5))

# 柱状图
bar1 = ax.bar(x - width/2, order_growth, width, label='Growth rate of takeaway orders', color='#8BC34A')
bar2 = ax.bar(x + width/2, food_growth, width, label='Growth rate of food items', color='#388E3C')

# 数值标注
for bar in bar1:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

for bar in bar2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# 设置图表元素
ax.set_ylabel('Growth rate (%)', fontsize=12)
ax.set_title('Growth rate of takeaway (Meituan) orders and food items', fontsize=13, weight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)

ax.set_ylim(0, 22.5)

c

# 紧凑布局 + 留白给标题和图例
plt.tight_layout()
plt.subplots_adjust(top=0.88, bottom=0.2)  # 增加顶部和底部空间
plt.show()