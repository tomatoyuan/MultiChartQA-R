import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = ["2019", "2020", "2021"]
x = np.arange(len(years))
consumption_scale = [100, 200, 300]

# 将数据插值为平滑曲线（为面积图拟合做准备）
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = np.interp(x_smooth, x, consumption_scale)

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- 绘制面积图（Area Chart） --------------------
ax.plot(x, consumption_scale, marker='o', color="#4dd0e1", linewidth=3, label="消费规模")
ax.fill_between(x_smooth, np.interp(x_smooth, x, consumption_scale), color="#b2ebf2", alpha=0.6)

# -------------------- 添加数据标注 --------------------
for i, val in enumerate(consumption_scale):
    ax.text(
        x[i], val + 10,
        f"{val}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight="bold",
        color="#00796b"
    )

# -------------------- 坐标轴设置 --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")

ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# -------------------- 添加标题与图例 --------------------
ax.set_title(
    "2019-2021年天猫国际“功能性零食”消费规模趋势",
    fontsize=14,
    fontweight="bold",
    pad=20
)

ax.legend(loc="upper left", fontsize=10, frameon=True, facecolor="white", edgecolor="white")

# -------------------- 布局与显示 --------------------
plt.tight_layout()
plt.show()