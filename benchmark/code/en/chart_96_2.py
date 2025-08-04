import matplotlib.pyplot as plt
import numpy as np

# Usage scenarios
scenarios = [
    "Commuting to and from work", "Picking up and dropping off children", "Short - distance self - driving tour",
    "Gathering with relatives and friends", "Shopping at malls/supermarkets", "Long - distance self - driving tour", "Long - distance visiting relatives"
]
# Simulated proportion data (as close to the original figure as possible)
percentages = [67.8, 61.2, 59.6, 45.6, 44.7, 44.0, 32.7]
# Color configuration (green close to the original figure)
color = "#A4C639"

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a horizontal bar chart
y = np.arange(len(scenarios))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=color)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # Label position: offset 5 to the right
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(scenarios)
# Set the x - axis ticks (0 - 70%)
ax.set_xlim(0, 70)
# Set the title
ax.set_title("MPV vehicle usage scenarios", fontsize=14, fontweight="bold")

# Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()