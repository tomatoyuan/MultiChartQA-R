import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['Insurance Claims', 'Insurance Types', 'Insurance Duration', 'Insurance Amount']
values = [41, 25, 22, 12]
colors = ['#ff7f9f', '#ffbf7f', '#7fffaa', '#7fbfff']  # 对应颜色

# 调整横坐标位置，增加间距
x = np.arange(len(labels)) * 1.2  # 扩大横坐标间距（原间距×1.2）

# 创建画布并适当增大宽度
fig, ax = plt.subplots(figsize=(10, 6))  # 加宽画布以容纳更宽的间距
rects = ax.bar(x, values, color=colors, width=0.8)  # 控制柱宽，避免过宽

# 添加数值标签
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}%'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 标签位置偏移
                textcoords="offset points",
                ha='center', va='bottom')

# 设置横坐标刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10)  # 可适当减小字体
ax.set_ylabel('Attention Ratio')
ax.set_title('What do people focus on when buying insurance?')

# 调整x轴范围，避免两端标签贴近边缘
ax.set_xlim(x[0] - 0.8, x[-1] + 0.8)

plt.tight_layout()  # 自动调整布局
plt.show()