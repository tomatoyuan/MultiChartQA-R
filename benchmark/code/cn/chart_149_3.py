import matplotlib.pyplot as plt
import numpy as np

# 数据准备
improve_directions = ["口味", "配料", "价格", "日期", "规格", "包装"]
proportions = [71.5, 56.2, 56.0, 46.5, 40.8, 39.3]  # 占比（%）

x = np.arange(len(improve_directions))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, proportions, color='coral')
ax.set_title('2023年中国消费者认为市面上无糖饮料需改进的方向', fontsize=14)
ax.set_ylabel('占比（%）')
ax.set_xlabel('改进方向')
ax.set_xticks(x)
ax.set_xticklabels(improve_directions)
ax.set_ylim(0, 80)  # 调整y轴范围，适配最大占比（71.5%）

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

plt.tight_layout()
plt.show()