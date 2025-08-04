import matplotlib.pyplot as plt
import numpy as np

# 城市等级
cities = ['一线城市', '二线城市', '三线城市', '四线城市']
x = np.arange(len(cities))

# 左侧Y轴：柱状图数据（关注度占比）
bar_values = [33, 17, 22, 15]  # 对应左侧坐标轴（0% - 40%）

# 右侧Y轴：折线图数据（另一个维度的关注度占比）
line_values = [33, 17, 22, 15]  # 对应右侧坐标轴（0% - 40%）

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制柱状图，左轴
bars = ax1.bar(x, bar_values, color='#1f77ff', width=0.5)
ax1.set_ylabel('关注度占比', fontsize=12)
ax1.set_ylim(0, 40)
ax1.set_yticks(np.arange(0, 41, 5))
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontsize=12)
ax1.set_title('2月奶粉行业分城市等级关注度占比', fontsize=15)

# 创建右轴绘制折线图
ax2 = ax1.twinx()
line, = ax2.plot(x, line_values, color='orange', linewidth=3, marker='o', markersize=8)
ax2.set_ylabel('另一个维度关注度占比', fontsize=12)
ax2.set_ylim(0, 40)
ax2.set_yticks(np.arange(0, 41, 5))

# 为折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(x, line_values)):
    # 根据数值大小调整标注位置，避免重叠
    if i in [0, 2]:  # 为避免与柱状图重叠，调整部分标注位置
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(10, 5),  # 向右上偏移
                    textcoords="offset points",
                    ha='left', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))
    else:
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, 10),  # 向上偏移
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# 美化图形边框
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# 添加图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, ['关注度占比', '另一个维度关注度占比'], loc='upper right')

plt.tight_layout()
plt.show()