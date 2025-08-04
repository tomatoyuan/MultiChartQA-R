import matplotlib.pyplot as plt
import numpy as np

# Purchase channels
channels = [
    "Professional home furnishing market/home furnishing city", "Brand exclusive stores", "Online purchase",
    "Recommendation or transfer from friends/family", "Arranged by designers or others",
    "Home furnishing expo", "Second - hand market/idle trading platform", "Shopping malls", "Factory pick - up"
]
# Corresponding proportions (%)
proportions = [37.70, 36.98, 35.19, 34.29, 33.57, 32.14, 28.19, 28.19, 24.24]

x = np.arange(len(channels))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Ways for Chinese consumers to purchase hard - decoration home furnishing products in 2025')

plt.tight_layout()
plt.show()