import matplotlib.pyplot as plt

# 数据
labels = ['医疗健康', '信息技术', '先进制造', '汽车交通', '新消费', '文化娱乐', '金融科技']
sizes = [29.5, 25.1, 13.9, 11.7, 10.0, 9.6, 0.2]

# 绘图
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10}
)
ax.axis('equal')

# 添加标题与数据来源
plt.title('整体出海企业行业分布情况', fontsize=15, loc='center')
plt.figtext(0.01, 0, '数据来源：百炼智能，36氪研究院整理',
            fontsize=10, ha='left')
plt.tight_layout()
plt.show()