import matplotlib.pyplot as plt
import numpy as np

# 改进建议及对应占比数据
suggestions = [
    "缺少教学等入门知识", "相关资讯更新不及时", "内容杂乱不够精细", 
    "缺少娱乐功能", "App使用不够流畅", "操作不方便"
]
proportions = [47.59, 44.92, 42.25, 37.97, 36.90, 28.34]

y = np.arange(len(suggestions))

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注，在条形右侧
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(suggestions)
ax.set_xlabel('占比（%）')
ax.set_title('中国券商自营类APP用户改进建议调查')

plt.tight_layout()
plt.show()