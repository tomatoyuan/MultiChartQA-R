import matplotlib.pyplot as plt
from matplotlib.patches import Arc, PathPatch, Path, Rectangle, Circle
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# 定义绘制云朵形状的函数 - 增强版
def draw_cloud(ax, x, y, scale=1, color='#ffffff', edge_color='#a8d5ff', shadow=True):
    """绘制立体感云朵形状"""
    # 主云朵
    verts = [
        (0, 0), (1, 0), (2, 1), (3, 0), (4, 0),
        (4, 1), (3, 2), (2, 1), (1, 2), (0, 1),
        (0, 0)
    ]
    verts = np.array(verts) * scale + [x, y]
    path = Path(verts)
    
    # 添加阴影效果
    if shadow:
        shadow_verts = verts + [0.1, -0.1]
        shadow_path = Path(shadow_verts)
        shadow_patch = PathPatch(shadow_path, facecolor='black', alpha=0.2)
        ax.add_patch(shadow_patch)
    
    patch = PathPatch(path, facecolor=color, edgecolor=edge_color, linewidth=1.5, alpha=0.9)
    ax.add_artist(patch)
    
    # 添加高光
    highlight_verts = [
        (1, 0.5), (2, 1.5), (1.5, 1.8), (0.5, 1), (1, 0.5)
    ]
    highlight_verts = np.array(highlight_verts) * scale * 0.6 + [x, y]
    highlight_path = Path(highlight_verts)
    highlight_patch = PathPatch(highlight_path, facecolor='white', alpha=0.6)
    ax.add_artist(highlight_patch)
    
    return patch

# 定义绘制雨滴形状的函数 - 增强版
def draw_rain(ax, x, y, num_drops=3, scale=1, color='#64b5f6'):
    """绘制带渐变效果的雨滴"""
    drop_verts = [(-0.2, 0), (0.2, 0), (0, -1)]
    drop_verts = np.array(drop_verts) * scale
    
    for i in range(num_drops):
        dx = (i - (num_drops - 1) / 2) * 0.5
        drop_path = Path(drop_verts + [x + dx, y - 0.5])
        
        # 创建渐变效果
        drop_patch = PathPatch(drop_path, facecolor=color, alpha=0.8)
        ax.add_artist(drop_patch)
        
        # 添加雨滴反光
        highlight_verts = [(-0.05, -0.2), (0.05, -0.2), (0, -0.5)]
        highlight_verts = np.array(highlight_verts) * scale
        highlight_path = Path(highlight_verts + [x + dx, y - 0.5])
        highlight_patch = PathPatch(highlight_path, facecolor='white', alpha=0.6)
        ax.add_artist(highlight_patch)

# 定义绘制彩虹效果的函数
def draw_rainbow(ax, x, y, width, height):
    """绘制背景彩虹效果"""
    colors = ['#ff6b6b', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
    for i, color in enumerate(colors):
        arc = Arc((x, y), width - i*0.3, height - i*0.3, 
                  theta1=0, theta2=180, color=color, alpha=0.1)
        ax.add_artist(arc)

# 创建画布 - 增加渐变背景
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 8)
ax.set_ylim(0, 10)
ax.axis('off')

