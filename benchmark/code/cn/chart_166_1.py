import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['护肤', '彩妆', '个护', '香水']
market_scale = [4823.5, 1700.9, 1193.5, 254]
growth_rate = [0.1, 13.5, 15.8, 11.4]

x = np.arange(len(categories))
width = 0.4

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图：市场规模
bars = ax1.bar(x, market_scale, width, color='#FFB6C1', label='市场规模（亿元）')
ax1.set_ylabel('市场规模（亿元）')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)
ax1.bar_label(bars, fmt='%.1f', label_type='edge', fontsize=10, color='crimson')

# 折线图：同比增长率
ax2 = ax1.twinx()
line = ax2.plot(x, growth_rate, color='gray', marker='o', label='市场规模同比', linewidth=2)
ax2.set_ylabel('同比增长率（%）')
for i, val in enumerate(growth_rate):
    ax2.text(x[i], val + 0.8, f'{val:.1f}%', ha='center', fontsize=10, weight='bold')

# 设置标题并增加间距防止重叠
plt.title('2023年各一级品类市场规模', fontsize=14, pad=20)

# 合并图例
handles = list(bars)[:1] + line  # 只取一个 bar 作为代表 + 折线
labels = ['市场规模（亿元）', '市场规模同比']
ax1.legend(handles, labels, loc='upper right', fontsize=10)

# 添加数据来源
plt.figtext(0.01, -0.05, '数据来源：CBNData', fontsize=10, ha='left')

plt.tight_layout()
plt.show()