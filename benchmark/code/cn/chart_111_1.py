import matplotlib.pyplot as plt
import numpy as np

# 观看时段
time_periods = ["周末、节假日", "空闲无聊时", "平时的碎片时间里", "睡觉前", "失眠、压力大时", "吃饭时"]
# 对应占比（%）
proportions = [41.73, 41.36, 37.65, 31.36, 30.74, 26.67]

x = np.arange(len(time_periods))  # x轴坐标

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(time_periods)
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国电视剧观众观看电视剧时段')

plt.tight_layout()
plt.show()