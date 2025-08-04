import matplotlib.pyplot as plt

# 数据
labels = ['无宣传酒店', '有提示牌', '有宣传海报']
sizes = [88, 7, 5]
colors = ['#058b83', '#dbe5c4', '#abd7a6']  # 自定义配色，与图中风格一致

# 生成饼状图
plt.figure(figsize=(5, 5))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# 设置标题
plt.title('酒店对新限塑令的各项宣传占比', fontsize=16)

# 显示图表
plt.tight_layout()
plt.show()