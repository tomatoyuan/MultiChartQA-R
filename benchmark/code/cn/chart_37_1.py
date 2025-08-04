import matplotlib.pyplot as plt
import numpy as np

# 渠道名称
channels = ["直播间", "短视频", "图文"]
# 对应渠道占比数据
percentages = [89, 34, 16]

x = np.arange(len(channels))  # x轴位置
width = 0.5  # 条形宽度

fig, ax = plt.subplots()
# 绘制条形图，颜色设置为接近原图的棕色系
bars = ax.bar(x, percentages, width, color='#C09A7B')  

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(channels)
# 设置y轴范围
ax.set_ylim(0, 100)  

# 在每个条形上显示百分比数值
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}%'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 数值距离条形的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

# 设置图表标题
ax.set_title('消费者在抖音电商购买秋冬服饰的主要渠道')

plt.show()