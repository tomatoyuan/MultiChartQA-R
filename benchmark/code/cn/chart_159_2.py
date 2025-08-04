import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['图片', '视频', '轮播', 'Reels']
counts = [17, 11, 36, 644]
colors = ['#3C9B8E', '#7E55C2', '#F3B63A', '#DA3B9C']

# 计算百分比
total = sum(counts)
percentages = [count / total for count in counts]
label_texts = [f"{label} {count} ({p:.1%})" for label, count, p in zip(labels, counts, percentages)]

# 绘图
fig, ax = plt.subplots(figsize=(9, 4.5))

# 环形图
wedges, texts = ax.pie(
    counts,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3)
)

# 添加数值标注在图中扇区内
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = 0.7 * np.cos(np.deg2rad(angle))
    y = 0.7 * np.sin(np.deg2rad(angle))
    ax.text(x, y, f"{counts[i]}\n({percentages[i]:.1%})",
            ha='center', va='center', fontsize=10, color='black')

# 图例放右侧
ax.legend(
    wedges,
    label_texts,
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=12
)

# 添加说明文字
description = (
    "通过 OneSight 营销云后台数据，我们\n"
    "发现 Insta360 的 Instagram 全球主页\n"
    "在 2023 年发布的内容中，Reels 视频\n"
    "占据了 90%以上。"
)
plt.text(-1.8, 0.2, description, fontsize=13, va='top')

# 美化图形
plt.axis('equal')  # 保证圆形
plt.tight_layout()
plt.show()