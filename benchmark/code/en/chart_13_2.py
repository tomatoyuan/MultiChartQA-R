import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Organize data
age_groups = ["Under 18", "18 - 24", "25 - 34", "35 - 49", "Over 50"]
sample_coverage = [23.1, 22.16, 39.41, 12.12, 2.8]  # Sample coverage data
total_coverage = [12.4, 28.44, 36.63, 20.16, 3.2]  # Total coverage data

x = np.arange(len(age_groups))  # x-axis tick positions
width = 0.35  # Bar width

# Create a figure and a subplot, optimize the figure size for adaptation
fig, ax = plt.subplots(figsize=(10, 7))
# Set the overall background color, similar to the blue in the original figure
fig.set_facecolor('#00a8e8')
ax.set_facecolor('#00a8e8')

# Draw the sample coverage bar chart, adjust the color to be softer
rects1 = ax.bar(
    x - width/2, 
    sample_coverage, 
    width, 
    label='Sample Coverage', 
    color='#003f5c',
    edgecolor='white',  # Add white strokes to distinguish columns
    linewidth=1
)
# Draw the total coverage bar chart, adjust the color to be softer
rects2 = ax.bar(
    x + width/2, 
    total_coverage, 
    width, 
    label='Total Coverage', 
    color='#457fca',
    edgecolor='white',  # Add white strokes to distinguish columns
    linewidth=1
)

# Customize the title style
ax.set_title(
    'Observation Mode: Office Workers are the Most Affected', 
    fontsize=20, 
    fontweight='bold', 
    color='#002f4a',  # Darker title for better visibility
    pad=20  # Increase the spacing between the title and the chart
)
ax.set_ylabel(
    'Population Attribute Distribution of Rainstorm Public Opinion', 
    fontsize=14, 
    color='#333333',
    labelpad=15  # Increase the spacing between the y-axis label and the chart
)

# Customize the x-axis tick label style
ax.set_xticks(x)
ax.set_xticklabels(
    age_groups, 
    fontsize=12, 
    color='#333333',
    rotation=0  # Keep horizontal display
)

# Optimize the y-axis scale, display percentages more clearly
ax.set_ylim(0, 50)  # Set a reasonable y-axis range
ax.yaxis.set_major_formatter('{x}%')  # Directly display the percentage style (requires matplotlib 3.3+)
ax.tick_params(axis='y', labelsize=12, colors='#333333')

# Optimize the data label style
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f'{height}%',
            xy=(rect.get_x() + rect.get_width()/2, height),
            xytext=(0, 5),  # Adjust the label position to avoid occlusion
            textcoords='offset points',
            ha='center', 
            va='bottom',
            fontsize=11,
            color='white',  # White labels are more eye-catching
            fontweight='bold'
        )

autolabel(rects1)
autolabel(rects2)

# Customize the legend style, place it above the chart
legend_elements = [
    Patch(facecolor='#003f5c', edgecolor='white', label='Sample Coverage'),
    Patch(facecolor='#457fca', edgecolor='white', label='Total Coverage')
]
ax.legend(
    handles=legend_elements,
    loc='upper center',  # Legend position
    bbox_to_anchor=(0.5, 1.15),  # Fine-tune the legend position above the chart
    ncol=2,  # Display the legend in two columns
    fontsize=12,
    frameon=False  # Remove the legend border
)

# Add gridlines to enhance readability
ax.grid(
    axis='y', 
    color='white', 
    linestyle='--', 
    alpha=0.8,
    linewidth=1
)

# Optimize the overall layout
plt.tight_layout()
# Display the chart
plt.show()