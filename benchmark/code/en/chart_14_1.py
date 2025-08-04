import matplotlib.pyplot as plt
import numpy as np

# Names of summer essentials
labels = ['Air conditioner', 'Sunscreen', 'Parasol', 'Swimsuit', 'Insect repellent', 'Electric fan', 'Refrigerator', 'Watermelon', 'Cool mat']
# Corresponding "combat power" percentage data
values = [73.15, 48, 35, 26, 10, 8.4, 7.8, 5, -7.9]

# Data sorting (ascending order, but will be reversed when plotting to make larger values on top)
sorted_data = sorted(zip(values, labels), reverse=False)
values, labels = zip(*sorted_data)

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Set gradient color bars (darker color for larger values)
colors = plt.cm.Oranges(np.linspace(0.4, 0.9, len(values)))

# Draw a beautified horizontal bar chart
bars = ax.barh(labels, values, color=colors, edgecolor='gray', linewidth=0.8)

# Set the X-axis range (Key modification: extend negatively to -15)
ax.set_xlim(-15, max(values) + 5)

# Add background grid lines
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Set the title and labels
ax.set_title('Summer Essentials "Combat Power" Ranking', fontsize=16, pad=15)
ax.set_xlabel('"Combat Power" Percentage', fontsize=12, labelpad=10)

# Adjust the tick and label styles
ax.tick_params(axis='both', which='major', labelsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Optimize the data label positions (adjust according to the new X-axis range)
for bar, value in zip(bars, values):
    # Adjust the position of positive value labels and increase the spacing
    x_pos = value + 0.8 if value > 0 else value - 0.8
    # Adjust the position of negative value labels according to the X-axis range
    ax.text(x_pos,
            bar.get_y() + bar.get_height()/2,
            f'{value}%',
            ha='left' if value > 0 else 'right',
            va='center',
            fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Add a reference line (at the 0 position)
ax.axvline(x=0, color='black', linestyle='-', alpha=0.3)

# Add a background color to the negative area (optional beautification)
ax.axvspan(-15, 0, alpha=0.05, color='lightgray')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()