import matplotlib.pyplot as plt
import numpy as np

# 数据
years = [f"{y}年1月" for y in range(2014, 2025)]
users = [1869, 2094, 2320, 2804, 3212, 3478, 3726, 4214, 4632, 4770, 5036]
growth = [12.0, 10.8, 20.9, 14.5, 8.3, 7.1, 13.1, 9.9, 3.0, 5.6]

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# 绘制柱状图
bars = ax.bar(years, users, color='#419D83', width=0.6)

# 添加柱顶用户数标签
for bar, value in zip(bars, users):
    ax.text(bar.get_x() + bar.get_width()/2, value + 100,
            f"{value:,}", ha='center', va='bottom', color='white', fontsize=11)

# 添加增长率标签（白底圆框模拟）
for i, (bar, pct) in enumerate(zip(bars[1:], growth)):
    # x = bar.get_x() + bar.get_width() / 2
    x = bar.get_x() - bar.get_width() / 3
    y = 200  # 设置在下方但不压缩主图
    ax.text(x, y, f"+{pct:.1f}%", ha='center', va='center',
            fontsize=10, color='black',
            bbox=dict(boxstyle="circle,pad=0.3", facecolor='white', edgecolor='none'))

# 坐标轴美化
ax.set_ylim(0, 5500)
ax.set_xlim(-0.5, len(years)-0.5)
ax.set_yticks([])
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, color='white', fontsize=11)
ax.spines[['left', 'top', 'right']].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.tick_params(axis='x', colors='white')

# 左上角主标题框
plt.text(-0.5, 5300, "2024年1月", fontsize=12, color='white',
         bbox=dict(facecolor='#1E6E57', boxstyle="round,pad=0.4"))
plt.title("历年社交媒体用户数", fontsize=16, color='white', loc='left', pad=20)

# 数据来源
plt.text(-0.5, -600, "*数据来源：We Are Social", color='white', fontsize=10)

plt.tight_layout()
plt.show()