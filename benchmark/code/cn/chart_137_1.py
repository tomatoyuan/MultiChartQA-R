import matplotlib.pyplot as plt
import numpy as np

# 数据
channels = ["网络搜索引擎", "社交媒体", "电商平台官方渠道", "传统新闻媒体", "行业报告和调查", "亲友", "其他"]
percentages = [63.0, 59.2, 55.3, 35.2, 11.4, 6.3, 0.2]

x = np.arange(len(channels))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('百分比（%）')
ax.set_xlabel('了解途径')
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=45, ha='right')
ax.set_title('2024年中国消费者了解AI电商的主要途径')

plt.tight_layout()
plt.show()