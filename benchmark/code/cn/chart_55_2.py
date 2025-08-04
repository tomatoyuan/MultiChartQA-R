import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2022, 2023, 2024, 2025, 2026, 2027]

# 各类市场占比（%）
mobile_eb = [51.9, 53.7, 54.5, 54.6, 54.3, 53.9]    # 移动电竞游戏占比
tournament_eb = [23.7, 23.6, 23.2, 22.7, 22.2, 21.6]  # 端游电竞游戏占比
ecosystem_eb = [24.4, 22.7, 22.3, 22.7, 23.5, 24.5]   # 电竞生态占比

# 颜色配置（贴近原图配色）
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- 绘制堆积柱状图 --------------------
# 移动电竞游戏占比（最下层）
ax.bar(
    years, 
    mobile_eb, 
    color=colors[0], 
    label="移动电竞游戏占比（%）",
    edgecolor="white",
    linewidth=1
)

# 端游电竞游戏占比（中层）
bottom_mobile = np.array(mobile_eb)
ax.bar(
    years, 
    tournament_eb, 
    bottom=bottom_mobile, 
    color=colors[1], 
    label="端游电竞游戏占比（%）",
    edgecolor="white",
    linewidth=1
)

# 电竞生态占比（最上层）
bottom_tournament = bottom_mobile + np.array(tournament_eb)
ax.bar(
    years, 
    ecosystem_eb, 
    bottom=bottom_tournament, 
    color=colors[2], 
    label="电竞生态占比（%）",
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加数据标注 --------------------
for i, (y, m, t, e) in enumerate(zip(years, mobile_eb, tournament_eb, ecosystem_eb)):
    # 移动电竞占比
    ax.text(y, m/2, f"{m}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # 端游电竞占比
    ax.text(y, m + t/2, f"{t}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # 电竞生态占比
    ax.text(y, m + t + e/2, f"{e}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- 美化图表 --------------------
# 设置y轴范围（占比总和为100%）
ax.set_ylim(0, 100)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加图例，并向上移动
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white",
    # 使用 bbox_to_anchor 精细调整位置，(x, y) 范围是 [0, 1]
    bbox_to_anchor=(0.1, 1.1)  # 向上移动，y > 1 表示在图的上方
)

# 添加标题
ax.set_title(
    "2022-2027年中国电竞市场细分规模占比",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# 调整布局（避免图例被截断）
plt.tight_layout()

# 如果图例位置超出图的范围，可通过 bbox_inches 调整保存时的范围（可选）
# plt.savefig("output.png", bbox_inches="tight")

plt.show()