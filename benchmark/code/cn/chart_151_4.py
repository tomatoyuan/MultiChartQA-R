import numpy as np
import matplotlib.pyplot as plt

# 数据
periods = ['MAT2206', 'MAT2306', 'MAT2406']
sales = [100, 110, 115]
avg_price = [150, 145, 155]

x = np.arange(len(periods))

fig, ax1 = plt.subplots(figsize=(8, 5))

# 柱状图：销售额
bars = ax1.bar(x, sales, width=0.4, color='lightgray', label='销售额')
ax1.set_ylabel('销售额（百万元）', fontsize=11)
ax1.set_ylim(0, 160)

# 在柱子顶部添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 3, f'{sales[i]}',
             ha='center', va='bottom', fontsize=9)

# 折线图：均价
ax2 = ax1.twinx()
line, = ax2.plot(x, avg_price, color='blue', marker='o', linewidth=2, label='均价')
ax2.set_ylabel('均价（元）', fontsize=11)
ax2.set_ylim(60, 160)

# 在折线上标注数值
for i, price in enumerate(avg_price):
    ax2.text(x[i], price + 3, f'{price}', ha='center', va='bottom', fontsize=9, color='blue')

# 标注箭头（趋势）
ax2.annotate('', xy=(2, avg_price[2]), xytext=(1, avg_price[1]),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))

# 设置X轴
ax1.set_xticks(x)
ax1.set_xticklabels(periods, fontsize=11)

# 标题
plt.title("整体线上 | 益生菌销售额（百万元）及均价（元）", fontsize=13)

# 合并图例
lines = [bars, line]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()