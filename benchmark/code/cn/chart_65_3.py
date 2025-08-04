import matplotlib.pyplot as plt

# 数据
labels = ["小于1000元", "1001-5000元", "5001-10000元", "1-3万元", "3万元以上", "没有收入"]
sizes = [33.3, 17.0, 9.4, 3.5, 3.5, 33.3]
# 颜色设置，尽量贴近原图颜色
colors = ["#A4C639", "#8DB328", "#7EA11E", "#668718", "#506D12", "#DCDCDC"]

fig, ax = plt.subplots()
# 绘制饼图，设置 autopct 显示百分比，pctdistance 调整百分比位置，textprops 调整文字样式
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", 
                                  startangle=90, pctdistance=0.8, textprops={"color": "black"})

# 调整标注文字大小
for autotext in autotexts:
    autotext.set_size(10)
for text in texts:
    text.set_size(10)

# 设置标题
ax.set_title("中国核心层创作者通过内容获得的收益分布")

# 让饼图保持圆形
ax.axis("equal")

plt.show()