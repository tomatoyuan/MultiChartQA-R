import matplotlib.pyplot as plt
import numpy as np

# Data
dates = [
    "Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", 
    "Apr 27", "Apr 28", "Apr 29", "Apr 30", "May 1", 
    "May 2", "May 3", "May 4", "May 5"
]
values_2024 = [112.1, 118.4, 102.0, 119.4, 91.9, 119.5, 122.3, 130.0, 132.0, 66.7, 61.7, 58.8, 62.9, 101.1]
values_2025 = [76.7, 71.7, 68.8, 101.1, 132.1, 120.0, 102.0, 120.4, 88.9, 119.5, 122.3, 130.3, 133.5, 136.2]

color_2024 = "#4dd0e1"
color_2025 = "#a5d6a7"

x = np.arange(len(dates))

# Create upper and lower sub - plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'hspace': 0.3})

# Plot the line chart for 2024
ax1.plot(x, values_2024, color=color_2024, marker='o', linewidth=2, label="2024")
for i, val in enumerate(values_2024):
    ax1.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2024)

ax1.set_title("Advertising Investment Trend in 2024", fontsize=12, fontweight="bold", color=color_2024)
ax1.set_ylabel("Advertising Index", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.2)

# Plot the line chart for 2025
ax2.plot(x, values_2025, color=color_2025, marker='o', linewidth=2, label="2025")
for i, val in enumerate(values_2025):
    ax2.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2025)

ax2.set_title("Advertising Investment Trend in 2025", fontsize=12, fontweight="bold", color=color_2025)
ax2.set_ylabel("Advertising Index", fontsize=11)
ax2.set_xticks(x)
ax2.set_xticklabels(dates, rotation=45, ha="right")
ax2.grid(True, linestyle="--", alpha=0.2)

# Overall title
fig.suptitle(
    "AdTracker Comparison of Advertising Investment Trends in Parks/Amusement Parks\nfrom Apr 22 to May 5, 2024 & 2025",
    fontsize=14, fontweight="bold", y=1.03
)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()