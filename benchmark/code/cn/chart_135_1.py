import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [1606, 1693, 1867, 1950, 2133, 2029, 2308, 2565, 2804, 3014, 3186]
growth_rate = [np.nan, 5.4, 10.3, 4.4, 9.4, -4.9, 13.8, 11.1, 9.3, 7.5, 5.7]

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
ax2.plot(x, growth_rate, marker='o', color='gold', label='同比增长（%）', linewidth=2)
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 30, f'{size}', ha='center', va='bottom')

# 添加同比增长数值标注（跳过2015年，因无同比数据）
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2015-2025年中国护肤品行业市场规模及预测')

plt.tight_layout()
plt.show()