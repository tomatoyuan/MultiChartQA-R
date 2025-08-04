import matplotlib.pyplot as plt
import numpy as np

# 日期数据（修正重复年份问题）
dates = ['7月1日', '7月6日', '7月11日', '7月16日', '7月21日', '7月26日']
# 搜索指数数据
heatstroke_index = [7000, 10000, 10000, 14000, 7000, 42000]
air_condition_illness_index = [3500, 7000, 7000, 10000, 10000, 21000]

# 将日期转为可用于绘图的索引
x = np.arange(len(dates))  

# 创建绘图对象
fig, ax = plt.subplots(figsize=(12, 7))

# 设置渐变色背景（从浅蓝到深蓝）
gradient = np.linspace(0.95, 0.85, 256).reshape(256, 1)
ax.imshow(gradient, aspect='auto', extent=[0, len(dates)-1, 0, max(heatstroke_index)*1.1], 
          alpha=0.3, cmap=plt.cm.Blues)

# 绘制优化后的折线图
ax.plot(x, heatstroke_index, color='#FF3333', marker='o', markersize=8, 
        label='中暑', linewidth=3, alpha=0.8)
ax.plot(x, air_condition_illness_index, color='#FF9933', marker='o', markersize=8, 
        label='空调病', linewidth=3, alpha=0.8)

# 设置x轴和y轴
ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=12)
ax.set_ylabel('搜索指数', fontsize=14, labelpad=10)
ax.set_ylim(0, max(heatstroke_index) * 1.1)  # 留出顶部空间

# 设置美化后的标题
ax.set_title('空调病与中暑搜索指数对比趋势', 
             fontsize=18, fontweight='bold', pad=20, color='#333333')

# 添加数据标签
for i, (xi, yi) in enumerate(zip(x, heatstroke_index)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
    
for i, (xi, yi) in enumerate(zip(x, air_condition_illness_index)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, -15), ha='center', fontsize=10, fontweight='bold')

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 设置图例和边框
ax.legend(fontsize=12, loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#AAAAAA')
ax.spines['bottom'].set_color('#AAAAAA')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()