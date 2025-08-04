import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2019", "2020", "2021", "2022", "2023", "2024.9"]
# 营业收入（亿美元）
operating_revenue = [2.41, 8.98, 17.79, 12.38, 17.14, 17.88]
# 净利润（亿美元）
net_profit = [-1.07, 0.07, -36.86, -10.28, -5.41, 4.95]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制营业收入柱状图（橙色）
bars_rev = ax.bar(x, operating_revenue, color='orange', label='营业收入（亿美元）', width=0.4)
# 绘制净利润柱状图（黄色）
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='净利润（亿美元）', width=0.4)

# 添加营业收入数值标注
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 0.5, f'{rev}', ha='center', va='bottom')

# 添加净利润数值标注，根据正负调整位置，保证显示在合理区域
for i, profit in enumerate(net_profit):
    if profit < 0:
        ax.text(i + 0.4, profit - 1, f'{profit}', ha='center', va='top')
    else:
        ax.text(i + 0.4, profit + 0.5, f'{profit}', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('金额（亿美元）')
ax.set_xlabel('年份')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='upper left')

ax.set_title('2019-2024年9月Robinhood营业收入和净利润')
plt.tight_layout()
plt.show()