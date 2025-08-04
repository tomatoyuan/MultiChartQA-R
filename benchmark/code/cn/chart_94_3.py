import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# 简化后的标签（用于图例）
short_labels = [
    "进程缓慢", "设备不匹配", 
    "需求沟通差", "缺一条龙服务", 
    "设计不满意", "无人安装调试", 
    "监管缺失", "供应商不专业"
]

# 原始数据
percentages = np.array([43.6, 33.1, 27.8, 27.1, 25.6, 19.5, 15.0, 6.8])
dashed_box_indices = [0, 1]

# 极坐标角度
N = len(short_labels)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# 颜色渐变设置
norm = mcolors.Normalize(vmin=min(percentages), vmax=max(percentages))
cmap = cm.get_cmap("YlGnBu")
colors = [cmap(norm(p)) for p in percentages]

# 创建图形和极坐标子图
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw={'projection': 'polar'})

# 绘制雷达柱图
bars = ax.bar(
    angles,
    percentages,
    width=2 * np.pi / N * 0.9,
    color=colors,
    edgecolor='white',
    linewidth=1
)

# 高亮前两项
for i in dashed_box_indices:
    bars[i].set_edgecolor('deepskyblue')
    bars[i].set_linewidth(2.5)
    bars[i].set_alpha(1.0)

# 添加数据标注
for angle, bar, label, percent in zip(angles, bars, difficulties, percentages):
    rotation = np.rad2deg(angle)
    alignment = 'left' if np.pi/2 < angle < 3*np.pi/2 else 'right'
    ax.text(
        angle,
        bar.get_height() + 3,
        f"{percent}%",
        ha='center',
        va='center',
        fontsize=9,
        color="#333"
    )

# 设置图例（每个颜色+类别）
for i in range(N):
    ax.bar(0, 0, color=colors[i], label=short_labels[i])

# 设置雷达图属性
ax.set_ylim(0, 50)
ax.set_yticklabels([])
ax.set_xticks([])  # 不显示极坐标刻度
ax.spines['polar'].set_visible(False)

# 添加图例
ax.legend(
    loc='center left',
    bbox_to_anchor=(1.1, 0.5),
    fontsize=10,
    title='难点分类',
    frameon=True
)

# 添加标题
ax.set_title(
    "餐饮企业开店遇到的难点",
    fontsize=14,
    fontweight="bold",
    pad=30
)

plt.tight_layout()
plt.show()