import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['截至2022.12', '截至2023.12']
population = [52000, 54800]  # 单位：万
penetration_rate = [48.8, 49.9]  # 单位：%

# 设置画布
fig, ax1 = plt.subplots(figsize=(7, 4))

# 绘制柱状图：人数（左轴）
bar_width = 0.4
x = np.arange(len(years))
bars = ax1.bar(x, population, bar_width, color='#4CAF50', label='人数（万）')
ax1.set_ylabel('人数（万）', fontsize=12)
ax1.set_ylim(50000, 56000)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.tick_params(axis='y', labelsize=10)

# 添加柱状图数值标签
for i, v in enumerate(population):
    ax1.text(i, v + 200, f"{v}", ha='center', va='bottom', fontsize=10)

# 设置第二个坐标轴：渗透率（右轴）
ax2 = ax1.twinx()
ax2.plot(x, penetration_rate, color='blue', marker='o', linewidth=2.5, label='渗透率（%）')
ax2.set_ylabel('占整体网民的渗透率（%）', fontsize=12)
ax2.set_ylim(48.25, 50.50)
ax2.tick_params(axis='y', labelsize=10)

# 添加渗透率数值标签
for i, v in enumerate(penetration_rate):
    ax2.text(i, v - 0.2, f"{v}%", color='blue', ha='center', va='bottom', fontsize=15, fontweight='bold')

# 标题与图例
plt.title('网上外卖用户规模及渗透率统计', fontsize=14, pad=15)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=10)

# 数据来源标注

plt.tight_layout()
plt.show()