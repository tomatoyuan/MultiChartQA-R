import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# 年份
years = np.arange(2015, 2025)
# 产量数据（万吨）
outputs = [6210.97, 6379.48, 6445.33, 6457.66, 6480.36, 
           6549.02, 6690.29, 6865.91, 7116.24, 7366.50]

# 创建画布和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(years, outputs, color='#FFA07A')  # 设置柱状图颜色

# 添加数值标注
for bar, output in zip(bars, outputs):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, 
            f'{output}', ha='center', va='bottom')

# 设置标题和坐标轴标签
ax.set_title('2015-2024年中国水产品总产量')
ax.set_xlabel('年份')
ax.set_ylabel('产量（万吨）')

# 设置y轴范围
ax.set_ylim(5600, 7600)  

# 显示图表
plt.show()