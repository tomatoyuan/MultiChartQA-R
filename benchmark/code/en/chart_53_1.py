import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
categories = [
    "Protein Powder (Overall)",
    "Protein Powder (Probiotics)",
    "Calcium, Iron, Zinc/Calcium, Magnesium/Calcium",
    "Vitamins/Minerals",
    "Enzyme Protein",
    "Collagen",
    "Fish Oil/Fish Oil Omega3",
    "Oyster/Shellfish Extract",
    "L-Carnitine",
    "Maca Extract",
    "Grape Seed Extract",
    "DHA/EPA/DPA",
    "Natto Extract",
    "Folic Acid",
    "Cranberry"
]

# Simulated data (can be replaced with real values)
values = [7.4, 5.2, 4.8, 4.5, 4.2, 3.9, 
          3.7, 3.5, 3.2, 3.0, 2.8, 2.6, 
          2.4, 2.2, 2.0]

# Special annotation (corresponding to "Protein Powder (Overall)")
special_note = (
    "“Protein Powder” is one of the most prominent markets in the sub - category of dietary nutritional supplements\n"
    "under the first - level category of health food/dietary nutritional supplements."
)

# Color configuration (similar to the green color scheme in the original figure)
bar_color = "#81c784"
highlight_color = "#a5d6a7"  # Highlight color (Protein Powder Overall)

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 7))

# -------------------- Draw a Horizontal Bar Chart --------------------
y = np.arange(len(categories))

# Highlight the first bar (Protein Powder Overall)
bars = ax.barh(
    y, 
    values, 
    color=[highlight_color] + [bar_color]*(len(categories)-1),
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# Add numerical annotations
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.2,  # Right offset
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# Text annotation (right - hand side description)
ax.text(
    max(values) + 1.5,  # Right offset
    y[0] - 0.5,  # Upward offset
    special_note,
    fontsize=9,
    color="#424242",
    linespacing=1.2,
    ha="left",
    bbox=dict(
        facecolor="white", 
        edgecolor=bar_color, 
        boxstyle="round,pad=0.5"
    )
)

# -------------------- Beautify the Chart --------------------
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=10, color="#424242")
ax.set_xticks([])  # Hide x - axis ticks

# Hide the frame
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide y - axis tick marks

# Add a title
ax.set_title(
    "Market Share of Sub - markets in Health Food/Dietary Nutritional Supplements (First - level Category)",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.subplots_adjust(left=0.3, right=0.7, top=0.85, bottom=0.1)

plt.show()