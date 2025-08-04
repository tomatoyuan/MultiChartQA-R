import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021e"]
# “三新”经济规模（亿元），数据大体一致即可
economic_scale = [113719, 129578, 145369, 161927, 169254, 197170]
# 占GDP比重（%），数据大体一致即可
gdp_ratio = [15.3, 15.7, 16.1, 16.3, 17.1, 17.2]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 400000)
ax2.set_ylim(10, 18)

# 绘制“三新”经济规模柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, economic_scale, width=bar_width, color="#A4C639", label="“三新”经济规模（亿元）")

# 绘制占GDP比重折线图
line, = ax2.plot(x, gdp_ratio, marker='o', color="#64B5F6", label="占GDP比重（%）", linewidth=2)

# 添加“三新”经济规模数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加占GDP比重数据标注
for x_val, y_val in zip(x, gdp_ratio):
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
ax1.set_ylabel("“三新”经济规模（亿元）", color="#A4C639")
ax2.set_ylabel("占GDP比重（%）", color="#64B5F6")
# 设置标题
ax1.set_title("2016-2021年中国新经济规模及占GDP比重", fontsize=14, fontweight="bold")

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