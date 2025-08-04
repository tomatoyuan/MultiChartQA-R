import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# Data
years = ["2020", "2021", "2022", "2023", "2024E"]
market_total = [3557, 3986, 4306, 4990, 5680]
market_b = [2774, 3109, 3359, 3980, 4630]
growth_total = [None, 12.1, 8.0, 15.9, 13.8]
growth_b = [None, 12.1, 8.0, 18.5, 16.3]

x = np.arange(len(years))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
bars1 = ax1.bar(x - width/2, market_total, width, label='Total Market Size (Billion Yuan)', color='red')
bars2 = ax1.bar(x + width/2, market_b, width, label='B - end Market Size (Billion Yuan)', color='blue')

# Add labels to the bars
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 50, f'{int(height)}', ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 50, f'{int(height)}', ha='center', va='bottom', fontsize=9)

ax1.set_ylabel('Market Size (Billion Yuan)')
ax1.set_xticks(x)
ax1.set_xticklabels(years)

# Secondary axis: Year - on - year change (%)
ax2 = ax1.twinx()
ax2.set_ylabel('Year - on - year Change (%)')
ax2.set_ylim(0, 20)  # Start from 0%
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# Draw the line chart starting from 2021
x_growth = x[1:]  # Corresponds to 2021 - 2024
growth_total_clean = [v for v in growth_total if v is not None]
growth_b_clean = [v for v in growth_b if v is not None]

line1 = ax2.plot(x_growth, growth_total_clean, color='orange', marker='o', label='Year - on - year Change (%)', linewidth=2)
line2 = ax2.plot(x_growth, growth_b_clean, color='gray', marker='o', label='B - end Year - on - year Change (%)', linewidth=2)

# Label the values on the line chart
for i, val in enumerate(growth_total_clean):
    ax2.text(x_growth[i], val + 0.6, f'{val}%', color='orange', ha='center', fontsize=9)
for i, val in enumerate(growth_b_clean):
    ax2.text(x_growth[i], val + 0.6, f'{val}%', color='gray', ha='center', fontsize=9)

# Legend
lines_labels = ax1.get_legend_handles_labels()
lines_labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines_labels[0] + lines_labels2[0], lines_labels[1] + lines_labels2[1], loc='upper left')

plt.title('National Pre - made Food Market Size and Its Year - on - year Change from 2020 to 2024')
plt.tight_layout()
plt.show()