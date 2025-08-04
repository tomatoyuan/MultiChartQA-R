import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 成长力量来源
sources = [
    "自己的内心", "父母的支持", "朋友的陪伴", 
    "老师的教导", "励志的榜样", "喜欢的作品", "国家稳健发展"
]
# 模拟占比数据（尽量贴近原图）
percentages = [32, 32, 27, 23, 21, 16, 16]
# 颜色配置（尽量贴近原图的渐变绿色、蓝色、黄色 ）
colors = ["#A8D089", "#8CC17F", "#68B26F", "#6CBAE5", "#59A5D8", "#F7D842", "#F2B73F"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制带条纹背景的柱状图
x = np.arange(len(sources))
bar_width = 0.6
# 先绘制条纹背景（用灰色斜线填充 ）
for i in range(len(sources)):
    ax.bar(x[i], 100, width=bar_width, color='white', edgecolor='lightgray', hatch='////', zorder=0)

# 再绘制前景彩色柱子
bars = ax.bar(x, percentages, width=bar_width, color=colors, zorder=1)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar_width/2, height),
                xytext=(0, 3),  # 标注位置：上方偏移 3
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置y轴刻度（0-40%）
ax.set_ylim(0, 40)
# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(sources, rotation=40, ha='right')  # 旋转标签避免重叠
# 设置标题
ax.set_title("大学生成长力量的来源", fontsize=14, fontweight="bold")

# 隐藏y轴（原图无y轴刻度 ）
ax.yaxis.set_visible(False)

# 隐藏顶部、右侧、左侧边框
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()