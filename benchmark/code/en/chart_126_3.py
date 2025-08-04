import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", 
         "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# Total transaction volume (in billions of yuan)
transaction_volume = [0.5, 9.4, 52.0, 191.0, 350.0, 805.0, 1230.0, 1770.0, 
                      2954.3, 3953.2, 6000.0, 8600.0, 9651.2, 11154.0, 11386.0, 14418.0]
# Growth rate (%)
growth_rate = [np.nan, 1770.0, 455.6, 267.3, 83.2, 130.0, 52.8, 43.9, 
               66.9, 33.8, 51.8, 43.3, 12.2, 15.6, 2.1, 26.6]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the bar chart of total transaction volume
ax1.bar(x, transaction_volume, color='orange', label='Total Transaction Volume (in billions of yuan)')
ax1.set_ylabel('Total Transaction Volume (in billions of yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='center left')

# Create a secondary y - axis and plot the line chart of growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='center right')

# Add annotations for total transaction volume
for i, vol in enumerate(transaction_volume):
    ax1.text(i, vol + 200, f'{vol}', ha='center', va='bottom')

# Add annotations for growth rate (Note: there is no growth rate in 2009, start from 2010)
for i, rate in enumerate(growth_rate):
    if i > 0:  # Skip 2009
        ax2.text(x[i], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Total Transaction Volume of "Double Eleven" on Chinese E - commerce Platforms from 2009 to 2024')

plt.tight_layout()
plt.show()