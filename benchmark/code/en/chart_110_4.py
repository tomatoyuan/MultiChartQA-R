import matplotlib.pyplot as plt
import numpy as np

# Evaluation dimensions
dimensions = [
    "Think that using audiobook apps helps \ndevelop reading habits and increase knowledge",
    "Think that audiobooks are easy to use and have low \nrequirements for reading ability (literacy and reading comprehension ability)",
    "Prefer to listen to audiobooks with high \nexisting data (number of plays, favorites, and reviews)",
    "Prefer to listen to completed audiobooks"
]
# Proportions of different ratings (1 - 5 stars) under each dimension, in the order of 5 stars, 4 stars, 3 stars, 2 stars, 1 star
data = np.array([
    [32.18, 36.84, 20.48, 9.44, 1.06],
    [30.32, 37.63, 18.88, 7.32, 5.85],
    [39.23, 30.85, 21.02, 6.91, 1.99],
    [35.11, 40.29, 12.63, 9.58, 2.39]
])

# Colors corresponding to the ratings, corresponding to the colors in the chart
colors = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
scores = ["5 stars", "4 stars", "3 stars", "2 stars", "1 star"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(dimensions))

for i in range(data.shape[1]):
    ax.bar(dimensions, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # Add numerical annotations
    for j in range(len(dimensions)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_title('Evaluation of the real experience and feelings of Chinese audiobook users in 2025')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()