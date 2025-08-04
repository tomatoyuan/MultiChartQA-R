import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.array([2020, 2021, 2022, 2023, 2024])
# Market size data of pets/pet food and supplies (approximate, adjustable)
market_size = np.array([40, 45, 55, 60, 70])
# Growth rate data (approximate, adjustable)
growth_rate = np.array([10, 9, 15, 8, 14])

# Create a canvas and axes
fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the chart size

# Draw a bar chart (Market size of pets/pet food and supplies)
bars = ax1.bar(years, market_size, color='blue', label='Pets/Pet Food and Supplies')
ax1.set_xlabel('Year')
ax1.set_ylabel('Market Size (Approximate Value)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add data labels above the bar chart
for bar, value in zip(bars, market_size):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{value}', ha='center', va='bottom', color='blue')

# Create a second axis for drawing a line chart (Growth rate)
ax2 = ax1.twinx()
line, = ax2.plot(years, growth_rate, color='orange', marker='o', label='Growth Rate')
ax2.set_ylabel('Growth Rate (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Set the y-axis scale, similar to the original chart
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 18, 2))

# Add annotations to each data point of the line chart
for x, y in zip(years, growth_rate):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='orange')

# Add a legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Set the chart title
plt.title('Trend of the Online E-commerce Market Size for Pets')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()