import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e", "2024e", "2025e", "2026e"]
# 全球职业教育规模（十亿美元），数据大体一致即可
market_size = [491, 520, 558, 585, 604, 647, 684, 720, 751, 779, 803]
# 职业教育市场YOY（%），数据大体一致即可
yoy = [5.8, 7.4, 4.7, 3.4, 7.0, 5.8, 5.2, 4.4, 3.7, 3.1]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 1600)
ax2.set_ylim(-5, 10)

# 绘制全球职业教育规模柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="全球职业教育规模（十亿美元）")

# 绘制职业教育市场YOY折线图（注意：yoy数据比年份少一个，因为 2016 年无增速对比数据，这里从 2017 年开始对应）
line_x = x[1:]  # 折线图 x 轴对应 2017 - 2026e 年
line, = ax2.plot(line_x, yoy, marker='o', color="#64B5F6", label="职业教育市场YOY（%）", linewidth=2)

# 添加全球职业教育规模数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加职业教育市场YOY数据标注
for x_val, y_val in zip(line_x, yoy):
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
ax1.set_ylabel("全球职业教育规模（十亿美元）", color="#A4C639")
ax2.set_ylabel("职业教育市场YOY（%）", color="#64B5F6")
# 设置标题
ax1.set_title("2016-2026年全球职业教育市场规模及增速", fontsize=14, fontweight="bold")

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