import matplotlib.pyplot as plt

# 数据
labels = ["会特别考虑", "会考虑，但不是最主要的因素", "不会考虑"]
sizes = [47.01, 39.58, 13.41]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字位置和样式（可选）
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('2025年中国消费者考虑当地知名品牌农货产品情况')

plt.show()