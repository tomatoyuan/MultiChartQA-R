import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# 数据
labels = ['05后', '00后', '95后', '90后', '85后', '80后', '80前']
values = [105, 73, 115, 115, 110, 80, 80]

# 颜色设置：浅粉 -> 深粉 渐变
cmap = mcolors.LinearSegmentedColormap.from_list("pink_gradient", ["#fddde6", "#ec6fa8"])
colors = [cmap(i / (len(values) - 1)) for i in range(len(values))]

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# 辅助线和标注
ax.axhline(100, color='deeppink', linestyle='--', linewidth=1.5)
for bar, val in zip(bars, values):
    va = 'bottom' if val >= 100 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2, val + (2 if val >= 100 else -5), f'{val}',
            ha='center', va=va, fontsize=12, color='black')

# 标题和说明
ax.set_title('不同代际女性对口腔健康关注度调研', fontsize=14)
ax.set_ylabel('TGI')
ax.set_ylim(50, 130)
ax.text(-0.5, 110, '高关注\nTGI>100', color='deeppink', fontsize=10)
ax.text(-0.5, 90, '低关注\nTGI<100', color='deeppink', fontsize=10)

plt.tight_layout()
plt.show()