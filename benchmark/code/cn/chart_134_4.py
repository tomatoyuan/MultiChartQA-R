import matplotlib.pyplot as plt
import numpy as np

# 数据
expectations = ["产品效果持续时间长", "产品功效更精细化", "包装设计更美观、有创意", 
                "价格亲民", "产品安全性高", "推出复合功效的产品"]
percentages = [71.4, 47.0, 45.0, 37.1, 32.7, 31.9]

x = np.arange(len(expectations))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('百分比（%）')
ax.set_xlabel('期待类型')
ax.set_xticks(x)
ax.set_xticklabels(expectations, rotation=15, ha='right')
ax.set_title('中国消费者对防晒化妆品的发展期待')

plt.tight_layout()
plt.show()