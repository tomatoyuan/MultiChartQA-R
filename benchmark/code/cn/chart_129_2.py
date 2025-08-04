import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
production = [68.33, 70.17, 74.51, 76.75, 83.52, 91.82, 100.92, 117.05, 127.59, 137.16, 148.54, 160.76, 176.39, 188.71, 204.94, 228.01, 231.72, 246.04, 259.01, 274.26, 293.18, 312.32, 334.21, 355.00]
growth_rate = [np.nan, 2.7, 6.2, 3.0, 8.7, 11.9, 10.0, 13.9, 7.2, 7.6, 8.3, 9.9, 9.6, 7.1, 8.6, 11.1, 1.6, 6.4, 6.1, 6.4, 5.6, 7.9, 5.6, 6.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(16, 9))

# 绘制产量柱状图
ax1.bar(x, production, color='orange', label='产量（万吨）')
ax1.set_ylabel('产量（万吨）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增长率（%）')
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加产量数值标注
for i, prod in enumerate(production):
    ax1.text(i, prod + 5, f'{prod}', ha='center', va='bottom')

# 添加增长率数值标注（跳过 2000 年，因无增长率）
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2000-2023年中国茶叶产量及增长率')

plt.tight_layout()
plt.show()