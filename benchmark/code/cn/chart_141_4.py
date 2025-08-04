import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["孕前检查", "备孕保健品", "备孕饮食", "验孕", "备孕书籍", "家居家电", "汽车", "其他"]
percentages = [78.5, 77.4, 74.7, 58.1, 31.7, 15.5, 5.7, 0.4]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange', label='新增消费占比（%）')
ax.set_ylabel('新增消费占比（%）')
ax.set_xlabel('消费品类')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_title('2023年中国备孕人群新增消费品类分布')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()