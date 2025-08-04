import matplotlib.pyplot as plt

# 数据
labels = [
    "功能+时尚+舒适同样重要\n多合一需求被提出",
    "功能性为主，时尚与舒适为辅",
    "只要求功能和运动机能",
    "只关注品类和品牌等产品信息",
    "只关注时尚"
]
sizes = [48, 26, 15, 5, 5]
colors = ['#FFB84C', '#FBC374', '#FFDCA8', '#FFE9C1', '#FFF3DC']

# 绘制饼图
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    startangle=140,
    autopct='%1.0f%%',
    textprops={'fontsize': 10}
)

# 标题与数据来源说明
plt.title('消费者对奢华户外服饰提出诉求分布（%）', fontsize=14)
plt.figtext(0.5, 0.02, "数据来源：CBNData 2024年5月调研；N=1000", ha="center", fontsize=10)

plt.tight_layout()
plt.show()