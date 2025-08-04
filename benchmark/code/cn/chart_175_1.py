import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据
labels = [
    '非常有信心，期待快速发展',
    '较有信心，期待稳中有升',
    '与2022年持平',
    '较没有信心，需要时间恢复'
]
values = [44.4, 43.2, 7.4, 4.9]
colors = ['#0070C0'] * 4

# 画图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=colors)

# 添加标签
for bar in bars:
    ax.text(
        bar.get_width() + 1,
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width():.1f}%',
        va='center',
        fontsize=12
    )

# 添加红色虚线框（框住前两项）
# 坐标从底部算起，两个 bar 的总高度为 2 个 bar 的高度 + 间距
y_top = bars[3].get_y() + bars[3].get_height() + 0.1
y_bottom = bars[2].get_y() - 0.1
rect = patches.Rectangle(
    (0, y_bottom), 50, y_top - y_bottom,
    linewidth=2, edgecolor='red', linestyle='--', facecolor='none'
)
ax.add_patch(rect)

# 添加“积极心态”标注
ax.text(
    52, y_bottom + (y_top - y_bottom)/2,
    '积极心态87.6%',
    color='red', fontsize=14, va='center'
)

# 美化
ax.set_xlim(0, 60)
ax.set_xlabel('比例（%）')
ax.set_title('2023年中国企业出海信心', fontsize=16)
plt.tight_layout()
plt.show()