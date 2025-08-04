import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# 年份数据
years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
# 互联网普及率数据
rates = np.array([59.6, 64.5, 70.4, 73.0, 75.6, 77.5, 78.6])

# 创建柱状图
fig, ax = plt.subplots()
bars = ax.bar(years, rates, color='orange')

# 在每个柱子上标注数值
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height,
            f'{height}',
            ha='center', va='bottom')

# 设置图表标题和坐标轴标签
ax.set_title('2018-2024年中国互联网普及率')
ax.set_xlabel('年份')
ax.set_ylabel('普及率 (%)')

# 显示图表
plt.show()