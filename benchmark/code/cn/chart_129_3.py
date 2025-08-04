import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
total_volume = [133.8, 150.3, 167.9, 171.1, 181.7, 191.1, 202.6, 220.2, 230.2, 239.8, 240.4]
growth_rate = [np.nan, 12.3, 11.8, 1.9, 6.2, 5.1, 6.0, 8.7, 4.5, 4.2, 0.3]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制内销总量柱状图
bars = ax1.bar(x, total_volume, color='orange', label='内销总量（万吨）')
ax1.set_ylabel('内销总量（万吨）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 添加内销总量数值标注
for i, vol in enumerate(total_volume):
    ax1.text(i, vol + 2, f'{vol}', ha='center', va='bottom')

# 创建双轴，绘制增幅折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增幅（%）', linewidth=2)
ax2.set_ylabel('增幅（%）')
ax2.legend(loc='upper right')

# 添加增幅数值标注（跳过 2013 年，因无增幅）
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.3, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2013-2023年中国茶叶内销总量及增幅')

plt.tight_layout()
plt.show()