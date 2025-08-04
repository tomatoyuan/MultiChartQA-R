import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
average_wage = [4.8, 4.9, 5.3, 6.3, 7.1, 9.1, 9.6, 11.1, 11.8]
growth_rate = [23.1, 2.1, 8.2, 18.9, 12.7, 28.2, 5.5, 15.6, 6.3]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制平均工资柱状图
ax1.bar(x, average_wage, color='orange', label='平均工资（千元）')
ax1.set_ylabel('平均工资（千元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='增长率（%）', linewidth=2)
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加平均工资数值标注
for i, wage in enumerate(average_wage):
    ax1.text(i, wage + 0.3, f'{wage}', ha='center', va='bottom')

# 添加增长率数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2015-2023年家政服务业薪资及其增长率')

plt.tight_layout()
plt.show()