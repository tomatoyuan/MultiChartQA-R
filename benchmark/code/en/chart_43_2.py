import matplotlib.pyplot as plt
import numpy as np

# Country/Region names
countries = ["USA", "China", "Japan", "UK", "Germany", "India", "China [She Economy]", "France", "Italy", "Canada", "Australia"]
# Corresponding data (Unit: Trillion RMB, roughly estimated based on the chart here, you can adjust it according to the actual precise data)
data = [1500, 600, 200, 200, 200, 200, 100, 100, 100, 100, 100]  

x = np.arange(len(countries))  # x-axis position
width = 0.5  # Bar width

fig, ax = plt.subplots()

# Set colors for each bar, "China [She Economy]" is orange, the rest are cyan
colors = ['cyan'] * len(countries)
index = countries.index("China [She Economy]")
colors[index] = 'orange'

rects = ax.bar(x, data, width, color=colors)

# Fix: Use the bbox parameter instead of the padding parameter and move the annotation up
ax.text(5.7, 300, "Over 10 trillion RMB", fontsize=12, ha='center', va='bottom',
        bbox=dict(facecolor='orange', alpha=1.0, pad=5))

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha='right')
# Set y-axis label
ax.set_ylabel('Scale (Trillion RMB)')
# Set the title
ax.set_title('In 2023, China\'s "She Economy" scale is large enough to form the seventh-largest economy')

# Display the chart
plt.tight_layout()
plt.show()