import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# ======================== 1. 数据与基础配置 ========================
labels = ["三聚氰胺", "室内装修", "护肤品", "饮酒", "海娜粉", "大气污染"]
sizes = [33, 10, 8, 8, 8, 7]

# 六边形环形分布坐标（极坐标转直角坐标）
theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
radius = 1.2  # 控制六边形环半径
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# 自定义渐变色盘（从浅粉到深粉）
cmap = LinearSegmentedColormap.from_list(
    'pink_cmap', 
    ['#FFE6F0', '#FFABCD', '#E66493', '#CC3377', '#B30059', '#8B003C'],
    N=len(labels)
)

# ======================== 2. 初始化画布与轴 ========================
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#F8F8FF')  # 浅蓝背景
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # 隐藏坐标轴

# ======================== 3. 绘制立体六边形（带阴影+渐变） ========================
for i in range(len(labels)):
    # 主六边形（渐变填充）
    hex_main = RegularPolygon(
        (x[i], y[i]), numVertices=6, radius=0.5, 
        facecolor=cmap(i), edgecolor='white', linewidth=2
    )
    ax.add_patch(hex_main)
    
    # 阴影六边形（模拟立体效果）
    hex_shadow = RegularPolygon(
        (x[i] + 0.05, y[i] - 0.05), numVertices=6, radius=0.5, 
        facecolor='gray', alpha=0.2, edgecolor='none'
    )
    ax.add_patch(hex_shadow)
    
    # 绘制占比数字（居中，加粗）
    ax.text(
        x[i], y[i], f"{sizes[i]}%", 
        ha='center', va='center', 
        fontsize=14, fontweight='bold', 
        color='white'
    )
    
    # 绘制标签文字（环绕布局，调整角度）
    text_angle = np.rad2deg(theta[i]) - 90  # 文字角度适配六边形
    ax.text(
        x[i] * 1.8, y[i] * 1.8, labels[i], 
        ha='center', va='center', 
        fontsize=12, color='#333333', 
        rotation=text_angle
    )

# ======================== 4. 添加标题与装饰 ========================
# 中心标题
ax.text(
    0, 0, "致癌原因占比", 
    ha='center', va='center', 
    fontsize=20, fontweight='bold', 
    color='#CC3377'
)

# 底部说明
ax.text(
    0, -2.2, "数据来源：模拟统计 | 单位：%", 
    ha='center', va='center', 
    fontsize=10, color='#666666', 
)

# 渐变背景（从中心向外扩散）
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient_img = np.tile(gradient, (256, 1))
ax.imshow(
    gradient_img, extent=(-2.5, 2.5, -2.5, 2.5), 
    cmap=cm.get_cmap('Blues_r'), alpha=0.3
)

plt.tight_layout()
plt.show()