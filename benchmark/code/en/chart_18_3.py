import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ["Chengdu", "Wuhan", "Suzhou", "Nanjing", "Tianjin", "Guangzhou", "Hangzhou", "Shanghai", "Beijing", "Shenzhen"]
# Marriage cost (unit: ten thousand yuan)
costs = [55, 65, 94, 102, 108, 128, 178, 200, 202, 208]

x = np.arange(len(cities))  # Used to set the position of the bar chart on the x - axis

# Create a canvas and an axis object
fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart, set the color to white and the border to pink
bars = ax.bar(x, costs, color='white', edgecolor='pink')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(cities)
# Set the y - axis label
ax.set_ylabel("Marriage Cost (Ten Thousand Yuan)")
# Set the title
ax.set_title("Top 10 Cities in China for Marriage Cost")
# Set the unit to be displayed beside the title
ax.text(0.95, 1.02, "Unit: Ten Thousand Yuan", transform=ax.transAxes, ha='right', va='bottom')

# Label the values on each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}',
            ha='center', va='bottom')

# Set the background color to pink
ax.set_facecolor('pink')
# Remove the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.show()