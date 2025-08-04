import matplotlib.pyplot as plt
import numpy as np

# 信息渠道
channels = ["新媒体内容平台（如微信、公众号等）", "综合电商平台（如淘宝、京东等）", "内容分享类平台（小红书、微博等）", 
            "视频分享类平台（B站等）", "短视频直播平台", "线下品牌店", "品牌官网", "户外广告（墙面、建筑物广告等）", 
            "亲友介绍", "地铁或电梯广告"]
# 对应占比（%）
proportions = [36.43, 34.27, 32.36, 30.70, 27.90, 26.75, 25.86, 24.20, 21.40, 20.25]

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
ax.set_title('2025年中国消费者了解智能产品的信息渠道')

plt.tight_layout()
plt.show()