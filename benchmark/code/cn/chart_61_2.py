import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
months = ["1月", "2月", "3月"]
years = ["2023年", "2024年", "2025年"]

# 数据：[2023, 2024, 2025]（分钟）
data = np.array([
    [286.5, 267.9, 265.5],  # 1月
    [288.3, 272.6, 267.9],  # 2月
    [300.6, 278.9, 268.0],  # 3月
])

# 色彩风格升级
colors = ["#7CB342", "#66BB6A", "#00ACC1"]  # 对应2023/2024/2025
markers = ["o", "s", "D"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(9, 5.5))

# -------------------- 绘制多条折线 --------------------
x = np.arange(len(months))
for i in range(len(years)):
    y = data[:, i]
    ax.plot(
        x, y, marker=markers[i], linewidth=2.5, 
        label=years[i], color=colors[i]
    )
    # 添加数据标注
    for j, val in enumerate(y):
        ax.text(
            x[j], val + 3,
            f"{val}", ha='center', fontsize=9,
            color=colors[i], fontweight='bold'
        )

# -------------------- 同比增长率标注（2024→2025） --------------------
for i in range(len(months)):
    rate = data[i][2] - data[i][1]
    rate_pct = round((rate / data[i][1]) * 100, 1)
    color = "red" if rate_pct < 0 else "green"
    ax.text(
        x[i] + 0.05, data[i][2] + 10,
        f"{rate_pct:+}%", color=color,
        fontsize=9, ha="left", va="center", fontweight="bold"
    )

# -------------------- 美化图表 --------------------
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylabel("单机单日有效时间（分钟）", fontsize=11)
ax.set_title("mUserTracker-2023-2025Q1 单机单日有效时间", fontsize=14, fontweight="bold", pad=15)

# 网格线
ax.grid(alpha=0.2)

# 图例
ax.legend(loc="upper right", fontsize=9, frameon=True)

# 去除多余边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()