import matplotlib.pyplot as plt
import numpy as np

# 对盲盒产业发展看法的描述
opinions = ["消费者容易成瘾，浪费大量金钱", "价格不合理，部分产品溢价严重", 
            "下游市场投机，炒作严重，行业发展处于无序状态", "噱头过大，盲盒产品本身缺乏故事感和实用性", 
            "部分产品设计抄袭，质量不佳，粗制滥造"]
# 对应占比（%）
proportions = [34.03, 34.95, 41.67, 43.52, 44.68]

y = np.arange(len(opinions))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(opinions)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国手办消费者对盲盒产业发展的看法')

plt.tight_layout()
plt.show()