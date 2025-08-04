import matplotlib.pyplot as plt
import numpy as np

# Categories and data
categories = [
    "Sports Goods and Related Product Manufacturing", "Sports Goods and Related Product Sales", "Sports Venue and Facility Management",
    "Sports Education and Training", "Sports Fitness and Recreation Activities", "Other Sports Services",
    "Sports Management Activities", "Sports Media and Information Services", "Sports Agency and Representation",
    "Sports Competition and Performance Activities", "Sports Venue and Facility Construction"
]
data = np.array([44.9, 16.5, 7.9, 7.4, 5.8, 5.7, 3.2, 3.1, 1.2, 1.0, 3.5])

# Construct a pseudo - time axis
x = np.linspace(0, 10, 100)
stack_data = np.array([np.ones_like(x) * v for v in data])

# Color enhancement (colorful + soft)
colors = [
    "#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF",
    "#A0C4FF", "#BDB2FF", "#FFC6FF", "#FFFFFC", "#D0F4DE", "#B0D0D3"
]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a stacked area chart
stacked = ax.stackplot(x, stack_data, labels=categories, colors=colors, alpha=0.95)

# Calculate the middle height position (for adding text)
cumsum_data = np.cumsum(stack_data, axis=0)
mid_height = cumsum_data - stack_data / 2

# Add percentage text, alternately arranged left and right
for i in range(len(categories)):
    y_mid = mid_height[i, len(x) // 2]  # Get the height at the middle point
    align = 'right' if i % 2 == 0 else 'left'
    x_pos = 2 if i % 2 == 0 else 8  # Left - right distribution

    ax.text(
        x_pos, y_mid,
        f"{data[i]}% {categories[i]}",
        fontsize=9,
        ha=align,
        va='center',
        color='black',
        fontweight='bold'
    )

# Title and legend
ax.set_title("Composition of China's Sports Industry in 2020 (Stacked Area Chart)", fontsize=14, fontweight="bold", pad=20)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.1), fontsize=9, frameon=False)

# Beautify the chart
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()