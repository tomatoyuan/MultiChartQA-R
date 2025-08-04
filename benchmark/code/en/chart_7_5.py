import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # Import PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Data
categories = ['Under 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Over 65']
age_percent = [2, 15, 40, 30, 20, 5, 2]  # Age percentage data
tgi_values = [70, 130, 120, 90, 80, 60, 60]  # TGI data

x = np.arange(len(categories))

# Create a chart
fig, ax1 = plt.subplots(figsize=(10, 5), dpi=100)

# Draw a bar chart for age percentage
bar_plot = ax1.bar(categories, age_percent, color='#4A7AFE', width=0.5, label='Age')
ax1.set_ylim([0, 50])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the left - hand y - axis to percentage format
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(10))

# Create a second y - axis to draw the TGI line chart
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# Set the tick interval for the right - hand y - axis
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Add a title
plt.title('Age of Legal Service Industry Practitioners', fontsize=14, fontweight='bold')

# Add data labels to the bar chart
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1,
             f'{age_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE', fontweight='bold')

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    # Adjust the label position according to the TGI value to avoid overlap
    y_offset = 8 if y_val < 100 else 12
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, y_offset),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combine the legends and adjust the position to below the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Age Percentage'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.15),
           ncol=2, fontsize=10)

# Optimize the layout to make space for the legend
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Display the chart
plt.show()