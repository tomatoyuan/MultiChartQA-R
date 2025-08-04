import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
# Satisfaction categories
labels = [
    "Very Satisfied", "9 Points", "8 Points", "7 Points", "6 Points",
    "5 Points", "4 Points", "3 Points", "2 Points", "Very Dissatisfied"
]
# Percentage data
percentages = [22.0, 23.6, 14.6, 17.1, 16.3, 4.9, 1.6, 0, 0, 0]
# Average satisfaction score
average_score = 7.97

# Color configuration (similar to the original green color scheme)
bar_color = "#a5d6a7"

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw a Horizontal Bar Chart --------------------
y = np.arange(len(labels))

bars = ax.barh(
    y,
    percentages,
    color=bar_color,
    height=0.6
)

# -------------------- Add Data Annotations --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{width}%",
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Add Average Satisfaction Annotation (Blue Droplet) --------------------
# Draw a vertical line
ax.axvline(
    average_score,
    color="lightblue",
    linestyle="--",
    linewidth=2,
    label=f"Average Satisfaction: {average_score} Points"
)

# Draw a droplet shape (simplified as an annotated text + arrow)
ax.annotate(
    f"{average_score} Points",
    xy=(average_score, len(labels) / 2),
    xytext=(average_score + 3, len(labels) / 2),
    arrowprops=dict(
        arrowstyle="->",
        color="blue",
        linewidth=1
    ),
    fontsize=12,
    color="blue",
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="lightblue",
        edgecolor="blue",
        alpha=0.8
    )
)

# -------------------- Beautify the Chart --------------------
# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# Hide x-axis ticks
ax.set_xticks([])

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title(
    "Satisfaction with the Effects of Private Domain Layout by Chinese Merchants in 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()