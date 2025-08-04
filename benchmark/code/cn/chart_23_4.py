import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["对催婚不予理会", "其他态度"]
sizes = [50, 50]
colors = ["#FF6B6B", "#4ECDC4"]  # 使用更现代的配色方案
explode = (0.05, 0)  # 突出显示第一部分

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# 绘制环形图
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)}人)' if p > 0 else '',
    startangle=90,
    colors=colors,
    wedgeprops={"width": 0.4, "edgecolor": "w", "linewidth": 2},
    textprops={"fontsize": 12, "color": "#333333"},
)

# 设置标题
ax.set_title("受访者面对催婚的态度分布", fontsize=16, fontweight="bold", pad=20)

# 调整图例
ax.legend(wedges, labels, title="态度类型", loc="center left", bbox_to_anchor=(1, 0.3, 0.5, 1))

# 添加数据标签样式
for autotext in autotexts:
    autotext.set_fontweight("bold")

# 背景和网格设置
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 设置坐标轴比例
plt.axis('equal')

# 添加注释说明
plt.figtext(0.5, 0.01, "数据来源：虚构示例", ha="center", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# 调整布局
plt.tight_layout()

# 保存图表（可选）
# plt.savefig('marriage_pressure_attitude.png', bbox_inches='tight', dpi=300)

# 显示图表
plt.show()