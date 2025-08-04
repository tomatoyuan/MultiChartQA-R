import matplotlib.pyplot as plt
import numpy as np

# Data
months = [
    "2024.1", "2024.2", "2024.3", "2024.4", "2024.5", 
    "2024.6", "2024.7", "2024.8", "2024.9", "2024.10", 
    "2024.11", "2024.12", "2025.1", "2025.2", "2025.3"
]
device_counts = [13.95, 13.98, 14.12, 14.03, 14.15, 14.12, 14.22, 14.26, 14.30, 14.32, 14.32, 14.34, 14.38, 14.38, 14.39]
growth_rates = [0.21, 0.15, 1.01, -0.63, 0.84, -0.19, 0.72, 0.29, 0.29, 0.14, -0.04, 0.19, 0.27, -0.03, 0.08]

# Color scheme
bar_color = "#a5d6a7"
line_color = "#4dd0e1"
highlight_color = "#ffe0f0"
text_color = "#424242"

# Create the chart
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

x = np.arange(len(months))

# Bar chart
bars = ax1.bar(
    x, device_counts, color=bar_color, width=0.6,
    edgecolor="white", linewidth=1,
    label="Monthly Independent Devices (100 million units)"
)

# Line chart
ax2.plot(
    x, growth_rates, color=line_color, marker="o",
    linewidth=2, markersize=5, label="Month-on-Month Growth Rate (%)"
)

# Axis range
ax1.set_ylim(13.7, 14.6)
ax2.set_ylim(-1.5, 1.5)

# Text labels for the bar chart (above the bar tops)
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.02,
        f"{height:.2f}",
        ha="center", va="bottom",
        fontsize=9, color=text_color,
        fontweight="bold"
    )

# Text labels for the line chart (avoid overlap)
for i, val in enumerate(growth_rates):
    y_offset = 0.08 if val >= 0 else -0.12
    va = "bottom" if val >= 0 else "top"
    ax2.text(
        i, val + y_offset,
        f"{val:.2f}%",
        ha="center", va=va,
        fontsize=9, color=text_color,
        fontweight="bold"
    )

# Highlight Q1 area
q1_start = months.index("2025.1")
q1_end = months.index("2025.3")
ax1.axvspan(q1_start - 0.3, q1_end + 0.3, facecolor=highlight_color, alpha=0.3, zorder=0)
ax1.text(
    (q1_start + q1_end) / 2, max(device_counts) + 0.05,
    "Q1 Average YoY +2.6%", ha="center", va="bottom",
    fontsize=10, color="red", fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc=highlight_color, ec="red", alpha=0.5)
)

# X-axis
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha="right", fontsize=10, color=text_color)

# Y-axis labels
ax1.set_ylabel("Monthly Independent Devices (100 million units)", fontsize=12, color=text_color)
ax2.set_ylabel("Month-on-Month Growth Rate (%)", fontsize=12, color=text_color)

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Remove borders
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Title
ax1.set_title(
    "mUserTracker - Monthly Independent Devices in China Mobile Internet from 2024.1 to 2025.3",
    fontsize=14, fontweight="bold", pad=20
)

plt.tight_layout()
plt.show()