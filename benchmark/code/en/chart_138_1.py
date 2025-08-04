import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [2813, 3167, 3553, 3955, 4362, 4814, 5295, 4236, 4998, 5498, 5966, 6413, 6689]
growth_rate = [np.nan, 12.6, 12.2, 11.3, 10.3, 10.4, 10.0, -20.0, 18.0, 10.0, 8.5, 7.5, 4.3]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='red', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of year - on - year growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - Year Growth (%)', linewidth=2)
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='center right')

# Add annotations for market size values
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Add annotations for year - on - year growth rate values (skip 2013 as there is no year - on - year data)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of China\'s Hot Pot Industry from 2013 to 2025')

plt.tight_layout()
plt.show()