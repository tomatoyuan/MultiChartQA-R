import matplotlib.pyplot as plt
import numpy as np

# Data preparation
drink_types = [
    "Sugar - free carbonated drinks (e.g., sugar - free cola,\n Yuanqi Forest series, sugar - free soda water, etc.)",
    "Sugar - free tea drinks (e.g., Dongfang Shuye series,\n sugar - free oolong tea, etc.)",
    "Sugar - free fruit and vegetable juices \n(e.g., NFC juices, sugar - free vegetable juices, etc.)",
    "Sugar - free milk - based drinks (e.g., sugar - free yogurt,\n sugar - free high - calcium milk, etc.)",
    "Other sugar - free drinks \n(e.g., sugar - free plum juice, etc.)"
]
proportions = [76.07, 70.09, 46.16, 45.90, 11.31]  # Proportion (%)

x = np.arange(len(drink_types))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart
bars = ax.barh(x, proportions, color='coral')
ax.set_title('Types of sugar - free drinks consumed by Chinese consumers in 2023', fontsize=14)
ax.set_xlabel('Proportion (%)')
ax.set_ylabel('Sugar - free drink types')
ax.set_yticks(x)
ax.set_yticklabels(drink_types)

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', ha='left', va='center', color='black')

# Add a legend and sample source description
ax.legend(bars, ['Proportion'], loc='lower right')
ax.text(0.7, -0.2, 'Sample source: Strawberry Pie Data Survey and Calculation System', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()