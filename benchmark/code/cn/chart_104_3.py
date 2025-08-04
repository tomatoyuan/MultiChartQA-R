import matplotlib.pyplot as plt
import numpy as np

# 学习音乐主要原因
reasons = ["培养孩子兴趣", "提升自身涵养", "增加一门特长", "培养孩子精神", "减缓就学压力", 
           "自身热爱", "升学加分", "别人的孩子都学了", "从事相关工作", "能与明星近距离接触"]
# 对应占比（%）
proportions = [30.09, 28.88, 27.26, 26.18, 25.37, 25.37, 21.46, 21.46, 21.05, 20.78]

x = np.arange(len(reasons))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 0.5, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国用户学习音乐主要原因')

plt.tight_layout()
plt.show()