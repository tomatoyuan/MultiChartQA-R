import matplotlib.pyplot as plt

# -------------------- 数据定义 --------------------
labels = ["乳清蛋白", "植物及混合蛋白"]
sizes = [70.4, 29.6]  # 占比数据

# -------------------- 配色：暖色调 --------------------
colors = ["#ffb74d", "#e57373"]  # 橙 + 红

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- 绘制环形图（Donut Chart） --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    textprops={"fontsize": 12, "color": "#424242"},
    wedgeprops={"linewidth": 2, "edgecolor": "white"}
)

# 添加中间圆形成“空心”效果
centre_circle = plt.Circle((0, 0), 0.4, fc="white")
fig.gca().add_artist(centre_circle)

# 美化百分比文字
for text in auto_texts:
    text.set_color("white")
    text.set_fontweight("bold")

# -------------------- 添加标题 --------------------
ax.set_title(
    "乳清蛋白在蛋白粉（整体）中的成交规模比重",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- 优化布局 --------------------
plt.tight_layout()
plt.show()