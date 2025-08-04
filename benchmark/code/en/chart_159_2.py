import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Photos', 'Videos', 'Carousels', 'Reels']
counts = [17, 11, 36, 644]
colors = ['#3C9B8E', '#7E55C2', '#F3B63A', '#DA3B9C']

# Percentages & label text
total = sum(counts)
percentages = [count / total for count in counts]
label_texts = [f"{label} {count} ({p:.1%})" for label, count, p in zip(labels, counts, percentages)]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Donut chart
wedges, _ = ax.pie(
    counts,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=1)
)

# Place external annotations with lines
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    angle_rad = np.deg2rad(angle)
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    # 外侧注释位置
    x_text = 1.2 * x
    y_text = 1.5 * y
    alignment = 'left' if x >= 0 else 'right'

    ax.annotate(
        f"{counts[i]} ({percentages[i]:.1%})",
        xy=(0.5 * x,  0.7*y),             # 箭头起点（扇区内）
        xytext=(x_text, y_text),           # 文字位置
        ha=alignment, va='center',
        fontsize=10, color='black',
        rotation=-30,
        arrowprops=dict(arrowstyle="-", color='gray', lw=1)
    )

# 图例放右侧
ax.legend(
    wedges,
    label_texts,
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=12
)

# 描述文字
description = (
    "Through the OneSight Marketing Cloud backend data,\nwe "
    "found that in the content published \non Insta360's global "
    "Instagram page in 2023, \nReels videos accounted for "
    "over 90%."
)
plt.text(-1.8, 0.2, description, fontsize=13, va='top')

ax.set_aspect('equal')
plt.tight_layout()
plt.show()