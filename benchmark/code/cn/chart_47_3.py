import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2022, 2023, 2024]
# 成交金额（亿元）
amounts = [2763, 2818, 2959]

x = np.arange(len(years))
width = 0.5

fig, ax = plt.subplots(figsize=(10, 6))
rects = ax.bar(x, amounts, width, label='成交金额', color='#D9B3A6')

# 标注成交金额
for rect, amount in zip(rects, amounts):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height + 5,
            f'{amount}', ha='center', va='bottom')

# 设置Y轴范围以放大高度差距
ax.set_ylim(2700, 3000)

ax.set_ylabel('单位：亿元')
ax.set_title('2022-2024护肤品零售额规模趋势')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()