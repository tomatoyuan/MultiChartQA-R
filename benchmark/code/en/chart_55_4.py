import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
age_groups = ["Under 25", "26 - 30", "31 - 35", "Over 36"]
percentages = [35.5, 33.0, 17.6, 13.9]  # Percentage (%)

# Color configuration (similar to the green in the original image)
bar_color = "#a5d6a7"

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Draw a Horizontal Bar Chart --------------------
y = np.arange(len(age_groups))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Add Percentage Annotations --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# -------------------- Beautify the Chart --------------------
# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(age_groups, fontsize=12, color="#424242")

# Hide the x-axis
ax.set_xticks([])

# Hide the borders
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide the y-axis tick marks

# Add a legend (simulate the legend style in the original image)
ax.legend(
    ["Percentage of E-sports Users by Age"],
    loc="upper right", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Add a title
ax.set_title(
    "Age Distribution of Chinese E-sports Users in 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()