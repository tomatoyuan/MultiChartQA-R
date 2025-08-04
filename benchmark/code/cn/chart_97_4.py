import matplotlib.pyplot as plt
import numpy as np

# 观看比赛原因（模拟数据，贴近原图逻辑）
reasons = [
    "为自己喜欢的球队/球星加油", "长期观看，已经成为习惯",
    "欣赏高水平的团队配合", "能够带来娱乐和激情",
    "欣赏球星高超的足球技术", "感受拼搏、奋斗的精神",
    "体验紧张/刺激感", "学习足球技巧",
    "想要释放压力", "可以和周围的人有共同话题",
    "主播/解说很有趣", "打发时间",
    "陪朋友/家人观看"
]
# 模拟占比（可调整，保留趋势）
percentages = [81.1, 63.5, 58.9, 56.2, 
               55.3, 44.7, 37.1, 24.9, 
               23.5, 19.6, 10.2, 9.5, 3.7]

# 自由配色（避免绿色，用蓝色系+橙色系组合）
bar_colors = ["#4169E1", "#1E90FF", "#87CEFA", "#ADD8E6", 
              "#FFA07A", "#FF8C00", "#FF6347", "#FF4500", 
              "#FFD700", "#FFC107", "#DAA520", "#B8860B", "#8B4513"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 7))  # 高度适配长列表

# 绘制横向柱状图
y = np.arange(len(reasons))
bars = ax.barh(y, percentages, color=bar_colors, height=0.6)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(
        f'{width}%', 
        xy=(width, bar.get_y() + bar.get_height()/2),
        xytext=(5, 0),  # 右侧偏移 5px
        textcoords="offset points",
        ha='left', va='center',
        fontsize=8,
        color='black'
    )

# 配置坐标轴与标题
ax.set_yticks(y)
ax.set_yticklabels(reasons, fontsize=9)  # 缩小字体避免拥挤
ax.set_title("2022年中国足球球迷观看比赛原因", fontsize=14, fontweight="bold", y=1.02)

# 美化：隐藏边框 + 横向网格
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.3)  # 增加辅助网格

plt.tight_layout()  # 自动优化布局
plt.show()