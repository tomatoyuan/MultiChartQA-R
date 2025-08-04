import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E", "2026E", "2027E"]
market_size = [2776, 3498, 4400, 5762, 6975, 8782, 10149, 10890, 11641, 12270, 12847, 13386, 13855]
growth_rate = [26.0, 25.8, 31.0, 21.1, 25.9, 15.6, 7.3, 6.9, 5.4, 4.7, 4.2, 3.5, 2.9]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增长率（%）')
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 100, f'{size}', ha='center', va='bottom')

# 添加增长率数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2015-2027年中国家政服务市场规模和增长率及预测')

plt.tight_layout()
plt.show()