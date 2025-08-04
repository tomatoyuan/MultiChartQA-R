import matplotlib.pyplot as plt
import numpy as np

# Data preparation
factors = ["Taste", "Price", "Packaging", "Promotion", "Others"]
proportions = [66.2, 63.2, 44.1, 42.1, 0.5]  # Proportion (%)

x = np.arange(len(factors))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, proportions, color='coral', width=0.6)
ax.set_title('Factors Influencing Chinese Consumers\' Purchase of Sugar - Free Drinks in 2023', fontsize=14)
ax.set_ylabel('Attention Proportion (%)')
ax.set_xticks(x)
ax.set_xticklabels(factors)
ax.set_ylim(0, 75)  # Adjust the y - axis range for better data display

# Add numerical annotations
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=12)

plt.tight_layout()
plt.show()