import matplotlib.pyplot as plt
import numpy as np

# Main factors
factors = [
    "Easy to take",
    "Good effect",
    "Portable",
    "No 'taking medicine' feeling",
    "Novel",
    "Nice packaging"
]
# Corresponding percentages (%), the data is consistent with the chart
percentages = [65.0, 56.0, 45.0, 38.0, 30.0, 23.0]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart (horizontal bar chart, adjusted to be consistent with the original chart's direction)
y = np.arange(len(factors))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#A4C639")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set the y - axis ticks and labels (adjust the order so that the first factor is at the top)
ax.set_yticks(y)
ax.set_yticklabels(factors)
# Hide the x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Main factors for consumers to choose 'functional snacks' in 2021", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()