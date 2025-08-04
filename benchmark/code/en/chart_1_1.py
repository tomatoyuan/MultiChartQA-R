import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Data preparation
age_groups = ['Under 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Over 65']
data = [20, 30, 15, 12, 10, 8, 8]

# Create gradient colors
colors = plt.cm.Blues(np.linspace(0.8, 0.4, len(age_groups)))
highlight_index = 1  # Highlight the second age group
colors[highlight_index] = plt.cm.Oranges(0.6)  # Use orange for highlighting

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# Set background style
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Draw a bar chart
bars = ax.bar(age_groups, data, color=colors, edgecolor='black', linewidth=0.5, alpha=0.9)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height}', ha='center', va='bottom', fontsize=10)

# Set title and labels
ax.set_title('Analysis of Age Groups of Coronary Heart Disease Search Population', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Age Group', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Searchers', fontsize=12, labelpad=10)

# Set the y - axis range and ticks
ax.set_ylim(0, max(data) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend
legend_labels = ['Other age groups' if i != highlight_index else '18 - 24 (Highest)' for i in range(len(age_groups))]
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(age_groups))]
ax.legend(handles[0:2], legend_labels[0:2], loc='upper right')

# Adjust the layout
plt.tight_layout()

# Display the graph
plt.show()