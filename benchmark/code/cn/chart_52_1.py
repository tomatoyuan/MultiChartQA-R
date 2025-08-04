import matplotlib.pyplot as plt
import numpy as np

# 数据定义
items = [
    {"name": "学习专业课程", "rate": 69.3, "color": "#a8e6cf"},
    {"name": "完成毕业论文", "rate": 64.0, "color": "#dcedc1"},
    {"name": "积累实习经验", "rate": 51.1, "color": "#ffd3b6"},
    {"name": "校外考试", "rate": 50.8, "color": "#c8e6c9"},
    {"name": "校园实践", "rate": 42.5, "color": "#e8eaf6"},
]

# 路径节点坐标
node_coords = [
    (0.1, 0.8),   # 学习专业课程
    (0.3, 0.65),  # 完成毕业论文
    (0.5, 0.5),   # 积累实习经验
    (0.7, 0.6),   # 校外考试
    (0.9, 0.3),   # 校园实践
]

# 连线顺序
connections = [(0,1), (1,2), (2,3), (3,4)]

fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 绘制连线
for start, end in connections:
    x1, y1 = node_coords[start]
    x2, y2 = node_coords[end]
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle='--', linewidth=1.5)

# 绘制气泡和文本
for i, item in enumerate(items):
    x, y = node_coords[i]
    
    # 绘制气泡
    bubble = plt.Circle((x+0.05, y), 0.05, color=item["color"], zorder=2)
    ax.add_artist(bubble)
    
    # 绘制文本
    text = f"{item['rate']}%\n{item['name']}"
    ax.text(x+0.12, y, text, 
            ha='left', va='center', 
            fontsize=10, color='black')

# 标题
ax.text(0.5, 0.92, "大学阶段最重要的事情TOP5", 
        ha='center', va='center', 
        fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()