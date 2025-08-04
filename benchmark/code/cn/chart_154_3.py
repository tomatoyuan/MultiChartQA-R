import matplotlib.pyplot as plt
import numpy as np

# 图表3：外卖订单数与商品数增长率
labels = ['2022.7-2023.6', '2023.7-2024.6']
order_growth = [13.21, 20.16]     # 外卖订单数增长率
food_growth = [15.16, 18.28]      # 餐饮商品数增长率

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 4.5))

# 柱状图
bar1 = ax.bar(x - width/2, order_growth, width, label='外卖订单数增长率', color='#8BC34A')
bar2 = ax.bar(x + width/2, food_growth, width, label='餐饮商品数增长率', color='#388E3C')

# 数值注释
for bar in bar1:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

for bar in bar2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# 设置图表
ax.set_ylabel('增长率（%）', fontsize=12)
ax.set_title('外卖（美团）订单数量及餐饮商品数量增长率', fontsize=13, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.legend(loc='upper left', fontsize=10)

# 数据来源标注

plt.tight_layout()
plt.show()