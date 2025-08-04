import matplotlib.pyplot as plt
import numpy as np

# Purchase reasons
reasons = ["Health monitoring", "Exquisite and personalized product design", "Record exercise status", "Show off and demonstrate status", "Check the location of children or the elderly", 
           "Convenience for daily life (e.g., sending and receiving messages and calls)", "Simple self - preference"]
# Corresponding proportions (%)
proportions = [45.48, 44.71, 43.44, 40.38, 25.35, 25.10, 19.11]

x = np.arange(len(reasons))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate labels
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=15, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Reasons for Chinese consumers to buy smartwatches in 2025')

plt.tight_layout()
plt.show()