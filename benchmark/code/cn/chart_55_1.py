import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2022, 2023, 2024, 2025, 2026, 2027]

# 各类市场规模（亿元）
mobile_eb = [819, 911, 975, 1020, 1060, 1095]    # 移动电竞游戏市场
tournament_eb = [375, 400, 415, 424, 432, 438]  # 端游电竞游戏市场
ecosystem_eb = [385, 386, 400, 424, 458, 497]   # 电竞生态市场

# 整体增长率（%）
growth_rates = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]  # 需根据实际计算，这里先占位

# 颜色配置（贴近原图配色）
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- 绘制堆积柱状图 --------------------
# 移动电竞游戏市场（最下层）
ax.bar(
    years, 
    mobile_eb, 
    color=colors[0], 
    label="移动电竞游戏市场规模（亿元）",
    edgecolor="white",
    linewidth=1
)

# 端游电竞游戏市场（中层）
bottom_mobile = np.array(mobile_eb)
ax.bar(
    years, 
    tournament_eb, 
    bottom=bottom_mobile, 
    color=colors[1], 
    label="端游电竞游戏市场规模（亿元）",
    edgecolor="white",
    linewidth=1
)

# 电竞生态市场（最上层）
bottom_tournament = bottom_mobile + np.array(tournament_eb)
ax.bar(
    years, 
    ecosystem_eb, 
    bottom=bottom_tournament, 
    color=colors[2], 
    label="电竞生态市场规模（亿元）",
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加数据标注 --------------------
# 标注各层数值
for i, (y, m, t, e) in enumerate(zip(years, mobile_eb, tournament_eb, ecosystem_eb)):
    # 移动电竞
    ax.text(y, m/2, f"{m}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # 端游电竞
    ax.text(y, m + t/2, f"{t}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # 电竞生态
    ax.text(y, m + t + e/2, f"{e}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_ylabel("市场规模（亿元）", fontsize=10, color="#424242")

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加图例
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "2022-2027年中国电竞整体市场规模",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()