import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['因慢性病死亡', '其他原因死亡']
sizes = [88.5, 100 - 88.5]  # 占比，和为100
colors = ['#008040', '#D3D3D3']  # 接近原图表的绿色和灰色

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制环形图（甜甜圈图），wedgeprops 用于设置环形宽度
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       colors=colors, wedgeprops={'width': 0.3})

# 设置标题
ax.set_title('中国2019年因慢性病导致的死亡人数占总死亡人数比例', y=-0.15, fontsize=12, fontweight='bold')

# 让饼图保持圆形
ax.axis('equal')

# 显示图表
plt.show()