import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # 补充导入PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# 数据
categories = ['本科及以上', '大专', '高中及以下']
education_level = [20, 30, 60]  # 学历数据
tgi_values = [140, 125, 100]  # TGI数据

x = np.arange(len(categories))

# 创建图表
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)

# 绘制学历柱状图
bar_plot = ax1.bar(categories, education_level, color='#4A7AFE', width=0.5, label='学历')
ax1.set_ylim([0, 80])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# 设置左侧坐标轴刻度间隔及格式
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(20))

# 创建第二个y轴绘制TGI折线图
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# 设置右侧坐标轴刻度间隔
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# 添加标题
plt.title('法律服务行业从事人群教育水平', fontsize=14, fontweight='bold')

# 为柱状图添加数据标注
for rect in bar_plot:
    height = rect.get_height()
    # 在柱状图顶部居中位置添加百分比标注
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1.5,
             f'{height}%',
             ha='center', va='bottom', fontsize=11, color='#4A7AFE', fontweight='bold')

# 为折线图添加数据标注
for i, (cat, tgi) in enumerate(zip(categories, tgi_values)):
    # 根据数据点位置调整标注偏移，避免重叠
    y_offset = 5 if tgi < 130 else 8  # 数值较高的点适当增加偏移
    ax2.annotate(f'{tgi}',
                 xy=(i, tgi),  # 使用索引定位，避免中文坐标问题
                 xytext=(0, y_offset),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 fontsize=11, color='#FF9900', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# 合并图例并调整位置到图表下方
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='学历分布'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1),
           ncol=2, fontsize=10)

# 优化布局，为图例留出空间
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# 显示图表
plt.show()