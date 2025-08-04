import matplotlib.pyplot as plt
import numpy as np

# 年份数据
years = np.arange(2015, 2025)  
# 对应年份的社会消费品零售总额（亿元），数据根据图表大致估算，可按需精准替换
retail_sales = [290000, 310000, 340000, 370000, 400000, 390000, 430000, 435000, 460000, 480000]  

# 创建画布和子图
fig, ax = plt.subplots()

# 绘制柱状图
bars = ax.bar(years, retail_sales, color='cyan', label='零售总额')  

# 计算趋势线
z = np.polyfit(years, retail_sales, 1)
p = np.poly1d(z)
ax.plot(years, p(years), 'blue', label='趋势线')  

# 设置x轴刻度显示为年份
plt.xticks(years)  

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1000,
            f'{height}',
            ha='center', va='bottom', rotation=0)

# 添加标题和坐标轴标签
ax.set_title('2015-2024年中国社会消费品零售总额变化趋势（亿元）')
ax.set_xlabel('年份')
ax.set_ylabel('零售总额（亿元）')

# 添加图例
ax.legend()  

# 显示图表
plt.show()