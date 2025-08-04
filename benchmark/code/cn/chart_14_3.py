import matplotlib.pyplot as plt
import numpy as np

# 时间轴数据
dates = ['15年1月', '15年3月', '15年5月', '15年7月', '15年9月', 
         '15年11月', '16年1月', '16年3月', '16年5月', '16年7月', '16年9月']

# 添加了微小波动的搜索指数数据（手动调整）
search_index = [
    2950,  # 原3000
    2980,  # 原3000
    3020,  # 原3000
    6000,
    9000,
    2950,  # 原3000
    2960,  # 原3000
    2970,  # 原3000
    3010,  # 原3000
    9000,
    15000
]

# 将时间轴转为可用于绘图的索引
x = np.arange(len(dates))  

# 创建绘图对象
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制折线图，设置线条宽度和标记样式
line, = ax.plot(x, search_index, color='orange', marker='o', markersize=6, 
                linewidth=2, label='空调病搜索指数趋势')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(dates, rotation=45, ha='right')

# 设置 y 轴范围和标签
ax.set_ylim(0, 1.1 * max(search_index))
ax.set_ylabel('搜索指数')

# 添加标题和副标题
ax.set_title('“空调病”相关搜索指数', fontsize=16, pad=15)

# 在折线上标注数值
for i, (xi, yi) in enumerate(zip(x, search_index)):
    ax.annotate(f'{int(round(yi))}',  # 取整显示
                (xi, yi),
                textcoords='offset points',
                xytext=(0, 10),  # 文本位置偏移
                ha='center',
                fontsize=9)

# 添加图例和网格线
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 隐藏上、右坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()