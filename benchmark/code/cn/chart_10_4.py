import matplotlib.pyplot as plt
import numpy as np

# 数据
cities = ["北京", "成都", "上海", "杭州", "深圳"]
search_ratios = [4.3, 3.4, 2.9, 2.5, 2.5]

# 创建画布和子图
plt.figure(figsize=(10, 6), dpi=300)
ax = plt.subplot(111)

# 设置渐变色柱状图
colors = plt.cm.viridis(np.linspace(0.3, 0.8, len(cities)))
bars = plt.bar(cities, search_ratios, color=colors, width=0.6, edgecolor='black', linewidth=0.8)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{height}%', ha='center', va='bottom', fontweight='bold')

# 添加标题和坐标轴标签
plt.title("5月职业培训行业TOP5搜索城市", fontsize=16, fontweight='bold')
plt.xlabel("城市", fontsize=12)
plt.ylabel("搜索占比（%）", fontsize=12)

# 设置坐标轴范围和刻度
plt.ylim(0, max(search_ratios) * 1.1)
plt.yticks(np.arange(0, 5, 0.5))

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加背景色
ax.set_facecolor('#f8f9fa')

# 调整边框
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# 添加图例
plt.legend([bars[0]], ['搜索占比'], loc='upper right')

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()