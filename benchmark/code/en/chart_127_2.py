import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
net_profit = [791.30, 646.83, 432.49, 417.85, 486.40, 567.37, 659.31]
growth_rate = [-0.4, -18.3, -33.1, -3.4, 16.4, 16.6, 16.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Draw the bar chart of net profit attributable to the parent company
bars = ax1.bar(x, net_profit, color='orange', label='Net profit attributable to the parent company (100 million yuan)', width=0.4)
ax1.set_ylabel('Net profit attributable to the parent company (100 million yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='center left')

# Add labels for net profit attributable to the parent company
for i, profit in enumerate(net_profit):
    ax1.text(i, profit + 10, f'{profit}', ha='center', va='bottom')

# Create a secondary y - axis and draw the line chart of year - on - year growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - year growth rate (%)', linewidth=2)
ax2.set_ylabel('Year - on - year growth rate (%)')
ax2.legend(loc='center right')

# Add labels for year - on - year growth rate
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom', color='red')

ax1.set_title('Net profit attributable to the parent company of listed new - energy vehicle manufacturing companies in China\'s A - share market from 2017 to 2023')

plt.tight_layout()
plt.show()