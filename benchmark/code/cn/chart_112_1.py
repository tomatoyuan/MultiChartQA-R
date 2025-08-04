import matplotlib.pyplot as plt
import numpy as np

# 数据（中文标签）
labels = ["很喜欢", "喜欢", "一般", "不喜欢", "从未关注过"]
sizes = [20.55, 55.78, 17.06, 6.61, 0.00]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots(figsize=(9, 9))  # 调整图表尺寸，适配中文显示

# 绘制环形图，优化文本位置参数
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct="%1.2f%%",
    startangle=90, 
    wedgeprops={"width": 0.4},
    pctdistance=0.85,  # 百分比标签距离圆心的距离
    labeldistance=1.15  # 中文标签距离圆心的距离（增大避免重叠）
)

# 优化中文文本显示样式
for text in texts:
    text.set_fontsize(12)  # 调整中文标签字体大小
    text.set_rotation(0)   # 中文水平显示

for autotext in autotexts:
    autotext.set_fontsize(11)  # 百分比字体大小
    autotext.set_color('white')  # 百分比白色显示，增强对比
    autotext.set_rotation(0)     # 百分比水平显示

# 处理小占比和0值标签（避免重叠和无意义显示）
for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
    if sizes[i] < 10:  # 针对"不喜欢"等小占比标签
        angle = (wedge.theta1 + wedge.theta2) / 2
        if angle > 90 and angle < 270:
            text.set_ha('right')  # 左侧文本右对齐
        else:
            text.set_ha('left')   # 右侧文本左对齐
    if sizes[i] == 0:  # 隐藏"从未关注过"的标签和数值
        text.set_visible(False)
        autotext.set_visible(False)

# 设置中文标题
ax.set_title("2025年中国消费者对手办的喜好程度", fontsize=14, pad=20)

plt.tight_layout()
plt.show()