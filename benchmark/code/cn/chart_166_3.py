import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2021年', '2022年', '2023年']
total = [6, 42, 69]
local = [4, 25, 52]

bar_width = 0.4
y_pos = np.arange(len(years))

# 颜色
total_color = '#FFDDDD'
local_color = '#E0E0E0'

# 创建图表
fig, ax = plt.subplots(figsize=(8, 5))

bars1 = ax.barh(y_pos, total, height=bar_width, color=total_color, label='新原料备案数（个）')
bars2 = ax.barh(y_pos, local, height=bar_width/2, color=local_color, label='本土企业新原料备案数（个）')

# 添加数值标签
for i, (b1, b2) in enumerate(zip(bars1, bars2)):
    ax.text(b1.get_width() + 1, b1.get_y() + b1.get_height()/2, f'{total[i]}', va='center', fontsize=10, color='red')
    ax.text(b2.get_width() + 1, b2.get_y() + b2.get_height()/2, f'{local[i]}', va='center', fontsize=10, color='black')

# 设置标题和标签
ax.set_yticks(y_pos)
ax.set_yticklabels(years)
ax.invert_yaxis()
ax.set_xlim(0, max(total) + 15)
ax.set_title('化妆品行业新原料备案数', fontsize=14, loc='left', pad=20)
ax.legend()

# 添加顶部文字说明
plt.figtext(0.01, 1.02, '2023年共有69个新原料完成备案，其中本土企业备案52个，占比75.36%，相比2022年，本土企业新原料备案数增长108%。',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()