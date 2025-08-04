import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Data preparation
industries = [
    'Health Care', 'Real Estate/Construction', 'Wholesale/Retail', 'Automotive',
    'Government/Non - profit Organizations', 'Hotel/Tourism', 'Finance',
    'Advertising/Marketing', 'IT/Internet'
]
coverage = [2.9, 3.5, 5.1, 6.1, 7.5, 8.2, 9.2, 19.9, 21.9]

# Create a gradient color map
cmap = LinearSegmentedColormap.from_list("custom_green", ["#E8F5E9", "#2E7D32"])

# Create a plotting object
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#F5F5F5')  # Set the chart background color
ax.set_facecolor('#FAFAFA')  # Set the axis background color

# Draw a horizontal bar chart (using gradient color)
y_pos = np.arange(len(industries))
bars = ax.barh(y_pos, coverage, color='#4CAF50', edgecolor='#2E7D32', linewidth=0.8)

# Apply gradient color
for i, bar in enumerate(bars):
    bar.set_color(cmap(i/len(bars)))

# Add data labels (optimize position and style)
for i, v in enumerate(coverage):
    ax.text(v + 0.3, i, f'{v}%', va='center', fontsize=11,
            fontweight='medium', color='#333333')

# Set the title and axis labels (optimize font and position)
ax.set_title('Which industries are more concerned about "Valentine\'s Day gifts"?',
             fontsize=18, pad=20, fontweight='bold', color='#333333')
ax.set_xlabel('Industry Coverage (%)', fontsize=13, labelpad=15, color='#555555')
ax.set_ylabel('Industry Categories', fontsize=13, labelpad=15, color='#555555')

# Set y - axis tick labels
ax.set_yticks(y_pos)
ax.set_yticklabels(industries, fontsize=11, color='#444444')

# Optimize axis ticks and grid lines
ax.set_xlim(0, max(coverage) + 3)
ax.grid(axis='x', linestyle='--', alpha=0.6, color='#CCCCCC')

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')

# Adjust the layout
plt.tight_layout(pad=2)

# Display the chart
plt.show()