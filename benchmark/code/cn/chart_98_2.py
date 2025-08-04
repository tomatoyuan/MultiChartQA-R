import matplotlib.pyplot as plt

# 年份与占比数据
years = ["2020年", "2021年"]
percentages = [10, 13]
# 自由配色（可调整）
colors = ["#A4C639", "#87CEEB"]

# 创建画布（双行布局）
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))  # 增大画布尺寸

# 设置整体标题
fig.suptitle("两轮锂电车线上交易占比", fontsize=16, fontweight="bold", y=0.95)

# 绘制2020年饼图
wedges, texts, autotexts = ax1.pie(
    [percentages[0], 100-percentages[0]],  # 显示占比部分和剩余部分
    labels=[years[0], ""],  # 主标签显示年份
    colors=[colors[0], 'lightgray'],  # 占比部分使用主色，剩余部分使用浅灰色
    autopct=lambda p: f'≈{p:.0f}%' if p >= percentages[0] else '',  # 仅在占比部分显示百分比
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}  # 添加白色边框分隔
)
ax1.set_title(f"{years[0]}市场份额: {percentages[0]}%", fontsize=14, pad=10)  # 明确标注年份和占比
ax1.set_aspect('equal')  # 确保圆形

# 绘制2021年饼图
wedges, texts, autotexts = ax2.pie(
    [percentages[1], 100-percentages[1]],
    labels=[years[1], ""],
    colors=[colors[1], 'lightgray'],
    autopct=lambda p: f'≈{p:.0f}%' if p >= percentages[1] else '',
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)
ax2.set_title(f"{years[1]}市场份额: {percentages[1]}%", fontsize=14, pad=10)
ax2.set_aspect('equal')

# 隐藏边框
for ax in [ax1, ax2]:
    ax.axis('off')  # 完全隐藏坐标轴

# 调整子图间距
plt.subplots_adjust(hspace=0.3)

plt.show()