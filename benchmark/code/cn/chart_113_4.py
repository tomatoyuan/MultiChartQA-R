import matplotlib.pyplot as plt
import numpy as np

# 资讯获取渠道
channels = ["内容社区类平台（小红书等）", "电商平台（淘宝、京东等）", "社交媒体类平台（微信等）", 
            "母婴垂直类平台（妈妈网等）", "短视频平台（抖音等）", "视频分享类平台（B站等）"]
# 各选择原因（图例顺序）
reasons = ["专业性较高（专家/问答）", "母婴资讯真实可靠", "用户活跃互动频繁", 
           "周围人推荐从众", "个人习惯", "偏好 方便快捷"]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']
# 各渠道下各原因的占比数据（按channels、reasons顺序）
data = np.array([
    [7.74, 14.26, 15.48, 12.83, 8.15, 4.07],
    [5.91, 17.52, 11.41, 13.65, 7.74, 4.68],
    [8.35, 12.83, 13.65, 9.98, 7.94, 2.24],
    [11.20, 14.87, 14.26, 10.59, 9.16, 3.46],
    [5.30, 11.00, 13.65, 9.57, 9.98, 4.48],
    [6.52, 13.24, 12.63, 12.42, 8.96, 3.87]
])

x = np.arange(len(channels))  # x轴对应不同渠道
bar_width = 0.8  # 柱子宽度

fig, ax = plt.subplots(figsize=(14, 8))
bottom = np.zeros(len(channels))

for i, reason in enumerate(reasons):
    # 遍历每个原因，绘制堆积柱形
    ax.bar(channels, data[:, i], width=bar_width, bottom=bottom, color=colors[i], label=reason)
    # 添加数值标注
    for j in range(len(channels)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国母婴消费者选择资讯获取渠道的原因')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # 图例放右侧
plt.xticks(x, channels, rotation=45, ha='right')
plt.tight_layout()
plt.show()