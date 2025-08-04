import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
categories = ["Internet Usage", "Learning and Training", "Cultural, Leisure and Entertainment", "Sports and Fitness"]
years = ["2008", "2018", "2024"]

# Data: [2008, 2018, 2024] (minutes)
data = [
    [14, 162, 363],    # Internet Usage: 14→162→363 (minutes)
    [27, 107, 287],    # Learning and Training: 27→107→287 (minutes)
    [40, 105, 153],    # Cultural, Leisure and Entertainment: 40→105→153 (minutes)
    [23, 31, 35]       # Sports and Fitness: 23→31→35 (minutes)
]

# Color configuration (similar to the original image)
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]  # Colors corresponding to 2008, 2018, 2024

# Annotation configuration (growth rate)
annotations = [
    {"year": "2018→2024", "growth": 125.9, "pos": (2, 363 + 10)},
    {"year": "2008→2018", "growth": 260.0, "pos": (1, 107 + 10)}
]

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Draw the grouped bar chart --------------------
x = np.arange(len(categories))
bar_width = 0.25

for i in range(len(years)):
    ax.bar(
        x + i * bar_width, 
        [d[i] for d in data], 
        width=bar_width, 
        color=colors[i], 
        label=years[i],
        edgecolor="white",
        linewidth=1
    )

# -------------------- Add data annotations (minutes) --------------------
for i in range(len(categories)):
    for j in range(len(years)):
        val = data[i][j]
        ax.text(
            x[i] + j * bar_width, 
            val + 5, 
            f"{val} minutes",
            ha="center", 
            va="bottom",
            fontsize=9,
            color="#424242",
            fontweight="bold"
        )

# -------------------- Beautify the chart --------------------
# Set the x-axis labels (activity types)
ax.set_xticks(x + bar_width)
ax.set_xticklabels(categories, fontsize=11, color="#424242", rotation=15, ha="right")

# Set the y-axis range (0 - 400 minutes, adjusted according to the data)
ax.set_ylim(0, 400)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add the legend
ax.legend(
    loc="upper left", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Add the title
ax.set_title(
    "Average Daily Activity Duration of National Residents",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()