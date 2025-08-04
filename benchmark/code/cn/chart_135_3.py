import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [401, 500, 600, 773, 977, 1207, 1461, 1750, 2046]
growth_rate = [np.nan, 24.7, 20.0, 28.8, 26.4, 23.5, 21.0, 15.2, 13.0]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比变化率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='coral', label='同比变化率（%）', linewidth=2)
ax2.set_ylabel('同比变化率（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 20, f'{size}', ha='center', va='bottom')

# 添加同比变化率数值标注（跳过2017年，因无同比数据）
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2017-2025年中国医美非手术类市场规模及预测')

plt.tight_layout()
plt.show()