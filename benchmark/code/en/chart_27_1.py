import matplotlib.pyplot as plt
import numpy as np

# TV drama names
labels = ["Crossing Oceans to See You", "Edge of the Razor", "In the Name of the People", "On the Peak of Clouds"]
# Corresponding search index data
values = [16693, 75744, 243831, 60535]
# Set colors for each group of data (can be adjusted as needed)
colors = ['c', 'orange', 'r', 'm']  

x = np.arange(len(labels))  # x-axis coordinates

fig, ax = plt.subplots()
# Draw a bar chart
bars = ax.bar(x, values, color=colors)  

# Add numerical labels above the bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, str(height),
            ha='center', va='bottom')  

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=11)
# Set the chart title
ax.set_title('Search Index of Spring TV Dramas', fontsize=14, fontweight='bold')  
# Set the y-axis label (not set here as the original chart is not clear, can be supplemented as needed)
# ax.set_ylabel('Search Index')  

plt.show()