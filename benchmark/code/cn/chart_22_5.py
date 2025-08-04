import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# 年份
years = np.arange(2012, 2017)  
# 模拟数据，大体贴近原图趋势，版权收入、商业赞助、资源置换
copyright_income = [0.5, 0.6, 0.6, 1, 10]  
sponsorship_income = [1, 2, 4.5, 8, 5]
resource_swap = [1, 1.2, 1.5, 1.6, 1.7]  

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))  # 增大图表尺寸

# 设置背景网格和颜色
ax.set_facecolor('#f8f9fa')
ax.grid(True, linestyle='--', alpha=0.7)

# 绘制三条折线，使用更美观的颜色和标记
line1, = ax.plot(years, copyright_income, color='#3498db', label='版权收入', linewidth=3, marker='o', markersize=8)
line2, = ax.plot(years, sponsorship_income, color='#e74c3c', label='商业赞助', linewidth=3, marker='s', markersize=8)
line3, = ax.plot(years, resource_swap, color='#2ecc71', label='资源置换', linewidth=3, marker='^', markersize=8)

# 设置标题和副标题
ax.set_title('2012年-2016年收入趋势分析', fontsize=18, fontweight='bold', pad=20)

# 设置坐标轴标签和刻度
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('收入（亿元）', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels([f'{year}年' for year in years], fontsize=10)
ax.set_yticks(np.arange(0, 11, 2.5))

# 为每个数据点添加数值标签
for x, y in zip(years, copyright_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)
for x, y in zip(years, sponsorship_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)
for x, y in zip(years, resource_swap):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)

# 高亮显示版权收入的增长
ax.fill_between(years, copyright_income, 0, color='#3498db', alpha=0.1)

# 调整图例位置和样式
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), 
          fancybox=True, shadow=True, ncol=3, fontsize=11)

plt.tight_layout()  # 调整布局
plt.show()