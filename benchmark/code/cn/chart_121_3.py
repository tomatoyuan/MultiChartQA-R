import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2018", "2019", "2020", "2021", "2022", "2023"]
# 营业收入（亿元）
operating_revenue = [99.25, 170.41, 237.49, 359.83, 336.42, 336.44]
# 净利润（亿元）
net_profit = [28.87, 52.28, 72.44, 104.30, 77.61, 78.79]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 6))

# 绘制营业收入柱状图
bars_rev = ax.bar(x, operating_revenue, color='brown', label='营业收入（亿元）', width=0.4)
# 绘制净利润柱状图（右移避免重叠）
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='净利润（亿元）', width=0.4)

# 添加营业收入数值标注
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# 添加净利润数值标注
for i, profit in enumerate(net_profit):
    ax.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('金额（亿元）')
ax.set_xlabel('年份')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='upper left')

# 添加右侧信息框（模拟原图样式）
info_box_text = (
    "2022年中国银河证券APP\n"
    "财富管理业务新开户 110.84万户，\n"
    "开户市占率达7.48%"
)
# 在图表右侧绘制信息框
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="orange", lw=2)
ax.text(5.8, 300, info_box_text, fontsize=10, bbox=bbox_props, va='top')

ax.set_title('2018-2023年中国银河证券的营业收入和净利润')
plt.tight_layout()
plt.show()