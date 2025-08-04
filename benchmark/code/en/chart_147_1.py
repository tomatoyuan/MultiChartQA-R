import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ["2018", "2019", "2020", "2021", "2022"]
national_income = [28228, 30733, 32189, 35128, 36883]  # National per capita disposable income (yuan)
urban_income = [39251, 42359, 43834, 47412, 49283]    # Urban per capita disposable income (yuan)
growth_rates = [8.7, 8.9, 4.7, 9.1, 5.0]              # Year-on-year growth rate of disposable income (%)

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw bar charts of national and urban per capita disposable income
ax1.bar(x - 0.2, national_income, width=0.4, color='lightcoral', label='National per capita disposable income (yuan)')
ax1.bar(x + 0.2, urban_income, width=0.4, color='coral', label='Urban per capita disposable income (yuan)')
ax1.set_ylabel('Income (yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and draw a line chart of the year-on-year growth rate
ax2 = ax1.twinx()
ax2.plot(x, growth_rates, marker='o', color='gray', label='Year-on-year growth rate (%)', linewidth=2)
ax2.set_ylabel('Year-on-year growth rate (%)')
ax2.legend(loc='center right')

# Add value labels for national and urban income
for i, (national, urban) in enumerate(zip(national_income, urban_income)):
    ax1.text(i - 0.2, national + 500, f'{national}', ha='center', va='bottom', color='black')
    ax1.text(i + 0.2, urban + 500, f'{urban}', ha='center', va='bottom', color='black')

# Add value labels for the year-on-year growth rate
for i, rate in enumerate(growth_rates):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom', color='black')

ax1.set_title('China\'s per capita disposable income from 2018 to 2022')
plt.tight_layout()
plt.show()