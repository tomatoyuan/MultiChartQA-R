import matplotlib.pyplot as plt
import numpy as np

# 城市名称
cities = ['北京', '深圳', '成都', '上海', '杭州']
# 各城市对应的搜索占比（基于图表估算，你可替换为精确数据）
percentages = [5.5, 3.5, 2.9, 2.8, 2.7]  

x = np.arange(len(cities))  # x轴坐标

fig, ax = plt.subplots()
# 绘制柱状图，设置柱子颜色为蓝色
rects = ax.bar(x, percentages, color='blue')  

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(cities)
# 设置y轴范围
ax.set_ylim([0, 6])  
# 设置y轴刻度
ax.set_yticks(np.arange(0, 7, 1))  
# 添加图表标题
ax.set_title('5月法律服务行业搜索城市TOP5')  
# 添加y轴标签
ax.set_ylabel('搜索占比（%）')  

# 在柱子上标注数值（可选，让图表信息更直观）
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 数值标注距离柱子的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()