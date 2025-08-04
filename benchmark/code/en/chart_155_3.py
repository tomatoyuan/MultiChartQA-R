import matplotlib.pyplot as plt
import numpy as np

# Chart 3: Market scale performance of the pharmaceutical e - commerce industry from 2018 to 2023
years = ['2018', '2019', '2020', '2021', '2022', '2023']
sales = [700, 950, 1500, 1850, 2500, 2900]  # Unit: 100 million yuan
growth_rate = [55, 45, 35, 30, 29, 15]  # Unit: %

fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary axis - Bar chart (Sales scale)
bars = ax1.bar(years, sales, color='#fdbf6f', label='Sales scale (100 million yuan)', width=0.6)
ax1.set_ylabel('Sales scale (100 million yuan)', fontsize=12)
ax1.set_ylim(0, 3200)

# Add numerical labels to the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 80, f'{int(height)}', ha='center', va='bottom', fontsize=10)

# Secondary axis - Line chart (Year - on - year growth rate)
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='brown', marker='o', linewidth=2.5, label='Year - on - year growth rate')
ax2.set_ylabel('Year - on - year growth rate (%)', fontsize=12)
ax2.set_ylim(0, 65)

# Add data labels to the line chart
for x, y in zip(years, growth_rate):
    ax2.text(x, y + 2, f'{y:.1f}%', ha='center', fontsize=10)

# Title and legend
plt.title('Market scale performance of the pharmaceutical e - commerce industry from 2018 to 2023', fontsize=14, weight='bold')
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper'
                              ' center')

plt.tight_layout()
plt.show()