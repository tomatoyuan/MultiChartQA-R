import matplotlib.pyplot as plt
import numpy as np

# 关注情况类别
categories = ["关注度提升", "基本没有变化，一直较为关注", "不太关注"]
# 对应占比数据（%），数据大体一致即可
data = [76.0, 19.0, 5.0]
# 颜色设置，贴近原图绿色系
color = "#8239C6"

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制水平条形图
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=color, edgecolor="white")

# 为“关注度提升”添加红色虚线边框
rect = plt.Rectangle((0, y[0] - bar_height/2), data[0], bar_height, fill=False, edgecolor='red', linestyle='--')
ax.add_patch(rect)

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
ax.set_title("消费者对奶粉成分/配方高端性关注度", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()