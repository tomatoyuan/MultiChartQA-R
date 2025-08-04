import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2014, 2025)
# 营收数据（万亿元），2024为预测值（E）
revenues = [2.5, 2.8, 3.2, 4.4, 5.4, 6.9, 7.4, 8.0, 8.3, 8.6, 9.0]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(12, 7))

# 设置网格样式
plt.grid(True, linestyle='--', alpha=0.7)

# 创建柱状图，使用渐变色
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(years)))
bars = ax.bar(years, revenues, color=colors, edgecolor='black', linewidth=0.5)

# 设置标题和坐标轴标签
ax.set_title('2014 - 2024年中国大健康产业整体营收及预测', fontsize=16, pad=20)
ax.set_xlabel('年份', fontsize=14, labelpad=10)
ax.set_ylabel('营收（万亿元）', fontsize=14, labelpad=10)

# 设置x轴和y轴刻度
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 10, 1))

# 为每个柱子添加数值标签
for bar, revenue in zip(bars, revenues):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{revenue}', ha='center', va='bottom', fontsize=10)

# 突出显示预测值
prediction_bar = bars[-1]
prediction_bar.set_color('lightgreen')
prediction_bar.set_edgecolor('black')
ax.text(prediction_bar.get_x() + prediction_bar.get_width()/2., 
        prediction_bar.get_height() + 0.4,
        f'{revenues[-1]} (预测)', ha='center', va='bottom', fontsize=10, weight='bold')

# 添加图例
ax.legend([bars[0], prediction_bar], ['实际值', '预测值（E）'], loc='upper left')

# 设置y轴范围
plt.ylim(0, 10)

# 美化图表
plt.tight_layout()

# 显示图表
plt.show()