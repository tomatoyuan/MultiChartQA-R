import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["婴幼儿奶粉", "大包粉", "稀奶油", "奶酪类", "乳清类", "奶油类", "蛋白类", "包装牛奶", "酸奶", "炼乳"]
import_value = [42.1, 29.2, 10.3, 9.7, 8.6, 8.3, 6.1, 5.6, 0.5, 0.4]
growth_rate = [-5.0, -34.0, 7.4, 25.9, -10.6, -11.3, -10.5, -16.2, -0.7, -18.7]

x = np.arange(len(categories))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制进口额柱状图
ax1.bar(x, import_value, color='orange', label='进口额（亿美元）')
ax1.set_ylabel('进口额（亿美元）')
ax1.set_xlabel('乳品类型')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=45, ha='right')
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='同比增长（%）', linewidth=2)
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加进口额数值标注
for i, val in enumerate(import_value):
    ax1.text(i, val + 1, f'{val}', ha='center', va='bottom')

# 添加同比增长数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2023年中国主要乳品进口额及同比增长')

plt.tight_layout()
plt.show()