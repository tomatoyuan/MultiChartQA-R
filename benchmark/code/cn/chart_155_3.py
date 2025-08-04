import matplotlib.pyplot as plt
import numpy as np

# 图表3：2018-2023年医药电商行业市场规模表现

years = ['2018年', '2019年', '2020年', '2021年', '2022年', '2023年']
sales = [700, 950, 1500, 1850, 2500, 2900]  # 单位：亿元
growth_rate = [55, 45, 35, 30, 29, 15]      # 单位：%

fig, ax1 = plt.subplots(figsize=(10, 6))

# 主轴 - 柱状图（销售规模）
bars = ax1.bar(years, sales, color='#fdbf6f', label='销售规模（亿元）', width=0.6)
ax1.set_ylabel('销售规模（亿元）', fontsize=12)
ax1.set_ylim(0, 3200)

# 添加柱状图数值标签
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 80, f'{int(height)}', ha='center', va='bottom', fontsize=10)

# 副轴 - 折线图（同比增速）
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='brown', marker='o', linewidth=2.5, label='同比增速')
ax2.set_ylabel('同比增速（%）', fontsize=12)
ax2.set_ylim(0, 65)

# 添加折线图数据标签
for x, y in zip(years, growth_rate):
    ax2.text(x, y + 2, f'{y:.1f}%', ha='center', fontsize=10)

# 标题和图例
plt.title('2018-2023年医药电商行业市场规模表现', fontsize=14, weight='bold')
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.show()