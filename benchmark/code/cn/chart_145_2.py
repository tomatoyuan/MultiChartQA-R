import matplotlib.pyplot as plt
import numpy as np

# --------------------- 购买频率饼图数据 ---------------------
frequency_labels = ["一月一次", "2-3个月一次", "一周一次", "一周2-3次及以上", "半年一次", "几乎不买"]
frequency_sizes = [31.0, 23.7, 16.2, 6.2, 9.6, 2.7]  # 按图例顺序整理数据
frequency_colors = ["#32CD32", "#8B4513", "#FFD700", "#FF7F50", "#D2B48C", "#8F9779"]

# --------------------- 可接受单价柱状图数据 ---------------------
price_labels = ["10元及以下", "11-30元", "31-50元", "51-100元", "101-150元", "151-200元", "200元以上"]
price_percents = [2.1, 10.2, 25.5, 32.3, 15.7, 8.3, 5.9]

# 创建画布，一行两列布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- 绘制购买频率饼图（左图） ---------------------
wedges, texts, autotexts = ax1.pie(frequency_sizes, colors=frequency_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023年中国消费者购买文创产品的频率')
# 调整图例（按原图顺序匹配）
ax1.legend(wedges, frequency_labels, title="购买频率", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制可接受单价柱状图（右图） ---------------------
x = np.arange(len(price_labels))
bars = ax2.bar(x, price_percents, color='orange')
ax2.set_title('2023年中国文创产品消费者可接受产品单价')
ax2.set_ylabel('占比（%）')
ax2.set_xticks(x)
ax2.set_xticklabels(price_labels, rotation=45, ha='right')
# 添加数值标注
for i, percent in enumerate(price_percents):
    ax2.text(i, percent + 1, f'{percent}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()