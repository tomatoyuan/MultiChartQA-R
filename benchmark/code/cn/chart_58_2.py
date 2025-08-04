import matplotlib.pyplot as plt
import numpy as np

# 数据
dates = [
    "4月22日", "4月23日", "4月24日", "4月25日", "4月26日", 
    "4月27日", "4月28日", "4月29日", "4月30日", "5月1日", 
    "5月2日", "5月3日", "5月4日", "5月5日"
]
values_2024 = [112.1, 118.4, 102.0, 119.4, 91.9, 119.5, 122.3, 130.0, 132.0, 66.7, 61.7, 58.8, 62.9, 101.1]
values_2025 = [76.7, 71.7, 68.8, 101.1, 132.1, 120.0, 102.0, 120.4, 88.9, 119.5, 122.3, 130.3, 133.5, 136.2]

color_2024 = "#4dd0e1"
color_2025 = "#a5d6a7"

x = np.arange(len(dates))

# 创建上下子图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'hspace': 0.3})

# 绘制2024年折线图
ax1.plot(x, values_2024, color=color_2024, marker='o', linewidth=2, label="2024年")
for i, val in enumerate(values_2024):
    ax1.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2024)

ax1.set_title("2024年广告投入趋势", fontsize=12, fontweight="bold", color=color_2024)
ax1.set_ylabel("广告指数", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.2)

# 绘制2025年折线图
ax2.plot(x, values_2025, color=color_2025, marker='o', linewidth=2, label="2025年")
for i, val in enumerate(values_2025):
    ax2.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2025)

ax2.set_title("2025年广告投入趋势", fontsize=12, fontweight="bold", color=color_2025)
ax2.set_ylabel("广告指数", fontsize=11)
ax2.set_xticks(x)
ax2.set_xticklabels(dates, rotation=45, ha="right")
ax2.grid(True, linestyle="--", alpha=0.2)

# 总标题
fig.suptitle(
    "AdTracker 2024 & 2025 年 4月22日-5月5日\n公园/游乐园广告投入趋势对比",
    fontsize=14, fontweight="bold", y=1.03
)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()