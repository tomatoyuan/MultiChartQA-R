import matplotlib.pyplot as plt

# 数据定义
labels = [
    "几乎全天佩戴",
    "需要看远处时才佩戴",
    "长时间用眼时才佩戴",
    "没有固定规律，感觉需要就戴上"
]
sizes = [54.1, 15.5, 11.6, 18.9]
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082"]

# 创建更宽的画布
fig, ax = plt.subplots(figsize=(12, 6))  # 横向扩展

# 调整饼图位置：左移中心点
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    textprops={
        "fontsize": 10,
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    },
    center=(-0.8, 0)  # 控制饼图中心向左移动
)

# 设置标题
ax.set_title(
    "近视人群佩戴框架眼镜的习惯",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()
plt.show()