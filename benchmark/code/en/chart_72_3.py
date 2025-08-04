import matplotlib.pyplot as plt
import numpy as np

# Categories of attention status
categories = ["Increased attention", "No significant change, always highly concerned", "Less concerned"]
# Corresponding proportion data (%)
data = [76.0, 19.0, 5.0]
# Color setting, close to the green - based color in the original image
color = "#8239C6"

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=color, edgecolor="white")

# Add a red dashed border to "Increased attention"
rect = plt.Rectangle((0, y[0] - bar_height/2), data[0], bar_height, fill=False, edgecolor='red', linestyle='--')
ax.add_patch(rect)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(categories)
# Hide the x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Consumers' attention to the high - end nature of milk powder ingredients/formulas", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()