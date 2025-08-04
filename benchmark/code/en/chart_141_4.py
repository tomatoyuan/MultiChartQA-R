import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Pre-pregnancy check-up", "Pre-pregnancy health products", "Pre-pregnancy diet", "Pregnancy test", "Pre-pregnancy books", "Household appliances", "Cars", "Others"]
percentages = [78.5, 77.4, 74.7, 58.1, 31.7, 15.5, 5.7, 0.4]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange', label='Proportion of new consumption (%)')
ax.set_ylabel('Proportion of new consumption (%)')
ax.set_xlabel('Consumption categories')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_title('Distribution of new consumption categories among Chinese pre - pregnancy population in 2023')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()