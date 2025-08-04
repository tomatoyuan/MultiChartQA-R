import matplotlib.pyplot as plt
import numpy as np

# 城市等级
city_levels = ['一线城市', '二线城市', '三线城市', '四线城市']
# 占比数据（对应柱状图）
proportion = [52, 15, 14, 10]
# 增速数据（对应折线图）
growth_rate = [3, -18, -30, -18]

x = np.arange(len(city_levels))  # 横坐标索引

fig, ax1 = plt.subplots(figsize=(10, 6))  # 调整图表大小

# 绘制柱状图（占比）
bars = ax1.bar(x, proportion, color='blue', label='占比')
ax1.set_ylabel('占比 (%)', color='blue')
ax1.set_xlabel('城市等级')
ax1.set_xticks(x)
ax1.set_xticklabels(city_levels)
ax1.tick_params(axis='y', labelcolor='blue')

# 为柱状图添加数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center',
                va='bottom',
                color='blue')

# 创建第二个纵轴绘制折线图（增速）
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_rate, color='orange', label='增速', marker='o', markersize=6)
ax2.set_ylabel('增速 (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 为折线图添加数据标注
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%',
                xy=(x[i], rate),
                xytext=(5, 5) if rate >= 0 else (5, -5),  # 根据正负调整位置
                textcoords="offset points",
                ha='left',
                va='bottom' if rate >= 0 else 'top',
                color='orange',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# 添加图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# 设置标题
plt.title('5月离婚诉讼行业分城市等级关注度占比和增速')

# 添加网格线
ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()  # 确保所有元素都适合图表区域
plt.show()