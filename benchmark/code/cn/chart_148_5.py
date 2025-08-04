import matplotlib.pyplot as plt
import numpy as np

# 数据准备
scenarios = ["休闲聚会", "工作/学习", "就餐", "运动", "电竞游戏", "新品上市的时候", "驾驶"]
proportions = [62.8, 53.1, 42.4, 42.0, 28.6, 28.1, 25.6]  # 占比（%）

x = np.arange(len(scenarios))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, proportions, color='coral')
ax.set_title('2023年中国消费者饮用无糖饮料场景', fontsize=14)
ax.set_ylabel('占比（%）')
ax.set_xlabel('饮用场景')
ax.set_xticks(x)
ax.set_xticklabels(scenarios, rotation=45, ha='right')  # 旋转x轴标签，避免重叠
ax.set_ylim(0, 70)  # 调整y轴范围，适配最大占比（62.8%）

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# 添加图例
ax.legend(bars, ['占比'], loc='upper right')

plt.tight_layout()
plt.show()