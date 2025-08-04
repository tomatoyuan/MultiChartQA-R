import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["服装鞋帽", "家具家电", "食品生鲜", "手机数码", "美装个护", "医疗保健"]
ranks = [1, 2, 3, 4, 5, 6]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 设置条形图颜色（蓝色系渐变）
colors = plt.cm.Blues(np.linspace(0.8, 0.3, len(categories)))

# 绘制水平条形图
bars = ax.barh(categories, ranks, color=colors)

# 添加数据标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2,
            f'{int(width)}', ha='left', va='center', fontsize=10)

# 设置标题和坐标轴标签
ax.set_title("双十一后悔购买的电商品类排行", fontsize=16, pad=15)
ax.set_xlabel("排行", fontsize=12, labelpad=10)
ax.set_ylabel("商品类别", fontsize=12, labelpad=10)

# 设置x轴刻度
ax.set_xticks(range(1, max(ranks) + 1))

# 添加网格线提高可读性
ax.grid(axis='x', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()