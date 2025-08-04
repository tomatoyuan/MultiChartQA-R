import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2022', '2030E']
values = [8.2, 17.4]

# 用于在柱状图上方合适位置显示复合增长率，这里简单设置在两柱子中间上方
x_pos = 0.5  
y_pos = max(values) + 1  

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制柱状图
ax.bar(years, values, color='skyblue')

# 添加数据标签
for x, y in zip(years, values):
    ax.text(x, y + 0.2, f'{y}', ha='center', va='bottom')

# 设置标题
ax.set_title('2022 - 2030年中国工学椅市场规模及展望（亿美元）')

# 显示图形
plt.show()