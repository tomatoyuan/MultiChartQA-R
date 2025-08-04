import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
market_size = [804, 802, 850, 777, 862, 944, 1029, 1117, 1210]  # Market size (billion yuan)
growth_rate = [6.0, -0.2, 6.0, -8.6, 10.9, 9.5, 9.0, 8.6, 8.3]  # Growth rate (%)

# Color configuration
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- Create two sub - plots (top and bottom) --------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True,
                               gridspec_kw={'height_ratios': [2, 1], 'hspace': 0.15})

x = np.arange(len(years))

# -------------------- Draw a bar chart --------------------
ax1.bar(
    x, 
    market_size, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Retail market size of Chinese eyewear products (billion yuan)"
)

# Add market size data labels
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 10, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax1.set_ylabel("Market size (billion yuan)", fontsize=12, color="#424242")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")
ax1.set_title("Retail market size of Chinese eyewear industry from 2019 - 2027e", fontsize=14, fontweight="bold", pad=10)

# -------------------- Draw a line chart --------------------
ax2.plot(
    x, 
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Growth rate (%)"
)

# Add growth rate data labels
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 0.5, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax2.set_ylabel("Growth rate (%)", fontsize=12, color="#424242")
ax2.set_ylim(min(growth_rate) - 5, max(growth_rate) + 5)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Set x - axis labels
ax2.set_xticks(x)
ax2.set_xticklabels(years, fontsize=10, color="#424242", rotation=0)

# -------------------- Adjust the layout --------------------
plt.tight_layout()
plt.show()