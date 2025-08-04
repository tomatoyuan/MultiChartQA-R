import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2020年', '2021年', '2022年', '2023年']
total_retail = [390000, 440000, 440000, 470000]  # 社会消费品零售总额（亿元）
online_retail = [110000, 120000, 120000, 130000]  # 实物商品网上零售额（亿元）
total_growth = [-0.04, 0.12, 0.00, 0.07]  # 同比增长率
online_growth = [0.14, 0.11, 0.11, 0.08]

x = np.arange(len(years))
width = 0.35

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# 柱状图
bar1 = ax1.bar(x - width/2, total_retail, width, label='社会消费品零售总额（亿元）', color='#e55322')
bar2 = ax1.bar(x + width/2, online_retail, width, label='实物商品网上零售额（亿元）', color='lightgray')

# 条形图数据标注
for i, rect in enumerate(bar1):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1000, f'{height}', ha='center', va='bottom', fontsize=9)

for i, rect in enumerate(bar2):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1000, f'{height}', ha='center', va='bottom', fontsize=9)

# 折线图
line1 = ax2.plot(x, total_growth, label='社会消费品零售总额同比增速', color='black', marker='o', linewidth=2)
line2 = ax2.plot(x, online_growth, label='实物商品网上零售额同比增速', color='#7f3f1d', marker='o', linewidth=2)

# 增长率标注
for i, v in enumerate(total_growth):
    ax2.text(x[i] + 0.1, v, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

for i, v in enumerate(online_growth):
    ax2.text(x[i] - 0.1, v - 0.01, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

# 坐标轴与图例
ax1.set_ylabel('金额（亿元）', fontsize=12)
ax2.set_ylabel('同比增速', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
plt.title('社会消费品零售总额当期值&实物商品网上零售额当期值（亿元）', fontsize=14, pad=20)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False, fontsize=10)

# 网格和背景
ax1.yaxis.grid(True, linestyle='--', alpha=0.4)
ax2.set_ylim(-0.05, 0.20)
ax1.set_facecolor('white')

# 数据来源（用 fig.text 放在底部外部）
fig.text(0.01, 0.01, '数据来源：国家统计局。有米云内容中心绘制', ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])  # 给底部文本留空间
plt.show()