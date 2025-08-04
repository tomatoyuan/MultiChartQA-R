import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2021年', '2022年', '2023年']
online_counts = [107, 336, 584]      # 上线备案数（左轴 - 柱状图）
filming_counts = [935, 3293, 3574]   # 拍摄备案数（右轴 - 折线图）

x = np.arange(len(years))
bar_width = 0.5

# 创建主图和双轴
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()  # 创建右轴

# 柱状图（左轴）：上线备案数
bars = ax1.bar(x, online_counts, width=bar_width, color='#ff2d55', label='上线备案数')

# 添加柱顶数字
for i, val in enumerate(online_counts):
    ax1.text(x[i], val - 10, str(val), ha='center', fontsize=10, color='black')

# 折线图（右轴）：拍摄备案数
ax2.plot(x, filming_counts, color='#586173', linewidth=2.5, marker='o', markersize=25, label='拍摄备案数', zorder=5)

# 节点圆点标注文字
for i, val in enumerate(filming_counts):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# 坐标轴与标签设置
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.set_ylabel('上线备案数', fontsize=12, color='#ff2d55')
ax2.set_ylabel('拍摄备案数', fontsize=12, color='#586173')

ax1.set_ylim(0, 700)      # 柱状图左轴
ax2.set_ylim(0, 4000)     # 折线图右轴

# 图标题
plt.title('2021年-2023年\n广电总局微短剧备案数', fontsize=14, fontweight='bold', pad=20)

# 图例（合并两个图层的图例）
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# 网格与样式
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['right'].set_visible(True)

# 数据来源
fig.text(0.01, 0.01, '数据来源：国家广播电视总局', fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()