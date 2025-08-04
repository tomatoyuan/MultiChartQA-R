import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2021', '2022', '2026E']
values = [64416, 69700.8, 93311.9]
x = np.arange(len(years))

# 图表创建
fig, ax = plt.subplots(figsize=(8, 6))

# 柱状图
bars = ax.bar(x, values, color='#00d2c8', width=0.5, label='市场规模（亿元）')

# 添加数值标签
for i, v in enumerate(values):
    ax.text(x[i], v + 2000, f'{v}', ha='center', va='bottom', fontsize=10)

# 添加 CAGR 注释
ax.annotate('CAGR = 7.6%',
            xy=(0, values[0] + 8000), xytext=(0.4, values[2] + 8000),
            textcoords='data',
            fontsize=13, color='#00d2c8', fontweight='bold')

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_ylim(0, 105000)
ax.set_ylabel('单位：亿元', fontsize=12)
ax.set_title('全球增强免疫力食品市场', fontsize=14, fontweight='bold', pad=20)

# 图例
ax.legend(loc='best', fontsize=10)

# 网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.3)

# 美化边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()