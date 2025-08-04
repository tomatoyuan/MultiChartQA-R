import matplotlib.pyplot as plt
import numpy as np

# Descriptions of views on the development of the blind box industry
opinions = ["Consumers are prone to addiction and waste a lot of money", 
            "The prices are unreasonable, and some products have a serious premium", 
            "The downstream market is speculative and hyped seriously, and the industry development is in a disorderly state", 
            "The gimmicks are too big, and the blind box products themselves lack a sense of story and practicality", 
            "Some products are plagiarized in design, with poor quality and shoddy workmanship"]
# Corresponding proportions (%)
proportions = [34.03, 34.95, 41.67, 43.52, 44.68]

y = np.arange(len(opinions))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(opinions)
ax.set_xlabel('Proportion (%)')
ax.set_title('Views of Chinese figurine consumers on the development of the blind box industry in 2025')

plt.tight_layout()
plt.show()