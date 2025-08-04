import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
quantities = [177, 201, 238, 290, 341, 377, 457, 474, 438]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart, using a pattern similar to a graduation cap (simplified as an orange bar chart, can be replaced with a custom pattern)
bars = ax.bar(x, quantities, color='orange')

# Add numerical annotations above the bars
for i, quantity in enumerate(quantities):
    ax.text(i, quantity + 10, f'{quantity}', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Quantity (in ten thousand people)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('Scale of Chinese postgraduate entrance examination candidates from 2016 to 2024')

plt.tight_layout()
plt.show()