import matplotlib.pyplot as plt
import numpy as np

# Effective means types
means = ["Strengthen the supervision of the TV drama market", "Innovate the script content", "Improve the acting skills of actors", "Reduce commercial interruptions", 
         "Shoot diverse themes", "Improve the production level", "Increase production costs"]
# Corresponding proportions (%)
proportions = [39.01, 37.78, 37.28, 33.46, 33.09, 31.85, 31.48]

x = np.arange(len(means))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(means, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Effective means for Chinese TV drama viewers to improve the quality and ratings of domestic TV dramas in 2025')

plt.tight_layout()
plt.show()