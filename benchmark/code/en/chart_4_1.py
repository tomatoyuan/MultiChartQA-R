import matplotlib.pyplot as plt
import numpy as np

# Generate complete May dates (from 1st to 31st)
dates = [f"5/{i}" for i in range(1, 32)]
x = np.arange(len(dates))  # Used for x - axis positioning

# Plastic surgery attention data (left y - axis, unit: million)
plastic_surgery = [
    6.5, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 9.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0
]

# Nose plastic surgery proportion data (right y - axis, unit: %)
nose_plastic = [
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0
]

# Eye plastic surgery proportion data (right y - axis, unit: %)
eye_plastic = [
    5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0
]

# Skin care proportion data (right y - axis, unit: %)
skin_care = [
    15.0, 15.0, 15.0, 15.0, 15.0, 14.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 13.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 16.0
]

# Create a canvas and dual - axis
fig, ax1 = plt.subplots(figsize=(14, 7))  # Increase the canvas size
ax2 = ax1.twinx()

# Draw the plastic surgery bar chart (left axis)
bar_width = 0.6
bars = ax1.bar(
    x,
    plastic_surgery,
    color="#1f77b4",  # Professional blue
    width=bar_width,
    label="Plastic Surgery"
)
ax1.set_ylabel("Attention (Million)", color="#1f77b4", fontsize=12, fontweight="bold")
ax1.set_ylim(0, 10)
ax1.set_yticks(np.arange(0, 11, 1))
ax1.tick_params(axis="y", labelcolor="#1f77b4", labelsize=10)

# Add numerical labels on top of the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2., height + 0.1,
        f'{height:.1f}',
        ha='center', va='bottom', fontsize=9
    )

# Draw the nose plastic surgery line chart (right axis)
ax2.plot(
    x,
    nose_plastic,
    color="#2ca02c",  # Professional green
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Nose Plastic Surgery"
)

# Draw the eye plastic surgery line chart (right axis)
ax2.plot(
    x,
    eye_plastic,
    color="#ff7f0e",  # Professional orange
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Eye Plastic Surgery"
)

# Draw the skin care line chart (right axis)
ax2.plot(
    x,
    skin_care,
    color="#d62728",  # Professional red
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Skin Care"
)
ax2.set_ylabel("Proportion (%)", color="black", fontsize=12, fontweight="bold")
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 20, 2))
ax2.tick_params(axis="y", labelcolor="black", labelsize=10)

# Set the x - axis tick marks (show one tick every 3 days to avoid overcrowding)
ax1.set_xticks(x[::3])  # Show a tick every 3 days
ax1.set_xticklabels(dates[::3], fontsize=10, rotation=45, ha="right")  # Rotate 45 degrees and align to the right

# Add a grid (only in the y - direction of the left axis)
ax1.grid(axis="y", linestyle="--", color="gray", alpha=0.4)

# Combine the legends (place them at the bottom)
lines_ax1, labels_ax1 = ax1.get_legend_handles_labels()
lines_ax2, labels_ax2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines_ax1 + lines_ax2,
    labels_ax1 + labels_ax2,
    loc="lower center",
    ncol=4,
    bbox_to_anchor=(0.5, -0.2),
    frameon=False,
    fontsize=11
)

# Set the title
ax1.set_title("Search Attention Trend of the Medical Aesthetics Industry in May", fontsize=16, fontweight="bold", y=1.05)

# Add background color to distinguish different areas
for i in range(0, len(dates), 6):
    if i % 12 == 0:
        ax1.axvspan(i - 0.5, i + 5.5, alpha=0.05, color='gray')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()