import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# 构建数据
provinces = ["广东", "浙江", "北京", "广西", "山东", "四川", "福建", "上海", "辽宁", "其它"]
percentages = [16.3, 7.5, 6.2, 5.7, 5.7, 5.6, 4.7, 4.5, 4.4, 31.9]

# 创建画布和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 设置渐变色（为"其它"使用不同颜色，其余省份使用渐变）
other_color = '#FF6B6B'  # 红色表示"其它"
province_colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(provinces) - 1))
colors = list(province_colors) + [other_color]  # 省份渐变在前，其它颜色在后

# 绘制水平条形图
bar_width = 0.6
y_pos = np.arange(len(provinces))
bars = ax.barh(y_pos, percentages, height=bar_width, color=colors, edgecolor='black', alpha=0.8)

# 自定义"烤串"样式
for i, (province, percent) in enumerate(zip(provinces, percentages)):
    # 计算珠子数量
    bead_count = max(1, int(percent * 0.7))  # 根据百分比确定珠子数量
    
    # 绘制珠子（圆形）
    for j in range(bead_count):
        bead_x = 0.5 + j * 0.8  # 珠子x位置
        if bead_x < percent - 0.5:  # 确保珠子不超出条形范围
            # "其它"项使用红色珠子，其余使用黄色渐变
            if i == len(provinces) - 1:
                bead_color = plt.cm.Reds(j/bead_count)
            else:
                bead_color = plt.cm.YlOrRd(j/bead_count)
            circle = mpatches.Circle(
                (bead_x, y_pos[i]), 
                radius=0.15, 
                color=bead_color,
                alpha=0.9
            )
            ax.add_patch(circle)
    
    # 添加省份标签（放在左侧）
    ax.text(-1.5, y_pos[i], province, ha='center', va='center', fontweight='bold', fontsize=11)

# 添加百分比数值标签（带背景框）
for i, rect in enumerate(bars):
    width = rect.get_width()
    ax.text(
        width + 0.3, rect.get_y() + rect.get_height()/2,
        f'{percentages[i]:.1f}%',  # 保留一位小数
        ha='left', va='center',
        fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.2')
    )

# 设置坐标轴和标题
ax.set_xlim(-2, max(percentages) + 5)  # 调整x轴范围
ax.set_ylim(-0.8, len(provinces) - 0.2)  # 调整y轴范围
ax.set_title('欧洲杯带动美食经济 - 夜宵消费总金额TOP10省份', fontsize=16, pad=15, fontweight='bold')
ax.set_xlabel('消费占比（%）', fontsize=12, labelpad=10)
ax.set_yticks([])  # 隐藏默认y轴标签

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.6)

# 添加图例并向下移动
province_patch = mpatches.Patch(color=province_colors[0], label='各省')
other_patch = mpatches.Patch(color=other_color, label='其他地区合计')
ax.legend(handles=[province_patch, other_patch], 
          loc='upper right', 
          bbox_to_anchor=(0.98, 0.85))  # 调整bbox_to_anchor参数向下移动

# 美化边框
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# 显示图表
plt.tight_layout()
plt.show()