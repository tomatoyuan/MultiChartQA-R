import matplotlib.pyplot as plt
import numpy as np

# 数据准备
factors = ["口味", "价格", "包装", "宣传", "其他"]
proportions = [66.2, 63.2, 44.1, 42.1, 0.5]  # 占比（%）

x = np.arange(len(factors))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, proportions, color='coral', width=0.6)
ax.set_title('2023年中国消费者购买无糖饮料关注因素', fontsize=14)
ax.set_ylabel('关注占比（%）')
ax.set_xticks(x)
ax.set_xticklabels(factors)
ax.set_ylim(0, 75)  # 调整y轴范围，使数据展示更美观

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=12)

plt.tight_layout()
plt.show()