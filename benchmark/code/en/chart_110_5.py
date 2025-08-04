import matplotlib.pyplot as plt
import numpy as np

# Improvement directions
directions = ["Enrich the variety of audiobooks", "Improve content quality", "Solve content homogenization problem", 
              "Optimize personalized recommendation", "Add community interaction features", "Use more accurate recommendation algorithms", "Create a better user interface"]
# Corresponding proportions (%)
proportions = [38.16, 38.16, 35.37, 32.71, 32.31, 32.18, 32.05]

x = np.arange(len(directions))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(directions, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Directions for improvement of Chinese audiobook platforms according to Chinese audiobook users in 2025')

plt.tight_layout()
plt.show()