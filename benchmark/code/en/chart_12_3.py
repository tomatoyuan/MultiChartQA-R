import matplotlib.pyplot as plt
import numpy as np

# Data
foods = ["Crawfish", "Barbecue", "Spicy Duck", "Beer", "Cola", "Edamame", "Popcorn", "Grilled Meat"]
values = [2264, 1030, 827, 804, 521, 462, 442, 352]

# Create a canvas and sub - plot (set larger size and resolution)
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# Set gradient colors (from dark blue to light blue)
colors = plt.cm.Blues(np.linspace(0.6, 0.95, len(foods)))

# Draw a bar chart with rounded corners (set the border via edgecolor and linewidth)
bars = ax.bar(
    x=np.arange(len(foods)),
    height=values,
    width=0.65,
    color=colors,
    edgecolor='black',
    linewidth=0.8,
    capstyle='round'
)

# Add numerical labels above the bar chart
for bar, value in zip(bars, values):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height + 30,  # The label position is slightly above the top of the bar
        f'{value}',
        ha='center', 
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Set x - axis tick labels (rotate 30 degrees to enhance readability)
ax.set_xticks(np.arange(len(foods)))
ax.set_xticklabels(foods, rotation=30, ha='right', fontsize=11)

# Add a title and axis labels (increase font size and boldness)
ax.set_title('Food Attention during the European Cup', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Food Types', fontsize=13, labelpad=10)
ax.set_ylabel('Attention Value', fontsize=13, labelpad=10)

# Set the y - axis range (leave some space at the top)
ax.set_ylim(0, max(values) * 1.1)

# Add grid lines to enhance readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Beautify the chart border
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(0.5)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()