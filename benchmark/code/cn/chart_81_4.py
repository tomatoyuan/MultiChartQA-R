import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2011, 2021)

# 数据（示例，可根据实际微调）
# 中国：物流成本占GDP比（%）
china_logistics = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7]
# 中国：保管成本占GDP比（%）
china_storage = [5.1, 5.2, 5.3, 5.3, 5.1, 5.0, 4.7, 5.1, 5.0, 5.0]
# 美国：物流成本占GDP比（%）
usa_logistics = [7.8, 7.8, 7.8, 7.8, 7.6, 7.4, 8.0, 7.8, 7.6, 7.4]
# 美国：保管成本占GDP比（%）
usa_storage = [3.6, 3.9, 3.1, 3.0, 2.5, 2.4, 2.2, 2.6, 2.5, 2.5]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 20)

# 绘制中国物流成本占比折线
ax.plot(years, china_logistics, marker='o', color='#8BC34A', label='中国：物流成本占GDP比（%）', linewidth=2)
# 绘制美国物流成本占比折线
ax.plot(years, usa_logistics, marker='o', color='#2196F3', label='美国：物流成本占GDP比（%）', linewidth=2)
# 绘制中国保管成本占比折线
ax.plot(years, china_storage, marker='o', color='#FFC107', label='中国：保管成本占GDP比（%）', linewidth=2)
# 绘制美国保管成本占比折线
ax.plot(years, usa_storage, marker='o', color='#F48FB1', label='美国：保管成本占GDP比（%）', linewidth=2)

# 添加数据标注
for y_arr, color in zip([china_logistics, usa_logistics, china_storage, usa_storage], 
                        ['#8BC34A', '#2196F3', '#FFC107', '#F48FB1']):
    for x, y in zip(years, y_arr):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(0, 3),
                    textcoords='offset points',
                    ha='center',
                    va='bottom',
                    color=color)

# 设置坐标轴与标题
ax.set_xlabel('年份')
ax.set_ylabel('占比（%）')
ax.set_title('2011-2020年中美物流成本占GDP比重对比', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# 添加图例
ax.legend(loc='upper right')

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()