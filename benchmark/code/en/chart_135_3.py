import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [401, 500, 600, 773, 977, 1207, 1461, 1750, 2046]
growth_rate = [np.nan, 24.7, 20.0, 28.8, 26.4, 23.5, 21.0, 15.2, 13.0]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of year - on - year change rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='coral', label='Year - on - Year Change Rate (%)', linewidth=2)
ax2.set_ylabel('Year - on - Year Change Rate (%)')
ax2.legend(loc='center right')

# Add numerical labels for market size
for i, size in enumerate(market_size):
    ax1.text(i, size + 20, f'{size}', ha='center', va='bottom')

# Add numerical labels for year - on - year change rate (skip 2017 as there is no year - on - year data)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of Non - surgical Aesthetic Medicine in China from 2017 to 2025')

plt.tight_layout()
plt.show()