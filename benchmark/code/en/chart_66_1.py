import matplotlib.pyplot as plt
import numpy as np

# Category text
labels = ["Regular daily supplementation required", "Periodic supplementation is sufficient, e.g., in infancy, old age, or pregnancy", "Supplementation only needed when sick or symptomatic"]
# Corresponding data
sizes = [51, 17, 16]
# Colors for different categories, trying to be a gradient in the green - like color scheme similar to the original image
colors = ["#A4C639", "#A4C639", "#6E8B3D"]

x = np.arange(len(labels))  # Used to set the x - axis position
bar_width = 0.5  # Width of the bar chart

fig, ax = plt.subplots()
# Draw the bar chart. A horizontal bar chart is closer to the display form of the original image, so use barh
bars = ax.barh(x, sizes, height=bar_width, color=colors, edgecolor="white")

# Add data labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Horizontal distance of the label from the bar chart
                textcoords="offset points",
                ha='left', va='center')

# Set the y - axis ticks and labels to make the labels clearer
ax.set_yticks(x)
ax.set_yticklabels(labels)
# Set the chart title
ax.set_title("Top 3 Pet Health Supplement Awareness", fontsize=14, fontweight="bold")

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# Adjust the x - axis range to make the labels display more appropriately
ax.set_xlim(0, max(sizes) + 5)
# Hide the x - axis ticks
ax.set_xticks([])

plt.show()