import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Build data
provinces = ["Guangdong", "Zhejiang", "Beijing", "Guangxi", "Shandong", "Sichuan", "Fujian", "Shanghai", "Liaoning", "Others"]
percentages = [16.3, 7.5, 6.2, 5.7, 5.7, 5.6, 4.7, 4.5, 4.4, 31.9]

# Create a canvas and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set gradient colors (use a different color for "Others", and gradients for the rest of the provinces)
other_color = '#FF6B6B'  # Red for "Others"
province_colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(provinces) - 1))
colors = list(province_colors) + [other_color]  # Province gradients first, followed by the color for "Others"

# Draw a horizontal bar chart
bar_width = 0.6
y_pos = np.arange(len(provinces))
bars = ax.barh(y_pos, percentages, height=bar_width, color=colors, edgecolor='black', alpha=0.8)

# Customize the "kebab" style
for i, (province, percent) in enumerate(zip(provinces, percentages)):
    # Calculate the number of beads
    bead_count = max(1, int(percent * 0.7))  # Determine the number of beads based on the percentage

    # Draw the beads (circles)
    for j in range(bead_count):
        bead_x = 0.5 + j * 0.8  # Bead x - position
        if bead_x < percent - 0.5:  # Ensure the beads do not exceed the bar range
            # Use red beads for the "Others" item, and yellow gradients for the rest
            if i == len(provinces) - 1:
                bead_color = plt.cm.Reds(j/bead_count)
            else:
                bead_color = plt.cm.YlOrRd(j/bead_count)
            circle = mpatches.Circle(
                (bead_x, y_pos[i]),
                radius=0.15,
                color=bead_color,
                alpha=0.9
            )
            ax.add_patch(circle)

    # Add province labels (on the left)
    ax.text(-1.5, y_pos[i], province, ha='center', va='center', fontweight='bold', fontsize=11)

# Add percentage value labels (with background boxes)
for i, rect in enumerate(bars):
    width = rect.get_width()
    ax.text(
        width + 0.3, rect.get_y() + rect.get_height()/2,
        f'{percentages[i]:.1f}%',  # Keep one decimal place
        ha='left', va='center',
        fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.2')
    )

# Set the axes and title
ax.set_xlim(-2, max(percentages) + 5)  # Adjust the x - axis range
ax.set_ylim(-0.8, len(provinces) - 0.2)  # Adjust the y - axis range
ax.set_title('European Cup Drives the Food Economy - Top 10 Provinces in Total Late - Night Snack Consumption Amount', fontsize=16, pad=15, fontweight='bold')
ax.set_xlabel('Consumption Proportion (%)', fontsize=12, labelpad=10)
ax.set_yticks([])  # Hide the default y - axis labels

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Add a legend and move it down
province_patch = mpatches.Patch(color=province_colors[0], label='Provinces')
other_patch = mpatches.Patch(color=other_color, label='Total of Other Regions')
ax.legend(handles=[province_patch, other_patch],
          loc='upper right',
          bbox_to_anchor=(0.98, 0.85))  # Adjust the bbox_to_anchor parameter to move it down

# Beautify the border
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# Display the chart
plt.tight_layout()
plt.show()