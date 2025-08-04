import matplotlib.pyplot as plt
import numpy as np

# 数据准备（线上、线下文娱活动及占比）
online_data = {
    "看电视剧电影": 73.2, "刷短视频": 59.0, "听音乐": 46.0, 
    "刷直播": 42.3, "看新闻资讯": 39.3, "逛内容社区": 32.5, 
    "看小说/漫画等电子书": 31.8, "打游戏": 31.5, "刷微博": 19.72, "其他": 0.14
}
offline_data = {
    "电影院看电影": 51.91, "运动健身": 45.53, "聚会": 40.99, 
    "KTV": 31.63, "逛书店": 30.07, "酒吧": 29.50, "跳广场舞": 26.38, 
    "夜摊活动": 25.96, "音乐节": 15.32, "密室逃脱": 14.61, "剧本杀": 11.63, 
    "夜间博物馆": 11.06, "付费自习室": 5.96, "其他": 0.57
}
# 环形占比
online_ring = 24.4
offline_ring = 34.9

# 创建画布，一行两列布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

# --------------------- 绘制左侧线上文娱横向柱状图 ---------------------
x_online = list(online_data.values())
y_online = list(online_data.keys())
ax1.barh(y_online, x_online, color='orange')
ax1.set_title('2023中国居民夜间线上文娱活动偏好', fontsize=12)
# 添加数值标注
for i, val in enumerate(x_online):
    ax1.text(val + 1, i, f'{val}%', ha='left', va='center', color='orange')
# 绘制环形占比
ax1_ring = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax1.add_artist(ax1_ring)
ax1.text(-0.3, -0.3, f'{online_ring}%', ha='center', va='center', fontsize=14, color='orange')
ax1.text(-0.3, -0.5, '线上文娱活动', ha='center', va='center', fontsize=12)

# --------------------- 绘制右侧线下文娱横向柱状图 ---------------------
x_offline = list(offline_data.values())
y_offline = list(offline_data.keys())
ax2.barh(y_offline, x_offline, color='gold')
ax2.set_title('2023中国居民夜间线下文娱活动偏好', fontsize=12)
# 添加数值标注
for i, val in enumerate(x_offline):
    ax2.text(val + 1, i, f'{val}%', ha='left', va='center', color='gold')
# 绘制环形占比
ax2_ring = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax2.add_artist(ax2_ring)
ax2.text(-0.3, -0.3, f'{offline_ring}%', ha='center', va='center', fontsize=14, color='gold')
ax2.text(-0.3, -0.5, '线下文娱活动', ha='center', va='center', fontsize=12)

# 调整布局
plt.suptitle('2023中国居民夜间线上线下文娱活动偏好', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()