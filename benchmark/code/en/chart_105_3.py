import matplotlib.pyplot as plt
import numpy as np

# Aspects of concern
aspects = ["Price", "Interface design and operation", "Battery", "Appearance design", "Phone matching speed", "Usage accuracy", 
           "Waterproof function", "After-sales service", "Brand", "Anti-shatter function"]
# Corresponding proportions (%)
proportions = [47.77, 44.33, 40.38, 36.56, 33.63, 32.48, 
               22.93, 22.17, 21.91, 14.01]

x = np.arange(len(aspects))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(aspects, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Aspects Chinese consumers are concerned about when buying smartwatches in 2025')

plt.tight_layout()
plt.show()