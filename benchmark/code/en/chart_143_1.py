import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Below 200 yuan", "201 - 500 yuan", "501 - 1000 yuan", "1001 - 1500 yuan", "1501 - 2000 yuan", "Above 2000 yuan"]
percentages = [15.0, 34.4, 38.9, 8.9, 1.6, 1.2]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange', label='Consumption proportion (%)')
ax.set_ylabel('Consumption proportion (%)')
ax.set_xlabel('Monthly average consumption amount range')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_title('Survey on monthly average cosmetics consumption of Chinese consumers in 2023')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()