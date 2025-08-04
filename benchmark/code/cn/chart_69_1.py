import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# 项目名称
items = ["教育", "医疗保健", "大额商品", "社交文化和娱乐", "购房", "旅游", "保险"]
# 对应数据（占比）
data = [28.1, 27.4, 18.7, 18.1, 16.9, 15.2, 13.9]
# 颜色设置，旅游为蓝色，其余为绿色，贴近原图
colors = ["#A4C639"] * len(items)
colors[items.index("旅游")] = "#64B5F6"

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制水平条形图
y = np.arange(len(items))
bar_height = 0.6
max_data = max(data)
for i in range(len(items)):
    # 绘制背景条（绿色边框效果）
    rect = Rectangle((0, y[i] - bar_height / 2), max_data, bar_height, facecolor="white", edgecolor="#A4C639", linewidth=1.5)
    ax.add_patch(rect)
    # 绘制前景条
    bar = ax.barh(y[i], data[i], height=bar_height, color=colors[i], edgecolor="white", label=items[i])
    # 添加数据标注
    ax.annotate(f'{data[i]}%',
                xy=(data[i], y[i]),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center',
                fontweight='bold')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(items)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("未来三个月内准备增加支出的项目", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()