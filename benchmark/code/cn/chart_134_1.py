import matplotlib.pyplot as plt
import numpy as np

# 左侧：防晒必要性数据
labels_left = ["认为防晒有必要", "认为防晒没有必要"]
proportions_left = [92.5, 7.5]

# 右侧：防晒重要性因素数据
labels_right = ["防止晒黑", "防止皮肤晒伤", "防止光老化", "防止色斑形成", "预防皮肤癌"]
proportions_right = [52.5, 83.2, 57.2, 57.3, 31.5]

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 6))

# 绘制左侧对比图
x_left = np.arange(len(labels_left))
bars = ax_left.bar(x_left, proportions_left, color=['#FFA07A', '#FFD700'])
for i, prop in enumerate(proportions_left):
    ax_left.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')
ax_left.set_ylabel('占比（%）')
ax_left.set_xticks(x_left)
ax_left.set_xticklabels(labels_left)
ax_left.set_title('中国消费者对于防晒的看法')
ax_left.yaxis.set_ticks([])
for spine in ['top', 'right', 'left']:
    ax_left.spines[spine].set_visible(False)

# 绘制右侧雷达图
num_vars = len(labels_right)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proportions_right += proportions_right[:1]
angles += angles[:1]
ax_right.fill(angles, proportions_right, color='#FFA07A', alpha=0.25)
ax_right.plot(angles, proportions_right, color='#FFA07A', linewidth=2)
for i, (angle, prop) in enumerate(zip(angles[:-1], proportions_right[:-1])):
    ax_right.text(angle, prop + 3, f'{prop}%', ha='center', va='bottom')
ax_right.set_yticklabels([])
ax_right.set_xticks(angles[:-1])
ax_right.set_xticklabels(labels_right)
ax_right.set_title('中国消费者认为防晒的重要性因素')

plt.tight_layout()
plt.show()