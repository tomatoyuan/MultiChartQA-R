import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = ["2019", "2020", "2021"]
quantity = [12, 14, 17]
x = np.arange(len(years))

# 气泡大小和颜色
sizes = np.array(quantity) ** 2.5 * 5  # 调整指数扩大差异
colors = ["#90caf9", "#ce93d8", "#f48fb1"]  # 渐变蓝紫粉配色

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- 绘制气泡图 --------------------
for i in range(len(x)):
    ax.scatter(
        x[i], quantity[i],
        s=sizes[i],
        color=colors[i],
        alpha=0.7,
        edgecolors="white",
        linewidth=2
    )
    # 添加数据标注
    ax.text(
        x[i], quantity[i] + 0.5,
        f"{quantity[i]}",
        ha='center', va='bottom',
        fontsize=14,
        fontweight='bold',
        color='white'
    )

# -------------------- 设置坐标轴 --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
ax.set_yticks([])  # 不显示y轴刻度
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylim(0, max(quantity) + 5)

# -------------------- 标题与美化 --------------------
ax.set_title(
    "SVC-2019-2021年综艺及女性综艺数量趋势",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 美化边框
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()