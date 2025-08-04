import matplotlib.pyplot as plt
import numpy as np

# Types of information of concern
info_types = ["Scientific parenting knowledge", "Pregnancy health care knowledge", "Recommendation of maternal and infant products/foods", "Scientific pregnancy guide", 
              "Postpartum rehabilitation guide", "Early education courses", "Baby and toddler fashion clothing", "Pregnancy dressing guide"]
# Corresponding proportions (%)
proportions = [34.62, 33.60, 33.20, 32.59, 32.59, 32.59, 31.16, 28.31]

x = np.arange(len(info_types))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(info_types, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Main information of concern for Chinese maternal and infant consumers during pregnancy and parenting in 2025')

plt.tight_layout()
plt.show()