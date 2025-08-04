import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Data
categories = ['Undergraduate and above', 'Junior college', 'High school and below']
education_level = [20, 30, 60]  # Education level data
tgi_values = [140, 125, 100]  # TGI data

x = np.arange(len(categories))

# Create the chart
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)

# Draw the education level bar chart
bar_plot = ax1.bar(categories, education_level, color='#4A7AFE', width=0.5, label='Education level')
ax1.set_ylim([0, 80])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the tick interval and format for the left y-axis
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(20))

# Create a second y-axis to draw the TGI line chart
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# Set the tick interval for the right y-axis
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Add the title
plt.title('Educational level of people engaged in the legal service industry', fontsize=14, fontweight='bold')

# Add data labels to the bar chart
for rect in bar_plot:
    height = rect.get_height()
    # Add percentage labels to the top center of the bar chart
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1.5,
             f'{height}%',
             ha='center', va='bottom', fontsize=11, color='#4A7AFE', fontweight='bold')

# Add data labels to the line chart
for i, (cat, tgi) in enumerate(zip(categories, tgi_values)):
    # Adjust the label offset according to the data point position to avoid overlap
    y_offset = 5 if tgi < 130 else 8  # Increase the offset appropriately for higher values
    ax2.annotate(f'{tgi}',
                 xy=(i, tgi),  # Use the index for positioning to avoid Chinese coordinate issues
                 xytext=(0, y_offset),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 fontsize=11, color='#FF9900', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combine the legends and adjust the position to the bottom of the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Education level distribution'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1),
           ncol=2, fontsize=10)

# Optimize the layout to leave space for the legend
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Display the chart
plt.show()