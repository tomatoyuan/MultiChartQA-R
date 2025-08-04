import matplotlib.pyplot as plt

# 设置数据
labels = ['消费升级，更舍得为新春送礼砸大价钱', '消费平级，不会超出自己平时消费水平', '消费降级，送礼是非必要支出，能省则省']
sizes = [42, 49, 8]
colors = ['#a32020', '#f25e41', '#ffa768']

# 绘制环状图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors,
    wedgeprops={'width': 0.4}, textprops={'fontsize': 10}
)

# 添加中心文字
plt.text(0, 0, "新年送礼\n消费态度", ha='center', va='center', fontsize=14, fontweight='bold')

# 添加数据来源和说明
plt.figtext(0.5, 0.01,
            "数据来源：2024年1月CBNData问卷调研  \n数据说明：相较于自己平时消费，"
            "您在购置新春礼品这件事上，消费变化更符合以下哪个选项？N=1500",
            wrap=True, horizontalalignment='center', fontsize=9)

# 设置标题
plt.title("相比于日常，大众对于新年送礼的消费态度分布", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()