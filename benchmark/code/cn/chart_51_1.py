import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025e", "2026e"]
# 各险种保费收入（亿元），数据大体模拟，可根据实际调整
premium_data = np.array([
    [22754, 11649, 7066, 1000],    # 2019
    [23982, 11929, 8173, 1100],    # 2020
    [23572, 11671, 8447, 1200],    # 2021
    [24519, 12712, 8653, 1300],    # 2022
    [27646, 13607, 9035, 1400],    # 2023
    [31917, 14331, 9773, 1500],    # 2024
    [33736, 14918, 10174, 1600],   # 2025e
    [35659, 15530, 10591, 1700]    # 2026e
])

# 各险种对应的颜色
colors = ['green', 'limegreen', 'mediumseagreen', 'lightseagreen']
# 险种名称
insurance_types = ["寿险 (亿元)", "财产险 (亿元)", "健康险 (亿元)", "意外险 (亿元)"]

x = np.arange(len(years))  # x轴刻度位置
bar_width = 0.6  # 柱状图宽度

fig, ax = plt.subplots(figsize=(14, 9))  # 进一步增大图表尺寸

# 绘制堆积柱状图
bottom = np.zeros(len(years))
for i in range(premium_data.shape[1]):
    bars = ax.bar(x, premium_data[:, i], width=bar_width, bottom=bottom, color=colors[i], label=insurance_types[i])
    bottom += premium_data[:, i]
    
    # 在每个柱状图上方添加数据标签
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 500:  # 只显示高度足够的标签，避免拥挤
            ax.text(
                bar.get_x() + bar.get_width()/2., 
                bar.get_y() + height/2,
                f'{int(height)}',
                ha='center', va='center',
                color='black', fontsize=8, fontweight='bold'
            )

# 添加标题
ax.set_title('2019-2026年中国保险业原保费收入及增长率', fontsize=16, pad=15)

# 设置x轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# 添加y轴标签
ax.set_ylabel('保费收入 (亿元)', fontsize=13)

# 添加图例
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=11)

# 计算各年总保费
total_premiums = premium_data.sum(axis=1)

# 添加总保费标注
for i, total in enumerate(total_premiums):
    ax.text(x[i], total + 1000,  # 调整垂直位置，避免与柱状图重叠
            f'{int(total)}', 
            ha='center', va='bottom', 
            fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, pad=2.0))

# CAGR标注函数
def add_cagr_annotation(start_idx, end_idx, cagr_value, ax, x, total_premiums):
    """添加CAGR折线标注"""
    start_x = x[start_idx]
    end_x = x[end_idx]
    start_y = total_premiums[start_idx]
    end_y = total_premiums[end_idx]
    
    # 计算中间点位置
    mid_x = (start_x + end_x) / 2
    mid_y1 = start_y + (end_y - start_y) * 0.3
    mid_y2 = start_y + (end_y - start_y) * 0.7
    
    # 绘制折线
    ax.plot([start_x, end_x], [start_y, end_y], 
            'gray', linestyle='--', linewidth=1.2)
    
    # 添加CAGR文本
    text_x = mid_x
    text_y = mid_y2 + (end_y - start_y) * 0.25
    ax.text(text_x, text_y, f'CAGR = {cagr_value}%', 
            ha='center', va='bottom', fontsize=12, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', pad=3.0))

# 添加2019-2024年CAGR标注
add_cagr_annotation(0, 5, 6, ax, x, total_premiums)

# 添加2024-2026年CAGR标注
add_cagr_annotation(5, 7, 5, ax, x, total_premiums)

# 美化图表
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加水平网格线
plt.tight_layout()  # 自动调整布局

plt.show()