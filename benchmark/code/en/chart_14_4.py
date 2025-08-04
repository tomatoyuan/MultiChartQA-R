import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['Elderly', 'Children/Toddlers', 'Women', 'Pets']
influence_level = [8, 7, 6, 5]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Set the background color and grid
ax.set_facecolor('#FFF8E7')  # Warm light orange background
ax.grid(axis='y', linestyle='--', alpha=0.3, color='gray')

# Draw a beautified bar chart
colors = plt.cm.Reds(np.linspace(0.6, 0.9, len(groups)))  # Gradient color
bars = ax.bar(groups, influence_level, color=colors, width=0.6, 
              edgecolor='black', linewidth=0.5)

# Add a title and subtitle
ax.set_title('Groups Prone to "Air - Conditioning Disease"', fontsize=18, pad=20, fontweight='bold')

# Adjust the axes
ax.set_ylim(0, 10)  # Fix the y - axis range for more intuitive comparison
ax.set_yticks([])  # Hide the y - axis tick marks
ax.set_xlabel('Group Types', fontsize=12, labelpad=10)

# Beautify the x - axis labels
ax.tick_params(axis='x', which='major', labelsize=12, pad=10)

# Hide the top, right, and left axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add a short description above each bar
for bar, group in zip(bars, groups):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{group}', ha='center', va='bottom', fontweight='bold', fontsize=12)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()