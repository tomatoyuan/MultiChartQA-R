import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 数据
labels = ["未确定关系的异性", "女朋友", "妻子"]
values = [1348, 621, 266]
total = sum(values)
percentages = [f"{v/total*100:.1f}%" for v in values]

# 设置更接近原图的颜色
colors = ["#FF85A2", "#FFB3C1", "#FFD1DC"]  # 柔和粉色系
edge_color = "#FF4D6D"  # 边框颜色

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图，添加边框和阴影效果
rects = ax.bar(
    labels, values, 
    color=colors, 
    edgecolor=edge_color, 
    linewidth=2, 
    width=0.6,
    alpha=0.9,
    zorder=3  # 确保柱子显示在网格上方
)

# 添加网格线，使其更清晰
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

# 在柱子上方添加数值和百分比
for i, rect in enumerate(rects):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width()/2., height + 10,
        f"{values[i]}\n({percentages[i]})",
        ha='center', va='bottom',
        fontsize=12, fontweight='bold'
    )

# 设置标题和轴标签
ax.set_title("男性送礼对象比例", fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel("数量", fontsize=14, labelpad=10)

# 调整y轴范围，使图表更美观
ax.set_ylim(0, max(values) * 1.1)

# 设置坐标轴刻度和样式
ax.tick_params(axis='both', which='major', labelsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# 添加背景色
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#ffffff')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()