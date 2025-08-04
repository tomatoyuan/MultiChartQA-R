import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Organization --------------------
# TGI data extracted from the graph (corresponding to three groups by row)
data = {
    "Primary School (7 - 11 years old)": [109, 102, 105, 111, 95, 107, 104, 102, 93, 79, 89, 78, 95, 69, 24],
    "Junior High School (12 - 14 years old)": [103, 98, 109, 84, 128, 107, 92, 102, 112, 123, 164, 121, 152, 111, 109],
    "Senior High School (15 - 17 years old)": [96, 87, 98, 92, 95, 88, 94, 98, 95, 105, 107, 106, 124, 99, 135, 212]
}

# Ensure the lengths of the three groups of data are the same (fill in missing values, should be adjusted according to the original data in practice)
max_len = max(len(v) for v in data.values())
for key in data:
    if len(data[key]) < max_len:
        data[key] += [np.nan] * (max_len - len(data[key]))

# Group labels (x - axis positions)
x = np.arange(max_len)

# Color configuration (light green similar to the original image)
colors = ["#a5d6a7", "#c8e6c9", "#e8f5e9"]

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Draw the grouped bar chart --------------------
bar_width = 0.25  # Width of each group of bars

for i, (group, values) in enumerate(data.items()):
    ax.bar(
        x + i * bar_width,
        values,
        width=bar_width,
        color=colors[i],
        label=group,
        edgecolor="white",
        linewidth=1
    )

# -------------------- Add data labels --------------------
for i, (group, values) in enumerate(data.items()):
    for j, val in enumerate(values):
        if not np.isnan(val):
            ax.text(
                x[j] + i * bar_width,
                val + 2,  # Offset upward
                f"{val}",
                ha="center",
                fontsize=8,
                color="#424242",
                fontweight="bold"
            )

# -------------------- Beautify the chart --------------------
# Set the x - axis ticks (hide them because it's a categorical comparison)
ax.set_xticks([])

# Set the y - axis range
ax.set_ylim(0, 220)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a legend
ax.legend(
    loc="upper left",
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Add a title
ax.set_title(
    "Comparison of TGI Data for Adolescents of Different Ages",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()