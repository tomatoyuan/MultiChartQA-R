import matplotlib.pyplot as plt
import numpy as np

# 企业规模类别及占比数据
labels = ["小型企业", "中型企业", "微型企业", "大型企业"]
sizes = [60.47, 25.64, 10.47, 3.42]
# 对应颜色
colors = ['blue', 'green', 'orange', 'purple']
# 各类别描述信息（用于标注）
descriptions = [
    "小型企业（员工人数20≤X<300人或营业收入300≤Y<2000万元）",
    "中型企业（员工人数300≤X<1000人或营业收入2000≤Y<40000万元）",
    "微型企业（员工人数<20人或营业收入<300万元）",
    "大型企业（员工人数X≥1000人或营业收入Y≥40000万元）"
]

# 构建漏斗图的多边形顶点坐标（大致模拟，可按需微调）
# 假设漏斗在水平方向对称，基于垂直方向分层
y_positions = [0.8, 0.6, 0.4, 0.2]  # 各层垂直位置
widths = [1, 0.6, 0.3, 0.1]  # 各层宽度，从大到小模拟漏斗
vertices_list = []
for y, w in zip(y_positions, widths):
    left = -w / 2
    right = w / 2
    vertices = [(left, y), (right, y), (right, y - 0.1), (left, y - 0.1)]
    vertices_list.append(vertices)

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(vertices_list)):
    # 绘制每个层级的多边形（漏斗分层）
    polygon = plt.Polygon(vertices_list[i], color=colors[i])
    ax.add_patch(polygon)
    # 添加占比和描述标注，位置在层级中间
    center_x = 0
    center_y = y_positions[i] - 0.05
    ax.text(center_x, center_y, f'{labels[i]}\n{descriptions[i]}\n占比：{sizes[i]}%',
            ha='center', va='center', fontsize=9)

ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, 1)
ax.axis('off')  # 隐藏坐标轴
ax.set_title('2025年中国数字化转型企业的规模情况')

plt.tight_layout()
plt.show()