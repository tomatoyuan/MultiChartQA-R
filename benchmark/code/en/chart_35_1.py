import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2000, 2019, 2020, 2021]
life_expectancy = [66.8, 73.2, 72.5, 71.4]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Convert years to categorical variables (uniform distribution)
y_pos = np.arange(len(years))

# Draw a horizontal bar chart with gradient color filling
colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(years)))
bars = ax.barh(y_pos, life_expectancy, color=colors, alpha=0.8, edgecolor='gray', linewidth=0.5)

# Add data labels
for bar, value in zip(bars, life_expectancy):
    ax.text(bar.get_width() + 0.2,
            bar.get_y() + bar.get_height() / 2,
            f'{value}',
            va='center',
            fontweight='bold',
            fontsize=10)

# Add an auxiliary note indicating the same level as 2012
ax.annotate('Same level as 2012',
            xy=(71.4, y_pos[-1]),
            xytext=(73, y_pos[-1] - 0.3),
            arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8),
            fontsize=10)

# Set y - axis tick labels to years (uniform distribution)
ax.set_yticks(y_pos)
ax.set_yticklabels(years, fontsize=11)

# Set the x - axis range and ticks
ax.set_xlim(65, 75)
ax.set_xticks(np.arange(65, 76, 1))

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Add a title and subtitle
fig.suptitle('Impact of the COVID - 19 pandemic on global life expectancy',
             fontsize=16,
             fontweight='bold',
             y=0.96)

ax.set_title('Global life expectancy trend (2000 - 2021)',
             fontsize=13,
             loc='left',
             pad=12)

# Add a legend
ax.legend([bars[0]], ['Life expectancy (years)'], loc='lower right')

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the layout
plt.subplots_adjust(bottom=0.1, left=0.15)

# Display the chart
plt.show()