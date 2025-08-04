import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# 门店数量（万家，模拟数据 ）
store_count = [339, 506, 602, 579, 657, 906, 917, 891]
# 同比增长率（%，模拟数据 ）
growth_rate = [49.3, 19.0, -3.8, 13.5, 37.9, 1.2, -2.8]

# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 2000)

# 绘制柱状图（门店数量 ）
ax1.bar(years, store_count, color="#A4C639", label="门店数量（万家）")
ax1.set_ylabel("门店数量（万家）", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# 创建次坐标轴绘制折线图（增长率 ）
ax2 = ax1.twinx()

ax2.set_ylim(-125, 100)

ax2.plot(years[:-1], growth_rate, marker='o', color="#87CEEB", label="同比增长率（%）", linewidth=2)
ax2.set_ylabel("同比增长率（%）", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# 添加柱状图数据标注
for x, y in zip(years, store_count):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# 添加折线图数据标注
for x, y in zip(years[:-1], growth_rate):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="black")

# 设置x轴刻度
ax1.set_xticks(years)
# 设置标题
ax1.set_title("2014-2021年中国餐饮门店数量", fontsize=14, fontweight="bold")

# 合并图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()