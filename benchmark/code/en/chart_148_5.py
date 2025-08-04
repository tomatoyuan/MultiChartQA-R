import matplotlib.pyplot as plt
import numpy as np

# Data preparation
scenarios = ["Leisure gathering", "Work/Study", "Dining", "Exercise", "E-sports games", "When new products are launched", "Driving"]
proportions = [62.8, 53.1, 42.4, 42.0, 28.6, 28.1, 25.6]  # Proportion (%)

x = np.arange(len(scenarios))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, proportions, color='coral')
ax.set_title('Scenarios of Chinese consumers drinking sugar - free beverages in 2023', fontsize=14)
ax.set_ylabel('Proportion (%)')
ax.set_xlabel('Drinking scenarios')
ax.set_xticks(x)
ax.set_xticklabels(scenarios, rotation=45, ha='right')  # Rotate the x - axis labels to avoid overlap
ax.set_ylim(0, 70)  # Adjust the y - axis range to fit the maximum proportion (62.8%)

# Add numerical annotations
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# Add a legend
ax.legend(bars, ['Proportion'], loc='upper right')

plt.tight_layout()
plt.show()