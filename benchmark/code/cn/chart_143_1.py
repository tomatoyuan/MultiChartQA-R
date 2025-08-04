import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["200元及以下", "201-500元", "501-1000元", "1001-1500元", "1501-2000元", "2000元以上"]
percentages = [15.0, 34.4, 38.9, 8.9, 1.6, 1.2]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange', label='消费占比（%）')
ax.set_ylabel('消费占比（%）')
ax.set_xlabel('月均消费金额区间')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_title('2023年中国消费者化妆品月均消费调查')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()