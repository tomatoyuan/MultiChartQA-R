import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E"]
market_size = [216.3, 234.6, 240.9, 250.3, 259.3, 230.5, 235.3, 253.4, 270.9, 304.3, 335.0, 364.1, 387.8]
growth_rate = [8.5, 2.7, 3.9, 3.6, -11.1, 2.1, 7.7, 6.9, 12.3, 10.1, 8.7, 6.5]

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
ax2.plot(x[1:], growth_rate, marker='o', color='brown', label='同比增长（%）', linewidth=2)  # 2012年无同比数据，从2013开始
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 5, f'{size}', ha='center', va='bottom')

# 添加同比增长数值标注（2012年无，从2013开始）
for i, rate in enumerate(growth_rate, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2012-2024年中国仓储会员超市行业市场规模及预测')

plt.tight_layout()
plt.show()