import matplotlib.pyplot as plt

# 数据
years = ['2019', '2020', '2021', '2022', '2023']
market_size = [1199, 1221, 1404, 1415, 1549]
growth_rate = [3, 2, 15, 1, 9]

# 创建图表和双坐标轴
fig, ax1 = plt.subplots(figsize=(10, 6))

# 设置主轴（左轴）- 柱状图
bars = ax1.bar(years, market_size, color='red', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）', fontsize=12, color='red')
ax1.tick_params(axis='y', labelcolor='#000000')

# 添加柱状图数据标签
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}', ha='center', va='bottom', fontsize=11, color='red')

# 创建次轴（右轴）- 折线图
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='#F6A700', marker='o', linewidth=2.5, label='同比增长率')
ax2.set_ylabel('同比增长率（%）', fontsize=14, color='#F6A700')
ax2.tick_params(axis='y', labelcolor='#000000')

# 添加折线图数据标签
for i, txt in enumerate(growth_rate):
    ax2.text(years[i], growth_rate[i] + 0.5, f'{txt}%', ha='center', va='bottom', fontsize=11, color='#F6A700')

# 添加标题和图例
plt.title('中国生活用纸市场规模趋势', fontsize=14, pad=20)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)
plt.text(0.5, -0.1, '数据来源：中国造纸协会', fontsize=10, ha='center', transform=ax1.transAxes)

plt.tight_layout()
plt.show()