import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2022.07", "2023.07", "2024.07"]
values = [86.7, 89.4, 92.0]

# Initialize the canvas
fig, ax = plt.subplots(figsize=(6, 1.5))  # Narrow canvas to simulate timeline layout

# Draw a horizontal line (timeline)
ax.axhline(y=0.5, color='#83B48A', linewidth=2, zorder=1)

# Draw green boxes with values
for i, (year, val) in enumerate(zip(years, values)):
    # Draw a green rectangle
    rect = plt.Rectangle((i - 0.2, 0.2), 0.4, 0.6,
                         facecolor='#C9EBD9', edgecolor='#83B48A',
                         linewidth=2, zorder=2)
    ax.add_patch(rect)
    # Label the value
    ax.text(i, 0.5, f"{val}", fontsize=12,
            ha='center', va='center', color='#333333')
    # Label the year
    ax.text(i, -0.3, year, fontsize=10,
            ha='center', va='top', color='#666666')

# Hide the axes
ax.set_xlim(-0.5, len(years)-0.5)
ax.set_ylim(-0.5, 1.2)
ax.axis('off')

# Add a title
plt.title("Consumer Confidence Index - Consumption Willingness", fontsize=14, fontweight='bold', y=1.3)

plt.tight_layout()
plt.show()