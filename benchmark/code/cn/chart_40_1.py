import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 数据
spicy_types = ["香辣", "酸辣", "番辣"]
preference_percentages = [45, 35, 30]
scoville_units = [250, 750, 1250]  # 辣度中间值
origins = ["中国、韩国等", "泰国、马来西亚等", "美国、墨西哥等"]
representative_dishes = [
    ["辣火锅", "辣泡菜", "辣炒年糕"],
    ["冬阴功汤", "青木瓜沙拉", "亚参叻沙"],
    ["德州烤肉", "烟熏辣肉", "墨西哥辣酱"]
]

# 颜色定义
colors = ['#FF5722', '#FF9800', '#FFC107']
light_colors = ['#FFCCBC', '#FFE0B2', '#FFF9C4']

# 创建画布
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1.5])

# 1. 偏好占比饼图
ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(preference_percentages, labels=spicy_types, autopct='%1.1f%%',
        startangle=90, colors=colors, wedgeprops={'edgecolor': 'w', 'linewidth': 2})
ax1.set_title('世界TOP3热门辣味偏好占比', fontsize=14, pad=15)
ax1.axis('equal')  # 保证饼图是圆的

# 2. 辣度对比条形图
ax2 = fig.add_subplot(gs[0, 1])
bars = ax2.bar(spicy_types, scoville_units, color=light_colors, edgecolor=colors, linewidth=1.5)
ax2.set_title('不同辣味风格的平均辣度 (SHU)', fontsize=14, pad=15)
ax2.set_xlabel('辣味类型', fontsize=12)
ax2.set_ylabel('辣度 (SHU)', fontsize=12)
ax2.set_ylim(0, 1600)

# 为每个条形添加数值标签
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 30,
             f'{height} SHU', ha='center', va='bottom', fontweight='bold')

# 3. 辣味类型信息表格
ax3 = fig.add_subplot(gs[1, :])
ax3.axis('off')

# 表格数据
table_data = []
for i, (spicy_type, percentage, scoville, origin, dishes) in enumerate(zip(
    spicy_types, preference_percentages, scoville_units, origins, representative_dishes
)):
    table_data.append([
        f'{spicy_type} ({percentage}%)', 
        f'{scoville} SHU', 
        origin,
        '\n'.join([f'• {dish}' for dish in dishes])
    ])

# 创建表格
table = ax3.table(
    cellText=table_data,
    colLabels=['辣味类型', '辣度', '发源地', '代表菜肴'],
    loc='center',
    cellLoc='left',
    colWidths=[0.15, 0.15, 0.25, 0.45]
)

# 设置表格样式
table.set_fontsize(12)
table.scale(1, 2)  # 调整表格大小

for i in range(len(spicy_types)):
    table[(i+1, 0)].set_facecolor(light_colors[i])
    table[(i+1, 0)].set_text_props(weight='bold', color='black')

for j in range(4):
    table[(0, j)].set_facecolor('#f0f0f0')
    table[(0, j)].set_text_props(weight='bold')

# 4. 辣味溯源地图（简化版）
ax4 = fig.add_subplot(gs[2, :])
ax4.set_title('辣味溯源地图', fontsize=14, pad=15)
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 6)
ax4.axis('off')

# 绘制简化的世界地图轮廓
world_map = plt.Rectangle((1, 1), 8, 4, fill=False, edgecolor='#CCCCCC', linewidth=2)
ax4.add_patch(world_map)

# 绘制辣味发源地和交汇点
origin_points = [
    (2, 2, "南美洲", colors[0]),  # 香辣发源地
    (8, 2, "东南亚", colors[1]),  # 酸辣发源地
    (5, 4, "中亚", colors[2])     # 辣味交汇地
]

# 添加发源地标记
for x, y, name, color in origin_points:
    ax4.plot(x, y, 'o', markersize=12, color=color)
    ax4.text(x, y-0.3, name, ha='center', va='top', fontweight='bold', color=color)

# 添加连接线
ax4.plot([2, 5], [2, 4], '--', color='#DDDDDD')
ax4.plot([8, 5], [2, 4], '--', color='#DDDDDD')

# 添加图例
legend_elements = [
    Patch(facecolor=colors[0], edgecolor='w', label='香辣发源地'),
    Patch(facecolor=colors[1], edgecolor='w', label='酸辣发源地'),
    Patch(facecolor=colors[2], edgecolor='w', label='辣味交汇地')
]
ax4.legend(handles=legend_elements, loc='lower right')

# 添加描述文字
ax4.text(5, 0.5, "说明：此地图为简化示意图，展示了三种辣味的主要发源地和交汇点", 
         ha='center', va='center', fontsize=10, color='#666666')

# 调整布局
plt.tight_layout()
plt.subplots_adjust(hspace=0.3)

# 显示图表
plt.show()