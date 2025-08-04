import matplotlib.pyplot as plt

# 数据
labels = ["否，并没有", "是，在经营策略中已有考虑及实施数字化转型"]
sizes = [13.81, 86.19]
# 对应颜色
colors = ['#FF7F27', '#4B53FF']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国企业经营规划加入数字化转型情况")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()