import matplotlib.pyplot as plt
import numpy as np

# Product types
product_types = ["Handicraft products", "Clothes, shoes and hats, etc.", "Agricultural and industrial production tools (e.g., sickles, hoes, machinery and equipment, etc.)", 
                 "Household appliances (e.g., mobile phones, computers, refrigerators, color TVs, etc.)", "Daily necessities (e.g., paper products for cleaning, household storage, skin - care products, etc.)", 
                 "Food and fresh products (e.g., grains and oils, fruits, alcoholic beverages, snacks, etc.)"]
# Corresponding proportions (%)
proportions = [23.94, 27.39, 38.83, 39.10, 41.76, 50.53]

y = np.arange(len(product_types))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(product_types)
ax.set_xlabel('Proportion (%)')
ax.set_title('Types of products sold by rural e-commerce operators in China in 2025')

plt.tight_layout()
plt.show()