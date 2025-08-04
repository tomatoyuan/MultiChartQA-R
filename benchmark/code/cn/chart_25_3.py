import matplotlib.pyplot as plt
import numpy as np

# 学历类别
labels = ['研究生及以上', '大学', '高中', '初中', '初中以下']
# 假设的各学历关注人群占比（需按实际数据替换，这里仅示例）
sizes = [10, 30, 25, 20, 15]  

# 创建画布和子图
fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       wedgeprops={'width': 0.3})  
ax.axis('equal')  # 保证饼图（环形）绘制为圆形

plt.title('关注人群学历分布')
plt.show()