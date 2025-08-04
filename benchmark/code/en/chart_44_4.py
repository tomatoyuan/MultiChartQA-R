import matplotlib.pyplot as plt
import numpy as np

# Snack categories
categories = ['Sweet drinks', 'Chewy snacks', 'Fried puffed foods', 'Yogurt', 'Baked goods', 'Nuts', 'Spicy snacks', 'High - sugar foods', 'Dried fruits and candied fruits']
# Corresponding selection percentages
percentages = [55, 43, 43, 42, 42, 39, 38, 36, 33]

# Create a canvas and a sub - plot, adjust the size
fig, ax = plt.subplots(figsize=(12, 6))

# Set gradient colors
cmap = plt.cm.get_cmap('viridis', len(categories))
colors = [cmap(i) for i in range(len(categories))]

# Draw a bar chart, add transparency and borders
rects = ax.bar(categories, percentages, color=colors, alpha=0.8, edgecolor='black', linewidth=0.8)

# Add a title and axis labels, set the font size
ax.set_title('Snack selection distribution of overtime workers when they get hungry at work', fontsize=16, pad=15)
ax.set_ylabel('Selection percentage (%)', fontsize=14, labelpad=10)

# Set the y - axis range
ax.set_ylim(0, max(percentages) * 1.1)

# Set grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Label the values on the bars, adjust the position and style
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5),  # Vertical offset
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# Beautify the chart border
for spine in ax.spines.values():
    spine.set_linewidth(0.5)

# Rotate the x - axis labels to make them more readable
plt.xticks(rotation=30, ha='right', fontsize=11)

# Adjust the layout
plt.tight_layout()

plt.show()