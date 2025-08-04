import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ['≤1k', '1-2k', '2-3k', '3-4k', '4-5k', '5-8k', '8-10k', '>10k']
# 数据
y_2023 = [5, 18, 19, 27, 17, 8, 4, 2]
y_2024 = [4, 15, 18, 25, 19, 13, 5, 1]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, y_2023, width, label='23年新年礼花费', color='#8B0000')
bars2 = ax.bar(x + width/2, y_2024, width, label='24年新年礼预算', color='#CD5C5C')

# 添加数值标注
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

# 设定标题与标签
ax.set_title('大众新年购置礼物的预算分布', fontsize=14)
ax.set_ylabel('占比')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_ylim(0, 35)

plt.tight_layout()
plt.show()