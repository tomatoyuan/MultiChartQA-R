import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['', '']
values = [8, 9.84]  # 准确数据：8 * (1+0.18) = 9.44，根据图表视觉微调为9.84
x = np.arange(len(categories))

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bar_width = 0.6
rects1 = ax.bar(x[0], values[0], width=bar_width, color='#6aa84f', label='之前销售额', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], values[1], width=bar_width, color='#3d85c6', label='2025年1月销售额', 
                edgecolor='black', linewidth=0.8)

# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12)

add_labels(rects1)
add_labels(rects2)

# 添加水平箭头标注（向右指向）
arrow_start = (x[0] + bar_width/2, values[0] + 0.3)  # 箭头起点：第一根柱子右侧
arrow_end = (x[1] - bar_width/4, values[0] + 0.3)  # 箭头终点：第二根柱子左侧
ax.annotate('增长 18%',
            xy=arrow_end,
            xytext=arrow_start,
            arrowprops=dict(arrowstyle='->, head_width=0.4, head_length=0.8', 
                           color='black', lw=1.5, shrinkA=0, shrinkB=0),
            ha='left', va='center', fontsize=12, 
            xycoords='data', textcoords='data')

# 设置图表样式
ax.set_ylim([0, 12])
ax.set_ylabel('十亿', fontsize=14)
ax.set_title('2025年1月保健食品行业销售额增长情况', fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=12, loc='upper left')

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 调整边框
for spine in ax.spines.values():
    spine.set_color('gray')

# 美化整体样式
plt.tight_layout()

# 显示图表
plt.show()