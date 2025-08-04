import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2018", "2019", "2020", "2021", "2022", "2023年上半年"]
export = [6116, 7981, 10850, 13918, 15321, 8254]  # 出口（亿元）
import_ = [4441, 4922, 5370, 5319, 5278, 2771]    # 进口（亿元）
total = [10557, 12903, 16220, 19237, 20599, 11025] # 进出口（亿元）

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制堆叠柱状图（从下到上：进出口、进口、出口 ，与原图顺序对应）
ax.bar(x, total, color='#8B4513', label='进出口（亿元）')
ax.bar(x, import_, bottom=total, color='#FF8C69', label='进口（亿元）')
ax.bar(x, export, bottom=np.array(total) + np.array(import_), color='#FFDAB9', label='出口（亿元）')

ax.set_ylabel('金额（亿元）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2018-2023年中国跨境电商进出口规模')

# 添加数值标注（分别标注进出口、进口、出口的数值 ）
for i in range(len(years)):
    # 标注进出口数值
    ax.text(i, total[i] / 2, f'{total[i]}', ha='center', va='center', color='white', fontweight='bold')
    # 标注进口数值
    ax.text(i, total[i] + import_[i] / 2, f'{import_[i]}', ha='center', va='center', color='white', fontweight='bold')
    # 标注出口数值
    bottom_sum = total[i] + import_[i]
    ax.text(i, bottom_sum + export[i] / 2, f'{export[i]}', ha='center', va='center', color='white', fontweight='bold')

plt.tight_layout()
plt.show()