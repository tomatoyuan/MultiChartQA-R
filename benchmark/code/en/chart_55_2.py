import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2022, 2023, 2024, 2025, 2026, 2027]

# Proportion of various markets (%)
mobile_eb = [51.9, 53.7, 54.5, 54.6, 54.3, 53.9]    # Proportion of mobile esports games
tournament_eb = [23.7, 23.6, 23.2, 22.7, 22.2, 21.6]  # Proportion of PC esports games
ecosystem_eb = [24.4, 22.7, 22.3, 22.7, 23.5, 24.5]   # Proportion of esports ecosystem

# Color configuration (similar to the original image color scheme)
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Draw the stacked bar chart --------------------
# Proportion of mobile esports games (bottom layer)
ax.bar(
    years, 
    mobile_eb, 
    color=colors[0], 
    label="Proportion of mobile esports games (%)",
    edgecolor="white",
    linewidth=1
)

# Proportion of PC esports games (middle layer)
bottom_mobile = np.array(mobile_eb)
ax.bar(
    years, 
    tournament_eb, 
    bottom=bottom_mobile, 
    color=colors[1], 
    label="Proportion of PC esports games (%)",
    edgecolor="white",
    linewidth=1
)

# Proportion of esports ecosystem (top layer)
bottom_tournament = bottom_mobile + np.array(tournament_eb)
ax.bar(
    years, 
    ecosystem_eb, 
    bottom=bottom_tournament, 
    color=colors[2], 
    label="Proportion of esports ecosystem (%)",
    edgecolor="white",
    linewidth=1
)

# -------------------- Add data labels --------------------
for i, (y, m, t, e) in enumerate(zip(years, mobile_eb, tournament_eb, ecosystem_eb)):
    # Proportion of mobile esports
    ax.text(y, m/2, f"{m}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # Proportion of PC esports
    ax.text(y, m + t/2, f"{t}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # Proportion of esports ecosystem
    ax.text(y, m + t + e/2, f"{e}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- Beautify the chart --------------------
# Set the y-axis range (the total proportion is 100%)
ax.set_ylim(0, 100)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a legend and move it upwards
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white",
    # Use bbox_to_anchor to finely adjust the position, the range of (x, y) is [0, 1]
    bbox_to_anchor=(0.1, 0.2)  # Move upwards, y > 1 means above the chart
)

# Add a title
ax.set_title(
    "Proportion of the segmented scale of the Chinese esports market from 2022 to 2027",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Adjust the layout (to avoid the legend being truncated)
plt.tight_layout()

# If the legend position exceeds the chart range, you can adjust the saved range via bbox_inches (optional)
# plt.savefig("output.png", bbox_inches="tight")

plt.show()