import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# Data
labels = [
    "Motivated to choose a more comfortable lifestyle in the past year",
    "Learned more about women - related issues from the outside world but didn't express publicly",
    "Participated in public discussions about women's topics in the past year",
    "Never really paid attention, thinking it's too far from my life and just focus on my own life",
    "Tried to influence other women around by speaking out in the past year (girls help girls)",
    "Reduced attention deliberately in the past year due to the topic being overly saturated"
]
percentages = [41.9, 18.3, 17.4, 10.1, 8.0, 4.3]

# Create a custom gradient color
colors = ["#4a6fe3", "#6a89f0", "#8aa5f7", "#a9bffb", "#c7d8fd", "#e5f0ff"]

# Create a chart
fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(labels))

# Draw a horizontal gradient - colored bar chart
for i, (value, label) in enumerate(zip(percentages, labels)):
    bar = ax.barh(i, value, align='center', color=colors[i], alpha=0.9, edgecolor='none')
    ax.text(value + 0.5, i, f'{value}%', va='center', fontsize=11, color='#333333')

# Set the Y - axis labels
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12)
ax.invert_yaxis()  # Arrange the labels from top to bottom

# Set the X - axis range
ax.set_xlim(0, max(percentages) * 1.15)  # Leave some space to display the labels

# Add gridlines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set the title and labels
ax.set_title('Survey on the impact of women - related topics on individual women', fontsize=16, pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12, labelpad=10)

# Adjust the borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()