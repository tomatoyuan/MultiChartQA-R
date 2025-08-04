import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.array([2020, 2021, 2022, 2023, 2024])
# 宠物/宠物食品及用品市场规模数据（大体示意，可调整）
market_size = np.array([40, 45, 55, 60, 70])  
# 增长率数据（大体示意，可调整）
growth_rate = np.array([10, 9, 15, 8, 14])  

# 创建画布和轴
fig, ax1 = plt.subplots(figsize=(10, 6))  # 调整图表大小

# 绘制柱状图（宠物/宠物食品及用品市场规模）
bars = ax1.bar(years, market_size, color='blue', label='宠物/宠物食品及用品')
ax1.set_xlabel('年份')
ax1.set_ylabel('市场规模（示意值）', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 在柱状图上方添加数据标签
for bar, value in zip(bars, market_size):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{value}', ha='center', va='bottom', color='blue')

# 创建第二个轴用于绘制折线图（增长率）
ax2 = ax1.twinx()
line, = ax2.plot(years, growth_rate, color='orange', marker='o', label='增长率')
ax2.set_ylabel('增长率（%）', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# 设置y轴刻度，与原图表类似
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 18, 2))

# 在折线图的每个数据点上添加标注
for x, y in zip(years, growth_rate):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='orange')

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 设置图表标题
plt.title('宠物线上电商市场规模趋势')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()