import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['“双减”前', '“双减”后']
tutoring = [56, 18]     # 报辅导班的家长比例
home_edu = [68, 77]     # 家庭教育时间占比

x = np.arange(len(labels))
width = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# 图1：报辅导班比例
ax1.bar(x, tutoring, color='orange')
ax1.set_title('“双减”前后报辅导班的家长占比')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylim(0, 100)
for i, v in enumerate(tutoring):
    ax1.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

# 图2：家庭教育时间比例
ax2.bar(x, home_edu, color='red')
ax2.set_title('“双减”前后家庭教育时间占比的变化')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylim(0, 100)
for i, v in enumerate(home_edu):
    ax2.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

plt.suptitle('数据来源：中华人民共和国教育部，《“双减”政策对家庭教育的影响调研》', fontsize=10, y=0)
plt.tight_layout()
plt.show()