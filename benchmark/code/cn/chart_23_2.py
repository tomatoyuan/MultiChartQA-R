import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["频繁被催婚", "春节一天相亲8次", "常赶场相亲"]
sizes = [70, 54.7, 30]
x = np.arange(len(labels))  # x轴位置

# 创建画布和子图，设置尺寸
fig, ax = plt.subplots(figsize=(10, 6))

# 创建渐变色列表
colors = plt.cm.RdPu(np.linspace(0.6, 0.9, len(sizes)))  # 使用RdPu色板的渐变色

# 绘制带阴影和边缘的柱状图
rects = ax.bar(
    x, 
    sizes, 
    width=0.6, 
    color=colors, 
    edgecolor='black', 
    linewidth=1.2,
    alpha=0.8,
    zorder=3  # 确保柱状图显示在网格线之上
)

# 设置x轴刻度与标签，增加旋转角度和字体大小
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=12)

# 添加数值标签，增加字体大小和背景框
for rect in rects:
    height = rect.get_height()
    ax.annotate(
        f"{height}%", 
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 5),  # 向上偏移5个点
        textcoords="offset points",
        ha="center", 
        va="bottom",
        fontsize=12,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7)
    )

# 添加标题与y轴标签，增加字体大小和样式
ax.set_ylabel("占比（%）", fontsize=14)
ax.set_title("受访单身男女婚恋压力调查数据", fontsize=16, fontweight='bold', pad=20)

# 添加网格线，设置透明度
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)  # 设置网格线在底层

# 设置y轴范围
ax.set_ylim(0, max(sizes) * 1.1)  # 稍微扩展y轴范围

# 添加图例
ax.legend([rects[0]], ["占比数据"], loc='upper right')

# 添加背景色
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f1f3f5')

# 调整布局
plt.tight_layout()

# 保存图表（可选）
# plt.savefig('dating_pressure_chart.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()