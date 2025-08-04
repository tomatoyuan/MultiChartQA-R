import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator  # Import MultipleLocator
from matplotlib.patches import Patch  # Import Patch for creating custom legend items
from matplotlib.lines import Line2D   # Import Line2D for creating custom legend items

# Data
categories = ['Married', 'Unmarried']
gender_percent = [80, 20]
tgi_values = [60, 90]

x = np.arange(len(categories))

# Create a chart
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)  # Increase the chart height to leave space for the legend below

# Draw a bar chart of gender percentage
bar_plot = ax1.bar(categories, gender_percent, color='#4A7AFE', width=0.5, label='Marital Status')
ax1.set_ylabel('Marital Status (%)', fontsize=12, color='#4A7AFE')
ax1.set_ylim([0, 100])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the tick interval of the left y-axis to 50
ax1.yaxis.set_major_locator(MultipleLocator(50))

# Create a second y-axis to draw the TGI line chart
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylabel('TGI', fontsize=12, color='#FF9900')
ax2.set_ylim(0, 150)

# Set the tick interval of the right y-axis to 50
ax2.yaxis.set_major_locator(MultipleLocator(50))

ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Add a title
plt.title('Marital Status of People Engaged in the Legal Service Industry', fontsize=14, fontweight='bold')

# Add data labels to the bar chart
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 1.5,
             f'{gender_percent[i]}%',
             ha='center', va='bottom', fontsize=12, color='#4A7AFE', fontweight='bold')

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    # Adjust the label position to be above or below the data point to avoid overlap
    y_offset = 7 if i == 0 else -10  # The married point is offset upward, and the unmarried point is offset downward
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, y_offset),
                textcoords='offset points',
                ha='center', va='bottom' if y_offset > 0 else 'top',
                fontsize=12,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combine the legends and adjust the position to below the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Marital Status'),  # Bar chart legend
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)  # Line chart legend
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimize the layout to leave space for the legend
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Adjust the chart boundary, leaving 10% space at the bottom

# Display the chart
plt.show()