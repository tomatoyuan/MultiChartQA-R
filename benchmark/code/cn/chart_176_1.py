import matplotlib.pyplot as plt

# 数据
labels = ['送爱人', '送小孩', '送朋友', '送长辈', '送自己']
sizes = [60, 14, 10, 8, 8]

# 饼图颜色可自定义，也可使用默认
colors = ['#FF5A7D', '#FF8DA1', '#FFA7B5', '#FFC3CB', '#FFE1E7']

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12}
)

# 保持圆形
ax.axis('equal')
plt.title('2023年情人节礼赠对象分布\n（礼赠对象成交UV在礼赠人群中占比）', fontsize=14)
plt.tight_layout()
plt.show()