import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2020", "2021", "2022", "2023", "2024E", "2025E"]
market_size = [240.0, 360.0, 1116.0, 2845.8, 5197.4, 8287.0]
growth_rate = [np.nan, 50.0, 210.0, 155.0, 82.6, 59.4]  # No year - on - year data for 2020, marked with np.nan

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and draw the line chart of year - on - year growth
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rate[1:], marker='o', color='gold', label='Year - on - Year Growth (%)', linewidth=2)  # No year - on - year data for 2020, start from 2021
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='center right')

# Add annotations for market size values
for i, size in enumerate(market_size):
    ax1.text(i, size + 100, f'{size}', ha='center', va='bottom')

# Add annotations for year - on - year growth values (no data for 2020, start from 2021)
for i, rate in enumerate(growth_rate[1:], start=1):
    ax2.text(i, rate + 5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China Cross - border Live - streaming E - commerce Market Size and Forecast from 2020 to 2025')

plt.tight_layout()
plt.show()