import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
categories = [
    "Vision problems",
    "Growth and development problems",
    "Immunity problems",
    "Strengthen bones/Promote bone development",
    "Concentration",
    "High mental stress",
    "Memory problems",
    "Promote gastrointestinal digestion",
    "Low mood",
    "Sleep problems (e.g., insomnia, light sleep)",
    "Skin health problems (e.g., acne)",
    "Easily fatigued/Lack of energy",
    "Obesity/Overweight",
    "Hair problems (e.g., hair loss)",
    "Depression",
    "Three - high problems (high blood lipid/pressure/sugar)",
    "Diabetes"
]

# Simulated data (the first 4 items are green, the rest are gray)
percentages = [61.1, 55.6, 52.5, 49.1, 41.3, 36.2, 34.6, 34.2, 26.6, 24.5, 24.3, 21.2, 19.7, 12.3, 10.9, 6.7, 4.5]

# Color configuration (the first 4 items are green, the rest are gray)
colors = ["#a5d6a7"]*4 + ["#dcdcdc"]*(len(categories)-4)

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(10, 8))

# -------------------- Draw a horizontal bar chart --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
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
        f"{width}",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# -------------------- Beautify the chart --------------------
# Set y - axis labels
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=11, color="#424242")

# Hide the x - axis
ax.set_xticks([])

# Hide the borders
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide the y - axis tick marks

# Add a title
ax.set_title(
    "Health concerns of 7 - 17 - year - old adolescents (%)",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # Simulate the title position of the original image
)

# Adjust the layout
plt.tight_layout()

plt.show()