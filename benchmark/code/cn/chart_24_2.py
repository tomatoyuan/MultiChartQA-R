import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# 标签和数据（对应男生版 鄙视逻辑：直观度——男性使用率 数据）
labels = [
    "文字表情包", "中老年表情包", "明星表情包", 
    "emoji", "QQ微信自带表情包", "漫画表情包"
]
values = [28, 31, 45, 64, 67, 72]

# 生成渐变色系
def get_gradient_colors(base_color, num_layers, lightness_range=(0.6, 1.0)):
    """生成从深到浅的渐变色"""
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.colors as mcolors
    
    # 将十六进制颜色转换为RGB
    rgb = mcolors.hex2color(base_color)
    
    # 创建渐变色映射
    cmap = LinearSegmentedColormap.from_list(
        f'custom_{base_color}', 
        [(rgb[0]*lightness_range[0], rgb[1]*lightness_range[0], rgb[2]*lightness_range[0]), 
         (rgb[0]*lightness_range[1], rgb[1]*lightness_range[1], rgb[2]*lightness_range[1])]
    )
    
    return [cmap(i/num_layers) for i in range(num_layers)]

# 使用绿色系作为基础
base_color = '#2c6f66'
colors = get_gradient_colors(base_color, len(labels))

# 图形参数
num_layers = len(labels)
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 底部顶点坐标
bottom_x = 0.5
bottom_y = 0.05

# 顶部宽度（整个倒三角上边）
top_left = (0.1, 0.95)
top_right = (0.9, 0.95)

# 每层高度（均分）
layer_height = (top_left[1] - bottom_y) / num_layers

# 绘制背景渐变
gradient_bg = np.zeros((100, 100, 3))
for i in range(100):
    for j in range(100):
        y_norm = i / 100
        # 背景色从浅绿到更浅的绿
        gradient_bg[i, j] = [0.95 - y_norm*0.1, 0.98 - y_norm*0.1, 0.95 - y_norm*0.05]
ax.imshow(gradient_bg, extent=[0, 1, 0, 1], aspect='auto', zorder=0)

# 添加阴影效果
shadow_offset = 0.015
for i in range(num_layers):
    # 顶部 y 和 底部 y
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # 计算对应高度下三角左右边界的 x 坐标
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # 构造阴影形状
    shadow_points = [
        (x_left_top + shadow_offset, y_top - shadow_offset),
        (x_right_top + shadow_offset, y_top - shadow_offset),
        (x_right_bottom + shadow_offset, y_bottom - shadow_offset),
        (x_left_bottom + shadow_offset, y_bottom - shadow_offset)
    ]
    shadow = Polygon(shadow_points, closed=True, facecolor='black', alpha=0.15, zorder=i+1)
    ax.add_patch(shadow)

# 绘制主图表
for i in range(num_layers):
    # 顶部 y 和 底部 y
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # 计算对应高度下三角左右边界的 x 坐标
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # 构造梯形/三角带形状
    points = [
        (x_left_top, y_top),
        (x_right_top, y_top),
        (x_right_bottom, y_bottom),
        (x_left_bottom, y_bottom)
    ]
    
    # 添加轻微的透明度变化，使底部更明显
    alpha = 0.95 - i * 0.03 if i < num_layers - 1 else 0.95
    tri = Polygon(points, closed=True, facecolor=colors[i], edgecolor='white', linewidth=1.5, alpha=alpha, zorder=i+2)
    ax.add_patch(tri)

    # 在每层中间写文字
    y_text = (y_top + y_bottom) / 2
    ax.text(0.5, y_text, f"{labels[i]}", 
            color='black', ha='right', va='center', fontsize=13, fontweight='medium',
            transform=ax.transAxes, zorder=10)
    
    # 添加百分比标签
    ax.text(0.52, y_text, f"{values[i]}%", 
            color='white', ha='left', va='center', fontsize=13, fontweight='bold',
            transform=ax.transAxes, zorder=10)

# 添加新的标题相关文字，按照男生版需求调整标题、副标题内容
plt.text(0.5, 1.02, "男生版", ha='center', fontsize=22, weight='bold', color=base_color, transform=ax.transAxes)
plt.text(0.5, 0.98, "鄙视逻辑：直观度——男性使用率", ha='center', fontsize=14, color='#666666', transform=ax.transAxes)

# 调整布局
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.05)
plt.show()