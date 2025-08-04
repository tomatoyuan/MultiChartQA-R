import matplotlib.pyplot as plt
import numpy as np

# Reasons for purchasing agricultural products online
reasons = [
    "Convenient, save time and energy", "Better understand products before purchase", "Rich selection of products", 
    "Many promotional activities", "Low price", "Can buy products from other regions", 
    "Guaranteed product quality", "Can buy out - of - season products"
]
# Corresponding proportions (%)
proportions = [41.29, 40.65, 40.00, 38.71, 38.71, 37.42, 32.90, 29.03]

x = np.arange(len(reasons))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Reasons why Chinese consumers prefer to buy agricultural products online in 2025')

plt.tight_layout()
plt.show()