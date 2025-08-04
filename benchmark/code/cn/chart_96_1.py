import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# MPV销量（万辆，模拟数据 ）
sales = [49.8, 49.3, 130.5, 191.4, 210.7, 249.7, 207.1, 173.5, 138.4, 105.4, 105.5]
# 年增长率（%，模拟数据 ）
growth_rates = [11.7, -0.9, 164.5, 46.7, 10.1, 18.5, -17.1, -16.2, -20.2, -23.8, 0.1]

# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 500)

# 绘制柱状图（MPV销量 ）
ax1.bar(years, sales, color="#A4C639", label="MPV销量(万辆)")
ax1.set_ylabel("MPV销量(万辆)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# 创建次坐标轴绘制折线图（增长率 ）
ax2 = ax1.twinx()

ax2.set_ylim(-200, 200)

ax2.plot(years, growth_rates, marker='o', color="#87CEEB", label="年增长率(%)", linewidth=2)
ax2.set_ylabel("年增长率(%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# 添加柱状图数据标注
for x, y in zip(years, sales):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# 添加折线图数据标注
for x, y in zip(years, growth_rates):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# 设置x轴刻度
ax1.set_xticks(years)
# 设置标题
ax1.set_title("2011-2021年中国MPV销量及增长率", fontsize=14, fontweight="bold")

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