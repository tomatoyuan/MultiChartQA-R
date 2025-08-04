import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2019, 2029)
# 线上市场份额（示例数据，贴近原趋势）
online_share = [16, 20, 31, 33, 35, 36, 37, 47, 55, 60]
# 线下市场份额 = 100 - 线上（简化模拟，保证总和逻辑 ）
offline_share = [100 - x for x in online_share]

# 柱状图宽度
bar_width = 0.6

# 创建画布
fig, ax = plt.subplots()

# 绘制线下份额（灰色，对应原图表底层）
ax.bar(years, offline_share, width=bar_width, color='#D3D3D3', label='线下')  
# 绘制线上份额（蓝色，对应原图表上层 ）
ax.bar(years, online_share, width=bar_width, bottom=offline_share, color='#4682B4', label='线上')  

# 设置 x 轴刻度
ax.set_xticks(years)
# 设置 y 轴标签
ax.set_ylabel('市场份额（%）')  
# 设置标题
ax.set_title('2019 - 2028年家清洗护线上线下渠道市场份额分布')  
# 添加图例
ax.legend()  

# 在柱状图上方添加数据标签
for i, year in enumerate(years):
    # 线下份额标签
    ax.text(year, offline_share[i]/2, f'{offline_share[i]}%', ha='center', va='center', color='black')
    # 线上份额标签
    ax.text(year, offline_share[i] + online_share[i]/2, f'{online_share[i]}%', ha='center', va='center', color='white')

# 显示图表
plt.show()