import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
# Months (simplified from July 2021 to June 2022)
months = [f"2021.{i}" for i in range(7, 13)] + [f"2022.{i}" for i in range(1, 7)]

# Simulated data (can be replaced with real values)
protein_index = [100, 110, 120, 150, 200, 180, 160, 170, 190, 220, 240, 260]  # Overall protein powder
whey_index = [90, 95, 100, 130, 160, 140, 130, 140, 160, 180, 200, 220]    # Whey protein

# Annotation data (corresponding to significant change points)
annotations = {
    "2021.11": "+70.3%",
    "2022.1": "+63.2%",
    "2022.5": "+17.4%",
    "2022.6": "+17.7%"
}

# Color configuration (similar to the original yellow - green + blue color scheme)
protein_color = "#a5d6a7"  # Overall protein powder
whey_color = "#81d4fa"     # Whey protein

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Draw a Double Line Chart --------------------
# Overall protein powder
ax.plot(
    months, 
    protein_index, 
    marker="o", 
    color=protein_color, 
    label="Turnover Index of Protein Powder (Overall)",
    linewidth=2
)

# Whey protein
ax.plot(
    months, 
    whey_index, 
    marker="o", 
    color=whey_color, 
    label="Turnover Index of Whey Protein",
    linewidth=2
)

# -------------------- Add Annotations and Arrows --------------------
for month, text in annotations.items():
    idx = months.index(month)
    # Annotations for overall protein powder (green arrows)
    if "2021.11" in month or "2022.5" in month:
        ax.annotate(
            text,
            xy=(idx, protein_index[idx]),
            xytext=(idx + 0.5, protein_index[idx] + 30),
            arrowprops=dict(
                facecolor=protein_color,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=protein_color
        )
    # Annotations for whey protein (blue arrows)
    else:
        ax.annotate(
            text,
            xy=(idx, whey_index[idx]),
            xytext=(idx + 0.5, whey_index[idx] + 25),
            arrowprops=dict(
                facecolor=whey_color,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=whey_color
        )

# -------------------- Beautify the Chart --------------------
# Set the y - axis range
ax.set_ylim(0, 300)

# Set the x - axis tick labels (tilt to avoid overlap)
plt.xticks(rotation=45, ha="right", fontsize=9)

# Set the legend
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title(
    "Monthly Turnover Trend Changes of Protein Powder (Overall) and Whey Protein",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()