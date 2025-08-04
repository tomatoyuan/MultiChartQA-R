import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
import numpy as np

# Data
sizes = [88.08, 11.69, 0.18, 0.05]
labels = ["Video Proportion", "Image - Text Proportion", "Mini - Program Proportion", "Atlas Proportion"]

# Custom color scheme
colors = [
    ["#1976d2", "#e3f2fd"],  # Video Proportion: Dark blue and light blue
    ["#f57c00", "#ffebee"],  # Image - Text Proportion: Orange and light orange
    ["#388e3c", "#e8f5e9"],  # Mini - Program Proportion: Green and light green
    ["#7b1fa2", "#f3e5f5"]   # Atlas Proportion: Purple and light purple
]

# Create a 3D effect
fig = plt.figure(figsize=(20, 10))
fig.subplots_adjust(top=0.85, bottom=0.15, wspace=0.3)

# Create 4 sub - plots
axes = []
for i in range(4):
    ax = fig.add_subplot(1, 4, i + 1, aspect='equal')
    axes.append(ax)

# Draw 3D pie charts
for i, ax in enumerate(axes):
    # Set colors
    chart_colors = [colors[i][0], colors[i][1]]

    # Calculate angles
    theta1 = 0
    theta2 = 360 * sizes[i] / 100

    # Create a 3D effect - Draw multi - layer sectors
    for height in [0, 0.1, 0.2]:
        if sizes[i] < 5:  # Thicken and highlight small values
            height_factor = 0.3
        else:
            height_factor = 0.1

        # Main sector
        wedge = Wedge((0, 0), 1, theta1, theta2, width=0.2,
                      facecolor=chart_colors[0], edgecolor='w', linewidth=1)
        ax.add_patch(wedge)

        # Bottom sector (light - colored part)
        wedge_bottom = Wedge((0, 0), 1, theta2, 360, width=0.2,
                             facecolor=chart_colors[1], edgecolor='w', linewidth=1)
        ax.add_patch(wedge_bottom)

        # Add 3D edge effect
        if height > 0:
            edge = Wedge((0, 0), 1, theta1, theta2, width=0.2,
                         facecolor=chart_colors[0], alpha=0.3)
            ax.add_patch(edge)

    # Set the title
    ax.set_title(labels[i], fontsize=18, pad=20)

    # Add percentage labels
    if sizes[i] >= 0.01:  # Only show labels greater than 0.1%
        angle = theta1 + (theta2 - theta1) / 2
        x = 0.6 * np.cos(np.deg2rad(angle))
        y = 0.6 * np.sin(np.deg2rad(angle))
        ax.text(x, y, f"{sizes[i]:.2f}%",
                ha='center', va='center', fontsize=12)

    # Set the coordinate range
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

# Set the main title
fig.suptitle("Attention Channels of Medical Aesthetics Industry News in May", fontsize=28, fontweight='bold', y=0.85)

plt.tight_layout()
plt.show()