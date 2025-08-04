import matplotlib.pyplot as plt
import numpy as np

# --------------------- 高考报名人数及增长率图表数据 ---------------------
years_gaokao = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
enroll_gaokao = [940, 940, 975, 1031, 1071, 1078, 1193]
growth_gaokao = [np.nan, 0.0, 3.7, 5.7, 3.9, 0.7, 10.7]  # 2016年无增长率（作为起始年）

# --------------------- 高等学校规模及增长率图表数据 ---------------------
years_school = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
scale_school = [2879, 2914, 2914, 2956, 3005, 3012, 3013, 3072]
growth_school = [np.nan, 1.2, 0.0, 1.4, 1.7, 0.2, 0.0, 0.0]  # 2016年无增长率（作为起始年）

# 创建画布，一行两列布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --------------------- 绘制高考报名人数及增长率图表（左图） ---------------------
ax1.bar(years_gaokao, enroll_gaokao, color='orange', label='报名人数（万人）')
ax1.set_ylabel('报名人数（万人）')
ax1.set_xlabel('年份')
ax1.set_title('2016-2022年中国高考报名人数及增长率')
ax1.legend(loc='upper left')

# 绘制增长率折线图（双轴）
ax1_2 = ax1.twinx()
ax1_2.plot(years_gaokao, growth_gaokao, marker='o', color='gold', label='增长率（%）', linewidth=2)
ax1_2.set_ylabel('增长率（%）')
ax1_2.legend(loc='upper right')

# 添加高考报名人数数值标注
for i, num in enumerate(enroll_gaokao):
    ax1.text(i, num + 10, f'{num}', ha='center', va='bottom')

# 添加高考增长率数值标注（2016年无，从2017开始）
for i, rate in enumerate(growth_gaokao[1:], start=1):
    ax1_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

# --------------------- 绘制高等学校规模及增长率图表（右图） ---------------------
ax2.bar(years_school, scale_school, color='orange', label='高等学校规模（所）')
ax2.set_ylabel('高等学校规模（所）')
ax2.set_xlabel('年份')
ax2.set_title('2016-2023年中国高等学校规模及增长率')
ax2.legend(loc='upper left')

# 绘制增长率折线图（双轴）
ax2_2 = ax2.twinx()
ax2_2.plot(years_school, growth_school, marker='o', color='gold', label='增长率（%）', linewidth=2)
ax2_2.set_ylabel('增长率（%）')
ax2_2.legend(loc='upper right')

# 添加高等学校规模数值标注
for i, num in enumerate(scale_school):
    ax2.text(i, num + 10, f'{num}', ha='center', va='bottom')

# 添加高等学校增长率数值标注（2016年无，从2017开始）
for i, rate in enumerate(growth_school[1:], start=1):
    ax2_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()