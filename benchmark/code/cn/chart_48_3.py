import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ['非常宽裕', '比较宽裕', '基本够用', '比较困难', '非常困难']
# 农村数据
rural = [2.3, 14.9, 61.3, 17.9, 3.6]
# 城镇数据
urban = [4.5, 22.0, 61.2, 10.5, 1.8]
# 合计数据
total = [3.5, 18.7, 61.2, 13.9, 2.7]

x = np.arange(len(categories))  # x 轴位置
width = 0.25  # 每个条形的宽度

fig, ax = plt.subplots()
# 绘制农村、城镇、合计的条形
rects1 = ax.barh(x - width, rural, width, label='农村', color='green')
rects2 = ax.barh(x, urban, width, label='城镇', color='darkgreen')
rects3 = ax.barh(x + width, total, width, label='合计', color='gray')

# 添加标签、标题等
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.set_xlabel('百分比%')
ax.set_title('2021年中国城乡老年人自评经济状况')
ax.legend()

# 在条形上显示数值
def label_bars(rects):
    for rect in rects:
        length = rect.get_width()
        ax.text(length + 0.5, rect.get_y() + rect.get_height() / 2, f'{length}%', va='center')

label_bars(rects1)
label_bars(rects2)
label_bars(rects3)

plt.show()