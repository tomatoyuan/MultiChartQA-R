import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['23清明', '23五一', '23端午', '23中秋国庆', '24元旦', '24清明']
people_pct = [68.0, 119.1, 112.8, 104.1, 109.4, 111.5]
income_pct = [39.2, 100.7, 94.9, 101.5, 105.6, 112.7]

x = np.arange(len(labels))
width = 0.35

# 颜色设置（蓝绿色系）
colors_people = '#0072B2'  # 蓝色
colors_income = '#009E73'  # 绿色

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, people_pct, width, label='出游人次恢复至19年同期', color=colors_people)
bars2 = ax.bar(x + width/2, income_pct, width, label='旅游收入恢复至19年同期', color=colors_income)

# 添加文本标签
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# 细节设置
ax.set_ylabel('恢复至2019年同期 (%)')
ax.set_title('旅行出游恢复情况')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.set_ylim(0, 130)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()