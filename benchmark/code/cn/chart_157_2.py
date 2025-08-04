import matplotlib.pyplot as plt
import numpy as np

# 数据
years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_size = [1195, 1261, 1258, 1202, 1337, 1472, 1570]
growth_rate = [None, 5.52, -0.24, -4.45, 11.23, 10.10, 6.66]

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图
bar = ax1.bar(years, market_size, color='#38C6D9', width=0.6, label='市场规模')
ax1.set_ylabel('市场规模（亿元）', fontsize=12)
ax1.set_ylim(0, 2000)

# 标注值
for i, val in enumerate(market_size):
    ax1.text(years[i], val + 30, str(val), ha='center', fontsize=10)

# 折线图
ax2 = ax1.twinx()
ax2.plot(years[1:], growth_rate[1:], color='darkred', linestyle='--', marker='o', linewidth=2, label='增速')
for i, val in enumerate(growth_rate[1:], 1):
    ax2.text(years[i], growth_rate[i] + 0.8, f'{val:.2f}%', color='darkred', fontsize=10, ha='center')

ax2.set_ylabel('增长率', fontsize=12)
ax2.set_ylim(-10, 15)

# 标题与图例
plt.title('2017–2023 中国替代蛋白市场规模变化情况', fontsize=16, weight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()