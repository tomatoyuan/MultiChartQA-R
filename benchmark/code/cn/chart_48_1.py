import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.array([2019, 2020, 2021, 2022, 2023])
# 60周岁及以上人口（万人）
elderly_population = np.array([25388, 26402, 26736, 28004, 29697])
# 60周岁及以上人口比重（%）
proportion = np.array([18.1, 18.7, 18.9, 19.8, 21.1])

# 创建画布和轴
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制柱状图（左轴）
bars = ax1.bar(years, elderly_population, color='darkgreen', label='60周岁及以上人口(万人)')
ax1.set_xlabel('年份')
ax1.set_ylabel('60周岁及以上人口(万人)', color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

# 在柱状图上方添加数据标签
for bar, pop in zip(bars, elderly_population):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200, 
             f'{pop}', ha='center', va='bottom', color='darkgreen')

# 创建右轴用于绘制折线图
ax2 = ax1.twinx()
line, = ax2.plot(years, proportion, marker='o', color='black', label='60周岁及以上人口比重(%)')
ax2.set_ylabel('60周岁及以上人口比重(%)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# 在折线图数据点旁边添加数据标签
for x, y in zip(years, proportion):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='black')

# 添加图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# 设置x轴刻度为年份
ax1.set_xticks(years)

# 展示图表
plt.title('2019 - 2023年60周岁及以上老年人口及其占全国总人口比重')
plt.tight_layout()  # 调整布局避免内容重叠
plt.show()