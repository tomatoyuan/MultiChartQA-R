import matplotlib.pyplot as plt
import numpy as np

# 手办类型
handmade_types = ["高达系列手办", "游戏类型手办", "虚拟人物手办", "漫威DC电影系列手办", 
                  "汽车模型手办", "国产动漫手办（秦时明月等）", "日系动漫手办（火影忍者等）"]
# 对应占比（%）
proportions = [28.94, 30.09, 32.41, 36.81, 37.04, 38.66, 38.89]

y = np.arange(len(handmade_types))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(handmade_types)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国手办消费者喜欢的手办类型')

plt.tight_layout()
plt.show()