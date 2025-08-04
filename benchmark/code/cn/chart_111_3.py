import matplotlib.pyplot as plt

# 数据
labels = ["看好，剧集质量尚可", "中立", "不看好，剧集质量堪忧"]
sizes = [49.63, 33.83, 16.54]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国电视剧观众对国产剧行业看法")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()