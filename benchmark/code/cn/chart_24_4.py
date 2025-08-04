import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# 表情包配色方案（严格对应类型）
color_map = {
    '明星表情包': '#FF5252',
    '文字表情包': '#00E5FF',
    'QQ微信自带表情包': '#FFD740',
    '中老年表情包': '#9C27B0',
    'emoji': '#00E676',
    '漫画表情包': '#2979FF',
}

# 数据定义（保持原逻辑）
categories = ['中老年表情包', 'QQ微信自带表情包', '明星表情包', 
              '漫画表情包', 'emoji', '文字表情包']
percentages = [52, 40, 35, 28, 38, 46]

# 鄙视链关系（明确类型对应，方便颜色映射）
connections = [
    ('中老年表情包', 'QQ微信自带表情包', 3.5),   # 中老年 → QQ微信
    ('QQ微信自带表情包', '明星表情包', 3),    # QQ微信 → 明星
    ('明星表情包', '文字表情包', 2.5),       # 明星 → 文字
    ('文字表情包', 'emoji', 2),    # 文字 → emoji
    ('emoji', '漫画表情包', 1.5),  # emoji → 漫画
]

# 创建画布与基础设置
fig, ax = plt.subplots(figsize=(14, 12), facecolor='#FAFAFA')
ax.set_facecolor('#FAFAFA')
ax.grid(True, linestyle='--', alpha=0.3, color='#EEEEEE')

# 绘制饼图（强化阴影与边框）
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=categories, 
    autopct=lambda p: f'{p:.1f}%\n({int(p * sum(percentages) / 100)})',
    colors=[color_map[c] for c in categories],
    startangle=140,
    pctdistance=0.75,
    explode=[0.04] * 6,
    shadow=True,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    textprops={'fontsize': 12, 'weight': 'bold', 'color': '#212121'}
)

# 中心白色遮罩（增强层次感）
center_circle = plt.Circle((0, 0), 0.4, color='#FAFAFA', linewidth=0, zorder=1)
ax.add_artist(center_circle)

# 优化百分比标签样式（带白色背景框）
for a in autotexts:
    a.set_bbox(dict(boxstyle="round,pad=0.3", fc="white", ec="#BDBDBD", alpha=0.85))

# 设置标题
ax.set_title('90后版 鄙视逻辑：恶搞与新颖程度', 
             fontsize=22, 
             fontweight='bold', 
             color='#212121',
             pad=25)

# 绘制鄙视链箭头（颜色严格对应表情包主色）
for start_cat, end_cat, weight in connections:
    # 找到对应扇区的角度
    start_wedge = [w for w, l in zip(wedges, categories) if l == start_cat][0]
    end_wedge = [w for w, l in zip(wedges, categories) if l == end_cat][0]
    
    start_angle = (start_wedge.theta2 + start_wedge.theta1) / 2
    end_angle = (end_wedge.theta2 + end_wedge.theta1) / 2
    
    # 计算坐标（统一半径，避免混乱）
    radius = 0.65
    start_x = np.cos(np.radians(start_angle)) * radius
    start_y = np.sin(np.radians(start_angle)) * radius
    end_x = np.cos(np.radians(end_angle)) * radius
    end_y = np.sin(np.radians(end_angle)) * radius
    
    # 绘制箭头（单色，与起始表情包颜色一致）
    ax.annotate(
        '', 
        xy=(end_x, end_y), 
        xytext=(start_x, start_y),
        arrowprops=dict(
            arrowstyle='-|>', 
            color=color_map[start_cat],  # 用起始类型的颜色
            lw=weight,
            connectionstyle="arc3,rad=0.2"
        )
    )

# 构建图例（分两组：类型 + 关系）
legend_type = [
    Line2D([0], [0], color=color_map[c], lw=4, label=c) 
    for c in categories
]

legend_arrow = [
    Line2D([0], [0], color=color_map[start], lw=weight, label=f'{start} → {end}') 
    for start, end, weight in connections
]

# 合并图例（先类型，后关系）
legend1 = ax.legend(
    handles=legend_type, 
    loc='upper right', 
    title="表情包类型", 
    fontsize=11, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)
ax.add_artist(legend1)

ax.legend(
    handles=legend_arrow, 
    loc='lower right', 
    title="鄙视链关系", 
    fontsize=11, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)

# 底部注释
plt.figtext(
    0.15, 0.02, 
    "注：本图表为趣味化展示，数据不代表真实统计结果，仅供娱乐讨论。", 
    ha="left", 
    fontsize=10, 
    bbox={"facecolor":"white", "alpha":0.8, "pad":6}
)

# 调整布局
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()