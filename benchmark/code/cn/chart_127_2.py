import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
net_profit = [791.30, 646.83, 432.49, 417.85, 486.40, 567.37, 659.31]
growth_rate = [-0.4, -18.3, -33.1, -3.4, 16.4, 16.6, 16.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制归母净利润柱状图
bars = ax1.bar(x, net_profit, color='orange', label='归母净利润（亿元）', width=0.4)
ax1.set_ylabel('归母净利润（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 添加归母净利润数值标注
for i, profit in enumerate(net_profit):
    ax1.text(i, profit + 10, f'{profit}', ha='center', va='bottom')

# 创建双轴，绘制同比增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='同比增长率（%）', linewidth=2)
ax2.set_ylabel('同比增长率（%）')
ax2.legend(loc='upper right')

# 添加同比增长率数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom', color='red')

ax1.set_title('2017-2023年中国A股新能源汽车整车制造上市公司归母净利润')

plt.tight_layout()
plt.show()