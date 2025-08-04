import matplotlib.pyplot as plt

# 数据
labels = [
    "护肤科技的加持\n可以更好发挥成分功效",
    "并不关心产品蕴含的科技\n还是以关心成分为主",
    "没有关注过“科技护肤”的概念"
]
sizes = [83, 12, 5]
colors = ['#FFB6C1', '#FFCCE5', '#FFE6F0']  # 粉色系渐变
explode = (0.05, 0, 0)  # 突出第一块

# 绘图
fig, ax = plt.subplots(figsize=(7, 5))
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)

ax.axis('equal')  # 保证饼图为圆形
plt.title("当代女性消费者对“科技护肤”理念的看法调研", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()