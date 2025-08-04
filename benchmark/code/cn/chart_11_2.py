import matplotlib.pyplot as plt

# 数据
labels = ["会", "不会"]
sizes = [39, 61]
# 饼图各部分颜色，可根据需求调整
colors = ["#87E8DE", "#FF6B6B"]  

# 创建饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
# 设置标题
ax.set_title("你会与父母共同查分吗？")
# 保证饼图为圆形
ax.axis("equal")  

# 展示图表
plt.show()