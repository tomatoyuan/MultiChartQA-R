import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['学校实力', '专业爱好', '地理位置', '其它']
values = [24, 36, 13, 27]
colors = ['#FF7F0E', '#2CA02C', '#FFD700', '#1F77B4']  # 对应颜色

# 创建画布和轴
fig, ax = plt.subplots()

# 绘制横向条形图
ax.barh(labels, values, color=colors)

# 添加数据标签
for i, v in enumerate(values):
    ax.text(v + 1, i, str(v) + '%', va='center')

# 设置标题
ax.set_title('面对多个学校可以选择时，你更关注？')

# 显示图表
plt.show()