import matplotlib.pyplot as plt
import numpy as np

# 数据
data = [1, 1, 1, 1, 0.4]  # 模拟各区间占比，总和对应平均 2.4 场景，可根据实际微调
labels = ["1个", "2个", "3个", "4个", "5个"]
colors = ["#4CAF50", "#FFC107", "#F44336", "#9C27B0", "#607D8B"]  # 模拟接近的颜色

# 绘制环形图（甜甜圈图）
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,
    pctdistance=0.85,  # 百分比标签距离圆心的距离
    wedgeprops={"width": 0.3, "edgecolor": "white"}  # 设置环形宽度和边缘颜色
)

# 添加中心文本，显示平均场景数
ax.text(
    0,
    0,
    "平均\n2.4个场景",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold"
)

# 右侧添加带颜色的图例说明
text_descriptions = [
    "日常通勤",
    "时尚穿搭",
    "高能健身",
    "山野户外",
    "居家放松"
]

# 计算文本显示的纵坐标，让文本均匀分布
y_positions = np.linspace(0.8, -0.8, len(text_descriptions))
for i, (desc, color) in enumerate(zip(text_descriptions, colors)):
    # 添加颜色标记
    ax.scatter(
        1.2,  # x位置（略左移，为标记腾出空间）
        y_positions[i],
        s=50,  # 标记大小
        color=color,  # 使用对应的颜色
        zorder=3  # 确保标记显示在最上层
    )
    # 添加文本说明
    ax.text(
        1.35,  # 文本起始位置（右移以避免重叠）
        y_positions[i],
        desc,
        fontsize=12,
        ha="left",
        va="center"
    )

# 添加标题
plt.title("用户场景使用分布", fontsize=16, fontweight="bold", pad=20)

# 调整布局，避免元素重叠（略微扩大右侧空间）
plt.subplots_adjust(right=0.75, top=0.85)

# 显示图表
plt.show()