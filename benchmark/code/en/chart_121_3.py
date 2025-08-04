import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2018", "2019", "2020", "2021", "2022", "2023"]
# Operating revenue (in billions of yuan)
operating_revenue = [99.25, 170.41, 237.49, 359.83, 336.42, 336.44]
# Net profit (in billions of yuan)
net_profit = [28.87, 52.28, 72.44, 104.30, 77.61, 78.79]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 6))

# Draw the bar chart for operating revenue
bars_rev = ax.bar(x, operating_revenue, color='brown', label='Operating Revenue (in billions of yuan)', width=0.4)
# Draw the bar chart for net profit (shifted to the right to avoid overlap)
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='Net Profit (in billions of yuan)', width=0.4)

# Add labels for operating revenue values
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Add labels for net profit values
for i, profit in enumerate(net_profit):
    ax.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Amount (in billions of yuan)')
ax.set_xlabel('Year')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='upper left')

# Add an information box on the right side (simulating the original image style)
info_box_text = (
    "In 2022, China Galaxy Securities APP\n"
    "opened 1.1084 million new accounts for wealth management business,\n"
    "with a market share of 7.48% in account opening."
)
# Draw the information box on the right side of the chart
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="orange", lw=2)
ax.text(5.8, 300, info_box_text, fontsize=10, bbox=bbox_props, va='top')

ax.set_title('Operating Revenue and Net Profit of China Galaxy Securities from 2018 to 2023')
plt.tight_layout()
plt.show()