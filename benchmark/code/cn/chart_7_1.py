import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator  # 导入 MultipleLocator
from matplotlib.patches import Patch  # 导入Patch用于创建自定义图例项
from matplotlib.lines import Line2D   # 导入Line2D用于创建自定义图例项

# 数据
categories = ['男', '女']
gender_percent = [51, 49]  # 性别占比
tgi_values = [85, 115]  # TGI值，可根据实际调整

x = np.arange(len(categories))

# 创建图表
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)  # 增加图表高度，为下方图例留出空间

# 绘制性别占比柱状图
bar_plot = ax1.bar(categories, gender_percent, color='#4A7AFE', width=0.5, label='性别')
ax1.set_ylabel('性别占比（%）', fontsize=12, color='#4A7AFE')
ax1.set_ylim([46, 52])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# 设置左侧坐标轴刻度间隔为2
ax1.yaxis.set_major_locator(MultipleLocator(2))

# 创建第二个y轴绘制TGI折线图
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylabel('TGI', fontsize=12, color='#FF9900')
ax2.set_ylim(0, 150)

# 设置右侧坐标轴刻度间隔为50
ax2.yaxis.set_major_locator(MultipleLocator(50))

ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# 添加标题
plt.title('法律服务行业从事人群男女比例', fontsize=14, fontweight='bold')

# 为柱状图添加数据标注
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 0.1,
             f'{gender_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# 为折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    # 调整标注位置，使其位于数据点右侧
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(10, 0),  # 向右偏移10个点
                textcoords='offset points',
                ha='left', va='center',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

# 合并图例并调整位置到图表下方
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='性别'),  # 柱状图图例
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)  # 折线图图例
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# 优化布局，为图例留出空间
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # 调整图表边界，底部留出10%空间

# 显示图表
plt.show()