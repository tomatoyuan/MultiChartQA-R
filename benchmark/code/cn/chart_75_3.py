import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021"]
# 咖啡生豆消费量（万吨），数据大体一致即可
bean_consumption = [13.5, 9.9, 12.9, 14.4, 21.9]
# 咖啡产品进口量（万吨），数据大体一致即可
import_volume = [3.3, 3.6, 3.8, 4.0, 3.9]

# 修复：确保两个增速数据长度相同（均比原始数据少1个）
# 咖啡生豆消费增速（%），数据大体一致即可
bean_growth_rate = [-26.7, 30.3, 11.6, 52.1]  # 移除了第一个错误数据点
# 咖啡产品进口增速（%），数据大体一致即可
import_growth_rate = [9.1, 5.6, 5.3, -2.5]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0,40)
ax2.set_ylim(-200, 100)

# 绘制咖啡生豆消费量柱状图
x = np.arange(len(years))
bar_width = 0.35
bean_bars = ax1.bar(x - bar_width/2, bean_consumption, width=bar_width, color="#A4C639", label="咖啡生豆消费量（万吨）")
# 绘制咖啡产品进口量柱状图
import_bars = ax1.bar(x + bar_width/2, import_volume, width=bar_width, color="#64B5F6", label="咖啡产品进口量（万吨）")

# 绘制增速折线图（从2018年开始，因为2017年没有增速数据）
growth_x = x[1:]  # 对应2018-2021年
bean_growth_line, = ax2.plot(growth_x, bean_growth_rate, marker='o', color="#A4C639", label="咖啡生豆消费增速（%）", linewidth=2, linestyle='--')
import_growth_line, = ax2.plot(growth_x, import_growth_rate, marker='o', color="#64B5F6", label="咖啡产品进口增速（%）", linewidth=2, linestyle='--')

# 添加数据标注（柱状图）
for bar in bean_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

for bar in import_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# 添加数据标注（折线图）
for x_val, y_val in zip(growth_x, bean_growth_rate):
    ax2.annotate(f'{y_val}%',
                xy=(x_val, y_val),
                xytext=(0, 5),
                textcoords='offset points',
                ha='center', va='bottom',
                color="#A4C639")

for x_val, y_val in zip(growth_x, import_growth_rate):
    ax2.annotate(f'{y_val}%',
                xy=(x_val, y_val),
                xytext=(0, 5),
                textcoords='offset points',
                ha='center', va='bottom',
                color="black")

# 设置坐标轴和标题
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylabel("数量（万吨）", color="#333333")
ax2.set_ylabel("增速（%）", color="#333333")
ax1.set_title("2017-2021年中国咖啡生豆消费量及进口咖啡产品消费量", fontsize=14, fontweight="bold")

# 合并图例
handles, labels = ax1.get_legend_handles_labels()
handles.extend([bean_growth_line, import_growth_line])
labels.extend([bean_growth_line.get_label(), import_growth_line.get_label()])
ax1.legend(handles, labels, loc='upper left')

# 美化图表
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()