import matplotlib.pyplot as plt

# 数据
labels = ['19岁-34岁', '≤18岁', '其他']
sizes = [83, 13, 4]  # 假设“其他”占比4%，可根据实际准确数据调整
colors = ['pink', 'blue', 'lightcoral']

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # 保证饼图是正圆形

# 添加标题
plt.title('不同年龄段搜索“教师资格证”占比情况')

# 显示图表
plt.show()