import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = ["非常满意", "比较满意", "一般", "不太满意"]
sizes = [27.2, 58.3, 14.0, 0.5]
# 对应颜色，可根据原图调整
colors = ["#4BA6FF", "#FF9933", "#FFCC33", "#FF6666"]

fig, ax = plt.subplots(figsize=(6, 6))
# 绘制饼图，设置起始角度、是否分离等
patches, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",
                                    startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字样式
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color("black")

ax.set_title("中国公众对自身健康的满意度调查", fontsize=14, y=1.05)
plt.show()