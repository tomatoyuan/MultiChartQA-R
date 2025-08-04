import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", 
         "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# 成交总额（亿元）
transaction_volume = [0.5, 9.4, 52.0, 191.0, 350.0, 805.0, 1230.0, 1770.0, 
                      2954.3, 3953.2, 6000.0, 8600.0, 9651.2, 11154.0, 11386.0, 14418.0]
# 增长率（%）
growth_rate = [np.nan, 1770.0, 455.6, 267.3, 83.2, 130.0, 52.8, 43.9, 
               66.9, 33.8, 51.8, 43.3, 12.2, 15.6, 2.1, 26.6]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制成交总额柱状图
ax1.bar(x, transaction_volume, color='orange', label='成交总额（亿元）')
ax1.set_ylabel('成交总额（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增长率（%）')
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加成交总额数值标注
for i, vol in enumerate(transaction_volume):
    ax1.text(i, vol + 200, f'{vol}', ha='center', va='bottom')

# 添加增长率数值标注（注意：2009 年无增长率，从 2010 年开始）
for i, rate in enumerate(growth_rate):
    if i > 0:  # 跳过 2009 年
        ax2.text(x[i], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2009-2024年中国电商平台“双十一”成交总额')

plt.tight_layout()
plt.show()