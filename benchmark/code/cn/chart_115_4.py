import matplotlib.pyplot as plt
import numpy as np

# 数字化转型主要方式
methods = [
    "利用人工智能和机器学习", "采用云计算和SaaS服务", "自主开发和建设数字化平台或系统",
    "依托供应链上下游企业开展", "利用第三方电子商务平台开展", "购买通用型数字化软件或解决方案",
    "利用产业链龙头企业搭建的工业互联网等平台", "购买细分行业数字化软件或解决方案"
]
# 对应占比（%）
proportions = [7.69, 15.60, 16.67, 17.52, 28.63, 42.95, 47.01, 53.85]

y = np.arange(len(methods))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注，在条形右侧
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(methods)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国企业数字化转型主要方式')

plt.tight_layout()
plt.show()