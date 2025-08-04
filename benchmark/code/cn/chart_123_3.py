import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025E", "2026E", "2027E"]
# 市场规模（亿元）
market_size = [3013, 4597, 5980, 6680, 10036, 11161, 15254, 16357, 17469, 18503, 19567]
# 同比增长（%）
yoy_growth = [52.6, 30.1, 16.9, 11.7, 50.2, 11.2, 36.7, 7.2, 6.8, 5.9, 5.8]
# 在线餐饮外卖行业渗透率（%）
penetration_rate = [7.6, 10.9, 12.8, 11.7, 21.4, 25.4, 28.8, 28.0, 28.0, 28.0, 28.0]  # 渗透率部分年份需按图确认，这里假设2023后保持28.0，可根据实际调整

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='orange', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长和渗透率折线图
ax2 = ax1.twinx()
ax2.plot(x, yoy_growth, marker='o', color='brown', label='同比增长（%）')
ax2.plot(x, penetration_rate, marker='o', color='blue', label='在线餐饮外卖行业渗透率（%）')
ax2.set_ylabel('比例（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 200, f'{size}', ha='center', va='bottom')

# 添加同比增长数值标注
for i, growth in enumerate(yoy_growth):
    ax2.text(i, growth + 1, f'{growth}%', ha='center', va='bottom')

# 添加渗透率数值标注
for i, rate in enumerate(penetration_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2017-2027年中国在线餐饮外卖市场规模及渗透率')

plt.tight_layout()
plt.show()