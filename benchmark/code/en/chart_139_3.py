import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [1181, 1543, 1905, 2264, 2556, 2961, 3492, 3834, 4237, 4631, 5033]
growth_rate = [30.7, 23.5, 18.8, 12.9, 15.8, 17.9, 9.8, 10.5, 9.3, 8.7]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of year - on - year growth rate
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rate, marker='o', color='brown', label='Year - on - Year Growth (%)', linewidth=2)  # No year - on - year data for 2015, start from 2016
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='center right')

# Add market size value labels
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Add year - on - year growth value labels (no data for 2015, start from 2016)
for i, rate in enumerate(growth_rate, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Market Size and Forecast of Chinese Convenience Store Industry from 2015 to 2025')

plt.tight_layout()
plt.show()