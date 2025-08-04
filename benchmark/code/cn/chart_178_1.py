import matplotlib.pyplot as plt

# 数据
categories = [
    "春节、中秋、端午",
    "生日、婚礼、纪念日",
    "情人节、七夕",
    "父亲节、母亲节",
    "圣诞节、元旦",
    "双11、618购物节"
]
values = [96, 92, 81, 76, 53, 48]

# 绘图
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(categories, values, color="#8B0000")
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("占比 (%)")
ax.set_title("中国礼品经济送礼节日分布", fontsize=14)

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center')

plt.tight_layout()
plt.show()