import matplotlib.pyplot as plt
import numpy as np

# Ways to learn about physical examination institutions
channels = ["Company organization", "Relatives and friends introduction", "Website information", "Offline advertising", "Health lectures", "Self-media", "Newspapers and magazines"]
# Corresponding proportion (%)
proportions = [37.93, 36.12, 34.85, 32.49, 31.94, 29.22, 27.22]

x = np.arange(len(channels))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=15, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Ways for Chinese health examination consumers to learn about physical examination institutions in 2025')

plt.tight_layout()
plt.show()