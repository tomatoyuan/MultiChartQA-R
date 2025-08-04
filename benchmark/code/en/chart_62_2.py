import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
sales_scales = [1047, 1325, 1644, 2074, 2519, 3064, 3778, 4519]  # Sales scale (billion yuan)
growth_rates = [26.5, 24.1, 26.1, 21.5, 21.6, 23.3, 19.6]        # Growth rate (%)

# Color configuration (close to the original image)
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- Create a canvas and a secondary y - axis --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# Create a secondary y - axis (growth rate)
ax2 = ax1.twinx()

# -------------------- Draw a bar chart (sales scale) --------------------
x = np.arange(len(years))

ax1.bar(
    x, 
    sales_scales, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Sales Scale of China's IC Design Industry (billion yuan)"
)

# -------------------- Draw a line chart (growth rate) --------------------
# The growth rate data has one less value than the sales scale (no growth rate in 2014), need to align the years
ax2.plot(
    x[1:],  # Start from 2015
    growth_rates, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Growth Rate of Sales Scale of China's IC Design Industry (%)"
)

# -------------------- Add data labels --------------------
# Label the sales scale
for i, val in enumerate(sales_scales):
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
        x[i+1], val + 0.5, 
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

# Set the primary y - axis label (sales scale)
ax1.set_ylabel("Sales Scale of China's IC Design Industry (billion yuan)", fontsize=12, color="#424242")

# Set the secondary y - axis label (growth rate)
ax2.set_ylabel("Growth Rate of Sales Scale of China's IC Design Industry (%)", fontsize=12, color="#424242")

# Hide redundant borders
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Add a title
ax1.set_title(
    "Sales Scale of China's IC Design Industry from 2014 - 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()