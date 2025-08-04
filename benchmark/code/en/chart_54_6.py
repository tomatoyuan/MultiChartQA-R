import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
categories = [
    "Sleep problems",
    "Easily fatigued/lack of energy",
    "High mental stress",
    "Immunity (less or no illness) problems",
    "Skin health problems",
    "Vision problems",
    "Hair problems (e.g., hair loss)",
    "Shoulder and neck pain",
    "Low mood/anxiety",
    "Memory problems",
    "Anti - aging",
    "Endocrine problems",
    "Three - high problems",
    "Obesity/overweight",
    "Cardiovascular and cerebrovascular problems",
    "Bone and joint problems",
    "Depression",
    "Diabetes"
]

# Simulated data (the first 3 items are green, the rest are gray)
percentages = [61.1, 50.5, 48.9, 45.9, 44.2, 43.3, 42.2, 42.1, 40.8, 36.9, 28.1, 22.9, 20.7, 20.7, 15.5, 15.5, 9.3, 5.3]

# Color configuration (the first 3 items are green, the rest are gray)
colors = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categories)-3)

# -------------------- Create the canvas --------------------
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
    "Health concerns of adults aged 18 - 65 (%)",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # Simulate the title position of the original image
)

# Adjust the layout
plt.tight_layout()

plt.show()