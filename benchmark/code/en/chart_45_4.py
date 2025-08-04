import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Basic Sunscreen', 'Functional and Fashionable Sunscreen Clothing', 'Luxury Sunscreen/Sunscreen Clothing Sets']
price_ranges = [
    ['Under 100 yuan', '100 - 150 yuan'],
    ['150 - 200 yuan', '200 - 250 yuan'],
    ['250 - 300 yuan', '300 - 500 yuan', 'Over 500 yuan']
]
percentages = [
    [3, 15],
    [29, 24],
    [16, 10, 3]
]

# Ensure all price ranges have legends
all_price_ranges = ['Under 100 yuan', '100 - 150 yuan', '150 - 200 yuan', '200 - 250 yuan', '250 - 300 yuan', '300 - 500 yuan', 'Over 500 yuan']

# Set graphic parameters
bar_width = 0.6
y_positions = np.arange(len(categories))

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define a color list to ensure the same color for each price range
colors = plt.cm.tab20.colors

# Draw a horizontal bar chart
bottoms = [0] * len(categories)
for i, (ranges, percs) in enumerate(zip(price_ranges, percentages)):
    for j, (price_range, percent) in enumerate(zip(ranges, percs)):
        color_idx = all_price_ranges.index(price_range)
        label = price_range  # Set a label for each price range
        ax.barh(y_positions[i], percent, bar_width, left=bottoms[i], 
                label=label, alpha=0.8, color=colors[color_idx])
        bottoms[i] += percent

# Add data labels
for i, (ranges, percs) in enumerate(zip(price_ranges, percentages)):
    current_bottom = 0
    for j, (price_range, percent) in enumerate(zip(ranges, percs)):
        if percent > 0:  # Only add labels when the percentage is greater than 0
            ax.text(current_bottom + percent/2, i, f"{percent}%", 
                    ha='center', va='center', color='black', fontweight='bold')
        current_bottom += percent

# Set chart attributes
ax.set_yticks(y_positions)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage (%)')
ax.set_title('Consumers\' Tendency of Purchase Price Ranges for Sunscreen Clothing and Supplies')

# Adjust the legend
handles, labels = ax.get_legend_handles_labels()
# Create unique legend items
unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
ax.legend(*zip(*unique), loc='lower right')

# Show grid lines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust the layout
plt.tight_layout()

# Show the chart
plt.show()