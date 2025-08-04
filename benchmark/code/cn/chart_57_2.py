import matplotlib.pyplot as plt
import numpy as np

# 渠道名称
channels = [
    "SEO", "SEM", "电子邮件营销", "社交媒体广告",
    "红人营销", "付费广告", "联盟营销"
]

# 将见效速度转换为数值等级（1=慢，3=快）
speed_levels = [1, 3, 2, 3, 2, 3, 2]

# 将成本转换为数值等级（1=低，3=高）
cost_levels = [1, 3, 1, 2.5, 2, 3, 2.5]

x = np.arange(len(channels))
width = 0.35  # 柱宽

fig, ax = plt.subplots(figsize=(12, 6))

bars1 = ax.bar(x - width/2, speed_levels, width, label='见效速度', color='#4CAF50')
bars2 = ax.bar(x + width/2, cost_levels, width, label='成本', color='#FF9800')

# 添加文本标签
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f"{bar.get_height()}", ha='center', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f"{bar.get_height()}", ha='center', fontsize=9)

# 轴设置
ax.set_ylabel('等级（1=低或慢，3=高或快）', fontsize=12)
ax.set_title('各营销渠道的见效速度与成本对比', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=30, ha='right')
ax.legend()

plt.tight_layout()
plt.show()