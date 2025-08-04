import matplotlib.pyplot as plt
import numpy as np

# Years and date ranges
years = ["Apr - Sep 2019", "Apr - Sep 2020", "Apr - Sep 2021", "Apr - Sep 2022", "Apr - Sep 2023"]
# Proportions of each category (%), in the order of [Jewelry inlay/platinum/K - gold jewelry, Gold jewelry and products, Watches]
category_proportions = np.array([
    [29.1, 64.5, 6.4],
    [30.1, 60.9, 9.0],
    [22.6, 70.7, 6.7],
    [19.1, 75.6, 5.3],
    [14.7, 80.1, 5.2]
])

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a stacked bar chart
bottom = np.zeros(len(years))
for i in range(category_proportions.shape[1]):
    ax.bar(x, category_proportions[:, i], bottom=bottom, width=0.6, label=['Jewelry inlay/platinum/K - gold jewelry', 'Gold jewelry and products', 'Watches'][i])
    # Add numerical labels
    for j in range(len(years)):
        ax.text(j, bottom[j] + category_proportions[j, i] / 2, f'{category_proportions[j, i]}%', ha='center', va='center')
    bottom += category_proportions[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_xlabel('Date')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Turnover proportion of Chow Tai Fook product categories in semi - annual reports from 2019 to 2023')

plt.tight_layout()
plt.show()