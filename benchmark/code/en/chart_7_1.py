import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator  # Import MultipleLocator
from matplotlib.patches import Patch  # Import Patch for creating custom legend items
from matplotlib.lines import Line2D   # Import Line2D for creating custom legend items

# Data
categories = ['Male', 'Female']
gender_percent = [51, 49]  # Gender proportion
tgi_values = [85, 115]  # TGI values, can be adjusted according to actual situation

x = np.arange(len(categories))

# Create the chart
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)  # Increase the chart height to leave space for the legend below

# Draw the gender proportion bar chart
bar_plot = ax1.bar(categories, gender_percent, color='#4A7AFE', width=0.5, label='Gender')
ax1.set_ylabel('Gender Proportion (%)', fontsize=12, color='#4A7AFE')
ax1.set_ylim([46, 52])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=12)

# Set the tick interval of the left y-axis to 2
ax1.yaxis.set_major_locator(MultipleLocator(2))

# Create a second y-axis to draw the TGI line chart
ax2 = ax1.twinx()
line_plot = ax2.plot(categories, tgi_values, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylabel('TGI', fontsize=12, color='#FF9900')
ax2.set_ylim(0, 150)

# Set the tick interval of the right y-axis to 50
ax2.yaxis.set_major_locator(MultipleLocator(50))

ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Add a title
plt.title('Gender Ratio of People Engaged in the Legal Service Industry', fontsize=14, fontweight='bold')

# Add data labels to the bar chart
for i, rect in enumerate(bar_plot):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height + 0.1,
             f'{gender_percent[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(categories, tgi_values)):
    # Adjust the label position to be on the right side of the data point
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(10, 0),  # Offset 10 points to the right
                textcoords='offset points',
                ha='left', va='center',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

# Combine the legends and adjust the position to below the chart
legend_items = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Gender'),  # Legend for the bar chart
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)  # Legend for the line chart
]

ax1.legend(handles=legend_items, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimize the layout to leave space for the legend
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Adjust the chart boundary, leaving 10% space at the bottom

# Display the chart
plt.show()