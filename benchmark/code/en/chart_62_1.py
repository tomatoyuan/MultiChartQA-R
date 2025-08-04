import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
enterprise_counts = [681, 736, 1362, 1380, 1698, 1780, 2218, 2810]  # Number of enterprises (units)
growth_rates = [8.1, 85.1, 1.3, 23.0, 4.8, 24.6, 26.7]              # Growth rate (%)

# Color configuration (close to the original image)
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- Create canvas and dual axes --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# Create secondary y-axis (growth rate)
ax2 = ax1.twinx()

# -------------------- Draw bar chart (number of enterprises) --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    enterprise_counts, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Number of Chinese IC design enterprises (units)"
)

# -------------------- Draw line chart (growth rate) --------------------
# The growth rate data has one less value than the number of enterprises (no growth rate in 2014), need to align the years
ax2.plot(
    x[1:],  # Start from 2015
    growth_rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Growth rate of the number of Chinese IC design enterprises (%)"
)

# -------------------- Add data labels --------------------
# Label the number of enterprises
for i, val in enumerate(enterprise_counts):
    ax1.text(
        i, val + 50, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Label the growth rate
for i, val in enumerate(growth_rates):
    # The growth rate corresponds to the years from 2015 - 2021 (x[1] to x[7])
    ax2.text(
        x[i+1], val + 2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Beautify the chart --------------------
# Set x-axis labels (years)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10, color="#424242")

# Set the main y-axis label (number of enterprises)
ax1.set_ylabel("Number of Chinese IC design enterprises (units)", fontsize=12, color="#424242")

# Set the secondary y-axis label (growth rate)
ax2.set_ylabel("Growth rate of the number of Chinese IC design enterprises (%)", fontsize=12, color="#424242")

# Hide redundant borders
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Add title
ax1.set_title(
    "Number of Chinese IC design enterprises from 2014 to 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust layout
plt.tight_layout()

plt.show()