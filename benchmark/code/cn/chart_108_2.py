import matplotlib.pyplot as plt

# 数据
labels = ["每天都看", "每周看4-5次", "每周看1-3次", "不定时，碎片式阅读"]
sizes = [19.96, 51.54, 21.93, 6.57]
# 对应颜色
colors = ["#FF7F27", "#4B53FF", "#32CD32", "#9400D3"]

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国财经新闻用户阅读财经媒体资讯频率")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()