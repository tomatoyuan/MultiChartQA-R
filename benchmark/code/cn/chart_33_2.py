import matplotlib.pyplot as plt
import numpy as np

# 年份数据
years = np.arange(2018, 2025)
# 模拟的 CR5 数据
cr5_data = [56, 57, 53, 52, 52, 52, 53]

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制带数据标记的折线图，使用更专业的蓝色
line, = plt.plot(years, cr5_data, color='#1f77b4', marker='o', markersize=8, 
                 linewidth=2.5, markeredgecolor='white', markeredgewidth=1.5)

# 添加数据标签
for x, y in zip(years, cr5_data):
    plt.annotate(f'{y}', (x, y), textcoords='offset points',
                 xytext=(0, 10), ha='center', fontsize=10)

# 设置坐标轴和刻度
plt.xticks(years, fontsize=12)
plt.ylim(48, 60)  # 调整Y轴范围使图表更紧凑
plt.yticks(np.arange(48, 61, 2), fontsize=12)

# 添加网格线增强可读性
plt.grid(True, linestyle='--', alpha=0.7)

# 添加标题和标签，使用更专业的字体大小
plt.title('2018-2024年中国衣物清洁护理市场集中度分析', fontsize=16, pad=15)
plt.xlabel('年份', fontsize=14, labelpad=10)
plt.ylabel('市场集中度 (%)', fontsize=14, labelpad=10)

# 美化图例
plt.legend([line], ['CR5市场集中度'], fontsize=12, loc='upper right')

# 调整图表布局
plt.tight_layout()

# 显示图表
plt.show()