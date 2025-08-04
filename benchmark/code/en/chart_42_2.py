import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2014, 2025)
# Revenue data (trillions of yuan), 2024 is the forecast value (E)
revenues = [2.5, 2.8, 3.2, 4.4, 5.4, 6.9, 7.4, 8.0, 8.3, 8.6, 9.0]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(12, 7))

# Set the grid style
plt.grid(True, linestyle='--', alpha=0.7)

# Create a bar chart with gradient colors
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(years)))
bars = ax.bar(years, revenues, color=colors, edgecolor='black', linewidth=0.5)

# Set the title and axis labels
ax.set_title('Overall Revenue and Forecast of China\'s Big Health Industry from 2014 to 2024', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Revenue (trillions of yuan)', fontsize=14, labelpad=10)

# Set the x - axis and y - axis ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 10, 1))

# Modify the x - axis label for 2024 to 2024E
xticks_labels = [str(year) for year in years]
xticks_labels[-1] = '2024E'
ax.set_xticklabels(xticks_labels)

# Add numerical labels to each bar
for bar, revenue in zip(bars, revenues):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{revenue}', ha='center', va='bottom', fontsize=10)

# Highlight the forecast value
prediction_bar = bars[-1]
prediction_bar.set_color('lightgreen')
prediction_bar.set_edgecolor('black')

# Add a legend
ax.legend([bars[0], prediction_bar], ['Actual Value', 'Forecast Value'], loc='upper left')

# Set the y - axis range
plt.ylim(0, 10)

# Beautify the chart
plt.tight_layout()

# Display the chart
plt.show()