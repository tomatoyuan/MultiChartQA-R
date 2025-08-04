import matplotlib.pyplot as plt
import numpy as np

# Satisfaction dimensions
dimensions = ["Brand Awareness", "Endorser/Advertising Promotion", "Taste", "Beverage Ingredients and Efficacy", 
              "Product Variety/Differentiation", "Price", "Promotional Activities", "Purchase Convenience", 
              "After - sales Service", "Appearance Design", "Hygiene Quality", "Marketing Methods (IP Co - branding/Experiential Consumption Activities)"]
# Proportion of different ratings (1 - 5 points) under each dimension, in the order of 5 points, 4 points, 3 points, 2 points, 1 point
data = np.array([
    [41.55, 43.16, 10.04, 5.36, 1.39],
    [32.98, 34.32, 24.13, 7.50, 1.07],
    [40.48, 37.80, 14.48, 4.58, 2.68],
    [33.51, 39.14, 17.43, 6.43, 3.49],
    [32.71, 36.19, 21.98, 7.24, 1.88],
    [26.27, 42.63, 20.64, 7.77, 2.69],
    [32.17, 36.46, 19.64, 8.85, 2.88],
    [28.95, 35.12, 20.65, 10.99, 4.29],
    [28.69, 33.24, 24.93, 9.12, 4.02],
    [32.98, 42.09, 17.43, 5.36, 2.18],
    [38.61, 36.73, 16.89, 4.03, 3.79],
    [29.49, 34.85, 25.21, 8.31, 2.16]
])

# Colors corresponding to the ratings, corresponding to the colors in the chart
colors = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
scores = ["5 Points", "4 Points", "3 Points", "2 Points", "1 Point"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(dimensions))

for i in range(data.shape[1]):
    ax.bar(dimensions, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # Add numerical annotations
    for j in range(len(dimensions)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_title('2025 Satisfaction Ratings of Chinese Consumers for Currently Available Packaged Drinking Water in the Market')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()