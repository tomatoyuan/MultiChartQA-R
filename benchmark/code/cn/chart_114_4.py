import matplotlib.pyplot as plt
import numpy as np

# 了解体检机构的途径
channels = ["单位组织", "亲友介绍", "网站信息", "线下广告", "健康讲座", "自媒体", "报刊杂志"]
# 对应占比（%）
proportions = [37.93, 36.12, 34.85, 32.49, 31.94, 29.22, 27.22]

x = np.arange(len(channels))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(channels)
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国健康体检消费者了解体检机构途径')

plt.tight_layout()
plt.show()