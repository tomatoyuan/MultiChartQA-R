import matplotlib.pyplot as plt
import numpy as np

# 使用场景类型
scenarios = ["睡前收听", "上下班通勤", "做家务时", "运动散步", "早晚洗漱时", 
             "驾驶途中", "学习工作时", "社交聚会中", "亲子教育"]
# 对应占比（%）
proportions = [35.24, 31.91, 30.85, 28.99, 26.86, 24.07, 23.67, 22.61, 21.68]

x = np.arange(len(scenarios))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(scenarios, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国有声书用户使用有声书APP场景类型')

plt.tight_layout()
plt.show()