import matplotlib.pyplot as plt
import numpy as np

# 日期数据
dates = ["14日", "15日", "16日", "17日", "18日", "19日"]
# 热度数据（单位：万）
heat_values = [4698, 3708, 3131, 2204, 2325, 2892]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')

# 设置网格样式
ax.grid(True, linestyle='--', alpha=0.7, color='#dddddd')

# 绘制折线图，使用渐变色
x = np.arange(len(dates))
line, = ax.plot(x, heat_values, marker='o', markersize=8, 
                color='#1e88e5', linewidth=3, alpha=0.8)

# 添加数据标签
for i, (date, value) in enumerate(zip(dates, heat_values)):
    ax.annotate(f'{value}',
                xy=(i, value),
                xytext=(0, 10),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1e88e5", alpha=0.8))

# 设置x轴标签
ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=11)

# 设置y轴范围和标签
ax.set_ylim(0, max(heat_values) * 1.1)
ax.set_ylabel('热度（万）', fontsize=12, labelpad=10)

# 添加标题
ax.set_title('小组赛首轮世界杯热度走势', fontsize=16, pad=15, fontweight='bold')

# 添加背景色
ax.set_facecolor('#f8f9fa')

# 添加趋势箭头
for i in range(len(x)-1):
    ax.annotate('',
                xy=(x[i+1], heat_values[i+1]),
                xytext=(x[i], heat_values[i]),
                arrowprops=dict(arrowstyle='->', color='#1e88e5', lw=1.5, alpha=0.6))

# 添加图例
ax.legend(['热度趋势'], loc='upper right', frameon=True, framealpha=0.9)

# 添加底部说明
plt.figtext(0.5, 0.01, '数据来源：虚构示例', ha='center', fontsize=9, color='#666666')

# 优化布局
plt.tight_layout(pad=2)

# 保存图表（可选）
# plt.savefig('worldcup_heat_trend.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()