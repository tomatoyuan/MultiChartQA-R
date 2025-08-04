import matplotlib.pyplot as plt
import numpy as np

# Evaluation dimensions
dimensions = ["Novel Format", "Real - time Update", "Rich Content", "Strong Interaction", "Professional and Authoritative", 
              "Exclusive Report", "Data Support", "International Perspective", "In - depth Analysis"]
# Proportions of different scores (1 - 5 points) in each dimension, in the order of 5 points, 4 points, 3 points, 2 points, 1 point
data = np.array([
    [29.82, 46.05, 14.04, 7.02, 3.07],
    [43.53, 32.89, 18.64, 3.51, 1.43],
    [36.62, 36.51, 16.89, 7.13, 2.85],
    [28.07, 35.20, 27.30, 7.46, 1.97],
    [35.64, 33.44, 21.60, 6.03, 3.29],
    [29.39, 38.93, 18.53, 11.61, 1.54],
    [38.05, 34.43, 18.53, 5.70, 3.29],
    [35.96, 37.39, 17.98, 6.92, 1.75],
    [35.96, 34.76, 20.18, 6.47, 2.63]
])

# Colors corresponding to scores, corresponding to the colors in the chart
colors = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
scores = ["5 Points", "4 Points", "3 Points", "2 Points", "1 Point"]

fig, ax = plt.subplots(figsize=(14, 8))  # 增加图形宽度以容纳外侧图例
bottom = np.zeros(len(dimensions))

for i in range(data.shape[1]):
    ax.bar(dimensions, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # Add numerical annotations
    for j in range(len(dimensions)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_title('2025 Importance Scores of Financial Media News Given by Chinese Financial News Users')

# 将图例移至图表右侧外侧
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()