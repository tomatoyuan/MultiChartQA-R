import matplotlib.pyplot as plt
import numpy as np

# 数据
years = np.array([2016, 2017, 2018, 2019, 2020, 2021])
percentages = np.array([1.8, 2.7, 4.6, 4.8, 5.4, 13.6])

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制面积图，使用渐变色填充
from matplotlib.collections import PolyCollection

# 创建填充区域坐标
verts = [(years[0], 0)] + list(zip(years, percentages)) + [(years[-1], 0)]
poly = PolyCollection([verts], facecolors=['#b2dfdb'], edgecolors='none', alpha=0.7)
ax.add_collection(poly)

# 叠加折线图 + 圆点
ax.plot(years, percentages, marker='o', color='#00796B', linewidth=2.5, label='新能源车产量占比（%）')

# 添加数据标签
for x, y in zip(years, percentages):
    ax.text(x, y + 0.5, f'{y}%', ha='center', fontsize=10, color='#004d40', fontweight='bold')

# 设置坐标轴
ax.set_xticks(years)
ax.set_ylim(0, max(percentages) + 3)
ax.set_ylabel("新能源车产量占比（%）")

# 添加标题
ax.set_title("2016-2021年中国新能源汽车产量占比", fontsize=14, fontweight='bold')

# 图例
ax.legend(loc='upper left', fontsize=10)

# 美化图表
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_alpha(0.2)
ax.spines["left"].set_alpha(0.2)

plt.tight_layout()
plt.show()