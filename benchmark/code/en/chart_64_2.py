import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = [
    'Up 1%-20%', 'Up 21%-40%', 'Up 41%-60%', 'Up 61%-80%',
    'Up 81%-100%', 'Up over 100%', 'Basically unchanged', 'Down 1%-20%',
    'Four intervals of 21%-100% decline', 'Layout and investment by the group headquarters'
]
percentages = [20.3, 36.6, 10.6, 6.5, 6.5, 2.4, 8.1, 4.1, 0, 4.9]

# Color configuration (similar to the original image, use gray for decline categories and green for others)
colors = ['#a5d65d'] * 7 + ['#d3d3d3'] + ['#a5d65d'] * 2

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(labels))
bars = ax.barh(y, percentages, color=colors, height=0.6)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', fontsize=9, color='#333')

# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# Hide x-axis ticks
ax.set_xticks([])

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a title
ax.set_title('Increase/Decrease of Private Domain Layout Costs of Chinese Merchants in 2022 Compared with the Initial Layout',
             fontsize=14, fontweight='bold', pad=20)

# Adjust the layout
plt.tight_layout()
plt.show()