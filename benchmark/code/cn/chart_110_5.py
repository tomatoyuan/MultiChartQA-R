import matplotlib.pyplot as plt
import numpy as np

# 改进方向
directions = ["丰富有声书种类", "内容质量提升", "内容同质化问题", "个性化推荐优化", 
              "增加社区交互功能", "更精确的推荐算法", "更好的用户界面"]
# 对应占比（%）
proportions = [38.16, 38.16, 35.37, 32.71, 32.31, 32.18, 32.05]

x = np.arange(len(directions))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(directions, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国有声书用户认为中国有声书平台需要改进的方向')

plt.tight_layout()
plt.show()