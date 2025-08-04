import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # 导入PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# 数据
categories = ['18以下', '18-24', '25-34', '35-44', '45-54', '55-64', '65以上']
age_percent = [2, 15, 40, 30, 20, 5, 2]  # 年龄占比数据
tgi_values = [70, 130, 120, 90, 80, 60, 60]  # TGI数据

x = np.arange(len(categories))

# 创建图表
fig, ax1 = plt.subplots(figsize=(10, 5), dpi=100)

# 绘制年龄占比柱状图
bar_plot = ax1.bar(categories, age_percent, color='#4A7AFE', width=0.5, label='年龄')
ax1.set_ylim([0, 50])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# 设置左侧坐标轴为百分比格式
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(10))

# 创建第二个y轴绘制TGI折线图
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# 设置右侧坐标轴刻度间隔
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# 添加标题
plt.title('法律服务行业从事人群年龄', fontsize=14, fontweight='bold')

# 为柱状图添加数据标注
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1,
             f'{age_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE', fontweight='bold')

# 为折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    # 根据TGI值大小调整标注位置，避免重叠
    y_offset = 8 if y_val < 100 else 12
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, y_offset),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# 合并图例并调整位置到图表下方
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='年龄占比'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.15),
           ncol=2, fontsize=10)

# 优化布局，为图例留出空间
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# 显示图表
plt.show()