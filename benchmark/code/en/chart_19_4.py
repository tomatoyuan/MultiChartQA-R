import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Female', 'Male']
values = [60, 40]
colors = ['#FF7B9C', '#7BC8F6']  # Soft pink and blue

# Create a chart
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the chart size
ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.2, alpha=0.8)

# Add title and labels
ax.set_title('Gender Distribution of "Most Regretful" Consumers', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Percentage (%)', fontsize=14, labelpad=10)

# Set the y-axis range and ticks
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Beautify the axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Display value labels
for i, v in enumerate(values):
    ax.text(i, v + 2, f'{v}%', ha='center', fontsize=14, fontweight='bold')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()