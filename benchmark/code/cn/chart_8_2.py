import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['计算机端检索占比', '移动端检索占比']
sizes = [12.03, 87.97]
# 颜色，可根据需求调整
colors = ['#b3d1ff', '#ff9966']  

# 创建画布和子图
fig, ax = plt.subplots()
# 绘制甜甜圈图，wedgeprops 用于设置环形宽度
ax.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=colors,
       wedgeprops={'width': 0.3})  

# 设置标题（可选，根据需求添加）
ax.set_title('离婚诉讼行业检索占比分布')  

plt.show()