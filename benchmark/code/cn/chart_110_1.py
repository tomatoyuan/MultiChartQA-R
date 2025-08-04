import matplotlib.pyplot as plt

# 数据
labels = ["每天三次以上", "每天1-2次", "每周4-6次", "每周2-3次", "每周1次及以下"]
sizes = [8.91, 41.49, 39.23, 7.05, 3.32]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国有声书用户使用有声书APP平均频率")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()