import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
average_wage = [4.8, 4.9, 5.3, 6.3, 7.1, 9.1, 9.6, 11.1, 11.8]
growth_rate = [23.1, 2.1, 8.2, 18.9, 12.7, 28.2, 5.5, 15.6, 6.3]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of average wage
ax1.bar(x, average_wage, color='orange', label='Average Wage (Thousand Yuan)')
ax1.set_ylabel('Average Wage (Thousand Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and plot the line chart of growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Growth Rate (%)', linewidth=2)
ax2.set_ylabel('Growth Rate (%)')
ax2.legend(loc='center right')

# Add labels for average wage values
for i, wage in enumerate(average_wage):
    ax1.text(i, wage + 0.3, f'{wage}', ha='center', va='bottom')

# Add labels for growth rate values
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Domestic Service Industry Wages and Their Growth Rates from 2015 to 2023')

plt.tight_layout()
plt.show()