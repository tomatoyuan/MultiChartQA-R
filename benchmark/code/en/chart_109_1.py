import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# Year-on-year growth rate (%)
growth_rates = [30.4, 19.1, 8.9, 11.3, 3.6, 12.9, 6.4]

x = np.arange(len(years))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a bar chart
bars = ax.bar(x, growth_rates, color='orange')

# Add numerical annotations
for i, rate in enumerate(growth_rates):
    ax.text(i, rate + 1, f'{rate}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel('Year-on-year growth rate (%)')
ax.set_title('Changes in the year-on-year growth rate of China\'s rural online sales from 2018 to 2024')

plt.tight_layout()
plt.show()