import matplotlib.pyplot as plt
import numpy as np

# 数据
city_levels = ["一线城市", "二线城市", "三线城市", "四线城市"]
proportion = [38, 19, 17, 12]  # 占比数据
growth_rate = [-6, -4, -8, -9]  # 增速数据

x = np.arange(len(city_levels))  # x 轴刻度位置

# 创建图表
fig, ax1 = plt.subplots(figsize=(10, 6))  # 调整图表大小

# 设置背景样式 - 使用 Matplotlib 内置样式
plt.style.use('ggplot')  # 修改为 Matplotlib 内置样式

# 绘制柱状图（占比） - 使用渐变色
bar_colors = ['#4A86E8', '#6AA1E8', '#8ABBE8', '#AAD5E8']  # 蓝色渐变
bars = ax1.bar(x, proportion, color=bar_colors, label='占比', width=0.6, edgecolor='black', linewidth=0.5)
ax1.set_ylabel('占比（%）', color='#4A86E8', fontsize=12)
ax1.set_xlabel('城市等级', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(city_levels, fontsize=11)
ax1.tick_params(axis='y', labelcolor='#4A86E8')

# 在柱状图上方添加数据标签
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom', fontsize=10)

# 创建第二个 y 轴，绘制折线图（增速）
ax2 = ax1.twinx()
line_color = '#FF9900'  # 橙色
ax2.plot(x, growth_rate, color=line_color, label='增速', linewidth=2.5, marker='o', markersize=8)
ax2.set_ylabel('增速（%）', color=line_color, fontsize=12)
ax2.tick_params(axis='y', labelcolor=line_color)
ax2.set_ylim([-10, 0])  # 设置增速轴的范围

# 在折线上添加数据标签
for i, txt in enumerate(growth_rate):
    ax2.annotate(f'{txt}%', (x[i], growth_rate[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=10, color=line_color)

# 添加图例 - 使用更美观的样式
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', 
           frameon=True, framealpha=0.9, edgecolor='black', fancybox=True)

# 添加图表标题
plt.title('5月职业培训行业分城市等级关注度占比', fontsize=16, fontweight='bold', pad=20)

# 添加网格线增强可读性
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.grid(axis='x', visible=False)
ax2.grid(visible=False)

# 调整图表布局
plt.tight_layout()

# 显示图表
plt.show()