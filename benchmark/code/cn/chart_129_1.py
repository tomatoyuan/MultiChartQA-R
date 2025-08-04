import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E", "2026E", "2027E", "2028E"]
market_size = [1946.6, 2157.4, 2396.0, 2626.6, 2910.3, 3210.0, 3511.8, 3838.4, 4164.6, 4527.0, 4902.7, 5309.6]
growth_rate = [10.8, 11.1, 10.0, 9.6, 10.8, 10.3, 9.4, 9.3, 8.5, 8.7, 8.3, 8.1]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增长率（%）')
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# 添加增长率数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2017-2028年中国茶叶行业市场规模及预测')

plt.tight_layout()
plt.show()