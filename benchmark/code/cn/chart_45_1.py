import matplotlib.pyplot as plt

# 数据
years = [2023, 2024, 2029]
market_size = [3500, 3700, 3850]  # 2023、2024 数据为近似，2029E 为示例值，可根据实际精准数据替换

# 创建图表
fig, ax = plt.subplots()

# 使用索引作为x位置，使条形均匀分布
x_pos = range(len(years))
bars = ax.bar(x_pos, market_size, color='pink')

# 添加标题和标签
ax.set_title('全球功能性服饰市场规模')
ax.set_ylabel('(亿美元)')
ax.text(0.5, 1.05, '年复合增长率=6.1%\n*2024 - 2029年', ha='center', va='bottom', transform=ax.transAxes)

# 设置x轴标签（用省略号表示中间年份，2029年添加E标记）
ax.set_xticks(x_pos)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# 在每个柱子上方添加数值标注
for i, (x, value) in enumerate(zip(x_pos, market_size)):
    ax.text(x, value + 5, f'{value}', ha='center', va='bottom')

# 设置y轴刻度
ax.set_ylim([3300, 3900])
ax.set_yticks(range(3300, 3901, 100))

# 显示图表
plt.show()