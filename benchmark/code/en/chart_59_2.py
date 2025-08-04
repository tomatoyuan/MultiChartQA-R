import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2018, 2019, 2020, 2021, 2022]
rates = [53.60, 50.20, 52.70, 52.60, 51.90]  # Myopia rate (%)

# Color configuration (similar to the green in the original image)
line_color = "#a5d6a7"

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw Line Chart --------------------
ax.plot(
    years, 
    rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Rate"
)

# -------------------- Add Data Annotations --------------------
for i, val in enumerate(rates):
    ax.text(
        years[i], val + 0.2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Beautify the Chart --------------------
# Set x-axis labels (years)
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, color="#424242")

# Set y-axis range (49 - 55%, adjusted according to the data)
ax.set_ylim(49, 55)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add legend
ax.legend(
    loc="upper right", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Add title
ax.set_title(
    "National Myopia Rate of Children and Adolescents from 2018 to 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust layout
plt.tight_layout()

plt.show()