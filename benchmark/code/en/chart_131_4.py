import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E", "2026E", "2027E"]
market_size = [2776, 3498, 4400, 5762, 6975, 8782, 10149, 10890, 11641, 12270, 12847, 13386, 13855]
growth_rate = [26.0, 25.8, 31.0, 21.1, 25.9, 15.6, 7.3, 6.9, 5.4, 4.7, 4.2, 3.5, 2.9]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the market size bar chart
ax1.bar(x, market_size, color='orange', label='Market Size (100 million yuan)')
ax1.set_ylabel('Market Size (100 million yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')

# Create a secondary y-axis and plot the growth rate line chart
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='center right')

# Add market size value labels
for i, size in enumerate(market_size):
    ax1.text(i, size + 100, f'{size}', ha='center', va='bottom')

# Add growth rate value labels
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China Domestic Service Market Size and Growth Rate from 2015 to 2027 and Forecast')

plt.tight_layout()
plt.show()