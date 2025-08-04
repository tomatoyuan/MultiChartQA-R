import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data
channels = ['Online E-commerce\n Channels', 'Hypermarkets and \nTraditional Supermarkets', 'Community Group Buying', 'Grocery Stores and \nConvenience Stores', 'Warehouse Membership Stores', 'High-end Supermarkets']
values = [80.5, 63.5, 39.9, 31.2, 20.8, 16.7]

# Color gradient (from light purple to dark purple)
colors = plt.cm.PuBu(np.linspace(0.4, 0.9, len(channels)))

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(channels, values, color=colors)

# Set the border area, a little farther from the bars
ax.add_patch(patches.Rectangle(
    (-5, -0.5),  # Left offset
    100,          # Width covers the maximum value + offset
    1,         # Height is slightly greater than a single line
    linewidth=2,
    edgecolor='saddlebrown',
    facecolor='none',
    linestyle='dotted'
))

# Value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
            f'{width:.1f}%', va='center', fontsize=10, color='black')

# Style settings
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel('Proportion (%)', fontsize=12)
ax.set_title('Distribution of Consumer Channels for Purchasing Tissue Paper', fontsize=14, pad=15)

# Data source
plt.figtext(0.5, -0.05, 'Data Source: CBNData Survey on Chinese Consumer Tissue Paper Trends in March 2024\nData Description: Which channels do you use to purchase tissue paper? N = 1000',
            ha='center', fontsize=9)

plt.tight_layout()
plt.show()