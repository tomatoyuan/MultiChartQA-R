import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['保险理赔', '保险种类', '保险期限', '保险金额']
values = [41, 25, 22, 12]
colors = ['#ff7f9f', '#ffbf7f', '#7fffaa', '#7fbfff']  # 对应颜色

x = np.arange(len(labels))  # x轴位置

fig, ax = plt.subplots()
rects = ax.bar(x, values, color=colors)

# 添加数值标签
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}%'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 标签位置偏移
                textcoords="offset points",
                ha='center', va='bottom')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('关注比例')
ax.set_title('购买保险关注什么？')

plt.show()