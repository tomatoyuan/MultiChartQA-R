import matplotlib.pyplot as plt
import numpy as np

# 数据准备（了解无糖饮料渠道）
understand_channels = [
    "电商平台（淘宝、拼多多等）", "短视频平台（抖音、快手等）", 
    "社交平台（微信、微博等）", "中长视频平台（B站、爱奇艺等）", 
    "线下宣传海报或广告", "亲朋好友推荐", 
    "社区团购平台", "商超地推"
]
understand_proportions = [52.1, 49.5, 44.5, 35.6, 33.9, 32.8, 27.2, 24.0]  # 占比（%）

# 数据准备（线上购买无糖饮料渠道占比）
purchase_channels = [
    "综合电商平台（淘宝、京东等）", "新型电商平台（抖音、快手）", 
    "线上商超平台（美团、饿了么等）", "社区团购平台", "其他"
]
purchase_proportions = [75.3, 55.8, 67.3, 42.6, 0.4]  # 占比（%）

# 创建画布（一行两列）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- 绘制左侧“了解渠道”柱状图 ---------------------
x_understand = np.arange(len(understand_channels))
ax1.bar(x_understand, understand_proportions, color='coral')
ax1.set_title('2023年中国消费者了解无糖饮料渠道', fontsize=14)
ax1.set_ylabel('占比（%）')
ax1.set_xlabel('了解渠道')
ax1.set_xticks(x_understand)
ax1.set_xticklabels(understand_channels, rotation=45, ha='right')
ax1.set_ylim(0, 60)  # 调整y轴范围适配最大占比（52.1%）

# 添加左侧数值标注
for i, prop in enumerate(understand_proportions):
    ax1.text(x_understand[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# --------------------- 绘制右侧“线上购买渠道”雷达图 ---------------------
# 雷达图角度数（渠道数量对应角度）
num_channels = len(purchase_channels)
angles = np.linspace(0, 2 * np.pi, num_channels, endpoint=False).tolist()
# 闭合雷达图（让最后一个点连回第一个点）
purchase_proportions += purchase_proportions[:1]
angles += angles[:1]

ax2 = plt.subplot(1, 2, 2, polar=True)
ax2.fill(angles, purchase_proportions, color='orange', alpha=0.3)
ax2.plot(angles, purchase_proportions, color='orange', label='占比')

# 设置雷达图的轴标签（渠道名称）
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(purchase_channels)
# 调整y轴刻度（适配占比范围）
ax2.set_yticks(np.arange(0, 80, 10))
ax2.set_yticklabels(np.arange(0, 80, 10))

# 添加右侧数值标注
for i, (angle, prop) in enumerate(zip(angles[:-1], purchase_proportions[:-1])):
    ax2.text(angle, prop + 2, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

ax2.set_title('2023年中国消费者线上不同渠道购买无糖饮料占比', fontsize=14, y=1.1)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()