# 创建渐变色背景
x = np.linspace(0, 8, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = Y

cmap = LinearSegmentedColormap.from_list('sky_gradient', ['#e6f2ff', '#b3d9ff', '#80bfff'])
im = ax.imshow(Z, cmap=cmap, extent=[0, 8, 0, 10], alpha=0.8, aspect='auto')

# 添加背景彩虹
draw_rainbow(ax, 4, -2, 10, 8)

# 绘制装饰性小云
for i in range(5):
    x_pos = np.random.uniform(0.5, 7.5)
    y_pos = np.random.uniform(7, 9.5)
    draw_cloud(ax, x_pos, y_pos, scale=0.2, color='#f0f8ff', shadow=False)

# 绘制标题区域 - 增强立体感（去掉左侧圆形及数字5相关代码）
# 右侧标题条 - 添加阴影和渐变
title_rect_bg = Rectangle((1.75, 8.85), 6.1, 0.7, facecolor='black', alpha=0.2)
ax.add_artist(title_rect_bg)
title_rect = Rectangle((1.8, 8.9), 6, 0.6, facecolor='#ffd166', edgecolor='white', linewidth=2)
ax.add_artist(title_rect)
ax.text(4.8, 9.2, '暴雨搜索关注度省份排行榜', fontsize=18, color='#073b4c', 
        ha='center', va='center', fontweight='bold')

# 绘制两个时间段的标题 - 添加圆角和立体感
def draw_fancy_rect(ax, x, y, width, height, color, text, font_size=10):
    """绘制带圆角和立体感的矩形标题"""
    rect_bg = Rectangle((x-0.05, y-0.05), width+0.1, height+0.1, 
                        facecolor='black', alpha=0.2, edgecolor='none')
    ax.add_artist(rect_bg)
    
    rect = Rectangle((x, y), width, height, facecolor=color, 
                    edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_artist(rect)
    
    ax.text(x + width/2, y + height/2, text, fontsize=font_size, 
            color='white', ha='center', va='center', fontweight='bold')

draw_fancy_rect(ax, 2.2, 8.0, 2, 0.4, '#0077b6', '7月1日-7日')
draw_fancy_rect(ax, 5.2, 8.0, 2, 0.4, '#0077b6', '7月20日')

# 绘制分隔线
divider = plt.Line2D([0, 8], [3.5, 3.5], color='#003e7e', alpha=0.2, linewidth=2)
ax.add_artist(divider)

# 绘制 7月1日-7日 省份云朵 - 添加渐变颜色
period1_provinces = ['湖北', '山东', '江苏', '安徽', '河南']
period1_colors = ['#ff6b6b', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
y_pos1 = np.linspace(7.2, 4.2, 5)

for i, (prov, color) in enumerate(zip(period1_provinces, period1_colors)):
    draw_cloud(ax, 3, y_pos1[i], scale=0.5, color='#ffffff', edge_color=color)
    # 添加省份名称背景
    name_bg = Rectangle((2.7, y_pos1[i]+0.15), 0.6, 0.3, facecolor=color, alpha=0.7, edgecolor='none')
    ax.add_artist(name_bg)
    ax.text(3, y_pos1[i] + 0.3, prov, fontsize=12, color='white', 
            ha='center', va='center', fontweight='bold')

# 绘制 7月20日 省份云朵 - 添加渐变颜色
period2_provinces = ['山东', '北京', '河北', '河南', '山西']
period2_colors = ['#ff6b6b', '#ef476f', '#ffd166', '#06d6a0', '#118ab2']
y_pos2 = np.linspace(7.2, 4.2, 5)

for i, (prov, color) in enumerate(zip(period2_provinces, period2_colors)):
    draw_cloud(ax, 6, y_pos2[i], scale=0.5, color='#ffffff', edge_color=color)
    # 添加省份名称背景
    name_bg = Rectangle((5.7, y_pos2[i]+0.15), 0.6, 0.3, facecolor=color, alpha=0.7, edgecolor='none')
    ax.add_artist(name_bg)
    ax.text(6, y_pos2[i] + 0.3, prov, fontsize=12, color='white', 
            ha='center', va='center', fontweight='bold')

# 绘制“最不关注暴雨的省份”标题
draw_fancy_rect(ax, 1, 2.5, 2.5, 0.4, '#6c757d', '最不关注暴雨的省份', font_size=10)

# 绘制最不关注省份（带雨滴） - 增强视觉效果
least_provinces = [('新疆', 1.8, 1.5, 3), ('宁夏', 3.5, 1.8, 3), 
                   ('广东', 5, 1.8, 3), ('内蒙古', 6.5, 1.5, 3), ('青海', 8, 1.2, 3)]

for i, (prov, x, y, drops) in enumerate(least_provinces):
    draw_cloud(ax, x, y, scale=0.35, color='#f8f9fa', edge_color='#6c757d')
    # 添加省份名称
    ax.text(x, y + 0.15, prov, fontsize=10, color='#073b4c', 
            ha='center', va='center', fontweight='bold')
    # 添加雨滴
    draw_rain(ax, x, y - 0.3, num_drops=drops, scale=0.3, color='#64b5f6')

# 添加装饰性雨滴背景
for _ in range(50):
    x_pos = np.random.uniform(0, 8)
    y_pos = np.random.uniform(0, 10)
    draw_rain(ax, x_pos, y_pos, num_drops=1, scale=0.15, color='#90caf9')

plt.tight_layout()
plt.show()