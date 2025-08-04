import matplotlib.pyplot as plt
import numpy as np

# Years and dates
years = ["2020/3/31", "2021/3/31", "2022/3/31", "2023/3/31", "2024/3/31"]
# Total operating revenue (in billions of yuan)
operating_revenue = [518.5, 593, 802.4, 828.9, 985.5]
# Net profit attributable to the parent company (in billions of yuan)
net_profit = [26.51, 50.93, 54.44, 47.14, 58.92]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the bar chart of total operating revenue
ax.bar(x, operating_revenue, color='orange', label='Total Operating Revenue (Billion Yuan)', width=0.6)
# Plot the bar chart of net profit attributable to the parent company
ax.bar(x, net_profit, color='red', label='Net Profit Attributable to Parent (Billion Yuan)', width=0.2)

# Add labels for total operating revenue values
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Add labels for net profit attributable to the parent company values
for i, profit in enumerate(net_profit):
    ax.text(i, profit + 2, f'{profit}', ha='center', va='bottom')

ax.set_ylabel('Amount (Billion Yuan)')
ax.set_xlabel('Date')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Chow Tai Fook\'s Operating Revenue and Net Profit Attributable to Parent from 2020 to 2024')

plt.tight_layout()
plt.show()