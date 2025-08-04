import matplotlib.pyplot as plt
import numpy as np

# 选择倍数播放的原因
reasons = ["视频质量不佳", "习惯倍速播放，感觉更舒适", "演员语速过慢，影响观看节奏", 
           "部分内容无趣或拖沓，不想细看", "节省时间，快速了解剧情"]
# 对应占比（%）
proportions = [29.33, 41.71, 45.71, 46.29, 50.10]

y = np.arange(len(reasons))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(reasons)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国电视剧观众选择倍数播放原因')

plt.tight_layout()
plt.show()