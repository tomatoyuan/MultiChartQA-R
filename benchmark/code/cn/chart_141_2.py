import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = ["图文", "短视频", "直播", "线下活动", "语音课程"]
percentages = [81.9, 75.5, 40.3, 40.4, 27.9]
colors = ["#FFA500"] * len(labels)  # 统一橙色

# 初始化图表
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(labels) * 2)
ax.set_axis_off()  # 隐藏坐标轴

for i, (label, perc, color) in enumerate(zip(labels, percentages, colors)):
    # 绘制橙色进度条
    ax.barh(i * 2 + 1, perc, height=1.5, left=15, color=color, alpha=0.8)
    # 绘制标签
    ax.text(10, i * 2 + 1.75, label, fontsize=12, va="center")
    # 绘制百分比数值
    ax.text(15 + perc + 2, i * 2 + 1.75, f"{perc}%", fontsize=12, va="center", ha="left")

ax.set_title("2023年中国备孕人群信息形式偏好", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()