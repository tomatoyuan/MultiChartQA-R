import matplotlib.pyplot as plt
import numpy as np

# 数据准备
online_channels = ["电商平台", "直播购物", "短视频购物", "微信购物", "其他"]
online_percentages = [69.4, 15.2, 10.3, 4.7, 0.4]

offline_channels = ["商场超市", "便利店", "步行街", "地摊", "其他"]
offline_percentages = [65.8, 55.0, 49.8, 26.2, 0.0]

# 设置画布和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制线上购物渠道柱状图
x1 = np.arange(len(online_channels))
bars1 = ax1.bar(x1, online_percentages, color='orange')
ax1.set_title('线上购物渠道')
ax1.set_ylabel('占比（%）')
ax1.set_xticks(x1)
ax1.set_xticklabels(online_channels, rotation=45, ha='right')

# 添加线上购物渠道数值标注
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom')

# 绘制线下购物渠道柱状图
x2 = np.arange(len(offline_channels))
bars2 = ax2.bar(x2, offline_percentages, color='gold')
ax2.set_title('线下购物渠道')
ax2.set_ylabel('占比（%）')
ax2.set_xticks(x2)
ax2.set_xticklabels(offline_channels, rotation=45, ha='right')

# 添加线下购物渠道数值标注
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom')

plt.suptitle('2023年中国居民线上及线下夜间购物细分渠道分布', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()