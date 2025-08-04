import matplotlib.pyplot as plt
import numpy as np

# 零食类别
categories = ['甜饮料', '耐啃零食', '油炸膨化食品', '酸奶', '烘焙食品', '坚果', '辣味零食', '高糖食品', '果干蜜饯']
# 对应选择比例
percentages = [55, 43, 43, 42, 42, 39, 38, 36, 33]

# 创建画布和子图，调整大小
fig, ax = plt.subplots(figsize=(12, 6))

# 设置渐变色
cmap = plt.cm.get_cmap('viridis', len(categories))
colors = [cmap(i) for i in range(len(categories))]

# 绘制柱状图，添加透明度和边框
rects = ax.bar(categories, percentages, color=colors, alpha=0.8, edgecolor='black', linewidth=0.8)

# 添加标题和坐标轴标签，设置字体大小
ax.set_title('朋克加班人上班嘴馋时的零食选择分布', fontsize=16, pad=15)
ax.set_ylabel('选择比例（%）', fontsize=14, labelpad=10)

# 设置y轴范围
ax.set_ylim(0, max(percentages) * 1.1)

# 设置网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 在柱子上标注数值，调整位置和样式
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5),  # 垂直偏移量
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# 美化图表边框
for spine in ax.spines.values():
    spine.set_linewidth(0.5)

# 旋转x轴标签，使其更易读
plt.xticks(rotation=30, ha='right', fontsize=11)

# 调整布局
plt.tight_layout()

plt.show()