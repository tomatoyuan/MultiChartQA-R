import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = [
    '上涨1%-20%', '上涨21%-40%', '上涨41%-60%', '上涨61%-80%',
    '上涨81%-100%', '上涨100%以上', '基本维持不变', '下降1%-20%',
    '下降21%-100%的四个区间', '由集团总部进行布局投入'
]
percentages = [20.3, 36.6, 10.6, 6.5, 6.5, 2.4, 8.1, 4.1, 0, 4.9]

# 颜色配置（贴近原图，下降类用灰色，其他用绿色）
colors = ['#a5d65d'] * 7 + ['#d3d3d3'] + ['#a5d65d'] * 2

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向条形图
y = np.arange(len(labels))
bars = ax.barh(y, percentages, color=colors, height=0.6)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', fontsize=9, color='#333')

# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# 隐藏x轴刻度
ax.set_xticks([])

# 隐藏顶部、右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 添加标题
ax.set_title('2022年中国商户私域布局成本较布局之初的涨幅/降幅情况',
             fontsize=14, fontweight='bold', pad=20)

# 调整布局
plt.tight_layout()
plt.show()