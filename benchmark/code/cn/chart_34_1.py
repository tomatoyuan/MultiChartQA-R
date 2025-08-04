import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# 年份数据
years = np.arange(2015, 2027)
# 模拟的市场规模数据（十亿美 元，大体趋势贴近，数值可微调）
market_size = [29.4, 28, 30, 32, 31, 38, 39, 41, 43, 45, 47, 49.2]
# 年份标签，处理 2025E、2026E
year_labels = [str(year) if year < 2025 else f"{year}E" for year in years]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
bars = ax.bar(years, market_size, color='#667799', width=0.8)

# 在柱子上标注数值
for bar, value in zip(bars, market_size):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{value}',
            ha='center', va='bottom')

# 标注 CAGR
ax.text(2022, 50, f'CAGR*: 4.04%', ha='left')

# 绘制30度斜向上的箭头
x_start = 2023
y_start = 48
# 计算30度角的终点坐标（dx = 3，dy = 3 * tan(30°)）
angle_rad = np.radians(60)
dx = 3
dy = dx * np.tan(angle_rad)
x_end = x_start + dx
y_end = y_start + dy

# 使用FancyArrowPatch绘制30度斜向箭头
arrow = FancyArrowPatch((x_start, y_start), (x_end, y_end), 
                        arrowstyle='->', 
                        connectionstyle='arc3,rad=0', 
                        color='black', 
                        mutation_scale=15)
ax.add_patch(arrow)

# 设置 x 轴刻度
ax.set_xticks(years)
ax.set_xticklabels(year_labels)

# 设置 y 轴范围
ax.set_ylim(0, 60)

# 设置图表标题
ax.set_title('2015 - 2026年中国内衣市场规模 (十亿美元)')

# 显示图表
plt.show()