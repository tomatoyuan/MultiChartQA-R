import matplotlib.pyplot as plt
import numpy as np

# 左侧销量数据
years_sales = ["2019", "2020", "2021", "2022", "2023"]
sales = [96.0, 85.0, 102.0, 103.0, 107.0]

# 右侧客流量数据
years_flow = ["2020", "2021", "2022", "2023"]
flow = [650.0, 670.0, 600.0, 750.0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 绘制左侧销量柱状图
x_sales = np.arange(len(years_sales))
bars = ax1.bar(x_sales, sales, color='orange', label='销量（百万件）')
ax1.set_ylabel('销量（百万件）')
ax1.set_xlabel('年份')
ax1.set_xticks(x_sales)
ax1.set_xticklabels(years_sales)
ax1.legend(loc='upper left')
# 添加销量数值标注
for i, sale in enumerate(sales):
    ax1.text(i, sale + 1, f'{sale}', ha='center', va='bottom')

# 绘制右侧客流量面积图
x_flow = np.arange(len(years_flow))
ax2.fill_between(x_flow, flow, color='gold', label='客流量（百万人次）')
ax2.set_ylabel('客流量（百万人次）')
ax2.set_xlabel('年份')
ax2.set_xticks(x_flow)
ax2.set_xticklabels(years_flow)
ax2.legend(loc='upper left')
# 添加客流量数值标注
for i, f in enumerate(flow):
    ax2.text(i, f + 10, f'{f}', ha='center', va='bottom')

ax1.set_title('2019-2023年潘朵拉销量')
ax2.set_title('2020-2023年潘朵拉客流量')

plt.tight_layout()
plt.show()