import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2022.07", "2023.07", "2024.07"]
values = [86.7, 89.4, 92.0]

# 初始化画布
fig, ax = plt.subplots(figsize=(6, 1.5))  # 窄画布模拟时间轴布局

# 绘制水平直线（时间轴）
ax.axhline(y=0.5, color='#83B48A', linewidth=2, zorder=1)  

# 绘制带数值的绿色方框
for i, (year, val) in enumerate(zip(years, values)):
    # 绘制绿色矩形
    rect = plt.Rectangle((i - 0.2, 0.2), 0.4, 0.6, 
                         facecolor='#C9EBD9', edgecolor='#83B48A', 
                         linewidth=2, zorder=2)
    ax.add_patch(rect)
    # 标注数值
    ax.text(i, 0.5, f"{val}", fontsize=12, 
            ha='center', va='center', color='#333333')
    # 标注年份
    ax.text(i, -0.3, year, fontsize=10, 
            ha='center', va='top', color='#666666')

# 隐藏坐标轴
ax.set_xlim(-0.5, len(years)-0.5)
ax.set_ylim(-0.5, 1.2)
ax.axis('off')

# 添加标题
plt.title("消费者信心指数-消费意愿", fontsize=14, fontweight='bold', y=1.3)

plt.tight_layout()
plt.show()