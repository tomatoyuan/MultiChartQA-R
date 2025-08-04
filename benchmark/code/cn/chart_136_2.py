import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
store_count = [895.0, 1100.0, 1410.0, 1802.0, 2138.0, 2446.0, 2705.0, 2770.0, 2690.0, 2619.0, 2651.0, 2651.0]
growth_rate = [np.nan, 22.9, 28.2, 27.8, 18.6, 14.4, 10.8, 2.4, -2.9, -2.6, 1.2, 0.0]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制概念店数量柱状图
ax1.bar(x, store_count, color='orange', label='概念店数量')
ax1.set_ylabel('概念店数量')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='coral', label='增长率（%）', linewidth=2)
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加概念店数量数值标注
for i, count in enumerate(store_count):
    ax1.text(i, count + 30, f'{count}', ha='center', va='bottom')

# 添加增长率数值标注（跳过2012年，因无同比数据）
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2012-2023年潘朵拉概念店数量及增长率')

plt.tight_layout()
plt.show()