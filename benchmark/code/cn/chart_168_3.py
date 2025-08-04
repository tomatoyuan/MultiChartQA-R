import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 数据
channels = ['线上电商渠道', '大卖场、传统商超', '社区团购', '杂货店、便利店', '仓储式会员店', '高端超市']
values = [80.5, 63.5, 39.9, 31.2, 20.8, 16.7]

# 颜色渐变（从浅棕到深棕）
colors = plt.cm.PuBu(np.linspace(0.4, 0.9, len(channels)))

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(channels, values, color=colors)

# 设置边框区域，稍微离柱子远一点
ax.add_patch(patches.Rectangle(
    (-5, -0.5),  # 左侧偏移
    100,          # 宽度覆盖最多的值+偏移
    1,         # 高度略大于单行
    linewidth=2,
    edgecolor='saddlebrown',
    facecolor='none',
    linestyle='dotted'
))

# 数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
            f'{width:.1f}%', va='center', fontsize=10, color='black')

# 样式设置
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel('占比 (%)', fontsize=12)
ax.set_title('消费者购买生活用纸的渠道分布', fontsize=14, pad=15)

# 数据来源
plt.figtext(0.5, -0.05, '数据来源：CBNData 2024年3月中国消费者生活用纸趋势的调研\n数据说明：请问您购买生活用纸的渠道有哪些？ N=1000',
            ha='center', fontsize=9)

plt.tight_layout()
plt.show()