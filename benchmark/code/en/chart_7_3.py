import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # Import PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Data
categories = ['High Consumption', 'Medium Consumption', 'Low Consumption']
consumption_level = [37, 40, 20]
tgi_values = [110, 90, 100]

x = np.arange(len(categories))

# Create the chart
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)

# Plot the consumption level bar chart
bar_plot = ax1.bar(categories, consumption_level, color='#4A7AFE', width=0.5)
ax1.set_ylim([0, 60])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the left y - axis to percentage format and remove the y - axis label
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(20))

# Create a second y - axis to plot the TGI line chart
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', linewidth=2)
ax2.set_ylim(0, 150)
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Set the tick interval for the right y - axis and remove the y - axis label
ax2.yaxis.set_major_locator(MultipleLocator(50))

# Add a title
plt.title('Consumption Level of People Engaged in the Legal Service Industry', fontsize=14, fontweight='bold')

# Add data labels to the bar chart
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1,
             f'{consumption_level[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE', fontweight='bold')

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, 7),  # Vertical offset
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combine the legends and adjust the position to below the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Consumption Level'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimize the layout
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Display the chart
plt.show()