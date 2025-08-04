import matplotlib.pyplot as plt
import numpy as np

# 图表1：在家做饭的频率 - 条形图 + 渐变色
labels = ["工作日天天回家做饭", "每周在家做饭不超过3天", "一次都难以保证"]
values = [38, 37, 5]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(np.arange(len(labels)), values, height=0.6,
               color=["limegreen", "mediumseagreen", "turquoise"],
               edgecolor='black')

# 添加数值标注
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f"{values[i]}%", va='center', fontsize=12, color='black')

# 设置y轴
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels, fontsize=12)
ax.invert_yaxis()  # 最高值在上

# 图表标题与来源
ax.set_title("在家做饭的频率", fontsize=14, fontweight='bold')
plt.text(0, -0.8, "数据来源：CBNData", fontsize=10)

# 去除多余线条
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

fig.tight_layout()
plt.show()