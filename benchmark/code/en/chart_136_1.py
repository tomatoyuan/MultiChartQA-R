import matplotlib.pyplot as plt
import numpy as np

# Left side sales data
years_sales = ["2019", "2020", "2021", "2022", "2023"]
sales = [96.0, 85.0, 102.0, 103.0, 107.0]

# Right side customer flow data
years_flow = ["2020", "2021", "2022", "2023"]
flow = [650.0, 670.0, 600.0, 750.0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Draw the left side sales bar chart
x_sales = np.arange(len(years_sales))
bars = ax1.bar(x_sales, sales, color='orange', label='Sales (Million pieces)')
ax1.set_ylabel('Sales (Million pieces)')
ax1.set_xlabel('Year')
ax1.set_xticks(x_sales)
ax1.set_xticklabels(years_sales)
ax1.legend(loc='upper left')
# Add sales value labels
for i, sale in enumerate(sales):
    ax1.text(i, sale + 1, f'{sale}', ha='center', va='bottom')

# Draw the right side customer flow area chart
x_flow = np.arange(len(years_flow))
ax2.fill_between(x_flow, flow, color='gold', label='Customer Flow (Million people)')
ax2.set_ylabel('Customer Flow (Million people)')
ax2.set_xlabel('Year')
ax2.set_xticks(x_flow)
ax2.set_xticklabels(years_flow)
ax2.legend(loc='upper left')
# Add customer flow value labels
for i, f in enumerate(flow):
    ax2.text(i, f + 10, f'{f}', ha='center', va='bottom')

ax1.set_title('Pandora Sales from 2019 - 2023')
ax2.set_title('Pandora Customer Flow from 2020 - 2023')

plt.tight_layout()
plt.show()