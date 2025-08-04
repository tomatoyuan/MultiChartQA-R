import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Minimum Standard", "6 - 9 years old", "10 - 13 years old", "14 - 17 years old"]
# Data (min), corresponding to the chart
data = [120, 64.3, 55.5, 44.9]
# The part that reaches the average in each category (schematic value, matching the visual effect of the chart)
avg_parts = [120, 30, 25, 20]
# Color settings
colors = ["#A4C639", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
avg_line_y = 54.9  # Average duration

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
for i in range(len(categories)):
    # Draw the bottom (gray or green)
    rect = ax.bar(x[i], data[i], width=bar_width, color=colors[i])
    # Draw the "average part" covered on the top (only the minimum standard does not need to be covered because it is green and exceeds the average)
    if categories[i] != "Minimum Standard":
        ax.bar(x[i], data[i] - avg_parts[i], bottom=avg_parts[i], width=bar_width, color=colors[0])
    # Add data labels
    ax.text(x[i], data[i] + 2, f'{data[i]}min', ha='center', va='bottom', color='black')

# Draw a yellow dotted line for the average duration
ax.axhline(y=avg_line_y, color='yellow', linestyle='--', linewidth=2)
ax.text(3.2, avg_line_y + 2, f'Average {avg_line_y}min', ha='left', va='bottom', color='gold', fontweight='bold')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Hide y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title('Outdoor sports situation of Chinese children and adolescents in 2018', fontsize=14, fontweight='bold')

# Beautify: hide the top, right and bottom borders
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()