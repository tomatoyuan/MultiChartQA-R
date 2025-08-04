import matplotlib.pyplot as plt

# 饼图数据
labels = ['了解蓝帽子的含义 (50%)', '听说过但不了解具体含义 (48%)', '完全不了解 (4%)']
sizes = [50, 48, 4]
colors = ['#4A90E2', '#50E3C2', '#B8E986']  # 自定义颜色

# 创建饼图
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 10}
)

# 添加标题
plt.title('消费者对保健食品蓝帽子标志的认知分布', fontsize=14, fontweight='bold')

# 添加数据来源
plt.figtext(0.5, 0.01, '数据来源：CBNData2023年保健品全渠道人群调研数据',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()