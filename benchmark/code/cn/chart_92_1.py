import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2016, 2017, 2018, 2019, 2020, 2021]
# 居民人均交通和通信消费支出（元，模拟数据 ）
expenditures = [2338, 2499, 2675, 2862, 2761, 3156]
# 增长率（%，模拟数据 ）
growth_rates = [12.0, 6.9, 7.0, 7.0, -3.5, 14.3]

# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 6000)

# 绘制柱状图（消费支出 ）
ax1.bar(years, expenditures, color="#A4C639", label="居民人均交通和通信消费支出(元)")
ax1.set_ylabel("消费支出(元)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# 创建次坐标轴绘制折线图（增长率 ）
ax2 = ax1.twinx()

ax2.set_ylim(-50, 25)

ax2.plot(years, growth_rates, marker='o', color="#87CEEB", label="增长率 (%)", linewidth=2)
ax2.set_ylabel("增长率 (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# 添加柱状图数据标注
for x, y in zip(years, expenditures):
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
ax1.set_title("2016-2021年中国居民人均交通和通信消费支出", fontsize=14, fontweight="bold")

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