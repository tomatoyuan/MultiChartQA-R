import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ["Beijing", "Chengdu", "Shanghai", "Hangzhou", "Shenzhen"]
search_ratios = [4.3, 3.4, 2.9, 2.5, 2.5]

# Create a canvas and a sub - plot
plt.figure(figsize=(10, 6), dpi=300)
ax = plt.subplot(111)

# Set a gradient - colored bar chart
colors = plt.cm.viridis(np.linspace(0.3, 0.8, len(cities)))
bars = plt.bar(cities, search_ratios, color=colors, width=0.6, edgecolor='black', linewidth=0.8)

# Add data labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{height}%', ha='center', va='bottom', fontweight='bold')

# Add a title and axis labels
plt.title("Top 5 Search Cities in the Vocational Training Industry in May", fontsize=16, fontweight='bold')
plt.xlabel("City", fontsize=12)
plt.ylabel("Search Proportion (%)", fontsize=12)

# Set the axis range and ticks
plt.ylim(0, max(search_ratios) * 1.1)
plt.yticks(np.arange(0, 5, 0.5))

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a background color
ax.set_facecolor('#f8f9fa')

# Adjust the border
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# Add a legend
plt.legend([bars[0]], ['Search Proportion'], loc='upper right')

# Optimize the layout
plt.tight_layout()

# Display the chart
plt.show()