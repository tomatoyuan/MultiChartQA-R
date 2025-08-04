import matplotlib.pyplot as plt
import numpy as np

# 购买渠道
channels = [
    "社区团购或微信群接龙", "超市", "菜市场", "农户直销或田间地头直购", 
    "农贸批发市场", "直播带货或短视频平台购买", "专门门店（如生鲜超市、水果店、农产品专卖店等）", 
    "本地生活平台（如美团、饿了么、每日优鲜等）", "电商平台（如拼多多、天猫、京东、苏宁易购等）"
]
# 对应占比（%）
proportions = [21.97, 22.78, 23.42, 23.75, 26.33, 27.30, 35.70, 36.35, 41.03]

y = np.arange(len(channels))  # y轴坐标

fig, ax = plt.subplots(figsize=(12, 8))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注，在条形右侧
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国消费者购买农货产品的渠道')

plt.tight_layout()
plt.show()