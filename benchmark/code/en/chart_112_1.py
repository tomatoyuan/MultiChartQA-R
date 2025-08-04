import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Very like", "Like", "Average", "Dislike", "Never concerned"]
sizes = [20.55, 55.78, 17.06, 6.61, 0.00]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots(figsize=(10, 8))  # 增大图表宽度，为水平文本预留空间

# 绘制环形图，关闭自动标签旋转
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct="%1.2f%%",
    startangle=90, 
    wedgeprops={"width": 0.4},
    pctdistance=0.85,  # 百分比标签距离圆心的距离
    labeldistance=1.15,  # 类别标签距离圆心的距离（增大以避免重叠）
    rotatelabels=False  # 强制标签不旋转
)

# 强制所有文本水平显示（旋转角度为0）
for text in texts + autotexts:
    text.set_rotation(0)  # 水平显示
    text.set_fontsize(11)

# 优化小占比部分的标签位置（避免重叠）
for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
    # 计算扇形中点角度（用于调整文本水平位置）
    angle = (wedge.theta1 + wedge.theta2) / 2
    angle_rad = np.deg2rad(angle)
    
    # 根据角度调整文本对齐方式（左/右对齐确保水平显示时不偏移）
    if angle < 90 or angle > 270:
        text.set_ha('left')  # 右侧扇形文本左对齐
    else:
        text.set_ha('right')  # 左侧扇形文本右对齐
    
    # 隐藏0%的标签（避免无意义显示）
    if sizes[i] == 0:
        autotext.set_visible(False)
        text.set_visible(False)  # 同时隐藏"Never concerned"标签

# 调整百分比标签样式（白色字体提高可读性）
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_ha('center')  # 百分比标签居中

# 设置标题
ax.set_title("Preference of Chinese consumers for figurines in 2025", fontsize=14, pad=20)

plt.tight_layout()
plt.show()