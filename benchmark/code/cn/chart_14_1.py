import matplotlib.pyplot as plt
import numpy as np

# 夏季必备品名称
labels = ['空调', '防晒霜', '遮阳伞', '泳衣', '花露水', '电风扇', '冰箱', '西瓜', '凉席']
# 对应的“战力”百分比数据
values = [73.15, 48, 35, 26, 10, 8.4, 7.8, 5, -7.9]

# 数据排序（升序，但绘图时会反转，实现值越大越靠上）
sorted_data = sorted(zip(values, labels), reverse=False)
values, labels = zip(*sorted_data)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 设置渐变色条（值越大颜色越深）
colors = plt.cm.Oranges(np.linspace(0.4, 0.9, len(values)))

# 绘制美化后的横向条形图
bars = ax.barh(labels, values, color=colors, edgecolor='gray', linewidth=0.8)

# 设置X轴范围（重点修改：负向扩展到-15）
ax.set_xlim(-15, max(values) + 5)

# 添加背景网格线
ax.grid(axis='x', linestyle='--', alpha=0.6)

# 设置标题和标签
ax.set_title('夏季必备品"战力"排行榜', fontsize=16, pad=15)
ax.set_xlabel('"战力"百分比', fontsize=12, labelpad=10)

# 调整刻度和标签样式
ax.tick_params(axis='both', which='major', labelsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 优化数据标签位置（根据新的X轴范围调整）
for bar, value in zip(bars, values):
    # 正值标签位置微调，增加间距
    x_pos = value + 0.8 if value > 0 else value - 0.8
    # 负值标签位置随X轴范围调整
    ax.text(x_pos,
            bar.get_y() + bar.get_height()/2,
            f'{value}%',
            ha='left' if value > 0 else 'right',
            va='center',
            fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# 添加参考线（0值位置）
ax.axvline(x=0, color='black', linestyle='-', alpha=0.3)

# 添加负向区域背景色（可选美化）
ax.axvspan(-15, 0, alpha=0.05, color='lightgray')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()