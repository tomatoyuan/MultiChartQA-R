import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

# 数据
labels = ['18岁以下', '18 - 24岁', '25 - 29岁', '30岁以上']
sizes = [35, 48, 13, 4]
# 颜色设置，尽量接近原图表
colors = ['#4CAF50', '#FF9800', '#9E9E9E', '#795548']  

# 创建饼图
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                  startangle=90, colors=colors)

# 设置字体大小等样式，让显示更接近原图表
for text in texts + autotexts:
    text.set_fontsize(12)

# 以下为添加中间图片的大致流程，需将 'your_image_path.png' 替换为实际图片路径
# 假设图片是正方形且已处理好，这里只是示例，实际可能需要调整尺寸、位置等
# image = plt.imread('your_image_path.png')
# image_box = OffsetImage(image, zoom=0.3)  # zoom 调整图片大小
# ab = AnnotationBbox(image_box, (0, 0), frameon=False)
# ax.add_artist(ab)

# 设置图表标题
ax.set_title('第一次配戴隐形眼镜的年龄与类型', fontsize=14, y=1.05)

# 让饼图保持圆形
ax.axis('equal')

plt.show()