import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [3181.0, 3396.0, 3656.0, 3942.0, 4256.0, 3958.0, 4553.0, 4858.1, 5169.0, 5458.0, 5791.0]
growth_rate = [np.nan, 6.8, 7.7, 7.8, 8.0, -7.0, 15.0, 6.7, 6.4, 5.6, 6.1]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart for market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart for year - on - year growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - Year Growth Rate (%)', linewidth=2)
ax2.set_ylabel('Year - on - Year Growth Rate (%)')
ax2.legend(loc='center right')

# Add annotations for market size
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Add annotations for year - on - year growth rate (skip 2015 as there is no year - on - year data)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of China\'s Cosmetics Industry from 2015 to 2025')

plt.tight_layout()
plt.show()