import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = ["2020", "2021", "2022", "2023", "2024", "2025e", "2026e", "2027e"]
market_size = [12379.2, 27365.3, 36369.2, 49168.4, 57863.8, 68048.4, 78086.4, 87871.0]  # Market size (in billions of yuan)
growth_rate = [121.1, 32.9, 35.2, 17.7, 17.6, 14.8, 12.5]  # Growth rate (%)

# Color configuration (similar to the original image)
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- Create a canvas and dual axes --------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create a secondary y - axis (growth rate)
ax2 = ax1.twinx()

# -------------------- Draw a bar chart (market size) --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    market_size, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="China Live - streaming E - commerce Market Size (in billions of yuan)"
)

# -------------------- Draw a line chart (growth rate) --------------------
ax2.plot(
    x[:-1],  # The growth rate data has one less item than the years (no growth rate for 2027e)
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Growth Rate (%)"
)

# -------------------- Add data labels --------------------
# Label the market size
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 1000, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Label the growth rate
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Beautify the chart --------------------
# Set the x - axis labels (years)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10, color="#424242")

# Set the primary y - axis label (market size)
ax1.set_ylabel("Market Size (in billions of yuan)", fontsize=12, color="#424242")

# Set the secondary y - axis label (growth rate)
ax2.set_ylabel("Growth Rate (%)", fontsize=12, color="#424242")

# Hide redundant borders
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combine legends (adjust the position, move it up)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines1 + lines2, 
    labels1 + labels2, 
    loc="upper left", 
    bbox_to_anchor=(0, 1.2),  # Move the legend up
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Add a title
ax1.set_title(
    "China Live - streaming E - commerce Market Size and Growth Rate",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()