import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.font_manager as fm

# 数据
dates = ["7月19日", "7月20日"]
searches = [234381, 534381]
increase = 41  # 增长率

# 创建自定义渐变色
colors = [(0.9, 0.95, 1), (0.1, 0.3, 0.6)]  # 从浅蓝到深蓝
custom_cmap = LinearSegmentedColormap.from_list("custom_blue", colors, N=100)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f8fafc")
ax.set_facecolor("#f8fafc")

# 绘制背景网格
for y in np.linspace(0, max(searches), 6):
    ax.axhline(y, color='lightblue', alpha=0.15, linewidth=1)

# 绘制柱状图（带立体效果）
x_pos = np.arange(len(dates))
bar_width = 0.6

for i, (date, search) in enumerate(zip(dates, searches)):
    # 主柱状图（渐变填充）
    rect = Rectangle((i-bar_width/2, 0), bar_width, search, 
                    facecolor='none', edgecolor='none')
    ax.add_patch(rect)
    
    img = np.ones((100, 1)) * np.linspace(0.3, 1, 100).reshape(-1, 1)
    ax.imshow(img, aspect='auto', extent=[i-bar_width/2, i+bar_width/2, 0, search],
              cmap=custom_cmap, alpha=0.9, clip_path=rect)
    
    # 顶部高光
    top_highlight = Rectangle((i-bar_width/2, search-10000), bar_width, 10000, 
                             facecolor='white', alpha=0.3)
    ax.add_patch(top_highlight)
    
    # 数值标签（带阴影效果）
    label_bg = Rectangle((i-0.25, search+15000), 0.5, 30000, 
                        facecolor='navy', alpha=0.8, zorder=3)
    ax.add_patch(label_bg)
    
    ax.text(i, search+30000, f'{search:,}', 
            ha='center', va='center', color='white', fontsize=18, 
            fontweight='bold', zorder=4)

# 添加增长率指示（使用箭头和百分比符号）
class CustomArrow(FancyArrowPatch):
    def __init__(self, posA, posB, **kwargs):
        super().__init__(posA, posB, arrowstyle='-|>', 
                         mutation_scale=20, **kwargs)

arrow = CustomArrow((1.1, searches[0]), (1.1, searches[1]*0.85), 
                   color='navy', alpha=0.8, linewidth=2)
ax.add_patch(arrow)

# 增长率百分比标记
growth_bg = Rectangle((1.1-0.15, searches[1]*0.85), 0.3, 30000, 
                     facecolor='navy', alpha=0.9, zorder=3)
ax.add_patch(growth_bg)

ax.text(1.1, searches[1]*0.85+15000, f'{increase}%', 
        ha='center', va='center', color='white', fontsize=20, 
        fontweight='bold', zorder=4)

# 设置标题（带装饰线）
title = ax.set_title('大雨天外卖检索次数', 
                     fontdict={'fontsize':26, 'fontweight':'bold', 'color':'navy'},
                     pad=40, loc='center')

# 标题下的装饰线
line_start = 0.35
line_end = 0.65
ax.plot([line_start, line_end], [0.94, 0.94], transform=ax.transAxes, 
        color='navy', alpha=0.3, linewidth=2)

# 隐藏坐标轴
ax.set_xticks(x_pos)
ax.set_xticklabels(dates, color='navy', fontsize=18, fontweight='bold')
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# 设置y轴范围
ax.set_ylim(0, max(searches) * 1.3)

# 添加底部装饰条
bottom_bar = Rectangle((-0.5, -30000), 2.5, 30000, 
                      facecolor='navy', alpha=0.1)
ax.add_patch(bottom_bar)

# 优化布局
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # 为标题腾出空间
plt.show()