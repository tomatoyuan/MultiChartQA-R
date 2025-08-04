import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024.9"]
# 营业收入（亿元）
operating_revenue = [227.19, 299.49, 352.00, 428.17, 354.71, 361.41, 290.00]
# 净利润（亿元）
net_profit = [67.08, 86.37, 111.22, 150.13, 115.07, 121.77, 95.23]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制营业收入柱状图
ax1.bar(x, operating_revenue, color='brown', label='营业收入（亿元）', width=0.4)
ax1.set_ylabel('营业收入（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制净利润柱状图
ax2 = ax1.twinx()
ax2.bar(x + 0.4, net_profit, color='gold', label='净利润（亿元）', width=0.4)
ax2.set_ylabel('净利润（亿元）')
ax2.legend(loc='upper right')

# 添加营业收入数值标注
for i, rev in enumerate(operating_revenue):
    ax1.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# 添加净利润数值标注
for i, profit in enumerate(net_profit):
    ax2.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

ax1.set_title('2018-2024年9月国泰君安的营业收入和净利润')
plt.tight_layout()
plt.show()