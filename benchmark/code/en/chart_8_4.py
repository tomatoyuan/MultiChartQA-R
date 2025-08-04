import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ['Beijing', 'Shenzhen', 'Wuhan', 'Shanghai', 'Guangzhou']
# Corresponding search proportion data (approximate values read from the graph, can be replaced with accurate data)
percentages = [19, 6, 5.5, 4.5, 2.5]

x = np.arange(len(cities))  # Used to set the position of the x - axis

fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the chart size
# Draw a bar chart, adjust the width and set the color
bars = ax.bar(x, percentages, width=0.6, color='skyblue')

# Add data labels to each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',  # Annotation text
                xy=(bar.get_x() + bar.get_width() / 2, height),  # Annotation position
                xytext=(0, 3),  # Vertical offset
                textcoords="offset points",
                ha='center',  # Horizontal alignment
                va='bottom',  # Vertical alignment
                fontsize=10)  # Font size

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(cities, fontsize=10)

# Set the y - axis range and ticks
ax.set_ylim(0, 22)  # Slightly increase the upper limit to make room for the annotations
ax.set_yticks(np.arange(0, 21, 5))

# Set the axis titles and the chart title
ax.set_ylabel('Search Proportion (%)', fontsize=12)
ax.set_title('Top 5 Cities for Divorce Litigation Industry Searches in May', fontsize=14)

# Add grid lines to enhance readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Beautify the chart
plt.tight_layout()  # Automatically adjust the layout
plt.show()