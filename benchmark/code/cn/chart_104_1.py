# 数据
labels = ["受益匪浅", "有所收获", "没有多大感触"]
sizes = [35.76, 53.31, 10.93]
# 对应颜色
colors = ["#FF7F27", "#4B53FF", "#32CD32"]

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国用户对音乐学习培养审美与思维的认知")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()