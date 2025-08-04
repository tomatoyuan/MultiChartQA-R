import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
# 母婴消费规模（亿元）
market_size = [23613, 26593, 29919, 31231, 34591, 37552, 40505, 43554]
# 增速（%）
growth_rate = [12.4, 12.6, 12.5, 4.4, 10.8, 8.6, 7.9, 7.5]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 100000)
ax2.set_ylim(0, 12)

# 绘制母婴消费规模柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="母婴消费规模（亿元）")

# 绘制增速折线图
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="增速(%)", linewidth=2)

# 添加母婴消费规模数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加增速数据标注
for x_val, y_val in zip(x, growth_rate):
    ax2.annotate(f'{y_val}%',
                xy=(x_val, y_val),
                xytext=(0, 5),  # 标注位置调整
                textcoords='offset points',
                ha='center', va='bottom',
                color="#64B5F6")

# 设置x轴刻度和标签
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# 设置y轴标签
ax1.set_ylabel("母婴消费规模（亿元）", color="#A4C639")
ax2.set_ylabel("增速(%)", color="#64B5F6")
# 设置标题
ax1.set_title("2017-2024年中国母婴消费规模及增速", fontsize=14, fontweight="bold")

# 合并图例
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# 美化图表，隐藏顶部和右侧边框（针对 ax1 和 ax2 ）
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()