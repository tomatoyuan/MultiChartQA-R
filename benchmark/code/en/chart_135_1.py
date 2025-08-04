import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [1606, 1693, 1867, 1950, 2133, 2029, 2308, 2565, 2804, 3014, 3186]
growth_rate = [np.nan, 5.4, 10.3, 4.4, 9.4, -4.9, 13.8, 11.1, 9.3, 7.5, 5.7]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Draw the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and draw the line chart of year - on - year growth
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - Year Growth (%)', linewidth=2)
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='lower right')

# Add annotations for market size values
for i, size in enumerate(market_size):
    ax1.text(i, size + 30, f'{size}', ha='center', va='bottom')

# Add annotations for year - on - year growth values (skip 2015 as there is no year - on - year data)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of China\'s Skincare Industry from 2015 to 2025')

plt.tight_layout()
plt.show()