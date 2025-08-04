import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2020", "2021", "2022e", "2023e", "2024e", "2025e"]
# 整体云服务市场规模（亿元）
market_size = [2256, 3280, 4769, 6812, 9550, 12683]
# 整体云服务市场增速（%）
growth_rate = [39.9, 45.4, 42.8, 40.2, 32.8, 30.6]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 26000)
ax2.set_ylim(0, 55)

# 绘制整体云服务市场规模柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="整体云服务市场规模（亿元）")

# 绘制整体云服务市场增速折线图
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="整体云服务市场增速（%）", linewidth=2)

# 添加市场规模数据标注
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
ax1.set_ylabel("整体云服务市场规模（亿元）", color="#A4C639")
ax2.set_ylabel("整体云服务市场增速（%）", color="#64B5F6")
# 设置标题
ax1.set_title("云共识：2020-2025年中国整体云服务市场规模及增速", fontsize=14, fontweight="bold")

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