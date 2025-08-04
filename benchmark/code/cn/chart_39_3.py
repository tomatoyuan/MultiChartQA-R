import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["经常去，海派文化很有特点", "去过，体验老上海咖啡文化", "没去过，但是比较感兴趣", "不想去，不太感兴趣"]
sizes = [31, 50, 16, 3]  # 数据大体一致即可
# 颜色，尽量接近原图，可根据实际微调
colors = ["#E67E22", "#F1C40F", "#BDC3C7", "#95A5A6"]  

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors)

# 设置标题
ax.set_title("消费者与海派咖啡馆体验意愿")

# 显示图表
plt.show()