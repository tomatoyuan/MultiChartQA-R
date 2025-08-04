import matplotlib.pyplot as plt
import numpy as np

# 数据准备
years = ["2018年", "2019年", "2020年", "2021年", "2022年"]
national_income = [28228, 30733, 32189, 35128, 36883]  # 全国居民人均可支配收入（元）
urban_income = [39251, 42359, 43834, 47412, 49283]    # 城镇居民人均可支配收入（元）
growth_rates = [8.7, 8.9, 4.7, 9.1, 5.0]              # 居民可支配收入同比增长率（%）

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制全国、城镇居民人均可支配收入柱状图
ax1.bar(x - 0.2, national_income, width=0.4, color='lightcoral', label='全国居民人均可支配收入（元）')
ax1.bar(x + 0.2, urban_income, width=0.4, color='coral', label='城镇居民人均可支配收入（元）')
ax1.set_ylabel('收入（元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长率折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rates, marker='o', color='gray', label='同比增长率（%）', linewidth=2)
ax2.set_ylabel('同比增长率（%）')
ax2.legend(loc='upper right')

# 添加全国、城镇居民收入数值标注
for i, (national, urban) in enumerate(zip(national_income, urban_income)):
    ax1.text(i - 0.2, national + 500, f'{national}', ha='center', va='bottom', color='black')
    ax1.text(i + 0.2, urban + 500, f'{urban}', ha='center', va='bottom', color='black')

# 添加同比增长率数值标注
for i, rate in enumerate(growth_rates):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom', color='black')

ax1.set_title('2018-2022年中国居民人均可支配收入')
plt.tight_layout()
plt.show()