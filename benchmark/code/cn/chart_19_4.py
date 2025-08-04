import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['女性', '男性']
values = [60, 40]
colors = ['#FF7B9C', '#7BC8F6']  # 柔和的粉色和蓝色

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))  # 调整图表大小
ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.2, alpha=0.8)

# 添加标题和标签
ax.set_title('“最爱后悔” 的消费者性别分布', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('百分比（%）', fontsize=14, labelpad=10)

# 设置 y 轴范围和刻度
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 美化坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# 显示数值标签
for i, v in enumerate(values):
    ax.text(i, v + 2, f'{v}%', ha='center', fontsize=14, fontweight='bold')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()