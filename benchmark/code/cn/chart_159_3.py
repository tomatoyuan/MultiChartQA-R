import matplotlib.pyplot as plt
import numpy as np



# 渠道
channels = ['社交媒体', '有影响力的人', '消息应用程序', '直播视频', '视频/实时聊天', '语音助手', '聊天']
# 发现阶段数据
discover = [50, 22, 14, 11, 8, 0, 0]
# 购买阶段数据
purchase = [59, 0, 36, 21, 20, 24, 20]

# 横坐标位置
x = np.arange(len(channels))
bar_width = 0.35

# 绘图
fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(x - bar_width/2, discover, width=bar_width, label='发现', color='#009800')
bars2 = ax.bar(x + bar_width/2, purchase, width=bar_width, label='购买', color='#005B4C')

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{int(height)}%', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{int(height)}%', ha='center', va='bottom', fontsize=10)

# 其他设置
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=20)
ax.set_ylabel('比例 (%)')
ax.set_title('全球使用特定渠道进行产品发现与购买的购物者')
ax.legend()
plt.tight_layout()
plt.show()