import matplotlib.pyplot as plt
import numpy as np

# 类别文本
labels = ["需要日常定期补充", "阶段性补充即可，如幼年、老年或孕期", "生病或有症状时补充即可"]
# 对应数据
sizes = [51, 17, 16]
# 不同类别的颜色，尽量贴近原图绿色系渐变
colors = ["#A4C639", "#A4C639", "#6E8B3D"]

x = np.arange(len(labels))  # 用于设置x轴位置
bar_width = 0.5  # 条形图宽度

fig, ax = plt.subplots()
# 绘制条形图，这里用水平条形图更贴近原图展示形式，所以用 barh
bars = ax.barh(x, sizes, height=bar_width, color=colors, edgecolor="white")  

# 添加数据标签
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标签距离条形图的水平距离
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签，让标签显示更清晰
ax.set_yticks(x)
ax.set_yticklabels(labels)
# 设置图表标题
ax.set_title("宠物保健品认知（TOP3）", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# 调整x轴范围，让标签显示更合适
ax.set_xlim(0, max(sizes) + 5)
# 隐藏x轴刻度
ax.set_xticks([])

plt.show()