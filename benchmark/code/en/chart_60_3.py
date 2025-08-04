import matplotlib.pyplot as plt
import numpy as np

# Data definition
categories = ["Replacement Cycle"]
labels = ["Less than 1 year", "1 - 2 years", "2 - 3 years", "3 - 5 years", "More than 5 years"]
sizes = [5.7, 41.4, 39.3, 11.1, 2.6]  # Proportion (%)
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # Color configuration

# Create a canvas: increase the height and decrease the width to make the chart taller and thinner
fig, ax = plt.subplots(figsize=(6, 5))  # Adjust to width 6 and height 5

# Draw a segmented bar chart (remove the incorrect height parameter)
start = 0
for i in range(len(sizes)):
    ax.bar(
        categories, 
        sizes[i], 
        bottom=start, 
        color=colors[i], 
        edgecolor="white",
        linewidth=1,
        label=labels[i]
    )
    # Add data labels
    ax.text(
        categories[0], 
        start + sizes[i]/2, 
        f"{sizes[i]}%",
        ha="center", 
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )
    start += sizes[i]

# Hide the y-axis (only keep the x-axis categories)
ax.set_yticks([])

# Hide the top, right, and left borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Set x-axis labels
ax.set_xticklabels(categories, fontsize=10, color="#424242")

# Add a legend (adjust the position to the bottom and arrange it horizontally)
ax.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.25),  # Fine-tune the legend position
    ncol=len(labels),            # Arrange horizontally
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Add a title
ax.set_title(
    "Replacement Cycle of Framed Eyeglasses",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout (make room for the legend)
plt.subplots_adjust(bottom=0.25)

plt.show()