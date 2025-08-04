import matplotlib.pyplot as plt
import numpy as np

# Data preparation
improve_directions = ["Taste", "Ingredients", "Price", "Date", "Specification", "Packaging"]
proportions = [71.5, 56.2, 56.0, 46.5, 40.8, 39.3]  # Proportion (%)

x = np.arange(len(improve_directions))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, proportions, color='coral')
ax.set_title('Directions for improvement of sugar - free beverages in the market according to Chinese consumers in 2023', fontsize=14)
ax.set_ylabel('Proportion (%)')
ax.set_xlabel('Improvement directions')
ax.set_xticks(x)
ax.set_xticklabels(improve_directions)
ax.set_ylim(0, 80)  # Adjust the y - axis range to fit the maximum proportion (71.5%)

# Add numerical annotations
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

plt.tight_layout()
plt.show()