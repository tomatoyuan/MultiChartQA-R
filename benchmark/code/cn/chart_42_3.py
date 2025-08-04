import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['之前', '2024年']
values = [100, 117]
x = np.arange(len(categories))

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bar_width = 0.6
rects1 = ax.bar(x[0], values[0], width=bar_width, color='#6aa84f', label='之前销售额', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], values[1], width=bar_width, color='#3d85c6', label='2024年销售额', 
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

# 添加水平增长箭头标注
ax.annotate('增长 17%', 
            xy=(0.8, 105),  # 箭头起点
            xytext=(0.2, 105),  # 箭头终点
            arrowprops=dict(facecolor='black', shrink=0.02, width=1.5, headwidth=8, connectionstyle="arc3"),
            ha='center', va='center', fontsize=12)

# 设置图表样式
ax.set_ylim([0, 140])
ax.set_ylabel('销售额 (十亿)', fontsize=14)
ax.set_title('2024年保健食品行业销售额增长情况', fontsize=16, pad=15)
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