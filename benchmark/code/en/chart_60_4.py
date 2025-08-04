import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
motivations = [
    "Glasses are worn, aged or damaged, affecting use",
    "Glasses are uncomfortable to wear (uncomfortable vision/frame discomfort)",
    "Change in functional requirements for glasses, get functional glasses",
    "Change in vision/eye degree",
    "Local looseness of the frame, unstable wearing",
    "Professional doctor's advice to replace/regularly change glasses",
    "Want to change image/try a new style",
    "The original glasses have been used for a long time and lost their freshness",
    "Match new styles for daily outfits",
    "Follow the current trend or celebrity/influencer同款 (Follow the current trend or get the same style as celebrities/influencers)",
    "Meet the needs of different scenarios, place glasses separately in different scenarios for convenient use"
]
percentages = [39.2, 35.9, 35.5, 30.6, 30.6, 28.3, 24.0, 23.7, 19.5, 18.3, 14.8]  # Percentage (%)

# Color configuration (similar to the green gradient in the original image)
bar_color = "#a5d6a7"

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw a horizontal bar chart --------------------
y = np.arange(len(motivations))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Add data labels --------------------
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Beautify the chart --------------------
# Set y-axis labels (motivation descriptions)
ax.set_yticks(y)
ax.set_yticklabels(motivations, fontsize=10, color="#424242")

# Hide the x-axis
ax.set_xticks([])

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title(
    "Motivations for Changing Glasses",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()