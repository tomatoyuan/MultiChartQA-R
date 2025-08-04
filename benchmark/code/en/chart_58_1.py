import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Parks/Amusement Parks", "Hotels", "Travel Agencies", "Tourism Bureaus"]
data_24 = [169.2, 89.2, 895.0, 137.1]
data_25 = [585.6, 70.6, 913.2, 149.1]
growth_rates = ["YoY +246.1%", "YoY -20.9%", "YoY +2.0%", "YoY +8.8%"]

# Colors
color_24 = "#4bb7e6"
color_25 = "#a5d65d"

# Create a canvas
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

# ✅ Unify the maximum value of the y - axis (slightly enlarge to avoid overlap)
y_max = max(max(data_24), max(data_25)) + 80

for i in range(4):
    ax = axes[i]
    x = np.arange(2)
    bars = ax.bar(
        x,
        [data_24[i], data_25[i]],
        width=0.6,
        color=[color_24, color_25],
        edgecolor='white'
    )

    # Add data labels (slightly closer to the top of the bar)
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 5,
            f'{height:.1f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    # Add growth rates (above the top of the bar)
    peak = max(data_24[i], data_25[i])
    ax.text(
        0.5,
        peak + 25,
        growth_rates[i],
        ha='center',
        va='bottom',
        fontsize=10,
        color="#333333",
        fontweight='bold'
    )

    # Set x - axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(["May Day Holiday Week in 2024", "May Day Holiday Week in 2025"], fontsize=9)

    # Hide the borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the title
    ax.set_title(categories[i], fontsize=11, fontweight='bold')

    # Set the unified y - axis upper limit
    ax.set_ylim(0, y_max)

# Overall title
fig.suptitle(
    "AdTracker Comparison of Online Advertising Investment Index for Tourism - Related during May Day Holidays (1 - 5th) in 2024 and 2025",
    fontsize=13,
    fontweight='bold',
    y=1.03
)

# ✅ Adjust the overall layout to avoid the suptitle being obscured
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Reserve space at the top for the title
plt.show()