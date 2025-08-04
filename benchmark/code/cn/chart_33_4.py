import matplotlib.pyplot as plt
import numpy as np

# 平台名称
platforms = ['天猫', '抖音', '京东']
# 市场份额数据（大体一致即可）
market_share = [30, 25, 15]

x = np.arange(len(platforms))  # x轴坐标
width = 0.5  # 柱子宽度

fig, ax = plt.subplots()
# 绘制柱状图，颜色设置为接近的蓝色，edgecolor设置为黑色描边
rects = ax.bar(x, market_share, width, color='#4CAF50', edgecolor='black')  

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(platforms)
# 设置y轴标签
ax.set_ylabel('市场份额')
# 设置图表标题
ax.set_title('MAT25各电商平台市场份额')

# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects)

plt.show()