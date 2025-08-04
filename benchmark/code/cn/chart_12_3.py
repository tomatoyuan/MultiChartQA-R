import matplotlib.pyplot as plt
import numpy as np

# 数据
foods = ["小龙虾", "烧烤", "黑鸭", "啤酒", "可乐", "毛豆", "爆米花", "烤肉"]
values = [2264, 1030, 827, 804, 521, 462, 442, 352]

# 创建画布和子图（设置更大尺寸和分辨率）
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# 设置渐变色（从深蓝色到浅蓝色）
colors = plt.cm.Blues(np.linspace(0.6, 0.95, len(foods)))

# 绘制带圆角的柱状图（通过edgecolor和linewidth设置边框）
bars = ax.bar(
    x=np.arange(len(foods)),
    height=values,
    width=0.65,
    color=colors,
    edgecolor='black',
    linewidth=0.8,
    capstyle='round'
)

# 在柱状图上方添加数值标签
for bar, value in zip(bars, values):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height + 30,  # 标签位置略高于柱子顶部
        f'{value}',
        ha='center', 
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# 设置x轴刻度标签（旋转45度增强可读性）
ax.set_xticks(np.arange(len(foods)))
ax.set_xticklabels(foods, rotation=30, ha='right', fontsize=11)

# 添加标题和坐标轴标签（增加字体大小和粗细）
ax.set_title('欧洲杯期间美食关注度', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('美食类型', fontsize=13, labelpad=10)
ax.set_ylabel('关注度数值', fontsize=13, labelpad=10)

# 设置y轴范围（留出顶部空间）
ax.set_ylim(0, max(values) * 1.1)

# 添加网格线增强可读性
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 美化图表边框
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(0.5)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()