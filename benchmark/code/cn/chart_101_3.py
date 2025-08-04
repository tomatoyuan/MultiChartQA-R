import matplotlib.pyplot as plt
import numpy as np

# 数据准备
content_types = ["短视频", "直播", "图文", "音频", "其他"]
proportions = [75.7, 25.6, 22.0, 13.2, 7.6]  # 占比（%）
colors = ["#ff7f27"]  # 橙色，贴近原图配色

x = np.arange(len(content_types))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向柱状图
bars = ax.barh(x, proportions, color=colors * len(content_types))
ax.set_title('2022年知识付费用户消费内容类型分布', fontsize=14)
ax.set_xlabel('占比（%）')
ax.set_ylabel('内容类型')
ax.set_yticks(x)
ax.set_yticklabels(content_types)
ax.set_xlim(0, 80)  # 调整 x 轴范围，适配最大占比（75.7%）

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

plt.tight_layout()
plt.show()