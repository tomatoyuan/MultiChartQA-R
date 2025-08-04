import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 出生人口数量（万人）
births = [1635, 1640, 1687, 1655, 1786, 1723, 1523, 1465, 1200, 1062, 956, 902]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, births, color='gold')

# 添加数值标注
for i, birth in enumerate(births):
    ax.text(i, birth + 20, f'{birth}', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('出生人口数量（万人）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('2012-2023年中国出生人口数量')

plt.tight_layout()
plt.show()