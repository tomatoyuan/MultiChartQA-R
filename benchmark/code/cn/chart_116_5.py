import matplotlib.pyplot as plt

# 数据
labels = ["非常看好", "比较看好", "一般", "比较不看好", "非常不看好"]
sizes = [20.84, 47.66, 21.22, 5.82, 4.46]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字位置和样式（可选），让标注更清晰
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('2025年中国消费者对农货零售未来的发展前景的看法')

plt.show()