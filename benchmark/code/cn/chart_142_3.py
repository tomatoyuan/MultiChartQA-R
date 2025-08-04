import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [240.0, 360.0, 1116.0, 2845.8, 5197.4, 8287.0]
growth_rate = [np.nan, 50.0, 210.0, 155.0, 82.6, 59.4]  # 2020年无同比数据，用np.nan标记

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长折线图
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rate[1:], marker='o', color='gold', label='同比增长（%）', linewidth=2)  # 2020年无同比数据，从2021开始
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 100, f'{size}', ha='center', va='bottom')

# 添加同比增长数值标注（2020年无，从2021开始）
for i, rate in enumerate(growth_rate[1:], start=1):
    ax2.text(i, rate + 5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2020-2025年中国跨境直播电商市场规模及预测')

plt.tight_layout()
plt.show()