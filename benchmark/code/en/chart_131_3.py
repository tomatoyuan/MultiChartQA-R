import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Proportion of the revenue scale of the household service industry in GDP (%)
proportions = [0.25, 0.33, 0.36, 0.40, 0.47, 0.55, 0.64, 0.73, 0.92, 0.88, 0.89, 0.92]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a line chart
line, = ax.plot(x, proportions, color='gold', marker='o', label='Proportion of household service industry revenue in GDP')

# Add numerical annotations
for i, prop in enumerate(proportions):
    ax.text(i, prop + 0.01, f'{prop}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Proportion (%)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylim(0.2, 1.0)  # Set the y - axis range to better display the data

ax.legend()
ax.set_title('Proportion of the revenue scale of the Chinese household service industry in GDP from 2012 to 2023')

plt.tight_layout()
plt.show()