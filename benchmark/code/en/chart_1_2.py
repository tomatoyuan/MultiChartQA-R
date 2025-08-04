import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_groups = ['Under 18', '18 - 24', '25 - 34', '35 - 44', 
              '45 - 54', '55 - 64', 'Over 65']
# Simulated data, generally in line with the diagram's proportions, can be fine - tuned according to actual situation
data = [22, 28, 14, 10, 7, 6, 5]  

# Set a modern color scheme - gradient from dark blue to light blue
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(age_groups)))
# Highlight the 18 - 24 age group
colors[1] = plt.cm.magma(0.6)

x = np.arange(len(age_groups))  # x-axis tick positions

# Create a figure and axes, use a wider canvas
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#ffffff')  # White background
ax.set_facecolor('#f5f5f5')  # Light gray axes background

# Draw a bar chart to add a sense of three - dimensionality
bars = ax.bar(x, data, width=0.7, color=colors, alpha=0.85, 
              edgecolor='#333333', linewidth=0.6)

# Add data labels above each bar and add a shadow effect
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.4,
            f'{height}', ha='center', va='bottom', 
            fontsize=11, fontweight='bold', color='black',
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.2'))

# Set x-axis tick labels to display horizontally
ax.set_xticks(x)
ax.set_xticklabels(age_groups, fontsize=12, fontweight='medium')

# Set the y-axis range and label, hide the y-axis tick marks
ax.set_ylim(0, max(data) * 1.2)
ax.set_ylabel('Search Proportion (%)', fontsize=13, fontweight='medium', labelpad=10)
ax.tick_params(axis='y', which='both', length=0)

# Add horizontal grid lines, use a lighter color
ax.grid(axis='y', linestyle='-', alpha=0.3, color='lightgray')

# Set the chart title and subtitle
ax.set_title('Age Distribution of Stroke Search Population', fontsize=18, pad=20, fontweight='bold')
ax.text(0.5, 0.96, 'The 18 - 24 age group has the highest search volume', transform=ax.transAxes, 
        ha='center', va='top', fontsize=13, color='#555555')

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the color and thickness of the left and bottom borders
ax.spines['left'].set_color('#cccccc')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_color('#cccccc')
ax.spines['bottom'].set_linewidth(1.5)


# Add an annotation arrow pointing to the highest bar
ax.annotate('Highest Proportion', xy=(1, 30), xytext=(1, 32),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            ha='center', fontsize=12)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()