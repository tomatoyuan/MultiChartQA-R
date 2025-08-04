import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 数据
months = ['6月', '7月', '8月', '9月', '10月', '11月', '12月']
data_2022 = [87, 100, 96, 88, 92, 91, 98]  # 构造型数值
growth = [0.13, 0.0, 0.04, 0.32, 0.30, 0.26, 0.02]
data_2023 = [data_2022[i] * (1 + growth[i]) for i in range(len(data_2022))]

x = np.arange(len(months))
width = 0.35

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 柱状图绘制
bars_2022 = ax.bar(x - width/2, data_2022, width, label='2022下半年', color='#e55322')
bars_2023 = ax.bar(x + width/2, data_2023, width, label='2023下半年', color='black')

# 添加数值标注（2022和2023）
for i in range(len(x)):
    # 2022柱子 - 内部标注
    ax.text(x[i] - width/2, data_2022[i] - 3,
            f'{int(data_2022[i])}', ha='center', va='top', fontsize=10, color='white')

    # 2023柱子 - 顶部外部标注
    ax.text(x[i] + width/2, data_2023[i] + 4,
            f'{int(data_2023[i])}', ha='center', va='bottom', fontsize=10, color='black')

# 添加增长率注释（略微上移）
for i, (x_pos, val) in enumerate(zip(x, data_2023)):
    ax.text(x_pos + width/2, val + 8,
            f'+{int(growth[i]*100)}%', ha='center', va='bottom', fontsize=9, color='gray')

# 坐标轴与标签
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylabel('月销售额（相对值）', fontsize=12)
plt.title('月销售额&同比增长率（2023下半年同比 / 抖音服饰鞋包）', fontsize=14, pad=20)

# 图例
ax.legend(loc='upper left', fontsize=10)

# 虚线框突出9–11月
highlight_start = x[3] - width*1.5
highlight_width = (x[5] - x[3]) + width*3
rect = patches.Rectangle(
    (highlight_start, 0), highlight_width, max(data_2023) * 1.2,
    linewidth=1.5, edgecolor='#e55322', linestyle='--', facecolor='none'
)
ax.add_patch(rect)

# 数据来源注释
fig.text(0.01, 0.01,
         '数据源：有米有数新电商营销大数据分析平台，统计时间为2022.6.1–12.31、2023.6.1–12.31',
         ha='left', va='bottom', fontsize=9)

# 网格
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()