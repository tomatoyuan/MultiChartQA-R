import matplotlib.pyplot as plt
import numpy as np

# Wedding budget ranges
categories = ["Below 50,000 yuan", "50,000 - 100,000 yuan", "100,000 - 200,000 yuan", "200,000 - 300,000 yuan", "300,000 - 400,000 yuan", "400,000 - 500,000 yuan", "Above 500,000 yuan"]
# Corresponding proportions (%)
proportions = [8.8, 30.4, 34.2, 18.2, 6.5, 1.2, 0.7]
# Simulated number of money bags (roughly corresponding to the proportion, can be fine - tuned to make the visual closer to the original image)
bag_counts = [1, 6, 7, 4, 2, 1, 1]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw the "money bag" bar chart (simulate the stacking effect with multiple small rectangles)
for i in range(len(categories)):
    for j in range(bag_counts[i]):
        rect = plt.Rectangle((x[i] - 0.2, j * 1), 0.4, 1, color='orange')
        ax.add_patch(rect)
        # Add the proportion label near the top - most money bag (only add it once)
        if j == bag_counts[i] - 1:
            ax.text(x[i], (j + 1) * 1 + 0.2, f'{proportions[i]}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Money bag stacking illustration')
ax.set_xlabel('Budget range')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, max(bag_counts) + 1)  # Reserve space for displaying labels
ax.axis('off')  # Hide the default axes to highlight the money bag style

ax.set_title('Survey on Chinese wedding planning expenses/budgets')

plt.tight_layout()
plt.show()