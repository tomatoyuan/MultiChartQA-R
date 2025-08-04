import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = [
    "时间不够用",
    "精力体力跟不上",
    "孩子学习困难",
    "课后辅导太复杂",
    "行为管理问题",
    "健康问题",
    "家庭教育方式难选"
]
values = [47, 40, 39, 38, 31, 28, 21]

# 设置颜色（红色系列渐变）
colors = [
    "#FF4C4C", "#FF6666", "#FF8080", "#FF9999", "#FFB3B3", "#FFCCCC", "#FFE5E5"
]

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels, values, color=colors)

# 添加数据标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center')

# 图表美化
ax.invert_yaxis()
ax.set_xlim(0, 55)
ax.set_xlabel("占比（%）")
ax.set_title("家长在孩子家庭教育上遇到的困难和烦恼", fontsize=14)

plt.tight_layout()
plt.show()