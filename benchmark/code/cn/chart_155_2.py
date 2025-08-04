import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2022年', '2023年']
medical_health = [4.08, 4.64]
supplements = [67.09, 70.83]
traditional = [28.83, 24.53]

bar_width = 0.5
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制堆叠柱状图
p1 = ax.bar(x, traditional, bar_width, label='传统滋补营养品', color='#b2df8a')
p2 = ax.bar(x, supplements, bar_width, bottom=traditional, label='保健品/膳食营养补充品', color='#fdbf6f')
bottom2 = [traditional[i] + supplements[i] for i in range(len(x))]
p3 = ax.bar(x, medical_health, bar_width, bottom=bottom2, label='医疗保健', color='#1f78b4')

# 添加文字标签
for i in range(len(x)):
    ax.text(x[i], traditional[i] / 2, f'{traditional[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], traditional[i] + supplements[i] / 2, f'{supplements[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], bottom2[i] + medical_health[i] / 2, f'{medical_health[i]:.2f}%', ha='center', va='center', fontsize=10)

# 设置标签与标题
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('销售占比（%）')
ax.set_title('2022-2023年抖快电商不同品类销售占比率', fontsize=14, weight='bold')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 数据来源标注
plt.figtext(0.5, -0.05, '数据来源：飞瓜数据（feigua.cn），统计平台：抖音、快手，数据周期：2022.01-2024.03',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()