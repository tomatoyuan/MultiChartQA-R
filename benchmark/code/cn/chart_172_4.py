import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2022', '2028E']
values = [449.25, 607.95]
x = np.arange(len(years))

# 图表创建
fig, ax = plt.subplots(figsize=(7, 6))

# 柱状图
bars = ax.bar(x, values, color='#00d2c8', width=0.5, label='市场规模（亿元）')

# 添加顶部数值标签
for i, v in enumerate(values):
    ax.text(x[i] - 0.1, v + 15, f'{v}', ha='center', va='bottom', fontsize=10)

# 添加 CAGR 注释
ax.annotate('CAGR = 5.17%',
            xy=(x[0], values[0] + 25), xytext=(x[1], values[1] + 25),
            textcoords='data',
            arrowprops=dict(arrowstyle='-', linestyle='dotted', color='#00d2c8', linewidth=2),
            fontsize=13, color='#00d2c8', fontweight='bold')

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_ylim(0, 700)
ax.set_ylabel('单位：亿元', fontsize=12)
ax.set_title('全球甜味剂市场规模', fontsize=14, fontweight='bold', pad=20)

# 图例
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# 美化
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])  # 给图例留空间
plt.show()