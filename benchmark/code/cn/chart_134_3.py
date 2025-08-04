import matplotlib.pyplot as plt
import numpy as np

# 数据
effects = ["保湿", "抗氧化", "舒缓", "美白", "提亮", "隔离"]
percentages = [57.8, 52.3, 47.1, 38.1, 31.2, 31.2]

x = np.arange(len(effects))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('百分比（%）')
ax.set_xlabel('功效类型')
ax.set_xticks(x)
ax.set_xticklabels(effects)
ax.set_title('中国消费者购买防晒化妆品倾向功效')

plt.tight_layout()
plt.show()