import matplotlib.pyplot as plt
import numpy as np

# Data definition
years = np.array([1950, 1960, 1970, 1980, 1990, 2016])
costs = np.array([10, 100, 500, 3000, 3000, 25])  # The value for 2016 is a schematic value
labels = [
    "10 yuan\nEquivalent to 1/5 of monthly income\n+ Organization certificate",
    "100 yuan\nEquivalent to 2 months' income\n+ A set of furniture",
    "500 yuan\nEquivalent to 15 months' income\n+ Three turns and one sound",
    "3000 yuan\nEquivalent to 30 months' income\n+ Refrigerator, TV, washing machine",
    "3000 yuan\nEquivalent to 30 months' income\n+ Three gold items, wedding banquet, wedding photos",
    ">250,000 yuan\nEquivalent to 30 months' income"
]

# Create a figure and axes, increase the top space
fig, ax = plt.subplots(figsize=(12, 8))
fig.subplots_adjust(top=0.85)  # Adjust the top spacing

# Draw a gradient - colored bar chart (using a color map)
cmap = plt.cm.viridis
norm = plt.Normalize(min(costs), max(costs))
colors = [cmap(norm(c)) for c in costs]
bars = ax.bar(np.arange(len(years)), costs, width=0.6, color=colors, edgecolor='gray')

# Set the title and labels
ax.set_title("History of Changes in Chinese Marriage Costs", fontsize=18, fontweight='bold', pad=30)
ax.set_ylabel("Marriage cost (Unit: yuan, the value for 2016 is a schematic value)", fontsize=12)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, fontsize=11)

# Add grid lines and background color
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f8f9fa')

# Optimize text annotations - Use box annotations instead of direct annotations on the bars
for i, (bar, label) in enumerate(zip(bars, labels)):
    height = bar.get_height()
    ax.annotate(label,
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 15),  # Vertical offset
                textcoords="offset points",
                ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                fontsize=9)

# Add a legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1, frameon=False)

plt.tight_layout()
plt.show()