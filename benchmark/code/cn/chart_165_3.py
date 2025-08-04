import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['复合预制菜/菜谱式调料', '基础调味品', '复合非预制菜调料', '地域特色/特产类调味品']
inner_data = [38, 35, 27, 0]  # 2023 Q1
outer_data = [38, 33, 29, 0]  # 2024 Q1

colors = ['#1f4e79', '#2ca197', '#f6a965', '#d1d1e0']

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')

# 内圈：2023 Q1
inner_wedges, _ = ax.pie(
    inner_data,
    radius=0.7,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# 外圈：2024 Q1
outer_wedges, _ = ax.pie(
    outer_data,
    radius=1.0,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# 添加百分比标签
def add_labels(wedges, data, radius):
    angle = 90
    total = sum(data)
    for i, (wedge, value) in enumerate(zip(wedges, data)):
        if value == 0:
            continue
        theta = (angle - value / total * 360 / 2) * np.pi / 180
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        ax.text(x, y, f'{value}%', ha='center', va='center', fontsize=10)
        angle -= value / total * 360

add_labels(inner_wedges, inner_data, radius=0.55)
add_labels(outer_wedges, outer_data, radius=1.15)

# 添加图例
plt.legend(outer_wedges, labels, title="品类", loc="center left", bbox_to_anchor=(1, 0.5))

# 添加标题
plt.title('2024年Q1调味品市场各品类销售趋势\n内圈：2024年Q1 | 外圈：2023年Q1')

# 添加数据来源说明
plt.figtext(
    0.1, 0.1,
    "数据来源：魔镜洞察，《2024中国调味品行业发展趋势》\n"
    "数据说明：调味品市场指天猫淘宝、京东、抖音三大平台粮油调味/速食/干货/烘焙 > 调味品/果酱/沙拉/干副食类目商品",
    ha='left', fontsize=9
)

plt.tight_layout()
plt.show()