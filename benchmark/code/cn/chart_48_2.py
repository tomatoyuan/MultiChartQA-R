import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# 年龄分组
age_groups = [
    "50-54岁", "55-59岁", "60-64岁", "65-69岁", 
    "70-74岁", "75-79岁", "80-84岁", "85-89岁", 
    "90-94岁", "95岁及以上"
]
# 按年龄分人口数（人）
population = [127635, 117482, 71964, 79964, 58782, 35928, 22434, 12542, 4297, 929]
# 占全国人口比重（%）
proportion = [8.84, 8.14, 4.98, 5.54, 4.07, 2.49, 1.55, 0.87, 0.30, 0.06]

x = np.arange(len(age_groups))  # x轴坐标
width = 0.35  # 柱子宽度

# 创建画布和主次坐标轴
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# 绘制人口数柱状图（深蓝色渐变）
cmap1 = plt.cm.Blues
norm1 = plt.Normalize(min(population), max(population))
colors1 = [cmap1(norm1(value)) for value in population]
rects1 = ax1.bar(x - width/2, population, width, label='按年龄分人口数(人)', color=colors1)

# 绘制占比柱状图（深绿色渐变）
cmap2 = plt.cm.Greens
norm2 = plt.Normalize(min(proportion), max(proportion))
colors2 = [cmap2(norm2(value)) for value in proportion]
rects2 = ax2.bar(x + width/2, proportion, width, label='占全国人口比重(%)', color=colors2)

# 设置坐标轴标签和标题
ax1.set_ylabel('人口数(万人)', fontsize=13, color='#004D40')
ax1.set_xlabel('年龄分组', fontsize=13)
ax1.set_title('2022年中国50岁以上人口年龄分布与占比', fontsize=16, pad=20, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(age_groups, rotation=30, ha='center', fontsize=12)

# 设置y轴格式
def thousands_formatter(x, pos):
    return f'{x/10000:.1f}'
ax1.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# 添加网格线
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle=':', alpha=0.5)

# 为每个柱子添加数值标签（带千分位分隔符）
def add_labels(rects, ax, is_percent=False):
    for rect in rects:
        height = rect.get_height()
        if is_percent:
            label = f'{height:.2f}%'
        else:
            label = f'{height:,}'
        ax.annotate(label,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 标签距离柱子的垂直距离
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

add_labels(rects1, ax1)
add_labels(rects2, ax2, is_percent=True)

# 美化图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right', frameon=True, framealpha=0.9, shadow=True)

# 调整布局
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 为底部和顶部留出空间
plt.show()