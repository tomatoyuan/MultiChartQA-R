import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2020", "2021", "2022", "2023", "2024", "2025E", "2026E", "2027E", "2028E", "2029E"]
# 市场规模（亿元）
market_size = [350.7, 425.2, 445.2, 594.9, 713.9, 833.1, 1083.0, 1245.5, 1413.6, 1563.5, 1763.6, 1925.8]
# 增长率（%）
growth_rate = [21.2, 6.8, -8.7, 33.6, 20.0, 16.7, 30.0, 15.0, 13.5, 10.6, 12.8, 9.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

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
    ax1.text(i, size + 20, f'{size}', ha='center', va='bottom')

# 添加增长率数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

plt.title('2016-2029年中国冰雪运动核心市场规模及预测')
plt.tight_layout()
plt.show()