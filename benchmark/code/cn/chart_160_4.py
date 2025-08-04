import matplotlib.pyplot as plt

# 数据
labels = ['电商', '数码家电', '手机游戏', '汽车', '美妆']
sizes = [45, 13.75, 13.75, 13.75, 13.75]  # 总和为100
colors = ['#b3cfff', '#c2d6ff', '#d1ddff', '#e0e5ff', '#eff2ff']  # 更浅的蓝色渐变

# 绘图
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
    textprops={'color': 'black', 'fontsize': 10}
)

# 添加标题
plt.title('哔哩哔哩腰部达人近180日TOP5合作行业', fontsize=14)

# 添加说明文字
plt.text(0, -1.3, "哔哩哔哩腰部达人近180天平均合作行业数 2.77个", ha='center', fontsize=12, color='#4a64c0')

# 保持饼状图为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()