import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np


# 数据
years = ["2020年", "2021年", "2022年", "2023年", "2024年E"]
market_total = [3557, 3986, 4306, 4990, 5680]
market_b = [2774, 3109, 3359, 3980, 4630]
growth_total = [None, 12.1, 8.0, 15.9, 13.8]
growth_b = [None, 12.1, 8.0, 18.5, 16.3]

x = np.arange(len(years))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图
bars1 = ax1.bar(x - width/2, market_total, width, label='市场规模（亿元）', color='red')
bars2 = ax1.bar(x + width/2, market_b, width, label='B端市场规模（亿元）', color='blue')

# 添加柱状图标签
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 50, f'{int(height)}', ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 50, f'{int(height)}', ha='center', va='bottom', fontsize=9)

ax1.set_ylabel('市场规模（亿元）')
ax1.set_xticks(x)
ax1.set_xticklabels(years)

# 副轴：同比变化（%）
ax2 = ax1.twinx()
ax2.set_ylabel('同比变化（%）')
ax2.set_ylim(0, 20)  # 从0%开始
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# 只从2021年起画折线
x_growth = x[1:]  # 对应2021到2024年
growth_total_clean = [v for v in growth_total if v is not None]
growth_b_clean = [v for v in growth_b if v is not None]

line1 = ax2.plot(x_growth, growth_total_clean, color='orange', marker='o', label='同比变化（%）', linewidth=2)
line2 = ax2.plot(x_growth, growth_b_clean, color='gray', marker='o', label='B端同比变化（%）', linewidth=2)

# 标注折线上数值
for i, val in enumerate(growth_total_clean):
    ax2.text(x_growth[i], val + 0.6, f'{val}%', color='orange', ha='center', fontsize=9)
for i, val in enumerate(growth_b_clean):
    ax2.text(x_growth[i], val + 0.6, f'{val}%', color='gray', ha='center', fontsize=9)

# 图例
# lines_labels = [*bars1, *bars2, line1[0], line2[0]]
# labels = ['市场规模（亿元）', 'B端市场规模（亿元）', '同比变化（%）', 'B端同比变化（%）']
# ax1.legend(lines_labels[:], labels[:], loc='upper left')

# 图例
lines_labels = ax1.get_legend_handles_labels()
lines_labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines_labels[0] + lines_labels2[0], lines_labels[1] + lines_labels2[1], loc='upper left')


plt.title('2020—2024年全国预制菜市场规模及其同比变化')
plt.tight_layout()
plt.show()