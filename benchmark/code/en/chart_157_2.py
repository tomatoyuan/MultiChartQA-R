import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_size = [1195, 1261, 1258, 1202, 1337, 1472, 1570]
growth_rate = [None, 5.52, -0.24, -4.45, 11.23, 10.10, 6.66]

# Create a figure
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
bar = ax1.bar(years, market_size, color='#38C6D9', width=0.6, label='Market Size')
ax1.set_ylabel('Market Size (Billion Yuan)', fontsize=12)
ax1.set_ylim(0, 2000)

# Label values
for i, val in enumerate(market_size):
    ax1.text(years[i], val + 30, str(val), ha='center', fontsize=10)

# Line chart
ax2 = ax1.twinx()
ax2.plot(years[1:], growth_rate[1:], color='darkred', linestyle='--', marker='o', linewidth=2, label='Growth Rate')
for i, val in enumerate(growth_rate[1:], 1):
    ax2.text(years[i], growth_rate[i] + 0.8, f'{val:.2f}%', color='darkred', fontsize=10, ha='center')

ax2.set_ylabel('Growth Rate', fontsize=12)
ax2.set_ylim(-10, 15)

# Title and legend
plt.title('Change in the Market Size of China\'s Alternative Protein from 2017 to 2023', fontsize=16, weight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()