import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# 数据
groups = ["吃货", "家庭主妇", "数码控", "音乐发烧友", "背包客", 
          "军迷", "家居", "体育迷", "理财家庭", "游戏达人"]
values = [1.2359, 1.1635, 1.0763, 1.0363, 1.0128, 
          1.0078, 0.9645, 0.8671, 0.7860, 0.5915]

# 符号映射（matplotlib 内置标记）
markers = ['o', 's', '^', 'D', 'p', '*', 'h', 'v', 'X', 'P']
marker_sizes = [100, 80, 90, 70, 85, 95, 80, 90, 75, 85]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f0f8ff")
ax.set_facecolor("#f0f8ff")

# 绘制柱状图（使用渐变色）
cmap = plt.cm.get_cmap('Blues', 12)
for i, (value, group) in enumerate(zip(values, groups)):
    color_idx = int(value * 5) if value > 1 else int(value * 5) + 2
    color = cmap(color_idx)
    
    ax.barh(i, value, height=0.6, color=color, edgecolor='white', alpha=0.85)
    ax.text(value + 0.02, i, f"{value:.4f}", 
            ha="left", va="center", color='navy', fontsize=10, fontweight='bold')

# 设置标题
ax.set_title("暴雨舆情兴趣分布（区分度）", 
             fontdict={"fontsize":20, "fontweight":"bold", "color":"navy"},
             pad=20)
ax.text(0, 1.02, "哪类人群最关注暴雨", 
        transform=ax.transAxes, fontsize=14, color='navy')

# 添加符号和类别标签
for i, (group, marker, size) in enumerate(zip(groups, markers, marker_sizes)):
    color_idx = int(values[i] * 5) if values[i] > 1 else int(values[i] * 5) + 2
    color = cmap(color_idx)
    
    ax.scatter(-0.05, i, marker=marker, s=size, color=color, edgecolor='white', zorder=3)
    ax.text(0.01, i, group, fontsize=12, ha="left", va="center", 
            color='navy', fontweight='bold')

# 添加参考线（区分度=1）
ax.axvline(x=1, color='navy', linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(1.01, -0.8, "区分度=1", fontsize=10, color='navy', alpha=0.8)

# 隐藏坐标轴
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# 设置x轴范围
ax.set_xlim(-0.1, 1.5)
ax.set_ylim(-1, 10)

# 添加图例（向下移动）
legend_elements = [
    Line2D([0], [0], color=cmap(8), lw=10, label='区分度 > 1：更关注'),
    Line2D([0], [0], color='navy', linestyle='--', lw=1.5, label='区分度 = 1：平均水平'),
    Line2D([0], [0], color=cmap(3), lw=10, label='区分度 < 1：较少关注')
]
ax.legend(handles=legend_elements, 
          loc='lower right',  # 定位到右下角
          bbox_to_anchor=(1, -0.1),  # 向下移动10%的高度
          frameon=False, 
          fontsize=10, 
          labelcolor='navy')

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.3, color='lightblue')

plt.tight_layout()
plt.show()