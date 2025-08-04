import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2019, 2024)
# 中国近视人口（亿人）
myopia_pop = [6.0, 6.5, 6.9, 6.9, 7.0]
# 中国人口总数（亿人）
total_pop = [14.1, 14.2, 14.6, 14.6, 14.6]
# 近视人口占比（%）
myopia_ratio = [42.6, 45.8, 47.3, 47.3, 47.9]

x = np.arange(len(years))  # x轴刻度位置

fig, ax1 = plt.subplots(figsize=(12, 6))  # 调整图表大小

# 调整柱状图宽度和位置，避免重叠
width = 0.35
rects1 = ax1.bar(x - width/2, myopia_pop, width, label='中国近视人口（亿人）', color='greenyellow', alpha=0.8)
rects2 = ax1.bar(x + width/2, total_pop, width, label='中国人口总数（亿人）', color='dodgerblue', alpha=0.8)

ax1.set_ylabel('人口数量（亿人）', fontsize=12)
ax1.set_xlabel('年份', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.legend(loc='lower center')
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线

# 创建第二个y轴，绘制折线图
ax2 = ax1.twinx()
ax2.plot(x, myopia_ratio, marker='o', markersize=8, label='近视人口占比（%）', color='blue', linewidth=2.5)
ax2.set_ylabel('占比（%）', fontsize=12)
ax2.set_ylim(40, 50)  # 调整y轴范围
ax2.legend(loc='upper left')

# 给柱状图添加数值标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

autolabel(rects1)
autolabel(rects2)

# 给折线图添加数值标签
for i, ratio in enumerate(myopia_ratio):
    ax2.annotate(f'{ratio}%',
                 xy=(x[i], ratio),
                 xytext=(0, 8),  # 垂直偏移
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))

plt.title('2019年-2023年中国近视人口总数及占比情况', fontsize=15, pad=15)
plt.tight_layout()  # 优化布局
plt.show()