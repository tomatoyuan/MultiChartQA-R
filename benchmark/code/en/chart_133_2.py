import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Infant formula", "Bulk milk powder", "Light cream", "Cheese", "Whey products", "Cream products", "Protein products", "Packaged milk", "Yogurt", "Condensed milk"]
import_value = [42.1, 29.2, 10.3, 9.7, 8.6, 8.3, 6.1, 5.6, 0.5, 0.4]
growth_rate = [-5.0, -34.0, 7.4, 25.9, -10.6, -11.3, -10.5, -16.2, -0.7, -18.7]

x = np.arange(len(categories))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Draw the bar chart for import value
ax1.bar(x, import_value, color='orange', label='Import value (billion US dollars)')
ax1.set_ylabel('Import value (billion US dollars)')
ax1.set_xlabel('Dairy product types')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=45, ha='right')
ax1.legend(loc='center left')

# Create a secondary y - axis and draw the line chart for year - on - year growth
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Year - on - year growth (%)', linewidth=2)
ax2.set_ylabel('Year - on - year growth (%)')
ax2.legend(loc='upper right')

# Add labels for import value
for i, val in enumerate(import_value):
    ax1.text(i, val + 1, f'{val}', ha='center', va='bottom')

# Add labels for year - on - year growth
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Import value and year - on - year growth of major dairy products in China in 2023')

plt.tight_layout()
plt.show()