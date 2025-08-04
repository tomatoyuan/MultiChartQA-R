import matplotlib.pyplot as plt
import numpy as np

# 城市名称
cities = ['北京', '深圳', '武汉', '上海', '广州']
# 对应搜索占比数据（从图中读取的近似值，可替换为精准数据）
percentages = [19, 6, 5.5, 4.5, 2.5]

x = np.arange(len(cities))  # 用于设置横坐标位置

fig, ax = plt.subplots(figsize=(10, 6))  # 调整图表大小
# 绘制柱状图，调整宽度并设置颜色
bars = ax.bar(x, percentages, width=0.6, color='skyblue')  

# 为每个柱子添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',  # 标注文本
                xy=(bar.get_x() + bar.get_width() / 2, height),  # 标注位置
                xytext=(0, 3),  # 垂直偏移量
                textcoords="offset points",
                ha='center',  # 水平对齐方式
                va='bottom',  # 垂直对齐方式
                fontsize=10)  # 字体大小

# 设置横坐标刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(cities, fontsize=10)

# 设置纵坐标范围和刻度
ax.set_ylim(0, 22)  # 略微增加上限，为标注留出空间
ax.set_yticks(np.arange(0, 21, 5))

# 设置坐标轴标题和图表标题
ax.set_ylabel('搜索占比 (%)', fontsize=12)
ax.set_title('5月离婚诉讼行业搜索城市TOP5', fontsize=14)

# 添加网格线，增强可读性
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 美化图表
plt.tight_layout()  # 自动调整布局
plt.show()