import matplotlib.pyplot as plt
import numpy as np

# 数据准备
years = ["2019", "2020", "2021", "2022", "2023E", "2024E"]
market_size = [1945.3, 2283.0, 2793.7, 3387.1, 4020.8, 4744.5]  # 市场规模（亿元）
growth_rates = [17.4, 22.4, 21.2, 18.7, 18.0]  # 同比增长率（%），2019年无前期数据，从2020开始计算增长率逻辑（实际按图中展示）

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 7))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='coral', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长率折线图
ax2 = ax1.twinx()
ax2.plot(x[1:], growth_rates, marker='o', color='gold', label='同比增长率（%）', linewidth=2)  # 2019年对应增长率是2020的17.4%，从2020开始关联年份
ax2.set_ylabel('同比增长率（%）')
ax2.legend(loc='upper right')

# 手动调整增长率折线的标注位置（匹配原图逻辑，2019年的17.4%对应2020的柱子上方 ）
rate_labels = [17.4, 22.4, 21.2, 18.7, 18.0]
for i, rate in enumerate(rate_labels):
    if i == 0:
        ax2.text(x[1], rate, f'{rate}%', ha='center', va='bottom', color='black')  # 2019的增长率标在2020柱子上方
    else:
        ax2.text(x[i], rate, f'{rate}%', ha='center', va='bottom', color='black')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom', color='black')

ax1.set_title('2019-2024年中国功能型瘦身食品市场规模及预测')
plt.tight_layout()
plt.show()