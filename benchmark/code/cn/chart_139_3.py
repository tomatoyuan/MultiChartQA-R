import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [1181, 1543, 1905, 2264, 2556, 2961, 3492, 3834, 4237, 4631, 5033]
growth_rate = [30.7, 23.5, 18.8, 12.9, 15.8, 17.9, 9.8, 10.5, 9.3, 8.7]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长折线图
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rate, marker='o', color='brown', label='同比增长（%）', linewidth=2)  # 2015年无同比数据，从2016开始
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# 添加同比增长数值标注（2015年无，从2016开始）
for i, rate in enumerate(growth_rate, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2015-2025年中国便利店行业市场规模及预测')

plt.tight_layout()
plt.show()