import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
# Market size (in billions of US dollars), values from 2023 - 2025 are forecast values (E)
market_size = np.array([2011, 1787, 2071, 2293, 2470, 2566, 2667])
# Mark special colors for forecast years (2023 - 2025)
colors = ['green'] * 4 + ['orange'] * 3

plt.figure(figsize=(10, 6))  # Set the chart size
bars = plt.bar(years, market_size, color=colors)

# Add numerical labels above each bar
for bar, value in zip(bars, market_size):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 15,
             f'{value}', ha='center', va='bottom', fontsize=10)

# Add title and axis labels
plt.title('Global Tea Market Size and Forecast from 2019 - 2025', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Size (in billions of US dollars)', fontsize=12)

# Set x-axis ticks to years
plt.xticks(years)

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()  # Adjust the layout
plt.show()