import matplotlib.pyplot as plt
import numpy as np

# 数据准备
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E"]
market_size = [292.1, 282.4, 324.3, 350.2, 366.3, 387.9, 411.2, 440, 475.2, 546.5, 628.5, 710.2, 799.6]  # 市场规模（亿元）
growth_rates = [-3.3, 14.8, 8.0, 4.6, 5.9, 6.0, 7.0, 8.0, 15.0, 15.0, 13.0, 12.6]  # 同比增长率（%），注意2012年无增长率，从2013开始

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='coral', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长率折线图
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rates, marker='o', color='gold', label='同比增长率（%）', linewidth=2)  # 2012年无增长率，从2013开始画
ax2.set_ylabel('同比增长率（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 10, f'{size}', ha='center', va='bottom', color='black')

# 添加同比增长率数值标注（从2013年开始）
for i, rate in enumerate(growth_rates, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom', color='black')

ax1.set_title('2012-2024年中国健身器材市场规模及预测')
plt.tight_layout()
plt.show()