import matplotlib.pyplot as plt
import numpy as np

# Food consumption frequency categories
frequencies = [
    "Once a day or more", "Once every two to three days", 
    "Once every four to five days", "Once a week", 
    "Once every two weeks", "Less than once every two weeks"
]
# Simulated proportion data (close to the original graph)
percentages = [54.9, 27.7, 11.6, 4.1, 1.1, 0.1]
# Free color scheme (adjustable, example uses blue)
bar_color = "#87CEEB"  # Can be replaced with other colors such as "#FF8C00"

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a horizontal bar chart
y = np.arange(len(frequencies))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # Label position: offset 5 to the right
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(frequencies)
# Set x-axis ticks (0 - 60%)
ax.set_xlim(0, 60)
# Set the title
ax.set_title("Fruit consumption frequency", fontsize=14, fontweight="bold")

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()