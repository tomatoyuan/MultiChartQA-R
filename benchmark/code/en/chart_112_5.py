import matplotlib.pyplot as plt
import numpy as np

# Factors
factors = ["Appearance", "After-sales service", "Quality", "Brand and reputation", "Rarity", "Price"]
# Proportion of each rating (1 - 5 points), in the order of 5 points, 4 points, 3 points, 2 points, 1 point
data = np.array([
    [30.79, 21.06, 17.59, 16.67, 13.89],
    [28.94, 24.31, 21.05, 15.28, 10.42],
    [27.08, 26.85, 18.06, 15.51, 12.50],
    [25.93, 28.70, 18.29, 14.81, 12.27],
    [23.61, 30.56, 18.52, 14.58, 12.73],
    [17.59, 29.40, 21.30, 16.20, 15.51]
])

# Colors corresponding to the scores, corresponding to the colors in the chart
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
scores = ["5 points", "4 points", "3 points", "2 points", "1 point"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(factors))

for i in range(data.shape[1]):
    ax.bar(factors, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # Add numerical annotations
    for j in range(len(factors)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_title('Rating of various factors of Chinese figurine consumers for figurines in 2025')

# 调整图例位置到右侧外侧
ax.legend(
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=10,
    title="Scores",
    title_fontsize=12
)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# 调整子图布局，为图例留出空间
plt.subplots_adjust(right=0.85)
plt.show()