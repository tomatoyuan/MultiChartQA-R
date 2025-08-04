import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2022, 2023, 2024, 2025, 2026, 2027]

# Various market sizes (in billions of yuan)
mobile_eb = [819, 911, 975, 1020, 1060, 1095]    # Mobile e - sports game market
tournament_eb = [375, 400, 415, 424, 432, 438]  # PC e - sports game market
ecosystem_eb = [385, 386, 400, 424, 458, 497]   # E - sports ecosystem market

# Overall growth rates (%)
growth_rates = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]  # To be calculated based on actual data, placeholder here

# Color configuration (similar to the original image color scheme)
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Draw Stacked Bar Chart --------------------
# Mobile e - sports game market (bottom layer)
ax.bar(
    years, 
    mobile_eb, 
    color=colors[0], 
    label="Mobile e - sports game market size (in billions of yuan)",
    edgecolor="white",
    linewidth=1
)

# PC e - sports game market (middle layer)
bottom_mobile = np.array(mobile_eb)
ax.bar(
    years, 
    tournament_eb, 
    bottom=bottom_mobile, 
    color=colors[1], 
    label="PC e - sports game market size (in billions of yuan)",
    edgecolor="white",
    linewidth=1
)

# E - sports ecosystem market (top layer)
bottom_tournament = bottom_mobile + np.array(tournament_eb)
ax.bar(
    years, 
    ecosystem_eb, 
    bottom=bottom_tournament, 
    color=colors[2], 
    label="E - sports ecosystem market size (in billions of yuan)",
    edgecolor="white",
    linewidth=1
)

# -------------------- Add Data Annotations --------------------
# Annotate values for each layer
for i, (y, m, t, e) in enumerate(zip(years, mobile_eb, tournament_eb, ecosystem_eb)):
    # Mobile e - sports
    ax.text(y, m/2, f"{m}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # PC e - sports
    ax.text(y, m + t/2, f"{t}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # E - sports ecosystem
    ax.text(y, m + t + e/2, f"{e}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- Beautify the Chart --------------------
# Set y - axis label
ax.set_ylabel("Market size (in billions of yuan)", fontsize=10, color="#424242")

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add legend
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Add title
ax.set_title(
    "China's overall e - sports market size from 2022 to 2027",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Adjust layout
plt.tight_layout()

plt.show()