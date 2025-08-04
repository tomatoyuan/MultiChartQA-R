import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# 数据
generations = ['05后', '00后', '95后', '90后', '85后', '80后', '80前']
values = [105, 73, 115, 115, 110, 80, 80]

# 渐变色生成函数
def gradient_rect(ax, x, y, width, height, color1, color2, vertical=True):
    cmap = LinearSegmentedColormap.from_list("custom_gradient", [color1, color2])
    n = 100
    for i in range(n):
        if vertical:
            yi = y + i * height / n
            hi = height / n
            rect = Rectangle((x, yi), width, hi, color=cmap(i / n), linewidth=0)
        else:
            xi = x + i * width / n
            wi = width / n
            rect = Rectangle((xi, y), wi, height, color=cmap(i / n), linewidth=0)
        ax.add_patch(rect)

# 创建图表
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.5
x = np.arange(len(generations))

# 绘制渐变柱状图
for i, val in enumerate(values):
    if val >= 100:
        gradient_rect(ax, x[i] - bar_width / 2, 100, bar_width, val - 100, '#f99bc5', '#c7008d', vertical=True)
    else:
        gradient_rect(ax, x[i] - bar_width / 2, val, bar_width, 100 - val, '#fddde6', '#fdaecf', vertical=True)

# 添加辅助线和文本
ax.axhline(100, color='gray', linestyle='--')
for i, v in enumerate(values):
    va = -10 if v < 100 else 5
    ax.text(x[i], v + va, str(v), color='black', ha='center', va='bottom' if v < 100 else 'top', fontsize=12)

# 设置轴标签
ax.set_xticks(x)
ax.set_xticklabels(generations, fontsize=12)
ax.set_ylabel('TGI')
ax.set_ylim(60, 130)
ax.set_title('不同代际女性对口腔健康关注度调研\n(TGI>100表示高关注)', fontsize=14)

# 显示图表
plt.tight_layout()
plt.show()