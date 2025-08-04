import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# 类别及对应数据
categories = ["纸尿裤", "拉拉裤", "纸尿片"]
data = [78.2, 76.4, 51.6]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制条形图
x = np.arange(len(categories))
bar_width = 0.4
bars = ax.barh(x, data, height=bar_width, color="#C63982")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(x)
ax.set_yticklabels(categories)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2022年中国婴儿纸尿裤产品消费者购买品类", fontsize=12, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()