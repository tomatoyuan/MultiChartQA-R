import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E", "2026E", "2027E", "2028E"]
market_size = [1946.6, 2157.4, 2396.0, 2626.6, 2910.3, 3210.0, 3511.8, 3838.4, 4164.6, 4527.0, 4902.7, 5309.6]
growth_rate = [10.8, 11.1, 10.0, 9.6, 10.8, 10.3, 9.4, 9.3, 8.5, 8.7, 8.3, 8.1]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (100 million yuan)')
ax1.set_ylabel('Market Size (100 million yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and plot the line chart of growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='upper right')

# Add annotations for market size values
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Add annotations for growth rate values
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of China\'s Tea Industry from 2017 to 2028')

plt.tight_layout()
plt.show()