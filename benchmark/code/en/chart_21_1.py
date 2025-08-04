import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Year data
years = np.arange(2002, 2018)
# Passenger volume data corresponding to each year (approximately close to the original data)
passenger_volumes = [1.28, 1.35, 1.37, 1.37, 1.44, 1.56, 
                     1.96, 1.92, 2.1, 2.2, 2.2, 2.4, 
                     2.66, 2.95, 3.25, 3.56]

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart, set the color to be close to the light green color scheme of the original chart
bar_rects = ax.bar(years, passenger_volumes, color='#87E8DE')

# Set x-axis ticks
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10)

# Set y-axis label
ax.set_ylabel('Number of Passengers Sent (in hundreds of millions)', fontsize=12)
# Set the title
ax.set_title('Annual National Railway Spring Festival Passenger Volume (Unit: hundreds of millions of passengers)', fontsize=14, pad=20)

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Label the values on the bars
for rect in bar_rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, f'{height}',
            ha='center', va='bottom', fontsize=9)

# Add some decorative elements, use pure graphics instead of pictures
hot_air_balloon = patches.Circle((2003.5, 3.3), 0.15, color='#FF7E79')
ax.add_patch(hot_air_balloon)

# Draw the basket and ropes of the hot air balloon
basket = patches.Rectangle((2003.35, 3.15), 0.3, 0.1, color='#A0522D')
ax.add_patch(basket)

# Draw the ropes
ax.plot([2003.35, 2003.425], [3.3, 3.15], color='#8B4513', linewidth=1)
ax.plot([2003.65, 2003.575], [3.3, 3.15], color='#8B4513', linewidth=1)

plt.tight_layout()
plt.show()