import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
ratios = [10.5, 11.0, 6.4, 9.5, 9.1, 7.7, 7.7]  # Marketing budget ratio (%)

# Color configuration (similar to the green in the original image)
line_color = "#a5d6a7"
trend_color = "#dcdcdc"  # Trend line color

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Plot Line Chart --------------------
ax.plot(
    years, 
    ratios, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Average marketing budget as a percentage of operating revenue"
)

# -------------------- Plot Trend Line (Dashed Line) --------------------
# Calculate the linear fitting trend
z = np.polyfit(years, ratios, 1)
p = np.poly1d(z)
ax.plot(years, p(years), color=trend_color, linestyle="--", linewidth=1)

# -------------------- Add Data Annotations --------------------
for i, val in enumerate(ratios):
    ax.text(
        years[i], val + 0.2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Add Bottom Annotation --------------------
ax.annotate(
    "Increasing macro - economic uncertainty leads to a decline in corporate marketing budget ratio",
    xy=(0.5, -0.25),  # Annotation position (centered at the bottom)
    xycoords="axes fraction",
    ha="center",
    va="top",
    fontsize=12,
    color="#424242",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# -------------------- Beautify the Chart --------------------
# Set x - axis labels (years)
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, color="#424242")

# Set y - axis range (0 - 12%)
ax.set_ylim(0, 12)

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
    "Average marketing budget as a percentage of operating revenue of global enterprises from 2019 - 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust layout
plt.tight_layout()

plt.show()