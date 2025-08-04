import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Data
cities = ['Beijing', 'Shenzhen', 'Xi\'an', 'Wuhan', 'Shanghai', 'Chengdu', 'Changsha', 'Chongqing', 'Guangzhou', 'Dongguan']
single_men = [68, 75, 62, 58, 65, 57, 54, 51, 59, 53]  # Number of single men (in ten thousands)
single_women = [72, 68, 59, 56, 69, 61, 58, 53, 63, 50]  # Number of single women (in ten thousands)

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Set bar chart parameters
x = np.arange(len(cities))
width = 0.35
bar_positions_men = x - width/2
bar_positions_women = x + width/2

# Define gradient color
def gradient_color(base_color, alpha):
    """Generate a gradient color based on the base color and transparency"""
    from matplotlib.colors import to_rgba
    return to_rgba(base_color, alpha)

# Draw gradient bar chart
base_color_men = '#4361EE'
base_color_women = '#3F37C9'

for i, (m, w) in enumerate(zip(single_men, single_women)):
    # Bar chart for men (with gradient effect)
    ax.bar(bar_positions_men[i], m, width, 
           color=gradient_color(base_color_men, 0.9), 
           edgecolor='#2b49a0', linewidth=0.8)
    
    # Bar chart for women (with gradient effect)
    ax.bar(bar_positions_women[i], w, width, 
           color=gradient_color(base_color_women, 0.9), 
           edgecolor='#282480', linewidth=0.8)

# Set title and labels
ax.set_title('Top Ten Cities with the Largest Number of Single Men and Women in China', 
             fontsize=20, fontweight='bold', pad=20, color='#333333')
ax.set_xlabel('Cities', fontsize=16, labelpad=15, color='#555555')
ax.set_ylabel('Number of Single People (in ten thousands)', fontsize=16, labelpad=15, color='#555555')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(cities, rotation=30, ha='right', fontsize=14, color='#555555')

# Set y - axis range and ticks
ax.set_ylim(0, max(max(single_men), max(single_women)) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure y - axis ticks are integers

# Add value labels
def add_labels(positions, heights, colors):
    for pos, height, color in zip(positions, heights, colors):
        ax.text(pos, height + 1, f'{height}', 
                ha='center', va='bottom', 
                fontsize=12, fontweight='bold', color=color)

add_labels(bar_positions_men, single_men, ['#2b49a0']*len(cities))
add_labels(bar_positions_women, single_women, ['#282480']*len(cities))

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7, color='#cccccc')

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=base_color_men, edgecolor='#2b49a0', label='Single Men'),
                   Patch(facecolor=base_color_women, edgecolor='#282480', label='Single Women')]
ax.legend(handles=legend_elements, loc='upper right', fontsize=14)

# Add horizontal reference line
ax.axhline(y=60, color='#e0e0e0', linestyle='-', linewidth=1)

# Beautify the border
for spine in ax.spines.values():
    spine.set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('#cccccc')

# Add data source annotation
ax.annotate('Data Source: Fictitious data (for example only)',
            xy=(0.05, 0.01), xycoords='figure fraction',
            fontsize=10, color='#999999')

# Adjust the layout
plt.tight_layout()

# Display the graph
plt.show()

# Save the chart (uncomment to save)
# plt.savefig('single_population_chart_beautiful.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())