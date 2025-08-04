import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
production = [3010.6, 2995.1, 3038.9, 3109.9, 3174.9, 3008.8, 3159.9, 3179.8, 3064.0, 3038.6, 3074.6, 3201.2, 3440.1, 3683.0, 3932.0, 4197.0]
growth_rate = [2.2, -0.5, 1.5, 2.3, 2.1, -5.2, 5.0, 0.6, -3.6, -0.8, 1.2, 4.1, 7.5, 7.1, 6.8, 6.7]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the production bar chart
ax1.bar(x, production, color='orange', label='Production (10,000 tons)')
ax1.set_ylabel('Production (10,000 tons)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the growth rate line chart
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - year growth (%)', linewidth=2)
ax2.set_ylabel('Year - on - year growth (%)')
ax2.legend(loc='center right')

# Add production value annotations
for i, prod in enumerate(production):
    ax1.text(i, prod + 20, f'{prod}', ha='center', va='bottom')

# Add growth rate value annotations
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China\'s Milk Production and Year - on - Year Growth from 2008 to 2023')

plt.tight_layout()
plt.show()