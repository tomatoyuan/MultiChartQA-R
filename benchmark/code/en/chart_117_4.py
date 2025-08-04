import matplotlib.pyplot as plt
import numpy as np

# Smart home functions
functions = [
    "Smart lighting control system", "Smart security control system", "Smart curtain control system", 
    "Smart environmental monitoring system", "Smart home audio - video control system", "Remote home appliance control system", 
    "Smart voice assistant", "One - key control scenario mode", "Background music system", "Energy management system"
]
# Corresponding proportion (%)
proportions = [35.40, 35.24, 31.59, 31.59, 30.79, 29.84, 29.84, 29.52, 22.70, 21.75]

x = np.arange(len(functions))  # x - axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# Set x - axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(functions, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Smart home functions that Chinese consumers are interested in 2025')

plt.tight_layout()
plt.show()