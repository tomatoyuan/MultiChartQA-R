import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 餐饮收入（万亿元）
catering_revenue = [3.96, 4.27, 4.67, 3.95, 4.69, 4.39, 5.29]
# 餐饮收入同比变动（%）
catering_yoy = [10.7, 7.8, 9.4, -15.4, 18.6, -6.3, 20.9]
# 限额以上餐饮收入同比变动（%）
above_limit_yoy = [7.4, 6.4, 7.1, -14.0, 23.5, -5.9, 20.4]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制餐饮收入柱状图
ax1.bar(x, catering_revenue, color='orange', label='餐饮收入（万亿元）')
ax1.set_ylabel('餐饮收入（万亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比变化折线图
ax2 = ax1.twinx()
ax2.plot(x, catering_yoy, marker='o', color='brown', label='餐饮收入同比变动（%）')
ax2.plot(x, above_limit_yoy, marker='o', color='blue', label='限额以上餐饮收入同比变动（%）')
ax2.set_ylabel('同比变动（%）')
ax2.legend(loc='upper right')

# 添加餐饮收入数值标注
for i, rev in enumerate(catering_revenue):
    ax1.text(i, rev + 0.1, f'{rev}', ha='center', va='bottom')

# 添加餐饮收入同比变动数值标注
for i, yoy in enumerate(catering_yoy):
    ax2.text(i, yoy + 1, f'{yoy}%', ha='center', va='bottom')

# 添加限额以上餐饮收入同比变动数值标注
for i, above_yoy in enumerate(above_limit_yoy):
    ax2.text(i, above_yoy + 1, f'{above_yoy}%', ha='center', va='bottom')

ax1.set_title('2017-2023年中国餐饮收入及同比变化')

plt.tight_layout()
plt.show()