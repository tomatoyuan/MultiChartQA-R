import matplotlib.pyplot as plt

# 数据
labels = ["两年", "三年", "四年及以上", "一年之内"]
sizes = [49.0, 33.7, 9.3, 8.0]
colors = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

fig, ax = plt.subplots(figsize=(6, 6))
# 绘制饼图，autopct 显示百分比，startangle 设置起始角度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)

# 调整标注文字颜色为白色，更清晰
for autotext in autotexts:
    autotext.set_color("white")

ax.set_title("中国消费者换手机的频率")
plt.show()