import matplotlib.pyplot as plt
import numpy as np

# 数据准备
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E", "2025E"]
market_size = [15.9, 26.5, 49.1, 148.3, 278.0, 392.0, 675.0, 1126.5, 1802.7, 2296.6, 2808.8]  # 市场规模（亿元）
yoy_growth = [66.7, 85.3, 202.0, 87.5, 41.0, 72.2, 66.9, 60.0, 27.4, 22.3]  # 同比增速（%），注意与 years 对应，2015 年无同比（或可根据需求调整），这里从 2016 开始有增速数据，与图表逻辑对齐

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# 绘制左侧 y 轴（市场规模，柱状图）
ax1.bar(x, market_size, color="#ee8208", width=0.6, label="市场规模（亿元）")
ax1.set_ylabel("市场规模（亿元）", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# 创建右侧 y 轴（同比增速，折线图）
ax2 = ax1.twinx()
ax2.plot(x[1:], yoy_growth, color="#ffd700", marker="o", label="同比增速（%）")  # 从 2016 年开始绘制折线，对应 x[1:]
ax2.set_ylabel("同比增速（%）", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# 添加市场规模数值标注（柱状图上）
for i, size in enumerate(market_size):
    ax1.text(x[i], size + 50, f'{size}', ha="center", va="bottom", color="#ee8208")

# 添加同比增速数值标注（折线上的点）
for i, growth in enumerate(yoy_growth):
    ax2.text(x[i + 1], growth + 2, f'{growth}%', ha="center", va="bottom", color="#ffd700")  # 对应 x[1:] ，所以索引 +1

# 合并图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

ax1.set_title("2015 - 2025 中国知识付费市场规模及预测", fontsize=14)
plt.tight_layout()
plt.show()