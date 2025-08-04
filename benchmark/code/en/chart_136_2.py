import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
store_count = [895.0, 1100.0, 1410.0, 1802.0, 2138.0, 2446.0, 2705.0, 2770.0, 2690.0, 2619.0, 2651.0, 2651.0]
growth_rate = [np.nan, 22.9, 28.2, 27.8, 18.6, 14.4, 10.8, 2.4, -2.9, -2.6, 1.2, 0.0]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of the number of concept stores
ax1.bar(x, store_count, color='orange', label='Number of Concept Stores')
ax1.set_ylabel('Number of Concept Stores')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='lower left')

# Create a secondary y - axis and plot the line chart of the growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='coral', label='Growth Rate (%)', linewidth=2)
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='upper right')

# Add numerical labels for the number of concept stores
for i, count in enumerate(store_count):
    ax1.text(i, count + 30, f'{count}', ha='center', va='bottom')

# Add numerical labels for the growth rate (skip 2012 as there is no year - on - year data)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Number of Pandora Concept Stores and Growth Rate from 2012 to 2023')

plt.tight_layout()
plt.show()