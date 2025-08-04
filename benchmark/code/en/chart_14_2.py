import matplotlib.pyplot as plt
import numpy as np

# Province names and simulated data (can be replaced with actual data)
provinces = ['Guangdong', 'Zhejiang', 'Shandong', 'Jiangsu', 'Beijing', 'Shanghai', 'Fujian', 'Henan', 'Sichuan', 'Hebei']
blue_percents = [100, 95, 80, 75, 60, 55, 50, 45, 40, 30]
white_percents = [100 - p for p in blue_percents]

# Sort the data (ascending order)
sorted_data = sorted(zip(blue_percents, white_percents, provinces))
blue_percents, white_percents, provinces = zip(*sorted_data)

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Set gradient colors (from light blue to dark blue)
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(provinces)))

# Draw a beautified horizontal stacked bar chart
bar_white = ax.barh(provinces, white_percents, color='white', edgecolor='lightgray', linewidth=0.8)
bar_blue = ax.barh(provinces, blue_percents, left=white_percents, color=colors, edgecolor='gray', linewidth=0.8)

# Add data labels
for i, (blue, white) in enumerate(zip(blue_percents, white_percents)):
    # Add percentage labels in the middle of the blue area
    ax.text(white + blue/2, i, f'{blue}', ha='center', va='center', 
            color='white' if blue > 40 else 'navy', fontweight='bold')

# Set the title and bottom explanatory text
ax.set_title('Attention of Each Province to Air - Conditioners', fontsize=14, pad=15)

# Set grid lines
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Hide the top, right, and bottom axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Adjust tick and label styles
ax.tick_params(axis='y', which='major', labelsize=10, pad=10)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

# Add a left reference line
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.5)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()