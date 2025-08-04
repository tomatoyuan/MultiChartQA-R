import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
# 市场规模（万亿元）
market_size = [22.6, 27.2, 31.3, 35.8, 39.2, 45.5, 50.2, 56.1, 63.2, 70.8]
# 同比增长（%）
yoy_growth = [20.4, 21.4, 15.1, 14.4, 9.5, 16.1, 10.3, 11.7, 12.7, 12.1]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制市场规模柱状图（模拟图标样式，用自定义符号近似）
for i in range(len(years)):
    # 绘制代表市场规模的“¥”符号柱状图（简化为橙色矩形 + 文本符号）
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, market_size[i], color='orange')
    ax1.add_patch(rect)
    ax1.text(x[i], market_size[i] + 1, f'¥{market_size[i]}', ha='center', va='bottom')

ax1.set_ylabel('市场规模（万亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylim(0, max(market_size) + 5)  # 预留空间显示标注
ax1.legend(['市场规模（万亿元）'], loc='upper left')

# 创建双轴，绘制同比增长折线图
ax2 = ax1.twinx()
ax2.plot(x, yoy_growth, marker='o', color='gold', label='同比增长（%）')
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加同比增长数值标注
for i, growth in enumerate(yoy_growth):
    ax2.text(i, growth + 0.5, f'{growth}%', ha='center', va='bottom')

ax1.set_title('2016-2025年中国数字经济总体规模及预测')

plt.tight_layout()
plt.show()