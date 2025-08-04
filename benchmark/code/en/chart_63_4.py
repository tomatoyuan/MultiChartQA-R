import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
# Shooting frequency categories
labels = [
    "More than 5 times a day on average", "2 - 5 times a day on average", "Once a day on average",
    "4 - 6 times a week on average", "2 - 3 times a week on average", "Once a week on average",
    "Less than once a week on average"
]
# Percentage data
percentages = [6.4, 27.1, 18.7, 20.9, 15.7, 5.9, 5.4]

# Group markers (The first three items are "Shoot at least once a day on average")
group_indices = [0, 1, 2]  # Indices of the first three items

# Color configuration (Close to the green color scheme in the original image)
bar_colors = ["#a5d6a7"] * len(labels)

# Annotation text (Blue box in the upper - right corner)
annotation_text = "Users who shoot at least once a day on average\naccount for 52.2%"
annotation_box = {
    "boxstyle": "round,pad=0.5",
    "facecolor": "lightblue",
    "edgecolor": "blue",
    "alpha": 0.8
}

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw a horizontal bar chart --------------------
y = np.arange(len(labels))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_colors, 
    height=0.6
)

# -------------------- Add data annotations --------------------
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

# -------------------- Draw a dashed box for the group --------------------
# Find the minimum and maximum y - coordinates of the group
min_y = min([y[i] for i in group_indices]) - 0.3
max_y = max([y[i] for i in group_indices]) + 0.3
max_width = max([percentages[i] for i in group_indices]) + 3  # Width of the dashed box

# Draw the dashed box
ax.plot([0, max_width], [min_y, min_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max_width], [max_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([max_width, max_width], [min_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [min_y, max_y], color="blue", linestyle="--", linewidth=1)

# -------------------- Add an annotation in the upper - right corner --------------------
ax.text(
    max_width - 2,  # Horizontal position
    max_y + 0.5,    # Vertical position (Above the dashed box)
    annotation_text,
    fontsize=9,
    color="blue",
    fontweight="bold",
    bbox=annotation_box
)

# -------------------- Beautify the chart --------------------
# Set y - axis labels
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# Hide x - axis ticks
ax.set_xticks([])

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title(
    "Shooting frequency of portrait photos by Chinese users of beauty - shooting apps in 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()