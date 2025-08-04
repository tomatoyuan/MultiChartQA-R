import matplotlib.pyplot as plt

# 数据
labels = ["每月少于3次", "每周1-2次", "每周3-4次", "每周5次以上"]
sizes = [9.92, 49.60, 29.22, 11.26]
# 对应颜色
colors = ["#FF7F27", "#4B53FF", "#32CD32", "#9467BD"]

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国消费者饮用包装饮用水频率")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()