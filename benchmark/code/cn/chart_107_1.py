import matplotlib.pyplot as plt
import numpy as np

# 运营商名称
operators = ["中国移动", "中国联通", "中国电信", "中国广电"]
# 对应占比（%）
proportions = [59.10, 38.65, 35.33, 16.27]

x = np.arange(len(operators))  # x轴坐标

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(operators)
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国用户常使用的通信运营商')

plt.tight_layout()
plt.show()