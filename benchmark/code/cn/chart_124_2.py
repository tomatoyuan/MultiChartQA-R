import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2019", "2020", "2021", "2022", "2023", "2024Q1-Q3"]
# 总营业收入（亿元）
total_revenue = [86624, 98514, 119064, 121805, 129515, 99668]
# 新业态营业收入（亿元）
new_format_revenue = [19868, 31425, 39623, 43860, 52395, 41616]
# 所占比重（%）
proportion = [22.9, 31.9, 33.3, 36.0, 40.5, 41.8]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制总营业收入柱状图
ax1.bar(x, total_revenue, color='lightcoral', label='总营业收入（亿元）', width=0.3)
# 绘制新业态营业收入柱状图（右移避免重叠）
ax1.bar(x + 0.3, new_format_revenue, color='coral', label='新业态营业收入（亿元）', width=0.3)
ax1.set_ylabel('营业收入（亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x + 0.15)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制所占比重折线图
ax2 = ax1.twinx()
ax2.plot(x, proportion, marker='o', color='gold', label='所占比重（%）')
ax2.set_ylabel('所占比重（%）')
ax2.legend(loc='upper right')

# 添加总营业收入数值标注
for i, rev in enumerate(total_revenue):
    ax1.text(i, rev + 1000, f'{rev}', ha='center', va='bottom')

# 添加新业态营业收入数值标注
for i, new_rev in enumerate(new_format_revenue):
    ax1.text(i + 0.3, new_rev + 1000, f'{new_rev}', ha='center', va='bottom')

# 添加所占比重数值标注
for i, prop in enumerate(proportion):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')

ax1.set_title('2019-2024年中国文化新业态营业收入情况')

plt.tight_layout()
plt.show()