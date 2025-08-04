import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 年份数据
years = np.arange(2002, 2018)
# 对应年份的客运量数据（大体接近原数据）
passenger_volumes = [1.28, 1.35, 1.37, 1.37, 1.44, 1.56, 
                     1.96, 1.92, 2.1, 2.2, 2.2, 2.4, 
                     2.66, 2.95, 3.25, 3.56]

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图，设置颜色接近原图表的浅绿色系
bar_rects = ax.bar(years, passenger_volumes, color='#87E8DE')

# 设置 x 轴刻度
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10)

# 设置 y 轴标签
ax.set_ylabel('发送旅客量（亿人次）', fontsize=12)
# 设置标题
ax.set_title('历年全国铁路春运发送旅客量（单位:亿人次）', fontsize=14, pad=20)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 在柱子上标注数值
for rect in bar_rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, f'{height}',
            ha='center', va='bottom', fontsize=9)

# 增加一些装饰元素，使用纯图形替代图片
hot_air_balloon = patches.Circle((2003.5, 3.3), 0.15, color='#FF7E79')
ax.add_patch(hot_air_balloon)

# 绘制热气球的篮子和绳子
basket = patches.Rectangle((2003.35, 3.15), 0.3, 0.1, color='#A0522D')
ax.add_patch(basket)

# 绘制绳子
ax.plot([2003.35, 2003.425], [3.3, 3.15], color='#8B4513', linewidth=1)
ax.plot([2003.65, 2003.575], [3.3, 3.15], color='#8B4513', linewidth=1)

plt.tight_layout()
plt.show()