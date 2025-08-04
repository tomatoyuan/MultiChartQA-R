import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = ["露天电影/音乐会", "交友沙龙", "外语角", "舞会"]
percentages = [76.4, 67.7, 40.3, 27.3]
# 用文字模拟图标（可自定义更贴近的符号）
icons = ["露天电影/音乐会", "交友沙龙", "外语角", "舞会"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(labels) * 2)
ax.set_axis_off()

for i, (label, perc, icon) in enumerate(zip(labels, percentages, icons)):
    # 绘制图标（文字形式）
    # ax.text(10, i * 2 + 1, icon, fontsize=20, va="center")
    # 绘制标签
    ax.text(20, i * 2 + 1, label, fontsize=12, va="center")
    # 绘制百分比
    ax.text(90, i * 2 + 1, f"{perc}%", fontsize=12, va="center", ha="right")
    # 绘制进度条
    ax.barh(i * 2 + 1, perc, left=20, height=1.5, color="#FF9933", alpha=0.8)

ax.set_title("2023年中国大学城主要消费群体对未来大学城商圈增值服务增设的期望", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()