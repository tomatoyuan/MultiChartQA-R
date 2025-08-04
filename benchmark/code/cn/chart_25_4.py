import matplotlib.pyplot as plt
import numpy as np

# 数据与标签
labels = ["手机", "网游", "抢红包", "恐归", "其他"]
values = [0.6, 0.4, 0.3, 0.2, 0.1]  # 模拟占比，可根据实际调整
colors = ["#F5A623"] * len(labels)  # 温度计主体颜色

# 创建画布
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#D52B1E")  # 红色背景

# 绘制水平条形图（模拟温度计）
y_pos = np.arange(len(labels))
bars = ax.barh(
    y_pos,
    values,
    color=colors,
    edgecolor="white",
    height=0.6,
    left=0.2  # 预留空白模拟温度计“玻璃管”
)

# 模拟温度计白色刻度线（叠加空白条形）
ax.barh(
    y_pos,
    [1 - v for v in values],
    color="white",
    edgecolor="white",
    height=0.6,
    left=0.2 + np.array(values)
)

# 添加数值标签
for i, (value, label) in enumerate(zip(values, labels)):
    # 计算标签位置（条形图中间）
    x_pos = 0.2 + value / 2
    ax.text(
        x_pos, i, 
        f"{value:.1f}", 
        ha='center', va='center',
        color='white', fontsize=12,
        fontweight='bold'
    )

# 美化设置
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12, color="gold")  # 金色文字
ax.set_xticks([])  # 隐藏x轴刻度
ax.spines[:].set_visible(False)  # 隐藏边框

# 添加标题与标语
ax.text(
    0.5, 1.1, 
    '手机成为“谋杀”春节仪式感的最大凶手', 
    ha='center', va='top', 
    fontsize=14, color='gold', 
    transform=ax.transAxes
)
ax.text(
    0.5, -0.15, 
    '放下手机陪陪家人。', 
    ha='center', va='bottom', 
    fontsize=12, color='white', 
    transform=ax.transAxes
)

plt.tight_layout()
plt.show()