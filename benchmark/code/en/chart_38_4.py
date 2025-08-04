import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Water content/Oxygen permeability', 'Material composition', 'Wearing parameters', 'Place of origin', 'Replacement schedule', 'Color process', 'Brand reputation', 'Price level', 'Related services', 'Packaging and storage']
values = [52, 52, 46, 45, 43, 43, 42, 41, 40, 35]

# Define y-axis positions
y_pos = np.arange(len(labels))

# Optimized gradient color scheme (from dark blue to light blue)
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(labels)))

# Create a figure (increase the size)
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart (increase margins and transparency)
bars = ax.barh(y_pos, values, color=colors, alpha=0.85, edgecolor='gray', linewidth=0.5)

# Set y-axis labels (increase label spacing)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10)

# Set x-axis label and title
ax.set_xlabel('Attention percentage', fontsize=12)
ax.set_title('Professional dimensions of consumers\' attention to contact lenses', fontsize=14, pad=15)

# Optimize numerical labels (increase font size and color)
for i, v in enumerate(values):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=10, color='black')

# Add grid lines (lighter grid)
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Set the x-axis range (increase margins)
ax.set_xlim(0, max(values) * 1.1)

# Beautify the border (hide the top and right borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()