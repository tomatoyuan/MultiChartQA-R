import matplotlib.pyplot as plt
import numpy as np

# 数据
years = [2000, 2019, 2020, 2021]
life_expectancy = [66.8, 73.2, 72.5, 71.4]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 将年份转换为分类变量（均匀分布）
y_pos = np.arange(len(years))

# 绘制水平条形图，使用渐变色填充
colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(years)))
bars = ax.barh(y_pos, life_expectancy, color=colors, alpha=0.8, edgecolor='gray', linewidth=0.5)

# 添加数据标签
for bar, value in zip(bars, life_expectancy):
    ax.text(bar.get_width() + 0.2, 
            bar.get_y() + bar.get_height()/2,
            f'{value}',
            va='center',
            fontweight='bold',
            fontsize=10)

# 添加 2021 年与 2012 年水平齐平的辅助说明
ax.annotate('与2012年\n水平齐平',
            xy=(71.4, y_pos[-1]),
            xytext=(73, y_pos[-1] - 0.3),
            arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8),
            fontsize=10)

# 设置 y 轴刻度标签为年份（均匀分布）
ax.set_yticks(y_pos)
ax.set_yticklabels(years, fontsize=11)

# 设置 x 轴范围和刻度
ax.set_xlim(65, 75)
ax.set_xticks(np.arange(65, 76, 1))

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.3)

# 添加标题和副标题
fig.suptitle('新冠疫情对全球预期寿命的影响', 
             fontsize=16, 
             fontweight='bold',
             y=0.96)

ax.set_title('全球预期寿命趋势（2000-2021）', 
             fontsize=13, 
             loc='left',
             pad=12)

# 添加图例
ax.legend([bars[0]], ['预期寿命(岁)'], loc='lower right')

# 隐藏顶部、右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 调整布局
plt.subplots_adjust(bottom=0.1, left=0.15)

# 显示图表
plt.show()