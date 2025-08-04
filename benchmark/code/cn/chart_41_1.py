import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
# 市场规模数据（大体模拟，接近即可）
market_size = np.array([2000, 2500, 2700, 2800, 3000, 3300])  

# 创建画布
fig, ax = plt.subplots()
# 绘制柱状图，设置颜色为蓝色，接近原图
ax.bar(years, market_size, color='#4B79A1')  

# 添加标题，与原图标题格式适配
ax.set_title('2020-2025年城镇（大猫）消费市场规模', fontdict={'fontsize': 12})  
# 设置 x 轴标签
ax.set_xlabel('年份')  
# 设置 y 轴标签
ax.set_ylabel('市场规模（亿元）')  

# 标记2024年首次突破3000亿的文本注释，位置可微调
ax.text(2024, 3000 + 50, '首次突破3000亿', ha='center', va='bottom', fontsize=10, color='orange')  

# 设置 x 轴刻度，将2025年显示为2025E
ax.set_xticks(years)
ax.set_xticklabels([str(year) + 'E' if year == 2025 else str(year) for year in years])

# 设置 y 轴刻度范围，让显示更贴合数据
ax.set_ylim(0, 3500)  

# 显示图表
plt.show()