import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2010, 2021)
# 万元以上设备总价值（万元），数据大体一致即可
values = [61623, 73154, 120292, 155770, 164474, 240805, 318904, 468174, 642335, 748276, 746559]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(years, values, color='#A4C639', width=0.6)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# 添加说明文本框
text_str = "康复医院万元以上设备总价值逐年提升，康复医疗器城市市场总体发展向好。"
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.09, 0.85, text_str, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# 设置坐标轴与标题
ax.set_xlabel('年份')
ax.set_ylabel('万元以上设备总价值（万元）')
ax.set_title('2010-2020年中国康复医院万元以上设备总价值', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()