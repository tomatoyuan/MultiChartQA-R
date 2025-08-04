import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# 数据
cities = ['北京', '深圳', '西安', '武汉', '上海', '成都', '长沙', '重庆', '广州', '东莞']
single_men = [68, 75, 62, 58, 65, 57, 54, 51, 59, 53]  # 单身男性数量（万）
single_women = [72, 68, 59, 56, 69, 61, 58, 53, 63, 50]  # 单身女性数量（万）

# 创建画布和子图
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 设置柱状图参数
x = np.arange(len(cities))
width = 0.35
bar_positions_men = x - width/2
bar_positions_women = x + width/2

# 定义渐变色
def gradient_color(base_color, alpha):
    """根据基础颜色和透明度生成渐变颜色"""
    from matplotlib.colors import to_rgba
    return to_rgba(base_color, alpha)

# 绘制渐变柱状图
base_color_men = '#4361EE'
base_color_women = '#3F37C9'

for i, (m, w) in enumerate(zip(single_men, single_women)):
    # 男性柱状图（带渐变效果）
    ax.bar(bar_positions_men[i], m, width, 
           color=gradient_color(base_color_men, 0.9), 
           edgecolor='#2b49a0', linewidth=0.8)
    
    # 女性柱状图（带渐变效果）
    ax.bar(bar_positions_women[i], w, width, 
           color=gradient_color(base_color_women, 0.9), 
           edgecolor='#282480', linewidth=0.8)

# 设置标题和标签
ax.set_title('全国单身男女数量分布前十城市', 
             fontsize=20, fontweight='bold', pad=20, color='#333333')
ax.set_xlabel('城市', fontsize=16, labelpad=15, color='#555555')
ax.set_ylabel('单身人数 (万)', fontsize=16, labelpad=15, color='#555555')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(cities, rotation=30, ha='right', fontsize=14, color='#555555')

# 设置y轴范围和刻度
ax.set_ylim(0, max(max(single_men), max(single_women)) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # 确保y轴刻度为整数

# 添加数值标签
def add_labels(positions, heights, colors):
    for pos, height, color in zip(positions, heights, colors):
        ax.text(pos, height + 1, f'{height}', 
                ha='center', va='bottom', 
                fontsize=12, fontweight='bold', color=color)

add_labels(bar_positions_men, single_men, ['#2b49a0']*len(cities))
add_labels(bar_positions_women, single_women, ['#282480']*len(cities))

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7, color='#cccccc')

# 添加图例
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=base_color_men, edgecolor='#2b49a0', label='单身男性'),
                   Patch(facecolor=base_color_women, edgecolor='#282480', label='单身女性')]
ax.legend(handles=legend_elements, loc='upper right', fontsize=14)

# 添加水平参考线
ax.axhline(y=60, color='#e0e0e0', linestyle='-', linewidth=1)

# 美化边框
for spine in ax.spines.values():
    spine.set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('#cccccc')

# 添加数据来源注释
ax.annotate('数据来源: 虚构数据（仅作示例）',
            xy=(0.05, 0.01), xycoords='figure fraction',
            fontsize=10, color='#999999')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()

# 保存图表（取消注释以保存）
# plt.savefig('single_population_chart_beautiful.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())