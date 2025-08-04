import matplotlib.pyplot as plt
import numpy as np

# 日期数据，这里用字符串表示，后续处理显示
dates = [f"5/{i}" for i in range(1, 32)]
# 对应每日搜索关注度近似数据（从图中读取，仅为示例，需按实际调整）
values = [60000, 57000, 62000, 80000, 100000, 90000, 95000, 90000, 80000, 70000, 
          65000, 45000, 60000, 58000, 55000, 48000, 52000, 50000, 47000, 55000, 
          70000, 55000, 65000, 70000, 75000, 78000, 78000, 78000, 80000, 82000, 85000]

# 设置横坐标位置
x = np.arange(len(dates))  

fig, ax = plt.subplots(figsize=(14, 7))  # 调整图表大小
# 绘制折线图，添加标记点
line, = ax.plot(x, values, color='blue', marker='o', markersize=4)  

# 设置横坐标标签，每三天展示一次
xtick_indices = np.arange(0, len(dates), 3)  # 每隔 3 个取索引
xtick_labels = [dates[i] for i in xtick_indices]
ax.set_xticks(xtick_indices)
ax.set_xticklabels(xtick_labels)  

# 添加数据标注
for i, (date, value) in enumerate(zip(dates, values)):
    # 对于前10个数据点，标注在上方；后10个标注在下方，避免超出图表
    if i < 10:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, 10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)
    elif i < 20:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, -10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='top',
                    rotation=0,
                    fontsize=8)
    else:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, 10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)

# 设置坐标轴标题等
ax.set_xlabel('日期', fontsize=12)
ax.set_ylabel('搜索关注度', fontsize=12)
ax.set_title('5月离婚诉讼行业搜索关注度趋势', fontsize=14)

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.7)

# 调整Y轴范围，留出标注空间
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - 5000, y_max + 5000)

plt.tight_layout()  # 确保所有元素都适合图表区域
plt.show()