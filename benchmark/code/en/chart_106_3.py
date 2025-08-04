import matplotlib.pyplot as plt
import numpy as np

# Brand names
brands = ["Nongfu Spring Mineral Water", "Wahaha Mineral Water", "C'estbon Mineral Water", "Ganten Mineral Water", "Master Kong Mineral Water", 
          "Gingkgo Spring Mineral Water", "Coca - Cola Sparkling Mineral Water", "Kunlun Mountains Mineral Water", "Ice Dew Mineral Water", "Evergrande Spring Mineral Water", 
          "French Evian Mineral Water", "San Pellegrino", "Poland Spring"]
# Corresponding proportions (%)
proportions = [48.53, 45.04, 36.73, 35.66, 29.49, 
               22.79, 22.25, 20.38, 20.11, 18.23, 
               14.75, 11.80, 10.72]

x = np.arange(len(brands))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate labels
ax.set_xticks(x)
ax.set_xticklabels(brands, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Most Frequently Purchased Packaged Drinking Water Brands by Chinese Consumers in 2025')

plt.tight_layout()
plt.show()