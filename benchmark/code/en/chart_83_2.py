import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# -------------------- Data Definition --------------------
years = ["2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e"]
market_size = [667, 817, 1011, 1266, 1618, 2079, 2686]
x = np.arange(len(years))
bar_width = 0.3

# -------------------- Color Scheme (Gradient + Cute Style) --------------------
colors = ['#A5D6A7', '#81C784', '#4DD0E1', '#4FC3F7', '#9575CD', '#BA68C8', '#F48FB1']

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# Set appropriate y-axis range to avoid bars being too tall and bursting the image
max_height = max(market_size)
ax.set_ylim(0, max_height * 1.15)  # 115% of the maximum value

# -------------------- Draw Rounded Rectangular Bars --------------------
for i in range(len(x)):
    bar_height = market_size[i]
    bar_color = colors[i % len(colors)]
    # Use FancyBboxPatch to draw a rounded rectangle (bar)
    rect = FancyBboxPatch(
        (x[i] - bar_width / 2, 0),     # Bottom left corner
        bar_width, bar_height,         # Width and height
        boxstyle="round,pad=0.02,rounding_size=6",  # Rounded corner configuration
        linewidth=0,
        facecolor=bar_color,
        edgecolor=None
    )
    ax.add_patch(rect)

    # Add data labels
    ax.text(
        x[i], bar_height + 50,
        f"{bar_height}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=bar_color
    )

# -------------------- Axes and Decoration --------------------
# Set x-axis
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
# Set y-axis label
ax.set_ylabel("Market Size and Space of China's \nRehabilitation Medical Services (Billion Yuan)", fontsize=11)

# Add CAGR label (top left corner)
ax.text(
    0.05, 0.93,
    "CAGR = 38.5%",
    transform=ax.transAxes,
    fontsize=12,
    fontweight="bold",
    color="#F06292",
    bbox=dict(facecolor="#ffe0f0", alpha=0.6, boxstyle="round,pad=0.3", edgecolor='none')
)

# Add title
ax.set_title("Market Size and Space of China's Rehabilitation Medical Services from 2019 - 2025", fontsize=14, fontweight="bold", pad=20)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Automatic layout
plt.tight_layout()
plt.show()