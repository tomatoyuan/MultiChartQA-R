import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# 数据
labels = ['补充微量元素', '含有膳食纤维', '含有益生菌', '含有DHA', '补充维生素']
values = [70, 56, 46, 41, 23]
x = np.arange(len(labels))

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 自定义渐变色列表（从深到浅）
gradient_colors = [
    ('#00d2c8', '#a2f0ec'),
    ('#00c0d6', '#a3e8f5'),
    ('#00a6de', '#a4dbf7'),
    ('#0091e6', '#a5cef9'),
    ('#0077ed', '#a7c2fb')
]

# 绘制每根渐变柱
bar_width = 0.6
for i, (val, (color_top, color_bottom)) in enumerate(zip(values, gradient_colors)):
    # 自定义渐变色柱子（矩形叠加方式模拟）
    for j in range(100):  # 100段模拟渐变
        fraction = j / 100
        height = val * (1 / 100)
        y = height * j
        color = LinearSegmentedColormap.from_list("grad", [color_bottom, color_top])(fraction)
        ax.add_patch(Rectangle((x[i] - bar_width / 2, y), bar_width, height, color=color, linewidth=0))

    # 添加柱顶百分比文字
    ax.text(x[i], val + 1.5, f'{val}%', ha='center', fontsize=10)

# 设置标签
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylim(0, 80)
ax.set_ylabel('占比（%）', fontsize=12)
ax.set_title('中国家长对具有功效性有益成分的关注度', fontsize=14, fontweight='bold', pad=20)

# 图例
ax.legend(['占比（%）'], loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# 美化
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()