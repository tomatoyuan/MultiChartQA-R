import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
total_volume = [133.8, 150.3, 167.9, 171.1, 181.7, 191.1, 202.6, 220.2, 230.2, 239.8, 240.4]
growth_rate = [np.nan, 12.3, 11.8, 1.9, 6.2, 5.1, 6.0, 8.7, 4.5, 4.2, 0.3]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Draw the bar chart of total domestic sales volume
bars = ax1.bar(x, total_volume, color='orange', label='Total Domestic Sales Volume (10,000 tons)')
ax1.set_ylabel('Total Domestic Sales Volume (10,000 tons)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Add annotations for total domestic sales volume
for i, vol in enumerate(total_volume):
    ax1.text(i, vol + 2, f'{vol}', ha='center', va='bottom')

# Create a secondary y - axis and draw the line chart of growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)', linewidth=2)
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='center right')

# Add annotations for growth rate (skip 2013 as there is no growth rate)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.3, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Total Domestic Sales Volume and Growth Rate of Chinese Tea from 2013 to 2023')

plt.tight_layout()
plt.show()