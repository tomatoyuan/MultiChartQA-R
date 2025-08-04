import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
production = [68.33, 70.17, 74.51, 76.75, 83.52, 91.82, 100.92, 117.05, 127.59, 137.16, 148.54, 160.76, 176.39, 188.71, 204.94, 228.01, 231.72, 246.04, 259.01, 274.26, 293.18, 312.32, 334.21, 355.00]
growth_rate = [np.nan, 2.7, 6.2, 3.0, 8.7, 11.9, 10.0, 13.9, 7.2, 7.6, 8.3, 9.9, 9.6, 7.1, 8.6, 11.1, 1.6, 6.4, 6.1, 6.4, 5.6, 7.9, 5.6, 6.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(16, 9))

# Plot the production bar chart
ax1.bar(x, production, color='orange', label='Production (10,000 tons)')
ax1.set_ylabel('Production (10,000 tons)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')

# Create a twin axis and plot the growth rate line chart
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='center right')

# Add production value labels
for i, prod in enumerate(production):
    ax1.text(i, prod + 5, f'{prod}', ha='center', va='bottom')

# Add growth rate value labels (skip the year 2000 as there is no growth rate)
for i, rate in enumerate(growth_rate):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China\'s Tea Production and Growth Rate from 2000 to 2023')

plt.tight_layout()
plt.show()