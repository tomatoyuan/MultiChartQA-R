import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 65 岁及以上人口数量（万人）
elderly_pop = [12777, 13262, 13902, 14524, 15037, 15961, 16724, 17767, 19064, 20056, 20978, 21676]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, elderly_pop, color='green')

# 添加数值标注
for i, pop in enumerate(elderly_pop):
    ax.text(i, pop + 200, f'{pop}', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('65 岁及以上人口数量（万人）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('2012-2023 年中国 65 岁及以上人口数量')

plt.tight_layout()
plt.show()