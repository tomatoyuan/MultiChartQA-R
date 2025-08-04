import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# 数据（根据图表视觉估算，若有精准数据可替换）
categories = ['18以下', '18-24', '25-34', '35-44', '45-54', '55-64', '65以上']
age_percent = [2, 10, 45, 25, 15, 5, 3]  # 年龄占比
tgi_values = [60, 90, 120, 100, 90, 110, 180]  # TGI数据

x = np.arange(len(categories))

# 创建图表
fig, ax1 = plt.subplots(figsize=(12, 6), dpi=100)

# 绘制年龄占比柱状图
bar_plot = ax1.bar(categories, age_percent, color='#4A7AFE', width=0.5, label='年龄')
ax1.set_ylim([0, 55])  # 增加上限以留出标注空间
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# 设置左侧坐标轴刻度间隔
ax1.yaxis.set_major_locator(MultipleLocator(10))

# 为柱状图添加数据标注
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1,
             f'{age_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# 创建第二个y轴绘制TGI折线图
ax2 = ax1.twinx()
line_plot, = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', 
                      label='TGI', linewidth=2, markersize=8)
ax2.set_ylim(0, 220)  # 增加上限以留出标注空间

# 设置右侧坐标轴刻度间隔
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# 为折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(x, tgi_values)):
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, 10) if i != 6 else (0, -15),  # 最后一个点标注在下方
                textcoords="offset points",
                ha='center',
                va='bottom' if i != 6 else 'top',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#FF9900", alpha=0.8))

# 添加标题
plt.title('离婚诉讼人群年龄', fontsize=16, fontweight='bold')

# 合并图例并调整位置到图表下方
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='年龄占比'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI指数', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.12),
           ncol=2, fontsize=12, frameon=False)

# 添加网格线增强可读性
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 优化布局，为图例留出空间
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# 显示图表
plt.show()