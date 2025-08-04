import matplotlib.pyplot as plt
import numpy as np

# Data for the new chart
labels = ["Difficulty in improving marketing communication ROI", "Difficulty in measuring and verifying effectiveness", "Media fragmentation"]
# Proportion data for each category (since it's a single - group data, use a one - dimensional array directly)
values = np.array([62, 54, 50])  
# Color scheme (matching the original image's color tone, can be fine - tuned)
colors = ['#4C72B0', '#818181', '#A9A9A9']  

# Create a canvas and a sub - plot, set the chart size
fig, ax = plt.subplots(figsize=(8, 4))  

# Draw a horizontal bar chart (single - group data, no stacking required)
for i, (label, value, color) in enumerate(zip(labels, values, colors)):
    bar = ax.barh(label, value, color=color, alpha=0.9, edgecolor='w', linewidth=0.5)
    
    # Annotate the percentage at the end of the bar
    ax.text(
        value + 1,  # The text is on the right side of the bar, the distance can be fine - tuned
        bar[0].get_y() + bar[0].get_height()/2,
        f"{value}%", 
        ha='left', 
        va='center',
        fontweight='bold',
        fontsize=10
    )

# Set the title
ax.set_title('Advertisers\' media selection challenges in 2021', fontsize=14, fontweight='bold', pad=20)  

# Set the labels (the x - axis represents the percentage, no additional label is needed for the y - axis, so it's commented)
ax.set_xlabel('Percentage (%)', fontsize=12, labelpad=10)  
# ax.set_ylabel('Category', fontsize=12, labelpad=10)  # Uncomment if you need a y - axis label

# Set the x - axis range to make the data display more reasonable
ax.set_xlim(0, 70)  

# Set the grid lines (x - axis direction, dashed line, semi - transparent)
ax.grid(axis='x', linestyle='--', alpha=0.7)  

# Hide the borders (can enhance the simplicity)
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust the layout for better display
plt.tight_layout()  

# Show the chart
plt.show()