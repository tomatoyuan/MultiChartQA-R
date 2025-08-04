import matplotlib.pyplot as plt
import numpy as np

data = {
    "王": 139, "李": 132, "刘": 127, "张": 127, 
    "陈": 113, "杨": 63, "黄": 58, "赵": 50, 
    "周": 50, "吴": 39
}

surnames = list(data.keys())
counts = list(data.values())

# 创建画布和子图
fig, ax = plt.subplots(figsize=(12, 7))

# 设置渐变色柱体
cmap = plt.cm.get_cmap('viridis', len(surnames))
colors = [cmap(i) for i in range(len(surnames))]
bars = ax.bar(surnames, counts, color=colors, edgecolor='black', alpha=0.8)

# 添加数值标注
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1.5,
            f'{height}', ha='center', va='bottom', fontsize=12)

# 添加标题和标签
ax.set_title('状元姓氏排行榜', fontsize=18, pad=20)
ax.set_xlabel('姓氏', fontsize=14, labelpad=10)
ax.set_ylabel('人数', fontsize=14, labelpad=10)

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 设置y轴范围
ax.set_ylim(0, max(counts) * 1.1)

# 添加背景色
ax.set_facecolor('#f8f9fa')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()