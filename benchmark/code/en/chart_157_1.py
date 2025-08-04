import matplotlib.pyplot as plt
import numpy as np

# Labels and colors for each layer (stacked from bottom to top)
categories = ['Unwilling to pay extra premium', 'Willing to pay within 5% extra', 'Willing to pay 5%-10% extra', 'Willing to pay 10%-20% extra', 'Willing to pay over 20% extra']
colors = ['#FF5C40', '#FF7B5C', '#FF9C80', '#FFBFA6', '#FFE3DC']

# Data arranged in stacking order
green_total = [34, 34, 22, 9, 1]
food_drink = [30, 36, 22, 10, 2]

# Transpose the data for stacked plotting
data = np.array([green_total, food_drink])
data_cum = data.cumsum(axis=1)

x = np.arange(data.shape[0])
width = 0.5

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the stacked bar chart (from bottom to top)
for i in range(len(categories)):
    bottoms = data_cum[:, i - 1] if i > 0 else np.zeros_like(x)
    values = data[:, i]
    bars = ax.bar(x, values, width, bottom=bottoms, label=categories[i], color=colors[i])

    # Add text labels
    for j in range(len(x)):
        if values[j] > 3:  # Avoid overlapping for small values
            ax.text(x[j], bottoms[j] + values[j]/2, f'{values[j]}%', ha='center', va='center', fontsize=10, color='white')

# Set the title and axes
ax.set_xticks(x)
ax.set_xticklabels(['Overview of green consumption willingness', 'Food and beverages'], fontsize=12)
ax.set_ylabel('Proportion (%)', fontsize=12)
ax.set_ylim(0, 105)
ax.set_title('Chinese consumers have a certain willingness to pay a green premium', fontsize=16, weight='bold')

# Legend (in the same order as the stacking in the chart)
ax.legend(loc='center', title='Proportion willing to pay extra premium', fontsize=8, title_fontsize=10)

plt.tight_layout()
plt.show()