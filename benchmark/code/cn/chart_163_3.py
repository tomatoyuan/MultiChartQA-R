import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import cm


# 数据
years = list(range(2012, 2023))
gdp_percent = [55, 54, 56, 56, 44, 42, 42, 40, 40, 40, 41]

# 颜色渐变（从浅红到深红）
colors = cm.Reds(np.linspace(0.3, 0.8, len(gdp_percent)))

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(years, gdp_percent, color=colors, edgecolor='black')

# 添加数值标签
for bar, value in zip(bars, gdp_percent):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
            f'{value}%', ha='center', va='bottom', fontsize=11)

# 标题与标签
ax.set_title("县域经济规模及全国GDP占比（2012–2022年）", fontsize=15)
ax.set_ylabel("占比（%）", fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()