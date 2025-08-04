import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# -------------------- Data Definition --------------------
years = ["2025e", "2026e", "2027e"]
market_size = [8.1, 9.4, 10.9]  # Market size (in billions of yuan)
growth_rate = [13.9, 16.6, 15.9]  # Growth rate (%)

# Color configuration (similar to the original image)
bar_color = "#a5d6a7"
line_color = "#4dd0e1"
cagr_color = "#a5d6a7"  # CAGR trend line color

# -------------------- Load illustration (simplified simulation, can be replaced with accurate image) --------------------
# Here we use simple shapes for simulation. If you need accurate illustrations, replace it with the actual image path.
# img = mpimg.imread('phone_illustration.png')  # Actual illustration path
# Temporarily use color blocks to simulate the illustration position
illustration = plt.Circle((0, 0), 1, color='lightblue')

# -------------------- Create the canvas and dual axes --------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create the secondary y - axis (growth rate)
ax2 = ax1.twinx()

# -------------------- Draw the bar chart (market size) --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    market_size, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Market Size of China's Overseas Influencer Marketing SaaS (in billions of yuan)"
)

# -------------------- Draw the line chart (growth rate) --------------------
ax2.plot(
    x, 
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Growth Rate (%)"
)

# -------------------- Draw the CAGR trend line and annotation --------------------
# Calculate CAGR (simplified for illustration, actual calculation requires formula)
cagr = 15.0
ax1.annotate(
    f"CAGR≈{cagr}%",
    xy=(2, 10.9),  # Arrow starting point (top of the 2027e bar)
    xytext=(2.2, 10.9), 
    arrowprops=dict(
        facecolor=cagr_color, 
        edgecolor=cagr_color, 
        arrowstyle="->", 
        linewidth=2
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.5)
)

# -------------------- Add data annotations --------------------
# Annotate the market size
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 0.2, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Annotate the growth rate
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 0.5, 
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

# Combine the legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Add the title
ax1.set_title(
    "Forecast of Market Size and Growth Rate of China's Overseas Influencer Marketing SaaS from 2025 to 2027",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()