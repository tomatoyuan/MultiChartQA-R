import matplotlib.pyplot as plt
import numpy as np

# Factors of concern
factors = [
    "Comfort", "Material texture", "Environmental friendliness", "Durability", "Ease of cleaning", "Safety", 
    "Style design", "Color matching", "Decorativeness", "Practicality", "Brand", "After - sales service", "Discount"
]
# Corresponding proportions (%)
proportions = [37.69, 36.92, 35.38, 33.85, 33.46, 32.88, 
               32.50, 31.35, 30.38, 30.19, 28.08, 27.12, 25.00]

x = np.arange(len(factors))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Factors that Chinese consumers are concerned about when buying soft - furnishings and home products in 2025')

plt.tight_layout()
plt.show()