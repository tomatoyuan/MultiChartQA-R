import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 家政行业营收规模占 GDP 比重（%）
proportions = [0.25, 0.33, 0.36, 0.40, 0.47, 0.55, 0.64, 0.73, 0.92, 0.88, 0.89, 0.92]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
line, = ax.plot(x, proportions, color='gold', marker='o', label='家政行业营收在 GDP 中的比重')

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(i, prop + 0.01, f'{prop}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('占比（%）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylim(0.2, 1.0)  # 设置 y 轴范围，更好展示数据

ax.legend()
ax.set_title('2012 - 2023 年中国家政行业营收规模占 GDP 比重')

plt.tight_layout()
plt.show()