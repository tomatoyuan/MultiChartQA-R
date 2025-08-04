import matplotlib.pyplot as plt
import numpy as np

# 了解手办资讯的渠道
channels = ["支付类平台", "亲朋好友介绍", "短视频平台（抖音、快手等）", 
            "内容分享平台（小红书、微博、豆瓣、知乎等）", "视频类分享平台（哔哩哔哩、腾讯视频等）"]
# 对应占比（%）
proportions = [24.31, 28.94, 41.20, 50.23, 52.55]

y = np.arange(len(channels))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国手办消费者了解手办资讯的渠道')

plt.tight_layout()
plt.show()