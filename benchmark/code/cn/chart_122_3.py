import matplotlib.pyplot as plt
import numpy as np

# 年份及日期
years = ["2020/3/31", "2021/3/31", "2022/3/31", "2023/3/31", "2024/3/31"]
# 营业总收入（亿元）
operating_revenue = [518.5, 593, 802.4, 828.9, 985.5]
# 归母净利润（亿元）
net_profit = [26.51, 50.93, 54.44, 47.14, 58.92]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制营业总收入柱状图
ax.bar(x, operating_revenue, color='orange', label='营业总收入（亿元）', width=0.6)
# 绘制归母净利润柱状图
ax.bar(x, net_profit, color='red', label='归母净利润（亿元）', width=0.2)

# 添加营业总收入数值标注
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# 添加归母净利润数值标注
for i, profit in enumerate(net_profit):
    ax.text(i, profit + 2, f'{profit}', ha='center', va='bottom')

ax.set_ylabel('金额（亿元）')
ax.set_xlabel('日期')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2020-2024年报告期内周大福营业收入和归母净利润')

plt.tight_layout()
plt.show()