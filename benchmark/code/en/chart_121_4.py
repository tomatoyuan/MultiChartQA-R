import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2019", "2020", "2021", "2022", "2023", "2024.9"]
# Operating revenue (in billions of US dollars)
operating_revenue = [2.41, 8.98, 17.79, 12.38, 17.14, 17.88]
# Net profit (in billions of US dollars)
net_profit = [-1.07, 0.07, -36.86, -10.28, -5.41, 4.95]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))
# Draw the operating revenue bar chart (orange)
bars_rev = ax.bar(x, operating_revenue, color='orange', label='Operating Revenue (in billions of US dollars)', width=0.4)
# Draw the net profit bar chart (yellow)
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='Net Profit (in billions of US dollars)', width=0.4)

# Add operating revenue value labels
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 0.5, f'{rev}', ha='center', va='bottom')

# Add net profit value labels, adjust the position according to positive or negative to ensure reasonable display
for i, profit in enumerate(net_profit):
    if profit < 0:
        ax.text(i + 0.4, profit - 1, f'{profit}', ha='center', va='top')
    else:
        ax.text(i + 0.4, profit + 0.5, f'{profit}', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Amount (in billions of US dollars)')
ax.set_xlabel('Year')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='lower left')

ax.set_title('Robinhood Operating Revenue and Net Profit from 2019 to September 2024')
plt.tight_layout()
plt.show()