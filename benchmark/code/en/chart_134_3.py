import matplotlib.pyplot as plt
import numpy as np

# Data
effects = ["Moisturizing", "Antioxidant", "Soothing", "Whitening", "Brightening", "Isolation"]
percentages = [57.8, 52.3, 47.1, 38.1, 31.2, 31.2]

x = np.arange(len(effects))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Efficacy Type')
ax.set_xticks(x)
ax.set_xticklabels(effects)
ax.set_title('Preferred Efficacy of Sunscreen Cosmetics among Chinese Consumers')

plt.tight_layout()
plt.show()