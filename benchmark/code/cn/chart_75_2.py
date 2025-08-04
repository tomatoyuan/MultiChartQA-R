import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021"]
# 云南省咖啡生豆产量（万吨），数据大体一致即可
production = [16.5, 15.1, 14.5, 13.5, 14.0]
# 产量增速（%），数据大体一致即可
growth_rate = [-8.2, -4.1, -6.8, 3.8]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0,32)
ax2.set_ylim(-40, 20)

# 绘制咖啡生豆产量柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, production, width=bar_width, color="#A4C639", label="云南省咖啡生豆产量（万吨）")

# 绘制产量增速折线图（注意：增速数据比年份少一个，因为 2017 年无增速对比数据，这里从 2018 年开始对应）
line_x = x[1:]  # 折线图 x 轴对应 2018 - 2021 年
line, = ax2.plot(line_x, growth_rate, marker='o', color="#64B5F6", label="云南省咖啡生豆产量增速（%）", linewidth=2)

# 添加产量数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加增速数据标注
for x_val, y_val in zip(line_x, growth_rate):
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
ax1.set_ylabel("云南省咖啡生豆产量（万吨）", color="#A4C639")
ax2.set_ylabel("云南省咖啡生豆产量增速（%）", color="#64B5F6")
# 设置标题
ax1.set_title("2017-2021年中国云南省咖啡生豆产量", fontsize=14, fontweight="bold")

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