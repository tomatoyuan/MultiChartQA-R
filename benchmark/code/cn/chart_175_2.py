import matplotlib.pyplot as plt

# 数据
labels = [
    '市场扩张和增长机会',
    '服务客户',
    '转型升级与创新',
    '推进可持续发展',
    '供应链',
    '技术、人才资源',
    '市场需求变化',
    '政策影响',
    '其他'
]
values = [55, 19, 7, 6, 4, 3, 3, 2, 1]
colors = ['orange', 'orange'] + ['#0070C0'] * 7  # 前两个橙色，后续蓝色

# 图表主体
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=colors[::-1])

# 添加百分比标签
for bar in bars:
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():.0f}%', va='center', fontsize=11)

# 设置轴标签和标题
ax.set_xlim(0, 60)
ax.set_xlabel('占比（%）', fontsize=12)
ax.set_title('当前阶段中国企业出海核心驱动因素', fontsize=14, pad=15)

# 去除图边线
ax.spines[['top', 'right']].set_visible(False)

# 添加图示说明和数据来源
plt.figtext(0.01, -0.04, '图示：当前阶段中国企业出海核心驱动因素',
            fontsize=10, ha='left')
plt.figtext(0.01, -0.08, '数据来源：德勤，36氪研究院整理',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()