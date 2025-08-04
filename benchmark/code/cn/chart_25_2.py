import matplotlib.pyplot as plt

# 数据
labels = ['25-34岁', '19岁以下', '19-24岁', '35岁以上']
sizes = [37, 28, 18, 17]

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # 保证饼图是正圆形

# 添加标题
ax.set_title('“春节仪式感” 关注人群年龄比')

# 显示图表
plt.show()