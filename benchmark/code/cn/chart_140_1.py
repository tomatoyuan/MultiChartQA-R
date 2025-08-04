import matplotlib.pyplot as plt
import numpy as np

# 购买情况数据
purchase_labels = ["购买过", "未购买，计划购买", "未购买，不计划购买", "还在观望中"]
purchase_sizes = [51.8, 11.8, 2.9, 33.5]
purchase_colors = ["#4169E1", "#00CED1", "#FF6347", "#9370DB"]

# 选购价位数据
price_labels = ["10万以下", "10-20万", "21-40万", "41-60万", "61-80万", "80万以上"]
price_sizes = [8.7, 38.7, 37.1, 8.9, 3.9, 2.7]
price_colors = ["#90EE90", "#1E90FF", "#FFD700", "#32CD32", "#4B0082", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制购买情况分类图（用饼图模拟分类展示，因是单一占比数据）
wedges, texts, autotexts = ax1.pie(purchase_sizes, colors=purchase_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('购买情况')
ax1.legend(wedges, purchase_labels, title="购买状态", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# 绘制选购价位饼图
wedges2, texts2, autotexts2 = ax2.pie(price_sizes, colors=price_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('选购价位')
ax2.legend(wedges2, price_labels, title="价位区间", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('2023年中国新能源汽车购买情况及选购价位调查', fontsize=14)
plt.tight_layout()
plt.show()