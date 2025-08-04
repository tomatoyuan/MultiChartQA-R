import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2022", "2023", "2024", "2025E", "2026E", "2027E", "2028E"]
# Market size (in billions of yuan)
market_size = [11.5, 79.3, 471.7, 805.8, 1665.3, 2317.6, 2767.4]
# Growth rate (%)
growth_rate = [589.6, 494.8, 70.8, 106.7, 39.2, 19.4]  # Note: The growth rate from 2022 - 2023 corresponds to the change from the previous year to the next year. Here it is arranged according to the line points in the graph. The correspondence needs to be confirmed.

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the bar chart of market size
ax1.bar(x, market_size, color='coral', label='Size (in billions of yuan)')
ax1.set_ylabel('Size (in billions of yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of growth rate (Note: The correspondence between growth rate data points and years may need to be adjusted)
ax2 = ax1.twinx()
# The growth rate data corresponds to the change from 2023 - 2028E, so the x - axis index starts from 1
ax2.plot(x[1:], growth_rate, marker='o', color='gold', label='Growth rate (%)')
ax2.set_ylabel('Growth rate (%)')
ax2.legend(loc='center right')

# Add annotations for market size values
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Add annotations for growth rate values (corresponding to line points)
for i, rate in enumerate(growth_rate):
    # The growth rate corresponds to the year index i + 1 (starting from 2023)
    ax2.text(x[i + 1], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China AIGC Core Market Size and Forecast from 2022 - 2028')

plt.tight_layout()
plt.show()