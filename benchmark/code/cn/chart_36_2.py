import matplotlib.pyplot as plt
import numpy as np

# 第一个饼图数据
labels_1 = ['4 - 5月产生成交', '其他']
sizes_1 = [86, 14]  # 数据大体一致，总和为100
colors_1 = ['#4fa3e1', '#c7b8e0']  # 颜色接近原图

# 第二个饼图数据
labels_2 = ['4 - 5月来访过', '其他']
sizes_2 = [94, 6]  # 数据大体一致，总和为100
colors_2 = ['#4fa3e1', '#f1c4e0']  # 颜色接近原图

# 创建画布
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 设置整体标题
fig.suptitle('618大促成交用户的4-5月行为分析', fontsize=16, fontweight='bold')

# 绘制第一个饼图
ax1.pie(sizes_1, labels=labels_1, autopct='%1.0f%%', startangle=90, colors=colors_1)

# 绘制第二个饼图
ax2.pie(sizes_2, labels=labels_2, autopct='%1.0f%%', startangle=90, colors=colors_2)

# 让饼图显示为正圆形
for ax in [ax1, ax2]:
    ax.axis('equal')

plt.tight_layout()
plt.subplots_adjust(top=0.85)  # 调整子图与顶部的距离
plt.show()