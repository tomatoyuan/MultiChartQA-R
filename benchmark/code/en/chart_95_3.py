import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Sources of growth power
sources = [
    "Own inner self", "Parental support", "Friendship", 
    "Teacher's guidance", "Inspirational role models", "Favorite works", "Steady national development"
]
# Simulated proportion data (try to be close to the original image)
percentages = [32, 32, 27, 23, 21, 16, 16]
# Color configuration (try to be close to the gradient green, blue, and yellow in the original image)
colors = ["#A8D089", "#8CC17F", "#68B26F", "#6CBAE5", "#59A5D8", "#F7D842", "#F2B73F"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart with a striped background
x = np.arange(len(sources))
bar_width = 0.6
# First, draw the striped background (filled with gray diagonal lines)
for i in range(len(sources)):
    ax.bar(x[i], 100, width=bar_width, color='white', edgecolor='lightgray', hatch='////', zorder=0)

# Then, draw the foreground colored bars
bars = ax.bar(x, percentages, width=bar_width, color=colors, zorder=1)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar_width/2, height),
                xytext=(0, 3),  # Label position: offset 3 above
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set the y-axis scale (0 - 40%)
ax.set_ylim(0, 40)
# Set the x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(sources, rotation=40, ha='right')  # Rotate the labels to avoid overlap
# Set the title
ax.set_title("Sources of college students' growth power", fontsize=14, fontweight="bold")

# Hide the y-axis (no y-axis ticks in the original image)
ax.yaxis.set_visible(False)

# Hide the top, right, and left borders
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()