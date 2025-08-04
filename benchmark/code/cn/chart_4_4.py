import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
import numpy as np

# 数据
sizes = [88.08, 11.69, 0.18, 0.05]
labels = ["视频占比", "图文占比", "小程序占比", "图集占比"]

# 自定义颜色方案
colors = [
    ["#1976d2", "#e3f2fd"],  # 视频占比：深蓝色和浅蓝色
    ["#f57c00", "#ffebee"],  # 图文占比：橙色和浅橙色
    ["#388e3c", "#e8f5e9"],  # 小程序占比：绿色和浅绿色
    ["#7b1fa2", "#f3e5f5"]   # 图集占比：紫色和浅紫色
]

# 创建3D效果
fig = plt.figure(figsize=(20, 10))
fig.subplots_adjust(top=0.85, bottom=0.15, wspace=0.3)

# 创建4个子图
axes = []
for i in range(4):
    ax = fig.add_subplot(1, 4, i+1, aspect='equal')
    axes.append(ax)

# 绘制3D饼图
for i, ax in enumerate(axes):
    # 设置颜色
    chart_colors = [colors[i][0], colors[i][1]]
    
    # 计算角度
    theta1 = 0
    theta2 = 360 * sizes[i]/100
    
    # 创建3D效果 - 绘制多层扇形
    for height in [0, 0.1, 0.2]:
        if sizes[i] < 5:  # 小数值部分加厚突出
            height_factor = 0.3
        else:
            height_factor = 0.1
            
        # 主扇形
        wedge = Wedge((0,0), 1, theta1, theta2, width=0.2, 
                     facecolor=chart_colors[0], edgecolor='w', linewidth=1)
        ax.add_patch(wedge)
        
        # 底部扇形（浅色部分）
        wedge_bottom = Wedge((0,0), 1, theta2, 360, width=0.2,
                           facecolor=chart_colors[1], edgecolor='w', linewidth=1)
        ax.add_patch(wedge_bottom)
        
        # 添加3D边缘效果
        if height > 0:
            edge = Wedge((0,0), 1, theta1, theta2, width=0.2,
                        facecolor=chart_colors[0], alpha=0.3)
            ax.add_patch(edge)
    
    # 设置标题
    ax.set_title(labels[i], fontsize=18, pad=20)
    
    # 添加百分比标签
    if sizes[i] >= 0.01:  # 只显示大于0.1%的标签
        angle = theta1 + (theta2 - theta1)/2
        x = 0.6 * np.cos(np.deg2rad(angle))
        y = 0.6 * np.sin(np.deg2rad(angle))
        ax.text(x, y, f"{sizes[i]:.2f}%", 
                ha='center', va='center', fontsize=12)
    
    # 设置坐标范围
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

# 设置总标题
fig.suptitle("5月医疗美容行业资讯关注度途径", fontsize=28, fontweight='bold', y=0.85)

plt.tight_layout()
plt.show()