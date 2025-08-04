import matplotlib.pyplot as plt
import numpy as np

# 产品类型
labels = ["硬装配家居产品", "软装配家居产品", "未购买且不了解"]
# 对应比例(%)
proportions = [72.34, 67.53, 6.23]

# 雷达图角度设置
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 闭合雷达图
proportions_full = proportions + proportions[:1]
angles_full = angles + angles[:1]

# 创建图表，增加尺寸
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# 绘制雷达图
ax.fill(angles_full, proportions_full, color='orange', alpha=0.25)
ax.plot(angles_full, proportions_full, color='orange', linewidth=2)

# 添加数值标签，优化位置计算
for i in range(num_vars):
    angle = angles[i]
    value = proportions[i]
    
    # 根据角度调整标签位置，避免遮挡
    if angle == 0:
        ha = 'center'
        va = 'bottom'
        offset = 5
    elif angle == np.pi/2:
        ha = 'left'
        va = 'center'
        offset = 5
    elif angle == np.pi:
        ha = 'center'
        va = 'top'
        offset = -5
    elif angle == 3*np.pi/2:
        ha = 'right'
        va = 'center'
        offset = -5
    elif 0 < angle < np.pi/2:
        ha = 'left'
        va = 'bottom'
        offset = 5
    elif np.pi/2 < angle < np.pi:
        ha = 'left'
        va = 'top'
        offset = 5
    elif np.pi < angle < 3*np.pi/2:
        ha = 'right'
        va = 'top'
        offset = -5
    else:
        ha = 'right'
        va = 'bottom'
        offset = -5
    
    # 添加标签，使用计算的位置参数
    ax.text(angle, value + offset, f'{value}%', ha=ha, va=va, fontsize=12)

# 设置坐标轴范围和刻度，避免数据被遮挡
ax.set_ylim(0, 85)
ax.set_yticks(np.arange(0, 85, 15))  # 调整刻度间隔
ax.set_yticklabels([])  # 隐藏默认刻度标签

# 设置坐标轴标签
ax.set_xticks(angles)
ax.set_xticklabels(labels, fontsize=12)

# 设置标题
ax.set_title('2025年中国消费者购买或了解的家居产品类型', fontsize=16, pad=20)

# 添加图例和网格线
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()