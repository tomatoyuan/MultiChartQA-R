import matplotlib.pyplot as plt

# 数据
years = [2023, 2024, 2029]
market_size = [9000, 9500, 15000]  # 2023、2024 数据为近似，2029E 为示例值，可根据实际精准数据替换 
# 若有精准的 2023、2024 市场规模数据，直接替换列表中对应数值即可

# 创建图表
fig, ax = plt.subplots()

# 使用索引作为 x 位置，使条形均匀分布
x_pos = range(len(years))
bars = ax.bar(x_pos, market_size, color='pink')  # 将条形对象保存到变量中

# 添加标题和标签
ax.set_title('中国功能性服饰市场规模')
ax.set_ylabel('(亿元)')
ax.text(0.5, 1.05, '年复合增长率=9.8%\n*2024-2029年', ha='center', va='bottom', transform=ax.transAxes)

# 设置 x 轴标签（用省略号表示中间年份，2029 年添加 E 标记）
ax.set_xticks(x_pos)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# 设置 y 轴刻度，根据数据范围调整
ax.set_ylim([0, 16000])  # 适当扩大上限，避免数值标注超出图表范围
ax.set_yticks(range(0, 16001, 5000))  

# 在每个条形上方添加数据标注
for bar in bars:
    height = bar.get_height()  # 获取条形高度（即数值）
    # 在条形正上方居中位置添加文本
    ax.text(bar.get_x() + bar.get_width()/2., height + 200,  # 200 为与条形的间距
            f'{height}',  # 显示数值
            ha='center', va='bottom')  # 水平居中，垂直靠下

# 显示图表
plt.show()