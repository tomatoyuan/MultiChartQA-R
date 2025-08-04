import matplotlib.pyplot as plt
import numpy as np

# 数据
groups = ['老人', '儿童/幼儿', '女性', '宠物']
influence_level = [8, 7, 6, 5]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 设置背景色和网格
ax.set_facecolor('#FFF8E7')  # 温暖的浅橙色背景
ax.grid(axis='y', linestyle='--', alpha=0.3, color='gray')

# 绘制美化后的条形图
colors = plt.cm.Reds(np.linspace(0.6, 0.9, len(groups)))  # 渐变色
bars = ax.bar(groups, influence_level, color=colors, width=0.6, 
              edgecolor='black', linewidth=0.5)

# 添加标题和副标题
ax.set_title('"空调病"易袭的几种群体', fontsize=18, pad=20, fontweight='bold')

# 调整坐标轴
ax.set_ylim(0, 10)  # 固定y轴范围，使比较更直观
ax.set_yticks([])  # 隐藏y轴刻度
ax.set_xlabel('群体类型', fontsize=12, labelpad=10)

# 美化x轴标签
ax.tick_params(axis='x', which='major', labelsize=12, pad=10)

# 隐藏上、右、左坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 在每个条形上方添加简短描述
for bar, group in zip(bars, groups):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{group}', ha='center', va='bottom', fontweight='bold', fontsize=12)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()