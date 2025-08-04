import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['每天1次及以上', '每周2 - 3次', '每月2 - 3次', '偶尔（每月≤1次）']
values = [32, 47, 17, 4]

# 优化的颜色方案，使用更现代的配色
colors = ['#4a86e8', '#4a86e8', '#b7b7b7', '#e6e6e6']

# 创建画布和子图，设置适当的大小
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制条形图，添加边框和透明度
bars = ax.bar(labels, values, color=colors, edgecolor='black', alpha=0.85, width=0.6)

# 添加数值标签，优化位置和样式
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 0.5,  # 微调标签位置
        f'{height}%',
        ha='center', 
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# 设置标题，添加样式
ax.set_title('上海静安区消费者咖啡饮用频次', fontsize=16, fontweight='bold', pad=20)

# 设置y轴标签和范围
ax.set_ylabel('百分比 (%)', fontsize=12, labelpad=10)
ax.set_ylim(0, max(values) * 1.15)  # 调整y轴范围，留出空间

# 美化坐标轴
ax.tick_params(axis='x', rotation=0, labelsize=11)  # x轴标签不旋转
ax.tick_params(axis='y', labelsize=10)

# 设置网格线，仅显示水平网格
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 隐藏右侧和上侧坐标轴，优化左侧和下侧坐标轴
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# 调整布局
plt.tight_layout(pad=2)

# 显示图表
plt.show()