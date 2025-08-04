import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E"]
market_size = [216.3, 234.6, 240.9, 250.3, 259.3, 230.5, 235.3, 253.4, 270.9, 304.3, 335.0, 364.1, 387.8]
growth_rate = [8.5, 2.7, 3.9, 3.6, -11.1, 2.1, 7.7, 6.9, 12.3, 10.1, 8.7, 6.5]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (100 million yuan)')
ax1.set_ylabel('Market Size (100 million yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of year - on - year growth
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rate, marker='o', color='brown', label='Year - on - Year Growth (%)', linewidth=2)  # No year - on - year data for 2012, start from 2013
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='lower right')

# Add market size value labels
for i, size in enumerate(market_size):
    ax1.text(i, size + 5, f'{size}', ha='center', va='bottom')

# Add year - on - year growth value labels (no data for 2012, start from 2013)
for i, rate in enumerate(growth_rate, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of Chinese Warehouse Membership Supermarket Industry from 2012 to 2024')

plt.tight_layout()
plt.show()