import matplotlib.pyplot as plt
import numpy as np

# Physical examination service indicators
indicators = ["Convenience of physical examination appointment", "Professionalism and completeness of physical examination report content", "Time to obtain physical examination report", 
              "Waiting time for physical examination", "Environment of the physical examination venue", "Equipment in the physical examination center", "Response and problem - solving speed during physical examination"]
# Proportions of each score (5 points, 4 points, 3 points, 2 points, 1 point)
data = np.array([
    [33.39, 38.66, 19.60, 7.08, 1.27],
    [32.85, 38.66, 18.15, 8.53, 1.81],
    [31.58, 31.94, 21.78, 13.07, 1.63],
    [26.50, 35.93, 25.59, 9.98, 2.00],
    [32.49, 41.38, 17.06, 7.44, 1.63],
    [41.74, 38.11, 15.98, 3.60, 0.54],
    [28.31, 45.01, 14.34, 9.44, 2.90]
])
# Colors corresponding to scores
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
scores = ["5 points", "4 points", "3 points", "2 points", "1 point"]

# 增大画布宽度以容纳外侧图例
fig, ax = plt.subplots(figsize=(14, 8))
bottom = np.zeros(len(indicators))

for i in range(data.shape[1]):
    ax.bar(indicators, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # Add numerical annotations
    for j in range(len(indicators)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', 
                ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)', fontsize=10)
ax.set_title('Satisfaction scores of Chinese consumers for various indicators of physical examination services in 2025', fontsize=12, pad=20)

# 将图例放在右侧外侧
ax.legend(
    loc='center left',  # 图例的锚点为左中部
    bbox_to_anchor=(1.02, 0.5),  # 锚点位置：右侧边界外2%，垂直居中
    fontsize=10,
    title="Scores",  # 图例标题
    title_fontsize=12
)

plt.xticks(rotation=15, ha='right', fontsize=9)  # 调整x轴标签字体大小
plt.ylim(0, 110)  # 预留顶部空间避免标注溢出
plt.tight_layout()
plt.subplots_adjust(right=0.8)  # 调整右侧边距，为图例留出空间
plt.show()