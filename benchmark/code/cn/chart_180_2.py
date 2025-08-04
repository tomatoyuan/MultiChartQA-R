import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2022H1', '2023H1']
register_total = [883, 670]
register_new = [134, 358]
register_others = [register_total[i] - register_new[i] for i in range(2)]
record_total = [1481, 1937]

x = np.arange(len(years))  # x轴位置
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))

# 注册部分：堆叠柱状图
bar_others = ax.bar(x - width/2, register_others, width, label='其他批件', color='lightgray')
bar_new = ax.bar(x - width/2, register_new, width, bottom=register_others, label='新产品批件', color='blue')

# 标注注册总量数值（顶部）
for i in range(len(years)):
    ax.text(x[i] - width/2, register_total[i] + 30, str(register_total[i]),
            ha='center', va='bottom', fontsize=10)

# ✅ 标注新产品批件数值（在堆叠中部）
for i in range(len(years)):
    ax.text(x[i] - width/2, register_others[i] + register_new[i] / 2,
            str(register_new[i]), ha='center', va='center', fontsize=9, color='white')

# 备案部分：独立柱状图
bar_record = ax.bar(x + width/2, record_total, width, label='备案', color='skyblue')

# 标注备案数值
for i in range(len(years)):
    ax.text(x[i] + width/2, record_total[i] + 30, str(record_total[i]),
            ha='center', va='bottom', fontsize=10)

# 设置轴标签和标题
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel('批件数量', fontsize=12)
ax.set_title('2022H1 v.s. 2023H1中国保健食品注册及备案情况', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')

# 数据来源说明
plt.figtext(0.5, 0.01, '注释：备案数据未包含进口备案产品\n数据来源：国家市场监督管理总局',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()