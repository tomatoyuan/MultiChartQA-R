import matplotlib.pyplot as plt
import numpy as np

# Consideration factors
factors = ["Audiobook content", "Narrator's voice and ability", "Audiobook duration", "Whether the audiobook is adapted from an IP", "Audiobook price", "Audiobook update frequency"]
# Corresponding proportions (%)
proportions = [40.82, 38.70, 34.71, 34.57, 34.04, 33.38]

x = np.arange(len(factors))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=30, ha='right', fontsize=11)
ax.set_ylabel('Proportion (%)')
ax.set_title('Primary considerations for Chinese audiobook users when choosing audiobooks in 2025')

plt.tight_layout()
plt.show()