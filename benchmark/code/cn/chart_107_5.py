import matplotlib.pyplot as plt
import numpy as np

# 5G应用领域
fields = ["5G智能终端", "5G传媒", "自动驾驶", "智能家居", "远程医疗", "教育", "VR"]
# 对应占比（%）
proportions = [44.00, 37.71, 37.71, 37.49, 36.80, 31.31, 27.09]

x = np.arange(len(fields))  # x轴坐标

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(fields)
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国用户期望未来5G应用的领域')

plt.tight_layout()
plt.show()