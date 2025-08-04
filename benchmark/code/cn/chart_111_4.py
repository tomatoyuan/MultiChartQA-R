import matplotlib.pyplot as plt
import numpy as np

# 有效手段类型
means = ["加强电视剧市场监管", "创新剧本内容", "提升演员演技", "减少广告插播", 
         "拍摄多元题材", "提高制作水平", "增加制作成本"]
# 对应占比（%）
proportions = [39.01, 37.78, 37.28, 33.46, 33.09, 31.85, 31.48]

x = np.arange(len(means))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(means, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国电视剧观众认为提高国产剧质量和收视率的有效手段')

plt.tight_layout()
plt.show()