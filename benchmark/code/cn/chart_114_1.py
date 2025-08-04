import matplotlib.pyplot as plt

# 数据
labels = ["半年一次", "一年一次", "两年一次", "没病不检查", "没有进行过体检", "其他"]
sizes = [3.94, 35.48, 39.41, 11.49, 9.52, 0.16]
# 对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots()
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 设置标题
ax.set_title("2025年中国消费者体检情况")

# 调整标注文字大小和颜色等（可选）
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()