# Chart 3: Redraw the horizontal bar chart and optimize the color scheme and label visualization

import matplotlib.pyplot as plt

factors = [
    "Comfortable to wear, no tightness or restraint",
    "Shape the hips and enhance the contour",
    "High - quality fabric, soft and skin - friendly",
    "High elasticity, high inclusiveness",
    "Micro - pressure shaping, slimming and fitting"
]
percentages = [38, 33, 32, 30, 28]

colors = ['#ec407a', '#f06292', '#f48fb1', '#f8bbd0', '#fce4ec']  # Gradient pink

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(factors, percentages, color=colors, edgecolor='gray')

# Add numerical labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', fontsize=10)

# Title and beautification
ax.set_title("Top 5 factors influencing shark leggings purchases", fontsize=14)
ax.invert_yaxis()  # The highest is on the top
ax.set_xlim(0, 45)
ax.set_xlabel("Percentage (%)")
plt.tight_layout()
plt.show()