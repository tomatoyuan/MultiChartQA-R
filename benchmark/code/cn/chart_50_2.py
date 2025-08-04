import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 模拟数据（与原图趋势一致）
years = np.arange(2013, 2025)
gdp_data = [4.4, 4.8, 5.1, 5.5, 6.1, 6.7, 7.1, 7.3, 8.3, 8.7, 9.2, 9.6]
income_data = [1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.1, 3.2, 3.5, 3.7, 3.9, 4.1]

# 计算 CAGR（模拟与原图接近的增长率）
def cagr(start, end, years):
    return ((end / start) ** (1/years) - 1) * 100

gdp_cagr = cagr(gdp_data[0], gdp_data[-1], len(years)-1)
income_cagr = cagr(income_data[0], income_data[-1], len(years)-1)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制折线图
gdp_line, = ax.plot(years, gdp_data, color='#A8D268', marker='o', label='中国人均GDP（万元）', linewidth=3)
income_line, = ax.plot(years, income_data, color='#59B9E1', marker='o', label='全国居民人均可支配收入（万元）', linewidth=3)

# 在折线上添加数据标注
for x, y in zip(years, gdp_data):
    ax.annotate(f'{y}', 
                (x, y),
                textcoords="offset points",
                xytext=(0,10),  # 垂直偏移量
                ha='center',
                color='#86C232')

for x, y in zip(years, income_data):
    ax.annotate(f'{y}', 
                (x, y),
                textcoords="offset points",
                xytext=(0,-15),  # 垂直偏移量（负值表示向下）
                ha='center',
                color='#2F9EBD')

# 添加 CAGR 指标卡（左上角绿色/蓝色标签） - 调整大小和位置
ax.text(0.02, 0.92, 'CAGR', fontsize=10, transform=ax.transAxes, color='white', ha='left', va='center', 
        bbox=dict(facecolor='#86C232', pad=3, edgecolor='none', boxstyle='round,pad=0.2'))
ax.text(0.08, 0.92, f'+{gdp_cagr:.1f}%', fontsize=10, color='#86C232', transform=ax.transAxes, ha='left', va='center')

ax.text(0.02, 0.85, 'CAGR', fontsize=10, transform=ax.transAxes, color='white', ha='left', va='center', 
        bbox=dict(facecolor='#2F9EBD', pad=3, edgecolor='none', boxstyle='round,pad=0.2'))
ax.text(0.08, 0.85, f'+{income_cagr:.1f}%', fontsize=10, color='#2F9EBD', transform=ax.transAxes, ha='left', va='center')

# 图表配置
ax.set_title('2013年-2024年中国人均GDP及全国居民人均可支配收入', fontsize=14, pad=30)
ax.set_xticks(years)
ax.set_ylim(0, 11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.68), frameon=False)

plt.tight_layout()
plt.show()