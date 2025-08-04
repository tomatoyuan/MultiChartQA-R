import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Data (estimated visually from the chart, replace with accurate data if available)
categories = ['Under 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Over 65']
age_percent = [2, 10, 45, 25, 15, 5, 3]  # Age proportion
tgi_values = [60, 90, 120, 100, 90, 110, 180]  # TGI data

x = np.arange(len(categories))

# Create the chart
fig, ax1 = plt.subplots(figsize=(12, 6), dpi=100)

# Plot the age proportion bar chart
bar_plot = ax1.bar(categories, age_percent, color='#4A7AFE', width=0.5, label='Age')
ax1.set_ylim([0, 55])  # Increase the upper limit to leave space for annotations
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the tick interval for the left y-axis
ax1.yaxis.set_major_locator(MultipleLocator(10))

# Add data annotations to the bar chart
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1,
             f'{age_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# Create a second y-axis to plot the TGI line chart
ax2 = ax1.twinx()
line_plot, = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', 
                      label='TGI', linewidth=2, markersize=8)
ax2.set_ylim(0, 220)  # Increase the upper limit to leave space for annotations

# Set the tick interval for the right y-axis
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Add data annotations to the line chart
for i, (x_val, y_val) in enumerate(zip(x, tgi_values)):
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, 10) if i != 6 else (0, -15),  # Place the annotation below for the last point
                textcoords="offset points",
                ha='center',
                va='bottom' if i != 6 else 'top',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#FF9900", alpha=0.8))

# Add the title
plt.title('Age of Divorce Litigation Population', fontsize=16, fontweight='bold')

# Combine the legends and adjust the position below the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Age Proportion'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI Index', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.12),
           ncol=2, fontsize=12, frameon=False)

# Add grid lines to enhance readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Optimize the layout to leave space for the legend
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Display the chart
plt.show()