import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
market_size = [804, 802, 850, 777, 862, 944, 1029, 1117, 1210]  # 市场规模（亿元）
growth_rate = [6.0, -0.2, 6.0, -8.6, 10.9, 9.5, 9.0, 8.6, 8.3]  # 增速（%）

# 颜色配置
bar_color = "#a5d6a7"
line_color = "#4dd0e1"

# -------------------- 创建上下两个子图 --------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True,
                               gridspec_kw={'height_ratios': [2, 1], 'hspace': 0.15})

x = np.arange(len(years))

# -------------------- 绘制柱状图 --------------------
ax1.bar(
    x, 
    market_size, 
    color=bar_color, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="中国眼镜产品零售市场规模（亿元）"
)

# 添加市场规模数据标注
for i, val in enumerate(market_size):
    ax1.text(
        i, val + 10, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax1.set_ylabel("市场规模（亿元）", fontsize=12, color="#424242")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")
ax1.set_title("2019-2027e年中国眼镜行业零售市场规模", fontsize=14, fontweight="bold", pad=10)

# -------------------- 绘制折线图 --------------------
ax2.plot(
    x, 
    growth_rate, 
    color=line_color, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="增速（%）"
)

# 添加增速数据标注
for i, val in enumerate(growth_rate):
    ax2.text(
        i, val + 0.5, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax2.set_ylabel("增速（%）", fontsize=12, color="#424242")
ax2.set_ylim(min(growth_rate) - 5, max(growth_rate) + 5)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# 设置x轴标签
ax2.set_xticks(x)
ax2.set_xticklabels(years, fontsize=10, color="#424242", rotation=0)

# -------------------- 调整布局 --------------------
plt.tight_layout()
plt.show()