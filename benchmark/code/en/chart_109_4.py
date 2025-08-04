import matplotlib.pyplot as plt
import numpy as np

# Factors to consider
factors = ["Origin", "Quality", "Brand", "Packaging", "Price", "Organic/Green Certification", 
           "Freshness", "Nutritional Content", "Purchase Convenience", "Supplier Reputation", "After-sales Service", "Promotions"]
# Corresponding proportions (%)
proportions = [42.42, 38.64, 35.00, 33.64, 29.70, 28.79, 
               21.82, 21.36, 14.09, 13.33, 12.73, 6.67]

x = np.arange(len(factors))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Factors Considered by Chinese Rural E-commerce Consumers When Buying Agricultural Products in 2025')

plt.tight_layout()
plt.show()