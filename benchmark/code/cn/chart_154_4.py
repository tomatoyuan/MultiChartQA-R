import matplotlib.pyplot as plt

# 图表4：对外卖的菜品的要求分布
labels = [
    "食物新鲜，食材品质有保障",
    "营养均衡，搭配合理",
    "口感丰富，口味好",
    "种类全，选择多",
    "食物温度保持的好",
    "食品可定制化",
    "分量大，能吃饱"
]
values = [77.2, 68.2, 68.0, 48.6, 31.9, 31.8, 23.5]

colors = plt.cm.Greens_r([0.2 + i*0.1 for i in range(len(values))])

fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.barh(labels, values, color=colors)

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1.5, bar.get_y() + bar.get_height()/2,
            f'{width:.1f}%', va='center', fontsize=10)

# 图表设置
ax.set_xlim(0, 85)
ax.set_xlabel("占比（%）", fontsize=12)
ax.set_title("对外卖的菜品的要求分布", fontsize=14, weight='bold')
plt.gca().invert_yaxis()  # 反转 y 轴使最大值在上方

# 数据来源

plt.tight_layout()
plt.show()