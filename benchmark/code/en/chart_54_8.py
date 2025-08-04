import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
categories = [
    "Improve immunity and enhance resistance",
    "Improve sleep",
    "Supplement energy and stay energetic",
    "Improve gastrointestinal health",
    "Ensure balanced nutrition intake",
    "Enhance eye/vision health",
    "Increase metabolic level",
    "Improve memory",
    "Regulate endocrine system",
    "Enhance bone and joint health"
]

# Simulated data (the first 3 are green, the rest are gray)
percentages = [75.7, 57.9, 47.7, 46.9, 44.9, 43.8, 35.6, 35.0, 34.4, 33.3]

# Color configuration (the first 3 are green, the rest are gray)
colors = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categories)-3)

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Draw a Horizontal Bar Chart --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
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
        f"{width}",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# -------------------- Beautify the Chart --------------------
# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=11, color="#424242")

# Hide the x-axis
ax.set_xticks([])

# Hide the frame
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide y-axis tick marks

# Add a title
ax.set_title(
    "Purposes of residents taking dietary nutritional supplements (%)",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()