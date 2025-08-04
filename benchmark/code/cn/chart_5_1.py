import matplotlib.pyplot as plt

# 数据
sizes = [8.24, 91.66]

# 颜色，更接近原图
computer_colors = ["#1976d2", "#e3f2fd"]  # 计算机端颜色：深蓝色和浅蓝色
mobile_colors = ["#f57c00", "#ffebee"]    # 移动端颜色：橙色和浅橙色

# 创建画布和两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(top=0.85, bottom=0.15)  # 调整顶部和底部边距

# 绘制计算机端检索占比图（标签颜色调整）
wedges1, texts1, autotexts1 = ax1.pie(
    [sizes[0], 100 - sizes[0]],
    labels=["计算机端", ""],  # 简化标签
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=computer_colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# 绘制移动端检索占比图（标签颜色调整）
wedges2, texts2, autotexts2 = ax2.pie(
    [sizes[1], 100 - sizes[1]],
    labels=["移动端", ""],  # 简化标签
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=mobile_colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# 设置标签颜色（与对应饼图颜色一致）
for text in texts1:
    text.set_color(computer_colors[0])  # 计算机端标签颜色为深蓝色
for text in texts2:
    text.set_color(mobile_colors[0])    # 移动端标签颜色为深橙色

# 设置百分比文本颜色为黑色
for text in autotexts1 + autotexts2:
    text.set_color('black')
    text.set_fontsize(14)

# 去除坐标轴，使图表为正圆形
ax1.axis('equal')
ax2.axis('equal')

# 设置小标题（在图表下方）
ax1.text(0.5, -0.1, "计算机端检索占比", 
         ha='center', va='center', transform=ax1.transAxes, fontsize=14)
ax2.text(0.5, -0.1, "移动端检索占比", 
         ha='center', va='center', transform=ax2.transAxes, fontsize=14)

# 设置总标题
fig.suptitle("2月奶粉行业检索设备分布", fontsize=16, fontweight='bold')

plt.tight_layout()  # 调整布局，避免重叠
plt.show()