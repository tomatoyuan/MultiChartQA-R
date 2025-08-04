import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
consume_groups = [
    "Below 1000 yuan",
    "1001 - 2000 yuan",
    "2001 - 3000 yuan",
    "3001 - 5000 yuan",
    "5001 - 8000 yuan",
    "8001 - 10000 yuan",
    "Above 10000 yuan"
]
percentages = [8.1, 15.8, 25.9, 27.1, 14.7, 4.0, 4.5]  # Percentage (%)

# Color configuration (similar to the green in the original image)
bar_color = "#a5d6a7"

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw a horizontal bar chart --------------------
y = np.arange(len(consume_groups))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Add percentage labels --------------------
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

# -------------------- Beautify the chart --------------------
# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(consume_groups, fontsize=12, color="#424242")

# Hide the x-axis
ax.set_xticks([])

# Hide the borders
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide y-axis tick marks

# Add a legend (simulate the legend style in the original image)
ax.legend(
    ["Percentage of monthly consumer spending of users"],
    loc="upper right", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Add a title
ax.set_title(
    "Monthly personal consumption level of Chinese e-sports users in 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()