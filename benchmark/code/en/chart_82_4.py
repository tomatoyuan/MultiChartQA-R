import matplotlib.pyplot as plt
import numpy as np

# Reason categories
reasons = [
    "Annual card mode has a long duration and is difficult to stick to",
    "Dissatisfied with the coach's teaching attitude and ability",
    "The store style is outdated and lacks appeal",
    "Annual card mode has high risks, worried about the merchant running away",
    "Often sending flyers or making sales pitches, leaving a bad impression",
    "High price, dissatisfied with the cost-performance",
    "The courses are quite homogeneous and cannot meet the needs",
    "There is often news about gyms closing down and running away, leaving a bad impression",
    "Inconvenient location"
]
# Corresponding percentages (%)
percentages = [47.5, 43.0, 42.4, 41.1, 39.9, 38.0, 30.4, 21.5, 12.0]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart (horizontal bar chart, adjusted to be consistent with the original image's orientation)
y = np.arange(len(reasons))
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

# Draw a dashed border for the Top 5 (the first 5 items)
for i in range(5):
    special_bar = bars[i]
    x0, y0 = special_bar.get_xy()
    width, height = special_bar.get_width(), special_bar.get_height()
    rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor='green', linestyle='--')
    ax.add_patch(rect)

# Set the y - axis ticks and labels (adjust the order so that the first reason is at the top)
ax.set_yticks(y)
ax.set_yticklabels(reasons)
# Hide the x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Reasons why Chinese gym users did not choose traditional gyms in 2022", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()