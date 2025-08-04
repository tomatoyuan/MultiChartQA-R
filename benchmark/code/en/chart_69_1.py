import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Project names
items = ["Education", "Healthcare", "Large - value goods", "Social culture and entertainment", "Home purchase", "Travel", "Insurance"]
# Corresponding data (proportion)
data = [28.1, 27.4, 18.7, 18.1, 16.9, 15.2, 13.9]
# Color settings, blue for travel, green for the rest, similar to the original image
colors = ["#A4C639"] * len(items)
colors[items.index("Travel")] = "#64B5F6"

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(items))
bar_height = 0.6
max_data = max(data)
for i in range(len(items)):
    # Draw the background bar (green border effect)
    rect = Rectangle((0, y[i] - bar_height / 2), max_data, bar_height, facecolor="white", edgecolor="#A4C639", linewidth=1.5)
    ax.add_patch(rect)
    # Draw the foreground bar
    bar = ax.barh(y[i], data[i], height=bar_height, color=colors[i], edgecolor="white", label=items[i])
    # Add data labels
    ax.annotate(f'{data[i]}%',
                xy=(data[i], y[i]),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center',
                fontweight='bold')

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(items)
# Hide the x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Projects to increase spending in the next three months", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()