import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["感觉根本找不到对象", "不擅沟通很难恋爱", "会积极的相亲", "享受单身文化", "其他"]
sizes = [40, 20, 19, 7.8, 13.2]  # “其他”占比通过 100 - 40 - 20 - 19 - 7.8 计算得 13.2 
colors = ["#f78199", "#a06cd5", "#ffe66d", "#ff4b5c", "#c3eaf4"]

# 创建环形图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90, pctdistance=0.85)

# 添加圆心白色圆，形成环形（甜甜圈图）效果
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig.gca().add_artist(centre_circle)

# 设置标题
ax.set_title("在选择逃避脱单者中")

# 调整布局并显示图表
plt.tight_layout()
plt.show()