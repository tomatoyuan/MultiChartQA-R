import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 球星名称
players = ["梅西", "内马尔", "萨拉赫", "C罗", "拉莫斯", "伊涅斯塔", "凯恩", "博格巴", "格列兹曼", "切里舍夫"]
# 热度数据
heats = [80, 33, 27, 20, 15, 12, 13.1, 13.1, 13, 6.4]
# 为了让 x 轴刻度对应球星，生成索引
x = np.arange(len(players))  

# 创建图形
fig, ax = plt.subplots()
# 绘制柱状图，设置柱子颜色为紫色到粉色渐变
bars = ax.bar(x, heats, color=plt.cm.get_cmap('Purples')(np.linspace(0.2, 0.8, len(players))))

# 设置 x 轴刻度显示球星名称
ax.set_xticks(x)
ax.set_xticklabels(players, rotation=45)  # 移除了fontproperties参数

# 设置 y 轴标签
ax.set_ylabel("热度（万）")
# 设置标题
ax.set_title("球星热度排行榜TOP10")

# 在柱子上标注数值
for bar, heat in zip(bars, heats):
    height = bar.get_height()
    ax.annotate(f'{heat}万',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 数值相对柱子的垂直偏移
                textcoords="offset points",
                ha='center', va='bottom')

# 调整布局，避免标签显示不全
plt.tight_layout()
# 显示图表
plt.show()