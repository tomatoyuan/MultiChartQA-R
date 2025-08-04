import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
income_groups = [
    "4000元及以下", "4001-6000元", "6001-8000元",
    "8001-10000元", "10001-15000元", "15000元以上"
]
percentages = [4.6, 18.3, 26.5, 21.2, 18.9, 10.4]

# -------------------- 极坐标设置 --------------------
N = len(percentages)
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = percentages
width = 2 * np.pi / N * 0.9  # 每个扇形的角度宽度

# 渐变配色（红→橙→黄→绿→蓝→紫）
colors = ["#e57373", "#ffb74d", "#fff176", "#81c784", "#64b5f6", "#ba68c8"]

# -------------------- 创建极坐标画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
bars = ax.bar(theta, radii, width=width, color=colors, edgecolor="white", linewidth=1, align="edge")

# -------------------- 添加标签 --------------------
for i, (angle, radius) in enumerate(zip(theta, radii)):
    ax.text(
        angle + width / 2, radius + 2, 
        f"{income_groups[i]}\n{radius}%", 
        ha="center", va="center",
        fontsize=10, fontweight="bold", color="#424242", rotation_mode='anchor'
    )

# -------------------- 美化图表 --------------------
ax.set_theta_zero_location('N')   # 起点设置为正上方
ax.set_theta_direction(-1)        # 顺时针方向
ax.set_rticks([])                 # 不显示半径刻度
ax.set_yticklabels([])            # 不显示径向标签
ax.spines["polar"].set_visible(False)  # 去掉极坐标边框

# 添加标题
plt.title(
    "2025年中国电竞用户个人月收入水平",
    fontsize=14, fontweight="bold", pad=20
)

plt.tight_layout()
plt.show()