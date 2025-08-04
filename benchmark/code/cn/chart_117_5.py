import matplotlib.pyplot as plt

# 数据
labels = ["智能家居", "高品质材料", "绿色环保", "个性化定制"]
sizes = [29.09, 22.85, 25.35, 22.71]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字位置和样式（可选），让标注更清晰
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('2025年中国消费者对未来家居行业发展趋势的看法')

plt.show()