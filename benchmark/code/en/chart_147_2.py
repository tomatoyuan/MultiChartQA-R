import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E"]
market_size = [292.1, 282.4, 324.3, 350.2, 366.3, 387.9, 411.2, 440, 475.2, 546.5, 628.5, 710.2, 799.6]  # Market size (in billions of yuan)
growth_rates = [-3.3, 14.8, 8.0, 4.6, 5.9, 6.0, 7.0, 8.0, 15.0, 15.0, 13.0, 12.6]  # Year-on-year growth rate (%), note that there is no growth rate in 2012, starting from 2013

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Draw a bar chart of the market size
ax1.bar(x, market_size, color='coral', label='Market Size (in billions of yuan)')
ax1.set_ylabel('Market Size (in billions of yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and draw a line chart of the year-on-year growth rate
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rates, marker='o', color='gold', label='Year-on-Year Growth Rate (%)', linewidth=2)  # There is no growth rate in 2012, start drawing from 2013
ax2.set_ylabel('Year-on-Year Growth Rate (%)')
ax2.legend(loc='center right')

# Add numerical labels for the market size
for i, size in enumerate(market_size):
    ax1.text(i, size + 10, f'{size}', ha='center', va='bottom', color='black')

# Add numerical labels for the year-on-year growth rate (starting from 2013)
for i, rate in enumerate(growth_rates, start=1):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom', color='black')

ax1.set_title('China Fitness Equipment Market Size and Forecast from 2012 to 2024')
plt.tight_layout()
plt.show()