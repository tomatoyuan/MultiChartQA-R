import matplotlib.pyplot as plt
import numpy as np

# 消费支出类别
categories = [
    "食品烟酒", "居住", "交通通信", "教育文化娱乐", 
    "医疗保健", "衣着", "生活用品及服务", "其他用品及服务"
]
# 对应占比数据（%），数据大体一致即可
data = [29.8, 23.4, 13.1, 10.8, 8.8, 5.9, 5.9, 2.4]
# 颜色设置，贴近原图绿色系
color = "#A4C639"

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制水平条形图
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=color, edgecolor="white")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(categories)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2021年中国居民人均消费支出构成", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()