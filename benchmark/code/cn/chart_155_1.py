import matplotlib.pyplot as plt

# 数据
labels = ['医疗服务市场', '药品市场', '非药品产品市场', '消费医疗服务市场', '医疗基础设施']
sizes = [53.9, 19.6, 13.7, 9.8, 2.9]
colors = ['#a6d854', '#d9ef8b', '#ffffbf', '#fee08b', '#f46d43']

fig, ax = plt.subplots(figsize=(8, 6))

# 饼图绘制
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%.2f%%',
    startangle=90,
    textprops={'fontsize': 10},
    wedgeprops={'edgecolor': 'white'}
)

# 标题
ax.set_title('2022年中国大健康行业细分市场份额分布', fontsize=14, weight='bold')

# 设置等高宽为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()