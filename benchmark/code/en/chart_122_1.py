import matplotlib.pyplot as plt
import numpy as np

# Data
sources = [
    "Introduced by relatives and friends", "Short - video platforms", "Content - sharing platforms", 
    "Met through others' weddings", "Wedding - related websites/APPs", "Internet search", "Advertising"
]
proportions = [43.8, 43.5, 38.8, 37.9, 36.5, 27.1, 25.9]

y = np.arange(len(sources))

fig, ax = plt.subplots(figsize=(8, 5))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(sources)
ax.set_xlabel('Proportion (%)')
ax.set_title('Survey on information sources of wedding companies in China')

plt.tight_layout()
plt.show()