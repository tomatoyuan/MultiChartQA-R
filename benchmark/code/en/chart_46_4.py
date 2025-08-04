import matplotlib.pyplot as plt
import numpy as np

# Data organization
categories = ['Basic Functions', 'Advanced Functions', 'Multidimensional Experience']
sub_categories = {
    'Basic Functions': ['Seating Comfort', 'Quality and Safety', 'Product Durability', 'Function Support'],
    'Advanced Functions': ['Ease of Operation', 'Adjustability', 'Green Environmental Friendliness'],
    'Multidimensional Experience': ['Intelligent Interaction', 'Emotional Value and Healing Function', 'Aesthetic Design', 'Personalization']
}
values = {
    'Basic Functions': [62, 56, 47, 43],
    'Advanced Functions': [38, 33, 28],
    'Multidimensional Experience': [25, 23, 22, 17]
}

# Used to set the position of each group of bars
x_positions = {}
bar_width = 0.25
spacing = 0.5  # Spacing between different main categories

# Dynamically calculate the x - position of each main category
current_x = 0
for cat in categories:
    n_sub = len(sub_categories[cat])
    x_positions[cat] = np.arange(current_x, current_x + n_sub)
    current_x += n_sub + spacing

# Create a figure
fig, ax = plt.subplots(figsize=(14, 8))  # Increase the figure height to accommodate labels

# Draw each group of bars and add percentage labels
for i, cat in enumerate(categories):
    bars = ax.bar(x_positions[cat], values[cat], width=bar_width, label=cat)

    # Add percentage labels to each bar
    for bar, value in zip(bars, values[cat]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{value}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Add sub - category labels for each main category (fine - tune the position)
    for j, pos in enumerate(x_positions[cat]):
        ax.text(pos, -3.5, sub_categories[cat][j], ha='center', rotation=45, fontsize=9)

# Set x - axis ticks (here we only need to mark the starting position of each main category)
ax.set_xticks([x_positions[cat][0] for cat in categories])
ax.set_xticklabels(categories)

# Add title, legend and labels
ax.set_title('Consumers\' Demands for Seat Consumption', fontsize=14)
ax.set_xlabel('Demand Types', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.legend()

# Set the y - axis range to make negative labels and numerical labels visible
ax.set_ylim(bottom=-5, top=75)  # Adjust the y - axis upper limit to ensure labels are not out of range

# Add grid lines for easy reading of values
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()