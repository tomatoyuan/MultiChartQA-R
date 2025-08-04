import matplotlib.pyplot as plt
import numpy as np

# 关注的信息类型
info_types = ["科学育儿知识", "孕期保健知识", "母婴用品/食品“种草”", "科学怀孕指南", 
              "产后康复指南", "早教课程", "婴童时尚服饰", "孕期穿搭指南"]
# 对应占比（%）
proportions = [34.62, 33.60, 33.20, 32.59, 32.59, 32.59, 31.16, 28.31]

x = np.arange(len(info_types))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(info_types, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国母婴消费者怀孕及育儿过程中主要关注的信息')

plt.tight_layout()
plt.show()