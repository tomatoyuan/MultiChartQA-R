import matplotlib.pyplot as plt
import numpy as np

# Data (Names, Percentages)
labels = [
    "Multiple times a day on average", "Once a day on average", "Once every 2 - 3 days on average",
    "Once every 4 - 6 days on average", "Once a week on average", "2 - 3 times a month on average",
    "Once a month on average", "Almost never"
]
percentages = [8.4, 13.5, 28.2, 12.2, 12.9, 10.9, 7.2, 6.7]

# Color configuration (Close to the original green color scheme, use gray for "Almost never")
colors = ["#a5d6a7"] * 7 + ["#d3d3d3"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(labels))
bars = ax.barh(y, percentages, color=colors, height=0.6)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
            f"{width}%", va="center", fontsize=9, color="#333")

# Draw a blue dashed box (Select the top three items)
ax.plot([0, max(percentages) + 5], [y[0] - 0.3, y[0] - 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max(percentages) + 5], [y[2] + 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([max(percentages) + 5, max(percentages) + 5], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)

# Set y - axis labels
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# Hide x - axis ticks
ax.set_xticks([])

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title("Frequency of original content posting by Chinese beauty shooting app users in 2022", fontsize=14, fontweight="bold", pad=20)

# Adjust the layout
plt.tight_layout()
plt.show()