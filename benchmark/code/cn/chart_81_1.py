import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2011, 2022)
# 社会物流总费用（万亿）
logistics_cost = [8.4, 9.4, 10.2, 10.6, 10.8, 11.1, 12.1, 13.3, 14.6, 14.9, 16.7]
# 占GDP比重（%）
gdp_ratio = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7, 14.6]

# 创建画布，使用双轴
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 32)
ax2.set_ylim(5, 20)

# 绘制社会物流总费用柱状图
ax1.bar(years, logistics_cost, width=0.6, color="#C63982", label="社会物流总费用（万亿）")
# 绘制占GDP比重折线图
ax2.plot(years, gdp_ratio, marker='o', color="#64B5F6", label="占GDP比重（%）", linewidth=2)

# 给柱状图添加数据标注
for x, y in zip(years, logistics_cost):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# 给折线图添加数据标注
for x, y in zip(years, gdp_ratio):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#64B5F6")

# 设置坐标轴标签和标题
ax1.set_xlabel("年份")
ax1.set_ylabel("社会物流总费用（万亿）", color="#C63982")
ax2.set_ylabel("占GDP比重（%）", color="#64B5F6")
ax1.set_title("2011-2021年中国社会物流总费用及占GDP比重", fontsize=14, fontweight="bold")

# 设置x轴刻度
ax1.set_xticks(years)
ax1.set_xticklabels(years)

# 合并图例
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()