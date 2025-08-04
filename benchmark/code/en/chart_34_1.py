import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Year data
years = np.arange(2015, 2027)
# Simulated market size data (in billions of US dollars, the general trend is close, and the values can be fine - tuned)
market_size = [29.4, 28, 30, 32, 31, 38, 39, 41, 43, 45, 47, 49.2]
# Year labels, handle 2025E, 2026E
year_labels = [str(year) if year < 2025 else f"{year}E" for year in years]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart
bars = ax.bar(years, market_size, color='#667799', width=0.8)

# Label the values on the bars
for bar, value in zip(bars, market_size):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{value}',
            ha='center', va='bottom')

# Label the CAGR
ax.text(2022, 50, f'CAGR*: 4.04%', ha='left')

# Draw an arrow slanting upwards at a 30 - degree angle
x_start = 2023
y_start = 48
# Calculate the end coordinates of the 30 - degree angle (dx = 3, dy = 3 * tan(30°))
angle_rad = np.radians(60)
dx = 3
dy = dx * np.tan(angle_rad)
x_end = x_start + dx
y_end = y_start + dy

# Use FancyArrowPatch to draw a 30 - degree slanting arrow
arrow = FancyArrowPatch((x_start, y_start), (x_end, y_end), 
                        arrowstyle='->', 
                        connectionstyle='arc3,rad=0', 
                        color='black', 
                        mutation_scale=15)
ax.add_patch(arrow)

# Set the x - axis ticks
ax.set_xticks(years)
ax.set_xticklabels(year_labels)

# Set the y - axis range
ax.set_ylim(0, 60)

# Set the chart title
ax.set_title('China\'s Underwear Market Size from 2015 to 2026 (Billions of US Dollars)')

# Display the chart
plt.show()