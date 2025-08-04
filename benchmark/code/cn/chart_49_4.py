import matplotlib.pyplot as plt
import numpy as np

# 场景名称
scenarios = [
    "逛街解渴", "社交聚会", "职场办公", "熬夜醒神", 
    "家庭会客", "日常佐餐", "深夜加班", "商务招待", 
    "出差携带", "过节送礼", "跟风体验"
]

# 对应场景的比例数据
percentages = [51, 47, 46, 46, 41, 38, 33, 23, 23, 22, 13]

# 数据排序（可选）
sort_data = True
if sort_data:
    # 按百分比从高到低排序
    sorted_data = sorted(zip(percentages, scenarios), reverse=True)
    percentages, scenarios = zip(*sorted_data)

# 创建画布和子图，设置图表尺寸
fig, ax = plt.subplots(figsize=(12, 7))

# 使用渐变色填充条形图
cmap = plt.cm.Greens
norm = plt.Normalize(min(percentages), max(percentages))
colors = cmap(norm(percentages))

# 创建条形图
bars = ax.bar(scenarios, percentages, color=colors, edgecolor='black', linewidth=0.5)

# 添加标题和标签
ax.set_title("消费者日常饮茶场景调研", fontsize=16, pad=20)
ax.set_ylabel("百分比（%）", fontsize=12, labelpad=10)

# 设置 x 轴标签旋转角度和字体大小
plt.xticks(rotation=30, ha='right', fontsize=10)

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 在每个条形上方添加数值标签
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.,
        height + 0.8,  # 微调标签位置
        f'{percentage}%',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# 设置 y 轴范围
plt.ylim(0, max(percentages) + 5)

# 添加背景色
ax.set_facecolor('#f8f9fa')

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()