import matplotlib.pyplot as plt
import numpy as np

# 图表1：MAT2406 线上FMCG及各品类增速（使用柱状图）
categories = ['网上零售', '线上FMCG', '食品', '美妆', '母婴']
growth = [4.9, 7.8, 8.1, 5.8, 10.2]
colors = ['black', '#0056d6', 'white', 'white', 'white']
edgecolors = ['black', '#0056d6', '#0056d6', '#0056d6', '#0056d6']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, growth, color=colors, edgecolor=edgecolors, linewidth=2)

# 添加数值标签
for bar, value in zip(bars, growth):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.3, f'{value}%', ha='center', va='bottom', fontsize=12)

# 设置标题与Y轴标签
ax.set_title('MAT2406 线上FMCG及各品类增速', fontsize=16)
ax.set_ylabel('同比增长率 (%)')
ax.set_ylim(0, 12)
ax.set_facecolor('#f8f9fa')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()