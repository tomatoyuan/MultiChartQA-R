import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["非常满意", "比较满意", "一般", "比较不满意", "非常不满意"]
percentages = [19.1, 46.4, 26.7, 6.7, 1.1]
# 用于排序的满意度评分（假设从高到低）
satisfaction_score = [5, 4, 3, 2, 1]

# 按满意度评分排序
sorted_indices = np.argsort(satisfaction_score)
labels = [labels[i] for i in sorted_indices]
percentages = [percentages[i] for i in sorted_indices]
satisfaction_score = [satisfaction_score[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
ax.plot(satisfaction_score, percentages, marker='o', color='orange', linewidth=2)
ax.fill_between(satisfaction_score, percentages, color='orange', alpha=0.2)

# 添加数据点和数值标注
for x, y, label in zip(satisfaction_score, percentages, labels):
    ax.scatter(x, y, color='orange', s=50)
    ax.text(x, y + 1.5, f'{y}%', ha='center', va='bottom')

# 设置 x 轴标签为满意度等级
ax.set_xticks(satisfaction_score)
ax.set_xticklabels(labels, rotation=15)
ax.set_ylabel('百分比（%）')
ax.set_title('中国居民对自身睡眠质量的主观评价')

plt.tight_layout()
plt.show()