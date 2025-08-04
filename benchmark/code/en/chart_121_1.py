import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024.9"]
# Operating revenue (in billions of yuan)
operating_revenue = [227.19, 299.49, 352.00, 428.17, 354.71, 361.41, 290.00]
# Net profit (in billions of yuan)
net_profit = [67.08, 86.37, 111.22, 150.13, 115.07, 121.77, 95.23]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw the operating revenue bar chart
ax1.bar(x, operating_revenue, color='brown', label='Operating Revenue (Billion Yuan)', width=0.4)
ax1.set_ylabel('Operating Revenue (Billion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and draw the net profit bar chart
ax2 = ax1.twinx()
ax2.bar(x + 0.4, net_profit, color='gold', label='Net Profit (Billion Yuan)', width=0.4)
ax2.set_ylabel('Net Profit (Billion Yuan)')
ax2.legend(loc='upper right')

# Add operating revenue value labels
for i, rev in enumerate(operating_revenue):
    ax1.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Add net profit value labels
for i, profit in enumerate(net_profit):
    ax2.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

ax1.set_title('Operating Revenue and Net Profit of Guotai Junan from 2018 to September 2024')
plt.tight_layout()
plt.show()