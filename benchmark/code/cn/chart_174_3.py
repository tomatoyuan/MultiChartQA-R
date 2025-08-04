import matplotlib.pyplot as plt

# 数据
labels = ['接受政策强制要求', '接受环保价值的宣传理由', '其他']
sizes = [56.3, 37.4, 7.3]
colors = ['#058b83', '#abd7a6', '#efe9d2']  # 与图表色彩匹配

# 生成饼状图
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# 设置标题
plt.title('消费者认可的宣传方式', fontsize=16)

# 显示图表
plt.tight_layout()
plt.show()