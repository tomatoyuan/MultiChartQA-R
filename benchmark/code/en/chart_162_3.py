import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Raw material \npurchase cost', 'Labor cost', 'Three - item expenses',
          'Rent and property \nmanagement cost', 'Energy cost', 'Taxes and fees']
sizes = [42.7, 21.9, 20.1, 8.8, 3.6, 2.9]
colors = ['#E73331', '#233B7B', '#999999', '#F5B92E', '#4BA2C8', '#892D2D']

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

# Draw pie chart
wedges, _ = ax.pie(
    sizes,
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=1.0)
)

# Annotate with dynamic offset to avoid overlap
total = sum(sizes)
small_indices = [i for i, val in enumerate(sizes) if val < 5]

for i, (wedge, label, size) in enumerate(zip(wedges, labels, sizes)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    angle_rad = np.deg2rad(angle)
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    # 外部文字位置
    label_x = 1.35 * x
    label_y = 1.35 * y

    # 为小扇区调整y坐标偏移
    if i in small_indices:
        label_y += (0.2 if i % 2 == 0 else -0.2)  # 上下错开

    ha = 'left' if x >= 0 else 'right'

    ax.annotate(
        f"{label}\n{size:.1f}%",
        xy=(1.0 * x, 1.0 * y),
        xytext=(label_x, label_y),
        ha=ha, va='center',
        fontsize=11,
        arrowprops=dict(arrowstyle='-', color='gray', lw=1),
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='gray', alpha=0.6)
    )

# Title
ax.set_title("Cost proportion of sample catering enterprises in China in 2023", fontsize=15, weight='bold', pad=60)
plt.tight_layout()
plt.show()