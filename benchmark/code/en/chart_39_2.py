import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Once a day or more', '2-3 times a week', '2-3 times a month', 'Occasionally (≤1 time a month)']
values = [32, 47, 17, 4]

# Optimized color scheme with modern colors
colors = ['#4a86e8', '#4a86e8', '#b7b7b7', '#e6e6e6']

# Create figure and subplot with appropriate size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bar chart with borders and transparency
bars = ax.bar(labels, values, color=colors, edgecolor='black', alpha=0.85, width=0.6)

# Add value labels with optimized position and style
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 0.5,  # Fine-tune label position
        f'{height}%',
        ha='center', 
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# Set title with style
ax.set_title('Coffee Consumption Frequency of Consumers in Jing\'an District, Shanghai', fontsize=16, fontweight='bold', pad=20)

# Set y-axis label and range
ax.set_ylabel('Percentage (%)', fontsize=12, labelpad=10)
ax.set_ylim(0, max(values) * 1.15)  # Adjust y-axis range to leave space

# Beautify axes
ax.tick_params(axis='x', rotation=0, labelsize=11)  # Keep x-axis labels horizontal
ax.tick_params(axis='y', labelsize=10)

# Set grid lines (only horizontal)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Hide right and top spines, enhance left and bottom spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Adjust layout
plt.tight_layout(pad=2)

# Display chart
plt.show()