import matplotlib.pyplot as plt
import numpy as np

# 数据准备
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E", "2025E"]
user_scale = [0.5, 1.0, 1.9, 3.0, 3.6, 4.2, 4.8, 5.3, 5.7, 6.1, 6.4]  # 用户规模（亿人）
yoy_growth = [100.0, 95.8, 56.9, 20.7, 17.4, 14.1, 10.5, 8.5, 7.1, 4.8]  # 同比增速（%），注意 2015 年无同比（或按逻辑 2016 年增速对应 2015-2016 变化，这里与图表数据对齐）

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# 绘制左侧 y 轴（用户规模，柱状图）
ax1.bar(x, user_scale, color="#ee8208", width=0.6, label="用户规模（亿人）")
ax1.set_ylabel("用户规模（亿人）", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# 创建右侧 y 轴（同比增速，折线图）
ax2 = ax1.twinx()
ax2.plot(x[1:], yoy_growth, color="#ffd700", marker="o", label="同比增速（%）")  # 增速从 2016 年（x[1:]）开始对应数据
ax2.set_ylabel("同比增速（%）", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# 添加用户规模数值标注（柱状图上）
for i, scale in enumerate(user_scale):
    ax1.text(x[i], scale + 0.2, f'{scale}', ha="center", va="bottom", color="#ee8208")

# 添加同比增速数值标注（折线上的点）
for i, growth in enumerate(yoy_growth):
    ax2.text(x[i + 1], growth + 2, f'{growth}%', ha="center", va="bottom", color="#ffd700")  # 对应 x[1:] ，索引 +1 对齐

# 合并图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

ax1.set_title("2015-2025年中国知识付费消费者规模及预测", fontsize=14)
plt.tight_layout()
plt.show()