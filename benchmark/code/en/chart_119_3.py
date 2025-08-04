import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2020", "2021", "2022", "2023", "2024", "2025E", "2026E", "2027E", "2028E", "2029E"]
# Market size (in billions of yuan)
market_size = [350.7, 425.2, 445.2, 594.9, 713.9, 833.1, 1083.0, 1245.5, 1413.6, 1563.5, 1763.6, 1925.8]
# Growth rate (%)
growth_rate = [21.2, 6.8, -8.7, 33.6, 20.0, 16.7, 30.0, 15.0, 13.5, 10.6, 12.8, 9.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='upper right')

# Add numerical labels for market size
for i, size in enumerate(market_size):
    ax1.text(i, size + 20, f'{size}', ha='center', va='bottom')

# Add numerical labels for growth rate
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

plt.title('China Ice and Snow Sports Core Market Size and Forecast from 2016 to 2029')
plt.tight_layout()
plt.show()