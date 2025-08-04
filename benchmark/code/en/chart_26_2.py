import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# Data
labels = ["Opposite - sex with undetermined relationship", "Girlfriend", "Wife"]
values = [1348, 621, 266]
total = sum(values)
percentages = [f"{v/total*100:.1f}%" for v in values]

# Set colors closer to the original image
colors = ["#FF85A2", "#FFB3C1", "#FFD1DC"]  # Soft pink color scheme
edge_color = "#FF4D6D"  # Border color

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart, add border and shadow effects
rects = ax.bar(
    labels, values, 
    color=colors, 
    edgecolor=edge_color, 
    linewidth=2, 
    width=0.6,
    alpha=0.9,
    zorder=3  # Ensure the bars are displayed above the grid
)

# Add grid lines to make it clearer
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

# Add values and percentages above the bars
for i, rect in enumerate(rects):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width()/2., height + 10,
        f"{values[i]}\n({percentages[i]})",
        ha='center', va='bottom',
        fontsize=12, fontweight='bold'
    )

# Set the title and axis labels
ax.set_title("Proportion of male gift - giving objects", fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel("Quantity", fontsize=14, labelpad=10)

# Adjust the y - axis range to make the chart more beautiful
ax.set_ylim(0, max(values) * 1.1)

# Set the axis ticks and styles
ax.tick_params(axis='both', which='major', labelsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Add background color
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#ffffff')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()