import matplotlib.pyplot as plt
import numpy as np

# 投诉渠道数据
channel_names = ["网址", "电话", "邮箱等"]
channel_percents = [68, 22, 10]

# 创建画布和子图
plt.figure(figsize=(8, 6))
ax = plt.subplot(111)

# 绘制投诉渠道占比条形图
bars = ax.bar(
    channel_names, 
    channel_percents, 
    color=["#FF7F50", "#FF6347", "#FFD700"],  # 保持原有颜色方案
    width=0.6  # 调整条形宽度
)

# 设置图表标题和坐标轴标签
ax.set_title("侵权投诉渠道占比分布", fontsize=16, fontweight="bold", pad=15)
ax.set_ylabel("占比（%）", fontsize=12)
ax.set_ylim(0, 100)  # 设置 y 轴范围为 0-100%

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height + 1.5,  # 调整标签位置
        f"{height}%",
        ha="center", 
        va="bottom",
        fontsize=12
    )

# 设置网格线和背景
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_axisbelow(True)  # 网格线置于底层

# 优化布局
plt.tight_layout()
plt.show()