import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2022", "2023", "2024", "2025E", "2026E", "2027E", "2028E"]
# 市场规模（亿元）
market_size = [11.5, 79.3, 471.7, 805.8, 1665.3, 2317.6, 2767.4]
# 增长率（%）
growth_rate = [589.6, 494.8, 70.8, 106.7, 39.2, 19.4]  # 注意：2022-2023的增长率对应前一年到后一年，这里按图中折线点整理，需确认对应关系

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制市场规模柱状图
ax1.bar(x, market_size, color='coral', label='规模（亿元）')
ax1.set_ylabel('规模（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制增长率折线图（注意：增长率数据点与年份的对应，可能需要调整索引）
ax2 = ax1.twinx()
# 增长率数据对应 2023-2028E 的变化，所以 x 轴索引从 1 开始
ax2.plot(x[1:], growth_rate, marker='o', color='gold', label='增长率（%）')
ax2.set_ylabel('增长率（%）')
ax2.legend(loc='upper right')

# 添加市场规模数值标注
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# 添加增长率数值标注（对应折线点）
for i, rate in enumerate(growth_rate):
    # 增长率对应年份索引是 i + 1（从 2023 开始）
    ax2.text(x[i + 1], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2022-2028年中国AIGC核心市场规模及预测')

plt.tight_layout()
plt.show()