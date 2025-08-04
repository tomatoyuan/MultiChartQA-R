import matplotlib.pyplot as plt
import numpy as np

# 评价维度
dimensions = [
    "认为使用有声书APP有助于阅读习惯的养成以及知识面的增加",
    "认为有声书的使用方式简单，对阅读能力（识字、阅读理解能力）要求不高",
    "倾向于收听已有数据（播放、收藏、评价数量）高的有声书",
    "倾向于收听已经完结的有声书"
]
# 各维度下不同评分（1-5分）的占比，按 5分、4分、3分、2分、1分 顺序
data = np.array([
    [32.18, 36.84, 20.48, 9.44, 1.06],
    [30.32, 37.63, 18.88, 7.32, 5.85],
    [39.23, 30.85, 21.02, 6.91, 1.99],
    [35.11, 40.29, 12.63, 9.58, 2.39]
])

# 评分对应的颜色，与图表中的颜色对应
colors = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
scores = ["5分", "4分", "3分", "2分", "1分"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(dimensions))

for i in range(data.shape[1]):
    ax.bar(dimensions, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # 添加数值标注
    for j in range(len(dimensions)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国有声书用户对有声书真实体验和感受评价情况')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()