import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

# 数据配置（合并性别和年龄段）
data = {
    "gender": {
        "groups": ["男", "女"],
        "tgi": [120, 93],
        "outer_color": "#D9D9D9",  # 外侧锯齿圆环颜色
        "inner_colors": ["#4CAD8F", "#4CAD8F"],  # 内侧圆颜色（男深女浅）
        "title": "分性别",
        "label_pos": [(-2.2, 0.5), (2.2, 0.5)],  # 标签位置（左右分布）
        "annotation": "关注度(TGI)"  # 注释文本
    },
    "age": {
        "groups": ["18-24", "25-34", "35-44", "＞45岁"],
        "tgi": [104, 117, 95, 82],
        "outer_color": "#D9D9D9",  # 外侧锯齿圆环颜色
        "inner_colors": ["#4DA6FF", "#4DA6FF", "#4DA6FF", "#4DA6FF"],  # 蓝色
        "title": "分年龄段",
        "label_pos": [(-2.2, 1.2), (2.2, 1.2), (-2.2, -0.8), (2.2, -0.8)],  # 标签位置
        "annotation": ""  # 年龄段不重复显示注释
    }
}

# 创建画布（调整高度以容纳两个分组）
fig = plt.figure(figsize=(6, 8), facecolor='white')  # 增加画布高度
ax = fig.add_subplot(111)

# 绘制锯齿外框的核心函数
def draw_serrated_ring(center, radius, color, num_teeth=30):
    """
    绘制带锯齿的固定外框
    :param center: 圆心坐标 (x, y)
    :param radius: 外框半径
    :param color: 外框颜色
    :param num_teeth: 锯齿数量（控制美观度）
    """
    theta = np.linspace(0, 2 * np.pi, num_teeth * 2, endpoint=False)
    radii = np.array([radius, radius * 0.95] * num_teeth)
    path_data = []
    for t, r in zip(theta, radii):
        x = center[0] + r * np.cos(t)
        y = center[1] + r * np.sin(t)
        path_data.append((Path.MOVETO if t == 0 else Path.LINETO, (x, y)))
    
    # 闭合路径
    path_data.append((Path.CLOSEPOLY, (center[0], center[1])))
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='none', edgecolor=color, lw=2)
    ax.add_patch(patch)

# 绘制动态内圆的函数
def draw_dynamic_inner_circle(center, tgi, color, max_tgi=120):
    """
    绘制随 TGI 动态变化的内圆
    :param center: 圆心坐标 (x, y)
    :param tgi: TGI 数值
    :param color: 内圆颜色
    :param max_tgi: 最大 TGI（用于归一化）
    """
    # 按 TGI 比例计算内圆半径
    radius_ratio = np.sqrt(tgi / max_tgi)
    base_radius = 0.9  # 基础半径（相对于外框半径 1.0）
    radius = base_radius * radius_ratio
    
    inner_circle = Circle(center, radius, color=color, zorder=2)
    ax.add_artist(inner_circle)
    
    # 添加 TGI 文本
    ax.text(
        center[0], center[1], 
        f"{tgi}", 
        ha='center', 
        va='center', 
        fontsize=14, 
        fontweight='bold', 
        color='#333333',
        zorder=3
    )

# 绘制分隔线函数
def draw_separator(y_pos, length=6, color='#E0E0E0', linestyle='-', linewidth=1.5):
    """
    绘制水平分隔线
    :param y_pos: 分隔线的y坐标位置
    :param length: 分隔线长度
    :param color: 分隔线颜色
    :param linestyle: 线型
    :param linewidth: 线宽
    """
    x_start = -length / 2
    x_end = length / 2
    ax.plot([x_start, x_end], [y_pos, y_pos], color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)

# 绘制所有分组
for group_type, group_data in data.items():
    # 垂直偏移量（性别组在上，年龄组在下）
    y_offset = -3.5 if group_type == "age" else 0  # 调整垂直偏移
    
    # 绘制每个分组的所有圆圈
    for i, (group, tgi, color) in enumerate(zip(
        group_data["groups"], 
        group_data["tgi"], 
        group_data["inner_colors"]
    )):
        # 计算圆心位置（左右交替分布）
        center = (1.5 if i % 2 == 1 else -1.5, y_offset + (1.0 if i < 2 else -1.0))
        
        # 绘制锯齿外框
        draw_serrated_ring(center, radius=1.0, color=group_data["outer_color"])
        
        # 绘制动态内圆
        draw_dynamic_inner_circle(center, tgi, color)
        
        # 添加分组标签
        label_x, label_y = group_data["label_pos"][i]
        ax.text(
            label_x, label_y + y_offset, 
            group, 
            ha='center', 
            va='center', 
            fontsize=12, 
            fontweight='bold', 
            color='#333333',
            bbox=dict(facecolor='white', edgecolor='none', pad=2),
            zorder=4
        )
    
    # 上移分组标题
    title_y = 2.5 + y_offset
    ax.text(
        -2.5, title_y, 
        group_data["title"], 
        ha='left', 
        va='center', 
        fontsize=16, 
        fontweight='bold', 
        color='#333333',
        zorder=5
    )
    
    # 上移注释箭头
    if group_data["annotation"]:
        ax.annotate(
            group_data["annotation"], 
            xy=(-0.5, 0.5 + y_offset), 
            xytext=(-1.2, 1.8 + y_offset),
            arrowprops=dict(arrowstyle='->', color='#666666'),
            fontsize=12, 
            color='#666666',
            zorder=6
        )

# 添加整体标题
ax.text(
    0, 4.0,  # 上移整体标题
    "分性别与年龄段对新国货的关注度 (TGI)", 
    ha='center', 
    va='center', 
    fontsize=18, 
    fontweight='bold', 
    color='#333333',
    zorder=7
)

# 下移底部说明文本
ax.text(
    0, -8.0,  # 进一步下移底部文本
    "TGI: 衡量关注度,高于100代表该用户群的关注度高于平均水平。\n"
    "圆圈面积与 TGI 值成正比", 
    ha='center', 
    va='center', 
    fontsize=12, 
    color='#666666',
    zorder=8
)

# 绘制三条分隔线
draw_separator(y_pos=3.0)  # 分隔标题和性别组
draw_separator(y_pos=-0.5)  # 分隔性别组和年龄组
draw_separator(y_pos=-6.4)  # 分隔年龄组和底部注释

# 设置坐标轴范围
ax.set_xlim(-3, 3)
ax.set_ylim(-9, 4.5)  # 扩大Y轴范围以容纳所有内容
ax.axis('off')  # 隐藏坐标轴

# 调整布局
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.25)
plt.show()