import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Frequent pressure to get married", "Eight blind dates in one day during Spring Festival", "Often rush to blind dates"]
sizes = [70, 54.7, 30]
x = np.arange(len(labels))  # x-axis positions

# Create a figure and a subplot, set the size
fig, ax = plt.subplots(figsize=(10, 6))

# Create a gradient color list
colors = plt.cm.RdPu(np.linspace(0.6, 0.9, len(sizes)))  # Use the gradient colors from the RdPu color palette

# Draw a bar chart with shadow and edges
rects = ax.bar(
    x, 
    sizes, 
    width=0.6, 
    color=colors, 
    edgecolor='black', 
    linewidth=1.2,
    alpha=0.8,
    zorder=3  # Ensure the bar chart is displayed above the grid lines
)

# Set x-axis ticks and labels, increase the rotation angle and font size
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=12)

# Add numerical labels, increase the font size and add a background box
for rect in rects:
    height = rect.get_height()
    ax.annotate(
        f"{height}%", 
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 5),  # Offset 5 points upwards
        textcoords="offset points",
        ha="center", 
        va="bottom",
        fontsize=12,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7)
    )

# Add a title and a y-axis label, increase the font size and style
ax.set_ylabel("Percentage (%)", fontsize=14)
ax.set_title("Survey data on the marriage and love pressure of single men and women interviewed", fontsize=16, fontweight='bold', pad=20)

# Add grid lines, set the transparency
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)  # Set the grid lines at the bottom layer

# Set the y-axis range
ax.set_ylim(0, max(sizes) * 1.1)  # Slightly expand the y-axis range

# Add a legend
ax.legend([rects[0]], ["Percentage data"], loc='upper right')

# Add a background color
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f1f3f5')

# Adjust the layout
plt.tight_layout()

# Save the chart (optional)
# plt.savefig('dating_pressure_chart.png', dpi=300, bbox_inches='tight')

# Display the chart
plt.show()